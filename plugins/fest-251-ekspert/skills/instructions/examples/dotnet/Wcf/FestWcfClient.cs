using System.ServiceModel;
using System.ServiceModel.Channels;
using System.Text;
using System.Xml;
using Fest.M30;

namespace Fest.M30.Wcf;

[ServiceContract(Namespace = "http://www.slv.no/201410325/", Name = "FestService251")]
public interface IFestService251Raw
{
    [OperationContract(Action = "http://www.slv.no/201410325/FestService251/GetM30", ReplyAction = "*")]
    Task<Message> GetM30Async(Message request);
}

public static class FestWcf
{
    public const string ServiceNs = "http://www.slv.no/201410325/";

    /// <summary>SOAP 1.2 + WS-Addressing 1.0 over HTTPS, samme som tjenestens WSHttpBinding med Transport-sikkerhet.</summary>
    public static Binding CreateBinding(TimeSpan timeout, bool streamed) => new CustomBinding(
        new TextMessageEncodingBindingElement(MessageVersion.Soap12WSAddressing10, Encoding.UTF8)
        {
            ReaderQuotas = XmlDictionaryReaderQuotas.Max
        },
        new HttpsTransportBindingElement
        {
            MaxReceivedMessageSize = streamed ? long.MaxValue : int.MaxValue,
            MaxBufferSize = int.MaxValue,
            TransferMode = streamed ? TransferMode.StreamedResponse : TransferMode.Buffered
        })
    {
        SendTimeout = timeout,
        ReceiveTimeout = timeout,
        OpenTimeout = TimeSpan.FromMinutes(1),
        CloseTimeout = TimeSpan.FromMinutes(1)
    };

    /// <summary>Strømmer SOAP-body til fil. Resultatet leses med M30Message.Open.</summary>
    public static async Task DownloadAsync(Uri endpoint, FestFilter filter, string? sistOppdatert, string targetFile, TimeSpan timeout)
    {
        var factory = new ChannelFactory<IFestService251Raw>(CreateBinding(timeout, streamed: true), new EndpointAddress(endpoint));
        var channel = factory.CreateChannel();
        try
        {
            var request = Message.CreateMessage(MessageVersion.Soap12WSAddressing10,
                "http://www.slv.no/201410325/FestService251/GetM30", new GetM30BodyWriter(filter, sistOppdatert));
            using var reply = await channel.GetM30Async(request);
            if (reply.IsFault)
                throw new FestException("SOAP Fault: " + MessageFault.CreateFault(reply, int.MaxValue).Reason.GetMatchingTranslation().Text);

            var temp = targetFile + ".part";
            using (var body = reply.GetReaderAtBodyContents())
            using (var writer = XmlWriter.Create(temp, new XmlWriterSettings { Encoding = new UTF8Encoding(false) }))
                writer.WriteNode(body, defattr: true);
            File.Move(temp, targetFile, overwrite: true);

            ((ICommunicationObject)channel).Close();
            factory.Close();
        }
        catch
        {
            ((ICommunicationObject)channel).Abort();
            factory.Abort();
            throw;
        }
    }

    private sealed class GetM30BodyWriter(FestFilter filter, string? sistOppdatert) : BodyWriter(isBuffered: true)
    {
        protected override void OnWriteBodyContents(XmlDictionaryWriter writer)
        {
            writer.WriteStartElement("GetM30", ServiceNs);
            writer.WriteElementString("filter", ServiceNs, filter.ToString());
            writer.WriteStartElement("incrementalDate", ServiceNs);
            if (sistOppdatert is null)
                writer.WriteAttributeString("xsi", "nil", "http://www.w3.org/2001/XMLSchema-instance", "true");
            else
                writer.WriteString(sistOppdatert);
            writer.WriteEndElement();
            writer.WriteEndElement();
        }
    }
}
