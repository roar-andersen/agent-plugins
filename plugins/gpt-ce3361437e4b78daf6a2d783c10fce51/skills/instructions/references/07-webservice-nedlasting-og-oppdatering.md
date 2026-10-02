# Webservice, nedlasting og oppdatering

## Tjenestemodell og `GetM30`

Alias og søkeord: WCF, SOAP, `GetM30`, `m30Response`, WS-Addressing  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

FEST er dokumentert som en standard synkron WCF-webservice med request-response. Både SOAP 1.1 og SOAP 1.2 støttes. Metoden `GetM30` har parameterne `Filter` og `SistOppdatert` og returnerer `m30Response`. WS-Addressing brukes, slik at `Action` og `To` må være med i SOAP-headeren. Eksempelet i kilden viser en eldre tjenestevariant; for 2.5.1 skal tjenestenavnet være `FestService251`, og klienten bør hente kontraktens faktiske Action/To fra 2.5.1-tjenestens metadata. [DMP-GRENSESNITT-2024-05-13, PDF-side 4-5, kapittel 3]

`m30Response` inneholder `M30Message` og `Returkode`. Dokumenterte returkoder er `V=1` for OK og `V=8` for uventet feil. Selv ved `V=1` kan `M30Message` være tom. [DMP-GRENSESNITT-2024-05-13, PDF-side 5, `m30Response`]

## Filtre

Alias og søkeord: filter, Rekvirent, Institusjon, Bandasjist, Veterinær, inkrementell  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`Filter` velger variant av FEST-meldingen: Rekvirent, Bandasjist, Veterinær eller Institusjon i webservice-tabellen. `SistOppdatert` kan bare brukes sammen med Rekvirent og Institusjon. Filteret påvirker hvilket kataloginnhold mottakeren får; spørsmål om forventet innhold bør derfor alltid angi filter og om uttrekket er fullt eller inkrementelt. [DMP-GRENSESNITT-2024-05-13, PDF-side 4-5, kapittel 3 og `GetM30`]

## Produksjon, staging og test

Alias og søkeord: endepunkt, produksjon, staging, test, `FestService251.svc`  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

| Miljø | Nett | Vert | Tjenestesti |
|---|---|---|---|
| Produksjon | NHN | `frontend-fest.nhn.no` | `Fest/FestService251.svc` |
| Produksjon | Internett | `fest.legemiddelverket.no` | `Fest/FestService251.svc` |
| Staging | NHN | `frontend-fest.nhn.no` | `StagingFest/FestService251.svc` |
| Test | NHN | `frontend-fest-test.nhn.no` | `TestFest/FestService251.svc` |
| Test | Internett | `fest-test.legemiddelverket.no` | `TestFest/FestService251.svc` |

Dette er nøyaktig dokumenterte adresser i grensesnittdokumentet datert 13.05.2024. Domener og drift kan endres etter dokumentdatoen; kunnskapsgrunnlaget gir ikke sanntidsbekreftelse. DMP anbefaler domenenavn fremfor IP-adresse for å unngå problemer ved IP-bytte. [DMP-GRENSESNITT-2024-05-13, PDF-side 4-5, kapittel 3]

## Oppdateringsløkken

Alias og søkeord: `SistOppdatert`, `HentetDato`, paginering, serie, inkrement  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

For et fullt uttrekk utelates `SistOppdatert`. For et inkrement brukes `HentetDato` fra sist ferdig behandlet melding som `SistOppdatert`. Hvis svaret har en annen `HentetDato`, behandles serien og neste kall gjøres med den nye verdien. Løkken avsluttes når mottatt `HentetDato` er lik parameteren. Klientens lokale klokke skal ikke brukes som erstatning. [DMP-GRENSESNITT-2024-05-13, PDF-side 5, `GetM30`; HIS-3020-2018, PDF-side 10, `HentetDato`]

## Kommunikasjon, sikkerhet og feil

Alias og søkeord: UTF-8, HTTPS, base64, feil, kontakt  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

DMP støtter bare UTF-8. Signerte dokumenter må være Base64-kodet. WCF-webservicen er sikret med HTTPS. Feil og kontaktinformasjon for FEST meldes til `fest@dmp.no`. [DMP-GRENSESNITT-2024-05-13, PDF-side 6, kapittel 4-6]

## Publiseringsrytme og staging

Alias og søkeord: oppdateringsfrekvens, hver 14. dag, nattlig sjekk, staging-fil  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Ordinære oppdateringer skjer hver 14. dag, vanligvis to dager før innholdet blir gjeldende. DMP anbefaler automatisk nattlig sjekk etter ny FEST-versjon. Kommende filer er normalt tilgjengelige i staging omtrent én uke før publisering, og veiledningen anbefaler rutinemessig innlasting i testmiljø for å avdekke konsekvenser av innholdsendringer. [DMP-IMPL-3.6, PDF-side 13-14, kapittel 2.4.4-2.4.6]
