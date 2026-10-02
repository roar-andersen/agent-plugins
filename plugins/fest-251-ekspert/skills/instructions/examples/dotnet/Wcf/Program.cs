using System.Diagnostics;
using Fest.M30;
using Fest.M30.Wcf;

// Bruk: stream <filter> [HentetDato] | typed <filter> [HentetDato] (krever generert proxy)
var endpoint = new Uri(Environment.GetEnvironmentVariable("FEST_ENDPOINT") ?? FestEndpoints.TestInternett.AbsoluteUri);
var filter = Enum.Parse<FestFilter>(args[1]);
var sist = args.Length > 2 ? args[2] : null;
var watch = Stopwatch.StartNew();

if (args[0] == "typed")
{
#if FEST_TYPED_PROXY
    var m = await TypedProxyExample.GetM30Async(endpoint, Enum.Parse<Fest.Wcf.FilterEnum>(filter.ToString()), sist, TimeSpan.FromMinutes(10));
    Console.WriteLine($"HentetDato={TypedProxyExample.HentetDatoSomTekst(m)} pakninger={m.KatLegemiddelpakning?.Length ?? 0} merkevarer={m.KatLegemiddelMerkevare?.Length ?? 0}");
#else
    Console.Error.WriteLine("Generer proxy først: dotnet-svcutil <endepunkt>?singleWsdl -n \"*,Fest.Wcf\" -o FestService251.cs");
    return 1;
#endif
}
else
{
    var file = Path.Combine(Path.GetTempPath(), "fest-wcf.xml");
    await FestWcf.DownloadAsync(endpoint, filter, sist, file, TimeSpan.FromMinutes(10));
    var message = M30Message.Open(file);
    var n = 0;
    foreach (var _ in message.ReadOppforinger()) n++;
    Console.WriteLine($"HentetDato={message.HentetDato} oppføringer={n} bytes={new FileInfo(file).Length}");
}
Console.WriteLine($"tid={watch.Elapsed.TotalSeconds:F1}s peakWorkingSet={Process.GetCurrentProcess().PeakWorkingSet64 / 1048576} MiB");
return 0;
