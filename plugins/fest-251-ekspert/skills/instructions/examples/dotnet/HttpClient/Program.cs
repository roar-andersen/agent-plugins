using System.Diagnostics;
using System.Net;
using Fest.M30;

// Demo/testprogram. Bruk: full <filter> <fest.xml> | inc <filter> <HentetDato> | update <filter> [HentetDato]
var endpoint = Environment.GetEnvironmentVariable("FEST_ENDPOINT") is { } e ? new Uri(e) : FestEndpoints.TestInternett;
var filter = Enum.Parse<FestFilter>(args[1]);
var work = Path.Combine(Path.GetTempPath(), "fest-demo");
Directory.CreateDirectory(work);

using var http = new HttpClient(new SocketsHttpHandler
{
    AutomaticDecompression = DecompressionMethods.All,
    PooledConnectionLifetime = TimeSpan.FromMinutes(5)
});
var client = new FestM30Client(http);
var watch = Stopwatch.StartNew();

switch (args[0])
{
    case "full":
    case "inc":
    {
        var file = Path.Combine(work, "svar.xml");
        await client.DownloadAsync(endpoint, filter, args[0] == "inc" ? args[2] : null, file, TimeSpan.FromMinutes(10));
        var message = M30Message.Open(file);
        var antall = new SortedDictionary<string, int>();
        var utgatt = 0;
        foreach (var (katalog, oppforing) in message.ReadOppforinger())
        {
            antall[katalog] = antall.GetValueOrDefault(katalog) + 1;
            if (oppforing.Element(M30Message.M30Ns + "Status")?.Attribute("V")?.Value == "U") utgatt++;
        }
        Console.WriteLine($"HentetDato={message.HentetDato} oppføringer={antall.Values.Sum()} utgått={utgatt} bytes={new FileInfo(file).Length}");
        Console.WriteLine(string.Join(", ", antall.Select(k => $"{k.Key}={k.Value}")));
        if (args[0] == "full" && args.Length > 2) message.SaveAsFestXml(args[2]);
        break;
    }
    case "update":
    {
        var store = new LogStore(args.Length > 2 ? args[2] : null);
        var serier = await new FestUpdater(client, store, work).UpdateAsync(endpoint, filter);
        Console.WriteLine($"Ferdig: {serier} meldinger anvendt, HentetDato={store.HentetDato}");
        break;
    }
}
Console.WriteLine($"tid={watch.Elapsed.TotalSeconds:F1}s peakWorkingSet={Process.GetCurrentProcess().PeakWorkingSet64 / 1048576} MiB");

sealed class LogStore(string? hentetDato) : IFestStore
{
    public string? HentetDato { get; private set; } = hentetDato;
    public Task<string?> GetHentetDatoAsync(FestFilter filter, CancellationToken ct) => Task.FromResult(HentetDato);
    public Task ApplyAsync(FestFilter filter, M30Message message, bool fulltUttrekk, CancellationToken ct)
    {
        var n = message.ReadOppforinger().Count();
        Console.WriteLine($"{(fulltUttrekk ? "Fullt" : "Inkrement")}: {HentetDato ?? "(tomt)"} -> {message.HentetDato}, {n} oppføringer");
        HentetDato = message.HentetDato;
        return Task.CompletedTask;
    }
}
