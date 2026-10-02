# Fullt og inkrementelt uttrekk

## Felles informasjonsinnhold og skjemavarianter

Alias og søkeord: fullt uttrekk, inkrementelt uttrekk, loose XSD, IDREF, string  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

Fullt og inkrementelt uttrekk bruker samme M30-rot, kataloger, oppføringsstruktur og faglige elementer. Forskjellen i de publiserte XSD-parene er at loose-skjemaene for inkrementell validering erstatter 24 konkrete `xs:IDREF`-forekomster med `xs:string`. Årsaken står i skjemaenes kommentar: et inkrement kan inneholde en referanse uten at den refererte forekomsten finnes i den samme XML-filen. Alle øvrige sammenlignede element- og kardinalitetsstrukturer er like. [XSD-M30-INCREMENTAL-2014-12-01 og XSD-FORSKRIVNING-INCREMENTAL-2014-12-01, innledende kommentar; programmatisk sammenligning i `structured/fest-2.5.1-schema.json#/extractVariants/structuralDifferences`]

Bruk fullt-skjemaene når alle refererte ID-er forventes å være i samme uttrekk. Bruk loose-skjemaene ved inkrementell validering. Ikke tolk `string` i loose-skjemaet som at referansen har mistet sin semantiske betydning; det er en valideringstilpasning.

## `typeEnkeltoppforingFest`

Alias og søkeord: oppførings-ID, registreringstidspunkt, registreringsstatus, aktiv, utgått  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Alle konkrete katalogoppføringer utvider `typeEnkeltoppforingFest`. `Id` er den unike oppførings-ID-en, `Tidspunkt` er tidspunktet oppføringen fikk gjeldende status og innhold, og `Status` angir aktiv eller utgått. Når innhold endres, settes den gamle oppføringen til utgått og en ny aktiv oppføring med ny oppførings-ID opprettes. Identifikatoren i den faglige klassen, for eksempel `Legemiddelpakning/Id`, er normalt stabil gjennom innholdsendringen. [HIS-3020-2018, PDF-side 10-11, kapittel 6.2.2; DMP-IMPL-3.6, PDF-side 72-73, kapittel 13.1]

En utgått oppføring leveres bare i inkrementelt uttrekk og kan inneholde kun `Id`, `Tidspunkt` og `Status`, uten det faglige objektet. Dette forklarer hvorfor de konkrete objektene under `Oppf...` vanligvis har skjemakardinalitet `0..1`. For en endret legemiddelpakning inneholder den nye aktive oppføringen hele den nye pakningsinformasjonen, også felter som ikke ble endret. [DMP-IMPL-3.6, PDF-side 72-74, kapittel 13.1; XSD-M30-FULL-2014-12-01, konkrete `Oppf...`-strukturer]

## Sletting, endring og gyldighetsperioder

Alias og søkeord: sletting, utgått oppføring, endring, gyldighetsdato, historikk  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Tre hendelser behandles gjennom oppføringsstatus: ny oppføring gir ny oppførings-ID; endring gir en utgått gammel oppføring og en ny aktiv oppføring; bortfall gir utgått status. Dette må ikke forveksles med faglige datoer under objektet, som prisperiode, markedsføringsdato, refusjonsperiode, byttegruppens gyldighet eller varselets gyldighetsperiode. Oppføringsstatus beskriver historikken til FEST-oppføringen; underliggende datoer beskriver faglig gyldighet. [DMP-IMPL-3.6, PDF-side 72-74, kapittel 13.1; HIS-3020-2018, PDF-side 10-11, kapittel 6.2.2]

## `HentetDato` og `SistOppdatert`

Alias og søkeord: `HentetDato`, `SistOppdatert`, inkrementell løkke, neste kall  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`HentetDato` er første element i `FEST` og inneholder dato og klokkeslett for genereringen av M30. Navnet kan misforstås som faktisk nedlastingstid, men grensesnitt- og implementeringsveiledningen presiserer at det er datagrunnlagets/genereringens tidspunkt. Ved neste inkrementelle kall skal `SistOppdatert` settes til den forrige meldingens `HentetDato`, nøyaktig som mottatt. [DMP-IMPL-3.6, PDF-side 74, kapittel 13.3; DMP-GRENSESNITT-2024-05-13, PDF-side 5, `GetM30`; HIS-3020-2018, PDF-side 10, `HentetDato`]

Grensesnittdokumentasjonen beskriver en gjentakelsesregel: Hvis mottatt `HentetDato` er forskjellig fra `SistOppdatert`, skal kallet gjentas med den mottatte `HentetDato` som ny parameter. Fortsett til verdiene er like. Dette håndterer at tjenesten kan returnere endringer i flere serier. [DMP-GRENSESNITT-2024-05-13, PDF-side 5, `GetM30`]

## Handelsvarer ved periodeoppdatering

Alias og søkeord: M30N, handelsvare, tremånedersperiode, pris  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Ved innlesing av ny M30N erstattes eksisterende handelsvarer av mottatte varer med pris for ny tremånedersperiode. Veiledningen advarer om at bare fremtidig pris kan ligge i FEST de siste dagene før perioden starter. Mottakerens prislogikk må derfor behandle gyldighetsdatoene eksplisitt. [DMP-IMPL-3.6, PDF-side 74, kapittel 13.2]

## Robust oppdateringsalgoritme

Alias og søkeord: algoritme, transaksjonell innlasting, idempotens, kontrollpunkt  
FEST-versjon: 2.5.1  
Påstandsstatus: TOLKNING

En robust mottaker kan: validere XML med riktig skjemapar; kontrollere at `HentetDato` kan leses; behandle alle utgåtte og aktive oppføringer samlet; oppdatere faglige forekomster etter stabil faglig ID; lagre siste ferdig anvendte `HentetDato`; og først deretter be om neste inkrement. Transaksjonell lagring, idempotens og lokalt kontrollpunkt er implementasjonsråd utledet fra protokollen, ikke eksplisitte FEST-krav. Når dette beskrives i et svar, merk det `TOLKNING`.
