# Integrasjon mot FestService251.svc (C#/.NET)

Denne referansen utdyper [webservice, nedlasting og oppdatering](07-webservice-nedlasting-og-oppdatering.md) med tjenestekontrakten fra WSDL, testede observasjoner og klientimplementasjon i C#/.NET. Hold de fire kildetypene adskilt i svar:

| Status | Betydning |
|---|---|
| `DIREKTE_KILDE` | Står i DMPs grensesnittdokumentasjon eller implementeringsveiledning. |
| `AVLEDET_WSDL` | Lest ut av tjenestens WSDL (`?singleWsdl`). Teknisk kontrakt. |
| `TESTET` | Observert ved kall mot tjenesten 2026-10-02. Ikke dokumentert av DMP og kan endres. |
| `TOLKNING` | Implementasjonsråd utledet fra kildene og testene, ikke krav fra DMP. |

Kilder: `DMP-GRENSESNITT-2024-05-13` (grensesnittdokumentasjon, 13.05.2024), `DMP-IMPL-3.6` (implementeringsveiledning v3.6), `FEST-WSDL-251` (`FestService251.svc?singleWsdl` hentet 2026-10-02 fra produksjon og test på internett; kontraktene var identiske bortsett fra adressen), `TEST-2026-10-02` (testprotokollen nederst).

## Dokumenterte krav og implementasjonsråd fra DMP

Alias og søkeord: krav, implementasjonsråd, nattlig sjekk, staging, kontaktliste  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

- Systemet må alltid bruke siste versjon av FEST. DMP anbefaler automatisk sjekk etter oppdateringer hver natt. [DMP-IMPL-3.6, kap. 2.4.4]
- Ordinære oppdateringer kommer hver 14. dag, vanligvis to dager før de blir gjeldende. Ekstraordinære oppdateringer kan forekomme. [DMP-IMPL-3.6, kap. 2.4.4]
- DMP anbefaler alltid siste FEST-versjon (2.5.1 framfor 2.5.0). [DMP-IMPL-3.6, kap. 2.4.5]
- Kommende filer ligger i staging omtrent én uke før publisering. De bør rutinemessig importeres i et testmiljø. [DMP-IMPL-3.6, kap. 2.4.6]
- Bruk domenenavn, ikke IP-adresse. [DMP-GRENSESNITT-2024-05-13, s. 5]
- Ved inkrementelt uttrekk settes `SistOppdatert` til `HentetDato` fra forrige nedlastede melding. Kallet gjentas med ny `HentetDato` til mottatt `HentetDato` er lik parameteren. Lokal klokke skal ikke brukes. [DMP-GRENSESNITT-2024-05-13, s. 5; DMP-IMPL-3.6, kap. 13.3]
- Utgåtte oppføringer leveres bare i inkrementer, med bare `Id`, `Tidspunkt` og `Status`. En endring gir utgått gammel oppføring og ny aktiv oppføring med fullt innhold. Oppførings-ID-er trengs ikke ved fullt uttrekk. [DMP-IMPL-3.6, kap. 13.1]
- Ved ny M30N erstattes alle handelsvarer av mottatte varer for den nye tremånedersperioden. De siste 2–3 dagene før perioden ligger bare framtidig pris i FEST. [DMP-IMPL-3.6, kap. 13.2]
- Kun UTF-8 støttes. Tjenesten er sikret med HTTPS. Feil meldes til `fest@dmp.no`. [DMP-GRENSESNITT-2024-05-13, s. 6]
- Brukere anbefales å stå på DMPs kontaktliste for driftsmeldinger (e-post til `fest@dmp.no` med navn, firma, rolle, system og FEST-versjon). [DMP-IMPL-3.6, kap. 2.4.3]

## Endepunkter

Alias og søkeord: produksjon, staging, test, NHN, internett, URL  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE (tabell), TESTET (kolonnen «Testet»)

| Miljø | Nett | Endepunkt | Filtre ifølge dokumentasjonen | Testet 2026-10-02 |
|---|---|---|---|---|
| Produksjon | Internett | `https://fest.legemiddelverket.no/Fest/FestService251.svc` | Institusjon og Rekvirent (inkl. inkrementelt), Bandasjist, Veterinær | Ja |
| Test | Internett | `https://fest-test.legemiddelverket.no/TestFest/FestService251.svc` | Som produksjon | Ja |
| Produksjon | NHN | `https://frontend-fest.nhn.no/Fest/FestService251.svc` | Som produksjon | Nei, krever Helsenett |
| Staging | NHN | `https://frontend-fest.nhn.no/StagingFest/FestService251.svc` | Institusjon og Rekvirent (inkl. inkrementelt), Veterinær. **Ikke Bandasjist.** | Nei, krever Helsenett |
| Test | NHN | `https://frontend-fest-test.nhn.no/TestFest/FestService251.svc` | Som produksjon | Nei, krever Helsenett |

Staging eksponerer data før den offisielle filen publiseres. Staging finnes bare på NHN. [DMP-GRENSESNITT-2024-05-13, s. 4]

`TESTET`: Testmiljøet har en egen, eldre datatilstand som ikke følger produksjon. Ved testing var `HentetDato` 2026-02-05T13:50:27 for Rekvirent og 2025-10-15T08:52:48 for Veterinær og Institusjon. Bruk test til å teste protokollen, ikke til innholdet.

Dokumentasjonen oppgir også IP-adresser, men anbefaler sterkt domenenavn. Gi ikke IP-adresser uten at brukeren ber om dem.

## Tjenestekontrakt (WSDL)

Alias og søkeord: WSDL, singleWsdl, kontrakt, SOAP 1.2, WS-Addressing, Action, binding  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_WSDL

| Del | Verdi |
|---|---|
| WSDL-namespace | `http://www.slv.no/201410325/` |
| Port/binding | `WSHttpBinding_FestService251`, `soap12:binding`, `style="document"`, `use="literal"` |
| Policy | `sp:TransportBinding` med `HttpsToken RequireClientCertificate="false"` og `wsaw:UsingAddressing`. Ingen meldingssikkerhet, ingen klientsertifikat og ingen tidsstempel. |
| Operasjon | `GetM30` |
| Input-Action | `http://www.slv.no/201410325/FestService251/GetM30` |
| Output-Action | `http://www.slv.no/201410325/FestService251/GetM30Response` |

Forespørselselementet, i namespace `http://www.slv.no/201410325/` med `elementFormDefault="qualified"`:

```xml
<xs:element name="GetM30">
  <xs:complexType><xs:sequence>
    <xs:element minOccurs="1" maxOccurs="1" name="filter" type="tns:FilterEnum"/>
    <xs:element minOccurs="1" maxOccurs="1" name="incrementalDate" nillable="true" type="xs:dateTime"/>
  </xs:sequence></xs:complexType>
</xs:element>
```

`FilterEnum` har verdiene `Farmalogg`, `Rekvirent`, `Bandasjist`, `Veterinær`, `NAV` og `Institusjon`.

Svaret er `GetM30Response/GetM30Result` av typen `M30Response`, med sekvensen `Returkode` (`kith:CS`, 0..1) og deretter `M30Message` (type `FEST` i M30-namespace, 0..1).

Merk forskjellene fra grensesnittdokumentasjonen:

- Dokumentet kaller parameterne `Filter` og `SistOppdatert`. På XML-nivå heter de `filter` og `incrementalDate`. Bruk WSDL-navnene i kode og dokumentnavnene når protokollen forklares.
- Dokumentet viser `M30Message` før `Returkode`. WSDL-en og de faktiske svarene har `Returkode` først.
- WSDL-ens innebygde M30-skjema er serialiseringsgenerert og avviker fra de offisielle XSD-ene. Blant annet har `typeEnkeltoppforingFest/Id` og `Status` kardinalitet `0..1` i WSDL, men `1` i XSD. Bruk de offisielle XSD-ene ([teknisk XSD-referanse](08-teknisk-xsd-referanse.md)) for struktur og validering, ikke WSDL-typene.

## SOAP-versjon og WS-Addressing

Alias og søkeord: SOAP 1.1, SOAP 1.2, Action, To, MessageID, AddressFilter  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE, AVLEDET_WSDL og TESTET (se hver påstand)

- `DIREKTE_KILDE`: Dokumentasjonen sier at både SOAP 1.1 og 1.2 støttes, og at WS-Addressing `Action` og `To` må være med i headeren.
- `AVLEDET_WSDL`: WSDL-en for FestService251 har bare én SOAP 1.2-binding.
- `TESTET`: SOAP 1.2 (`Content-Type: application/soap+xml; charset=utf-8`) fungerer. SOAP 1.1 (`text/xml` med `SOAPAction`) ga HTTP 415 mot produksjon på internett. Konklusjon: bruk SOAP 1.2 for 2.5.1. SOAP 1.1-påstanden gjelder trolig eldre tjenester.
- `TESTET`: Uten WS-Addressing-header ga tjenesten HTTP 500 med fault «AddressFilter mismatch». `MessageID` er ikke påkrevd. Uten den mangler `RelatesTo` i svaret.
- `TOLKNING`: Sett `a:To` til nøyaktig endepunktet som kalles. Det må ikke være en konfigurert produksjonsadresse når testmiljøet kalles.

Minimal forespørsel som er testet (fullt uttrekk, Rekvirent, produksjon):

```xml
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
  <s:Header>
    <a:Action s:mustUnderstand="1">http://www.slv.no/201410325/FestService251/GetM30</a:Action>
    <a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID>
    <a:To s:mustUnderstand="1">https://fest.legemiddelverket.no/Fest/FestService251.svc</a:To>
  </s:Header>
  <s:Body>
    <GetM30 xmlns="http://www.slv.no/201410325/">
      <filter>Rekvirent</filter>
      <incrementalDate xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
    </GetM30>
  </s:Body>
</s:Envelope>
```

Ved inkrementelt uttrekk byttes `incrementalDate` ut med `<incrementalDate>2026-09-28T11:58:18</incrementalDate>`, altså mottatt `HentetDato` uendret. `incrementalDate` har `minOccurs="1"`. Send derfor elementet med `xsi:nil="true"` ved fullt uttrekk, og ikke utelat det.

## Filtre, fullt uttrekk og inkrementell oppdatering

Alias og søkeord: filter, Rekvirent, Institusjon, Veterinær, Bandasjist, NAV, Farmalogg, fullt, inkrementelt, serier  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE og TESTET

| Filter | Fullt uttrekk | Inkrementelt | Kilde |
|---|---|---|---|
| `Rekvirent` | Ja | Ja | DIREKTE_KILDE, TESTET |
| `Institusjon` | Ja | Ja | DIREKTE_KILDE, TESTET |
| `Veterinær` | Ja | Nei: Returkode 5 | DIREKTE_KILDE, TESTET |
| `Bandasjist` | Ja | Nei: Returkode 5 | DIREKTE_KILDE, TESTET |
| `NAV`, `Farmalogg` | Returkode 4 «Ugyldig filter spesifisert: … er ikke tilgjengelig på service» på de åpne internettendepunktene | – | AVLEDET_WSDL (finnes i enum), TESTET |

`TESTET`, oppførsel for inkrementelt uttrekk:

- Hvert kall returnerer én serie: endringene fram til neste publisering etter `incrementalDate`, med den publiseringens `HentetDato`. Fra `2026-07-08T14:02:26` trengte Rekvirent fem kall for å nå `2026-09-28T11:58:18`, og et sjette kall bekreftet at det ikke var flere serier. Løkken fra dokumentasjonen er altså nødvendig og ikke bare teoretisk.
- `incrementalDate` trenger ikke være en tidligere `HentetDato`. En vilkårlig dato ga serien fra neste publisering. Bruk likevel alltid forrige `HentetDato`, slik DMP krever.
- En svært gammel dato (2010-01-01) ga Returkode 5 «Ugyldig innkommende dato». Datoer tilbake til 2025-06-01 ble godtatt. Grensen er ikke dokumentert. Behandle Returkode 5 ved inkrementelt kall som at fullt uttrekk må kjøres på nytt.
- En dato i framtiden ga Returkode 1 og en melding med bare `HentetDato`, lik siste publisering. Det var ingen feil. En naiv løkke vil da skrive en eldre `HentetDato` tilbake. Klienten må avvise mottatt `HentetDato` som er eldre enn parameteren.
- Tjenesten så ut til å ignorere tidssoneangivelse og bruke klokkeslettet slik det står. Både `11:58:18+02:00` og `11:58:18Z` ga tomt svar mot `HentetDato` 11:58:18, mens `09:58:18Z` ga en hel serie. Send verdien uten offset, eksakt som mottatt. Ikke konverter til UTC eller lokal tid.

`TESTET`: Fullt uttrekk over webservice ga samme innhold som ZIP-filen fra DMP for samme publisering. Rekvirent hadde samme `HentetDato` og samme antall oppføringer per katalog (68 971 oppføringer). Svaret inneholdt ingen utgåtte oppføringer.

## `HentetDato`, `SistOppdatert` og tomme svar

Alias og søkeord: HentetDato, SistOppdatert, incrementalDate, tom melding, ferdig  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE og TESTET

- `DIREKTE_KILDE`: `HentetDato` er genereringstidspunktet for meldingen, ikke nedlastingstidspunktet. Det er normalt flere dager før meldingen publiseres. [DMP-IMPL-3.6, kap. 13.3]
- `DIREKTE_KILDE`: Selv ved `V=1` kan `M30Message` være tom. [DMP-GRENSESNITT-2024-05-13, s. 5]
- `TESTET`: «Tom» betydde i praksis en `M30Message` med bare `HentetDato` og ingen kataloger. Svaret var 682 byte. Dette er avslutningssignalet når `HentetDato` er lik parameteren. Når `HentetDato` er ulik, må det behandles som en feil tilstand, se over.
- `TOLKNING`: Lagre `HentetDato` som mottatt tekst, eller som `DateTime` med `Kind=Unspecified`, sammen med filter og miljø. Ikke bruk `datetimeoffset`, UTC-konvertering eller lokal klokke. Oppdater den lagrede verdien i samme transaksjon som dataene fra serien.

## Returkoder

Alias og søkeord: Returkode, V=1, V=4, V=5, V=8, feilkoder  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE og TESTET

| V | DN | Kilde | Når | Håndtering (`TOLKNING`) |
|---|---|---|---|---|
| `1` | OK | DIREKTE_KILDE | Vellykket. Kan være uten kataloger. | Behandle. |
| `4` | Ugyldig filter spesifisert: … | TESTET | `NAV`/`Farmalogg` på åpent endepunkt | Konfigurasjonsfeil. Ikke prøv på nytt. |
| `5` | Ugyldig innkommende dato | TESTET | `incrementalDate` med filter uten inkrementell støtte, eller for gammel dato | Konfigurasjonsfeil eller kjør fullt uttrekk. Ikke prøv på nytt med samme verdi. |
| `8` | Uventet feil | DIREKTE_KILDE | Feil på tjenesten | Forbigående. Prøv igjen med backoff og varsle ved gjentakelse. |

`TESTET`: Ved Returkode ulik 1 manglet `M30Message`. En filterverdi utenfor enum ga HTTP 500 med generell SOAP Fault, ikke en returkode. Behandle andre koder enn 1 som feil, og logg `V` og `DN`.

## Størrelse, komprimering, minne og tidsavbrudd

Alias og søkeord: meldingsstørrelse, gzip, komprimering, MaxReceivedMessageSize, minne, timeout, strømming  
FEST-versjon: 2.5.1  
Påstandsstatus: TESTET og TOLKNING

Målt 2026-10-02 mot produksjon på internett (`TESTET`; størrelser varierer med publisering):

| Svar | Størrelse | Tid |
|---|---:|---:|
| Fullt Rekvirent | 95,2 MB | ca. 11 s |
| Fullt Institusjon | 96,0 MB | ca. 11 s |
| Fullt Bandasjist | 9,1 MB | ca. 3 s |
| Fullt Veterinær | 6,0 MB | ca. 2,5 s |
| Inkrement Rekvirent, én serie (siste publisering) | 14,4 MB | 4–6 s |
| Inkrement Rekvirent, vanlig serie | 2–9 MB | 1–3 s |
| Tomt svar | 682 byte | under 0,1 s |

- `TESTET`: Tjenesten komprimerer ikke. Med `Accept-Encoding: gzip, deflate, br` kom svaret uten `Content-Encoding`, med `Content-Length` og ukomprimert. Svaret ble ikke chunked. DMPs ZIP-filer er ca. 14,5 MB for Rekvirent og Institusjon, men webservicen leverer ikke ZIP.
- `TOLKNING`: Standardgrensen i WCF (`MaxReceivedMessageSize` = 65 536) er altfor lav. Sett grensen høyt nok til fullt uttrekk med god margin, eller strøm svaret. `ReaderQuotas` må også heves for bufret WCF-deserialisering.
- `TESTET` (.NET 10, Linux x64, peak working set i hele prosessen): Strømming til fil og lesing én oppføring om gangen brukte ca. 90–100 MiB ved fullt Rekvirent. En generert WCF-proxy med bufret deserialisering til objektgraf brukte ca. 390 MiB. Komprimer lagrede kopier lokalt ved behov (gzip). Det er et lokalt valg (`TOLKNING`).
- `TOLKNING`: Bruk en total tidsgrense for hele kallet inkludert lesing av svaret. Ikke bruk bare tidsgrensen til headerne kommer. 10 minutter gir god margin over målt tid. `HttpClient.Timeout` dekker ikke lesing av body ved `HttpCompletionOption.ResponseHeadersRead`. I WCF er standardverdien for `SendTimeout`/`ReceiveTimeout` 1 minutt, som er for lavt på trege linjer.

## Feilbehandling

Alias og søkeord: retry, backoff, SOAP Fault, idempotens, transaksjon, kontrollpunkt  
FEST-versjon: 2.5.1  
Påstandsstatus: TOLKNING (med TESTET der det er angitt)

- `GetM30` er et lesekall, så å gjenta det er trygt. Prøv igjen med økende pause ved nettverksfeil, tidsavbrudd, avkortet XML (`XmlException`) og Returkode 8. Ikke prøv igjen ved Returkode 4/5 eller ved SOAP Fault. `TESTET`: Fault kommer som HTTP 500 med `s:Fault/s:Reason/s:Text`.
- Last ned til en midlertidig fil og flytt den på plass først når hele svaret er mottatt. Kontroller `Returkode` før innholdet brukes.
- Anvend hver serie i én transaksjon, sammen med ny lagret `HentetDato`. Avbrudd midt i en serie gir da ny henting av samme serie, ikke hull.
- Sammenlign mottatt og sendt `HentetDato`: lik betyr ferdig, nyere betyr anvend og fortsett, eldre betyr stopp med feil. Sett et øvre tak på antall serier per kjøring.
- Fullt uttrekk erstatter hele lokal tilstand for filteret og miljøet. Ikke bland data fra test, staging og produksjon, eller fra ulike filtre.
- Kjør nattlig (DMP-anbefaling), og varsle drift ved feil som gjentar seg. Ikke la en jobb som feiler stille gi utdaterte data. Varsle når lagret `HentetDato` blir eldre enn om lag 14 dager pluss margin.

## Klientimplementasjon i C#/.NET

Alias og søkeord: C#, .NET, HttpClient, XmlReader, WCF, System.ServiceModel, dotnet-svcutil, proxy  
FEST-versjon: 2.5.1  
Påstandsstatus: TESTET (koden) og TOLKNING (valgene)

Eksemplene ligger i `examples/dotnet/` ved siden av denne skillen. De sikter mot .NET 10 og er kompilert og kjørt mot tjenesten. Vis brukeren relevante deler, og ikke hele filer, når det holder.

| Variant | Filer | Avhengigheter | Minne ved fullt uttrekk | Egnet når |
|---|---|---|---|---|
| A. `HttpClient` + `XmlReader` | `HttpClient/FestM30Client.cs` | Bare BCL | ca. 90–100 MiB (strømming) | Nye løsninger, containere, full kontroll over dato og header |
| B1. WCF med `Message`-kontrakt | `Wcf/FestWcfClient.cs` | `System.ServiceModel.Http` og `.Primitives` 10.x | ca. 95 MiB (`TransferMode.StreamedResponse`) | Organisasjonen bruker allerede WCF-klienter |
| B2. WCF-proxy fra `dotnet-svcutil` | `Wcf/TypedProxyExample.cs` og generert kode | Som B1 | ca. 390 MiB (bufret) | Rask start og små filtre. Typene følger WSDL, ikke offisiell XSD. |

Felles byggeklosser i `FestM30Client.cs` (`TESTET`):

- `FestM30Client.DownloadAsync`: SOAP 1.2-konvolutt med `Action`, `MessageID` og `To`, `xsi:nil` ved fullt uttrekk, strømming til `.part`-fil, total tidsgrense og tolking av SOAP Fault.
- `M30Message.Open`: kontrollerer `Returkode` og leser `HentetDato` som tekst. `ReadOppforinger()` gir én `Oppf*`-oppføring om gangen med katalognavn. `SaveAsFestXml()` skriver et frittstående `FEST`-dokument. Den filen ble importert med pluginens `register` (Institusjon, 69 579 oppføringer).
- `FestUpdater`: fullt uttrekk ved tom tilstand, inkrementell løkke for Rekvirent/Institusjon, vern mot eldre `HentetDato`, øvre grense for antall serier, retry for forbigående feil og `IFestStore` for transaksjonell lagring.

Minimalt bruk (variant A):

```csharp
using var http = new HttpClient(new SocketsHttpHandler { PooledConnectionLifetime = TimeSpan.FromMinutes(5) });
var updater = new FestUpdater(new FestM30Client(http), store, workDirectory: Path.Combine(Path.GetTempPath(), "fest"));
var serier = await updater.UpdateAsync(FestEndpoints.ProduksjonInternett, FestFilter.Institusjon, cancellationToken);
```

`store` er brukerens implementasjon av `IFestStore`. Den skal lagre aktive oppføringer etter faglig ID, slette eller deaktivere etter oppførings-ID ved `Status V="U"`, og lagre `HentetDato` i samme transaksjon. Fullt uttrekk erstatter alt for filteret.

WCF-binding (B1/B2, `TESTET`): bruk SOAP 1.2 med WS-Addressing 1.0 over HTTPS.

```csharp
var binding = new CustomBinding(
    new TextMessageEncodingBindingElement(MessageVersion.Soap12WSAddressing10, Encoding.UTF8) { ReaderQuotas = XmlDictionaryReaderQuotas.Max },
    new HttpsTransportBindingElement { MaxReceivedMessageSize = long.MaxValue, TransferMode = TransferMode.StreamedResponse })
{ SendTimeout = TimeSpan.FromMinutes(10), ReceiveTimeout = TimeSpan.FromMinutes(10) };
```

`WSHttpBinding` med `SecurityMode.Transport`, som `dotnet-svcutil` genererer, fungerer også i bufret modus. `TESTET` med `MaxReceivedMessageSize = int.MaxValue` og `ReaderQuotas.Max`. Med `BasicHttpBinding` blir det SOAP 1.1 uten WS-Addressing, som ikke fungerer mot 2.5.1.

Generering av proxy (B2): `dotnet-svcutil https://fest.legemiddelverket.no/Fest/FestService251.svc?singleWsdl -n "*,Fest.Wcf" -o FestService251.cs`. Verktøyet legger til `System.ServiceModel.*` 4.10-pakker i prosjektet. Disse kan fjernes når 10.x-pakkene allerede er referert (`TESTET`). Konverter `HentetDato` med `XmlConvert.ToString(value, XmlDateTimeSerializationMode.Unspecified)` og tilbake med `XmlConvert.ToDateTime(..., Unspecified)`. Ikke bruk `ToUniversalTime()`.

`TESTET`: Pakken `System.ServiceModel.Http` 10.0.652802 drar inn `System.Security.Cryptography.Xml` 10.0.0, som har kjente sårbarheter (NU1903). Prosjektfilen løfter den eksplisitt til 10.0.12. Sjekk nyeste versjon når koden tas i bruk.

Kjøring av eksemplene: `dotnet run --project examples/dotnet/HttpClient -- update Rekvirent` (testmiljø som standard; sett `FEST_ENDPOINT` for et annet endepunkt). Kommandoene er `full <filter> [fest.xml]`, `inc <filter> <HentetDato>` og `update <filter> [HentetDato]`. Programmene er demonstrasjoner. Butikken (`LogStore`) skriver bare ut.

## Testprotokoll 2026-10-02

Alias og søkeord: testet, verifisert, testprotokoll  
FEST-versjon: 2.5.1  
Påstandsstatus: TESTET

Testet fra Linux med .NET SDK 10.0.112 mot produksjon og test på internett:

- WSDL fra produksjon og test var identisk bortsett fra adressen. Kontrakten er gjengitt over.
- Rå SOAP via `curl`/nettleser: SOAP 1.2 OK, SOAP 1.1 gir HTTP 415, manglende WS-Addressing gir HTTP 500 (AddressFilter), ingen komprimering.
- Alle seks filterverdier, fullt og inkrementelt der relevant, samt returkodene 1, 4 og 5 med ugyldige og framtidige datoer.
- Variant A: `full`, `inc` og `update` (fem serier og stopp), avvisning av Bandasjist med dato (klientvalidering), Returkode 5 og framtidig dato. `SaveAsFestXml` og import med pluginens `register`/`search`.
- Variant B1: fullt og inkrementelt uttrekk, Returkode 5. Variant B2: fullt og inkrementelt uttrekk med generert proxy.
- Fullt Rekvirent over webservice sammenlignet med `fest251.zip`: lik `HentetDato` og likt antall oppføringer per katalog.

Ikke testet: NHN-endepunktene (produksjon, staging, test) krever Helsenett. Returkode 8, faktiske nettverksbrudd og retry-forløp er ikke fremprovosert. Windows/.NET Framework er ikke testet. Ingen XSD-validering av svarene er gjort, fordi de offisielle XSD-filene ikke var tilgjengelige fra testmiljøet. `IFestStore` mot database er ikke implementert i eksemplene.
