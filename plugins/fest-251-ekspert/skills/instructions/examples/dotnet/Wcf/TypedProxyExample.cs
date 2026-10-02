using System.ServiceModel;
using System.Xml;
using Fest.M30;
using Fest.M30.Wcf;

namespace Fest.M30.Wcf;

/// <summary>
/// Generert proxy fra dotnet-svcutil. Enkel, men hele svaret deserialiseres i minnet.
/// Kompileres bare når ServiceReference/FestService251.cs finnes.
/// </summary>
public static class TypedProxyExample
{
    public static async Task<Fest.Wcf.FEST> GetM30Async(Uri endpoint, Fest.Wcf.FilterEnum filter, string? sistOppdatert, TimeSpan timeout)
    {
        var client = new Fest.Wcf.FestService251Client(FestWcf.CreateBinding(timeout, streamed: false), new EndpointAddress(endpoint));
        try
        {
            // Unspecified bevarer klokkeslettet slik det ble mottatt. Ikke konverter til UTC eller lokal tid.
            DateTime? incrementalDate = sistOppdatert is null
                ? null
                : XmlConvert.ToDateTime(sistOppdatert, XmlDateTimeSerializationMode.Unspecified);
            var result = (await client.GetM30Async(filter, incrementalDate)).GetM30Result;
            await client.CloseAsync();

            if (result?.Returkode?.V != "1")
                throw new FestReturkodeException(result?.Returkode?.V ?? "", result?.Returkode?.DN);
            return result.M30Message ?? throw new FestException("Returkode er OK, men M30Message mangler.");
        }
        catch
        {
            client.Abort();
            throw;
        }
    }

    public static string HentetDatoSomTekst(Fest.Wcf.FEST message) =>
        XmlConvert.ToString(message.HentetDato, XmlDateTimeSerializationMode.Unspecified);
}
