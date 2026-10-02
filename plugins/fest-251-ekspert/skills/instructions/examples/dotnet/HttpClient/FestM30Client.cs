using System.Globalization;
using System.Net;
using System.Text;
using System.Xml;
using System.Xml.Linq;

namespace Fest.M30;

public enum FestFilter { Rekvirent, Institusjon, Veterinær, Bandasjist }

public static class FestEndpoints
{
    public static readonly Uri ProduksjonInternett = new("https://fest.legemiddelverket.no/Fest/FestService251.svc");
    public static readonly Uri TestInternett = new("https://fest-test.legemiddelverket.no/TestFest/FestService251.svc");
    public static readonly Uri ProduksjonNhn = new("https://frontend-fest.nhn.no/Fest/FestService251.svc");
    public static readonly Uri StagingNhn = new("https://frontend-fest.nhn.no/StagingFest/FestService251.svc");
    public static readonly Uri TestNhn = new("https://frontend-fest-test.nhn.no/TestFest/FestService251.svc");
}

public class FestException(string message, Exception? inner = null) : Exception(message, inner);

public sealed class FestReturkodeException(string kode, string? beskrivelse)
    : FestException($"FEST returnerte Returkode V={kode} ({beskrivelse}).")
{
    public string Kode { get; } = kode;
    public bool KreverFulltUttrekk => Kode == "5";
}

public sealed class FestSoapFaultException(HttpStatusCode status, string reason)
    : FestException($"SOAP Fault (HTTP {(int)status}): {reason}");

/// <summary>SOAP 1.2 + WS-Addressing 1.0 over HTTPS, uten WCF-avhengighet.</summary>
public sealed class FestM30Client(HttpClient http)
{
    private const string Action = "http://www.slv.no/201410325/FestService251/GetM30";
    private const string ServiceNs = "http://www.slv.no/201410325/";
    private static readonly XNamespace Soap = "http://www.w3.org/2003/05/soap-envelope";

    /// <summary>
    /// Kaller GetM30 og strømmer hele SOAP-svaret til <paramref name="targetFile"/>.
    /// <paramref name="sistOppdatert"/> er HentetDato fra forrige behandlede melding, uendret tekst; null gir fullt uttrekk.
    /// </summary>
    public async Task DownloadAsync(Uri endpoint, FestFilter filter, string? sistOppdatert, string targetFile,
        TimeSpan timeout, CancellationToken cancellationToken = default)
    {
        if (sistOppdatert is not null && filter is not (FestFilter.Rekvirent or FestFilter.Institusjon))
            throw new ArgumentException("SistOppdatert kan bare brukes med Rekvirent og Institusjon.", nameof(sistOppdatert));

        using var cts = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        cts.CancelAfter(timeout); // dekker også lesing av body, som HttpClient.Timeout ikke gjør med ResponseHeadersRead

        using var request = new HttpRequestMessage(HttpMethod.Post, endpoint)
        {
            Content = new StringContent(CreateEnvelope(endpoint, filter, sistOppdatert), Encoding.UTF8, "application/soap+xml")
        };
        using var response = await http.SendAsync(request, HttpCompletionOption.ResponseHeadersRead, cts.Token);

        var temp = targetFile + ".part";
        await using (var body = await response.Content.ReadAsStreamAsync(cts.Token))
        await using (var file = new FileStream(temp, FileMode.Create, FileAccess.Write, FileShare.None, 81920, useAsync: true))
            await body.CopyToAsync(file, cts.Token);

        if (!response.IsSuccessStatusCode)
        {
            var reason = TryReadFaultReason(temp) ?? response.ReasonPhrase ?? "ukjent feil";
            File.Delete(temp);
            throw new FestSoapFaultException(response.StatusCode, reason);
        }
        File.Move(temp, targetFile, overwrite: true);
    }

    private static string CreateEnvelope(Uri endpoint, FestFilter filter, string? sistOppdatert)
    {
        XNamespace a = "http://www.w3.org/2005/08/addressing";
        XNamespace xsi = "http://www.w3.org/2001/XMLSchema-instance";
        XNamespace tns = ServiceNs;
        var envelope = new XElement(Soap + "Envelope",
            new XAttribute(XNamespace.Xmlns + "s", Soap), new XAttribute(XNamespace.Xmlns + "a", a),
            new XElement(Soap + "Header",
                new XElement(a + "Action", new XAttribute(Soap + "mustUnderstand", "1"), Action),
                new XElement(a + "MessageID", "urn:uuid:" + Guid.NewGuid()),
                new XElement(a + "To", new XAttribute(Soap + "mustUnderstand", "1"), endpoint.AbsoluteUri)),
            new XElement(Soap + "Body",
                new XElement(tns + "GetM30",
                    new XElement(tns + "filter", filter.ToString()),
                    sistOppdatert is null
                        ? new XElement(tns + "incrementalDate", new XAttribute(xsi + "nil", "true"))
                        : new XElement(tns + "incrementalDate", sistOppdatert))));
        return envelope.ToString(SaveOptions.DisableFormatting);
    }

    private static string? TryReadFaultReason(string path)
    {
        try
        {
            return XDocument.Load(path).Descendants(Soap + "Text").FirstOrDefault()?.Value;
        }
        catch (XmlException)
        {
            return null;
        }
    }
}

/// <summary>Leser et lagret GetM30-svar strømmende. Bare én oppføring holdes i minnet om gangen.</summary>
public sealed class M30Message
{
    private static readonly XNamespace ServiceNs = "http://www.slv.no/201410325/";
    public static readonly XNamespace M30Ns = "http://www.kith.no/xmlstds/eresept/m30/2014-12-01";

    private readonly string _path;

    public string HentetDato { get; }

    private M30Message(string path, string hentetDato) => (_path, HentetDato) = (path, hentetDato);

    /// <summary>Kontrollerer Returkode og leser HentetDato. Kaster ved Returkode ulik 1.</summary>
    public static M30Message Open(string path)
    {
        using var reader = CreateReader(path);
        if (!reader.ReadToFollowing("Returkode", ServiceNs.NamespaceName))
            throw new FestException("Svaret mangler Returkode.");
        var kode = reader.GetAttribute("V");
        if (kode != "1")
            throw new FestReturkodeException(kode ?? "", reader.GetAttribute("DN"));
        if (!reader.ReadToFollowing("HentetDato", M30Ns.NamespaceName))
            throw new FestException("Returkode er OK, men M30Message mangler HentetDato.");
        return new M30Message(path, reader.ReadElementContentAsString());
    }

    /// <summary>Alle Oppf*-elementer, med katalognavnet de står i.</summary>
    public IEnumerable<(string Katalog, XElement Oppforing)> ReadOppforinger()
    {
        using var reader = CreateReader(_path);
        if (!reader.ReadToFollowing("M30Message", ServiceNs.NamespaceName) || reader.IsEmptyElement)
            yield break;
        var katalogDepth = reader.Depth + 1;
        string? katalog = null;
        reader.Read();
        while (!reader.EOF && reader.Depth >= katalogDepth)
        {
            if (reader.NodeType != XmlNodeType.Element) { reader.Read(); continue; }
            if (reader.Depth == katalogDepth)
            {
                katalog = reader.LocalName;
                reader.Read();
            }
            else if (reader.Depth == katalogDepth + 1 && katalog is not null)
                yield return (katalog, (XElement)XNode.ReadFrom(reader));
            else
                reader.Skip();
        }
    }

    /// <summary>Skriver innholdet som et frittstående FEST-dokument (samme form som DMPs ZIP-filer).</summary>
    public void SaveAsFestXml(string targetFile)
    {
        using var reader = CreateReader(_path);
        if (!reader.ReadToFollowing("M30Message", ServiceNs.NamespaceName))
            throw new FestException("Svaret mangler M30Message.");
        using var writer = XmlWriter.Create(targetFile, new XmlWriterSettings { Encoding = new UTF8Encoding(false) });
        writer.WriteStartDocument();
        writer.WriteStartElement("FEST", M30Ns.NamespaceName);
        if (!reader.IsEmptyElement)
        {
            var depth = reader.Depth;
            reader.Read();
            while (!reader.EOF && reader.Depth > depth)
            {
                if (reader.NodeType == XmlNodeType.Element) writer.WriteNode(reader, defattr: true);
                else reader.Read();
            }
        }
        writer.WriteEndElement();
    }

    private static XmlReader CreateReader(string path) => XmlReader.Create(path, new XmlReaderSettings
    {
        DtdProcessing = DtdProcessing.Prohibit,
        XmlResolver = null,
        IgnoreWhitespace = true,
        IgnoreComments = true
    });

    public static DateTime ParseHentetDato(string value) =>
        XmlConvert.ToDateTime(value, XmlDateTimeSerializationMode.Unspecified);
}

public interface IFestStore
{
    /// <summary>HentetDato for siste ferdig anvendte melding, eller null hvis lageret er tomt.</summary>
    Task<string?> GetHentetDatoAsync(FestFilter filter, CancellationToken cancellationToken);

    /// <summary>Anvend alle oppføringer og lagre HentetDato i samme transaksjon.</summary>
    Task ApplyAsync(FestFilter filter, M30Message message, bool fulltUttrekk, CancellationToken cancellationToken);
}

/// <summary>Oppdateringsløkken fra grensesnittdokumentasjonen, med vern mot feil tilstand.</summary>
public sealed class FestUpdater(FestM30Client client, IFestStore store, string workDirectory)
{
    public TimeSpan CallTimeout { get; init; } = TimeSpan.FromMinutes(10);
    public int MaxSerier { get; init; } = 200;
    public int MaxForsok { get; init; } = 3;

    public async Task<int> UpdateAsync(Uri endpoint, FestFilter filter, CancellationToken cancellationToken = default)
    {
        Directory.CreateDirectory(workDirectory);
        var sist = await store.GetHentetDatoAsync(filter, cancellationToken);
        var inkrementell = filter is FestFilter.Rekvirent or FestFilter.Institusjon;

        if (sist is null || !inkrementell)
        {
            var full = await FetchAsync(endpoint, filter, null, cancellationToken);
            if (sist is not null && Compare(full.HentetDato, sist) <= 0) return 0; // ingen ny publisering
            await store.ApplyAsync(filter, full, fulltUttrekk: true, cancellationToken);
            if (!inkrementell) return 1;
            sist = full.HentetDato;
        }

        for (var serie = 0; serie < MaxSerier; serie++)
        {
            M30Message message;
            try
            {
                message = await FetchAsync(endpoint, filter, sist, cancellationToken);
            }
            catch (FestReturkodeException e) when (e.KreverFulltUttrekk)
            {
                throw new FestException($"Tjenesten avviste SistOppdatert={sist}. Kjør fullt uttrekk på nytt.", e);
            }

            if (message.HentetDato == sist) return serie; // ferdig: ingen flere serier
            if (Compare(message.HentetDato, sist) < 0)
                throw new FestException($"Mottatt HentetDato {message.HentetDato} er eldre enn SistOppdatert {sist}. Lagret tilstand er trolig feil.");

            await store.ApplyAsync(filter, message, fulltUttrekk: false, cancellationToken);
            sist = message.HentetDato;
        }
        throw new FestException($"Avbrutt etter {MaxSerier} serier uten at HentetDato stabiliserte seg.");
    }

    private async Task<M30Message> FetchAsync(Uri endpoint, FestFilter filter, string? sist, CancellationToken cancellationToken)
    {
        var file = Path.Combine(workDirectory, $"m30-{filter}-{DateTime.UtcNow:yyyyMMddHHmmssfff}.xml");
        for (var forsok = 1; ; forsok++)
        {
            try
            {
                await client.DownloadAsync(endpoint, filter, sist, file, CallTimeout, cancellationToken);
                return M30Message.Open(file);
            }
            catch (Exception e) when (forsok < MaxForsok && IsTransient(e, cancellationToken))
            {
                await Task.Delay(TimeSpan.FromSeconds(10 * forsok), cancellationToken);
            }
        }
    }

    private static bool IsTransient(Exception e, CancellationToken cancellationToken) => e switch
    {
        FestReturkodeException r => r.Kode == "8",
        FestSoapFaultException => false,
        HttpRequestException => true,
        IOException => true,
        XmlException => true, // avkortet svar
        OperationCanceledException => !cancellationToken.IsCancellationRequested,
        _ => false
    };

    private static int Compare(string a, string b) =>
        M30Message.ParseHentetDato(a).CompareTo(M30Message.ParseHentetDato(b));
}
