# FEST 2.5.1: oversikt og begreper

## Formål og innhold

Alias og søkeord: hva er FEST, legemiddeldata, reseptkjeden, datagrunnlag  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Forskrivnings- og ekspedisjonsstøtte (FEST) er et felles datagrunnlag med oppdatert legemiddelinformasjon for aktørene i reseptkjeden. FEST inneholder varer som kan rekvireres eller ordineres i Norge: legemidler, medisinsk utstyr og næringsmidler til medisinsk bruk, forutsatt at varene er i salg i det norske markedet med nasjonalt varenummer. Veiledningen nevner blant annet markedsførte legemidler, sykehusproduserte legemidler, NAF-preparater, uregistrerte legemidler, enkelte kosttilskudd og refusjonsberettigede handelsvarer. Institusjonsuttrekket kan dessuten inneholde ompakkede endoser og bulkpakninger for ompakking i apotek. [DMP-IMPL-3.6, PDF-side 7-9, kapittel 1, 2.1 og 2.2]

FEST er en informasjonsmodell og XML-melding. Det stilles ikke krav om en bestemt fysisk lagringsmodell hos mottakeren. Den generelle Forskrivning-modellen gjenbrukes i flere e-reseptmeldinger; M30 inneholder katalogstrukturen og FEST-spesifikke felter. Ved skjemabruk må M30- og Forskrivning-XSD behandles samlet. [DMP-IMPL-3.6, PDF-side 9, kapittel 2.2; HIS-3020-2018, PDF-side 5, kapittel 1.1]

## Kataloger og innfallsvinkler

Alias og søkeord: katalog, nivå, hovedkatalog, `KatLegemiddelVirkestoff`, `KatHandelsvare`  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

FEST organiserer innholdet i kataloger. Fem kataloger fungerer som hovedinnfallsvinkler for rekvirering:

- `KatLegemiddelVirkestoff` gir oppføringer for virkestoffrekvirering.
- `KatLegemiddelMerkevare` gir en bestemt merkevare med styrke og form.
- `KatLegemiddelpakning` gir bestemte pakninger og varenummer.
- `KatLegemiddeldose` gir minste plukkbare enhet representert med LMR-nummer når det finnes.
- `KatHandelsvare` gir refusjonsberettigede næringsmidler, medisinsk forbruksmateriell og brystproteser.

Andre kataloger leverer støtteinformasjon, blant annet `KatVirkestoff`, `KatRefusjon`, `KatVilkar`, `KatByttegruppe`, `KatInteraksjon`, `KatVarselSlv`, `KatKodeverk`, `KatDiagnose`, `KatStrDosering` og `KatOrdineringVirkestoff`. Roten `FEST` kan inneholde hver av de 15 katalogene med skjemakardinalitet `0..1`. Hver katalog inneholder sine oppføringer med `0..*` i XSD. [DMP-IMPL-3.6, PDF-side 10, kapittel 2.3 og visuelt kontrollert figur 2; HIS-3020-2018, PDF-side 9-10, kapittel 6.2; XSD-M30-FULL-2014-12-01, `/schema/element[@name='FEST']`]

## Sentrale begreper

Alias og søkeord: administrering, ATC, rekvirering, oppføring, katalog  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`Administrasjonsvei` er veien et legemiddel tas inn i kroppen, for eksempel oralt eller intravenøst. Administrering betyr å gi eller ta et legemiddel. ATC er anatomisk, terapeutisk og kjemisk klassifisering. Rekvirering er å foreskrive legemiddel, næringsmiddel eller medisinsk forbruksmateriell. En katalogoppføring er pakket inn i en `Oppf...`-struktur som bygger på `typeEnkeltoppforingFest` med `Id`, `Tidspunkt` og `Status`. [DMP-IMPL-3.6, PDF-side 75-77, kapittel 14; HIS-3020-2018, PDF-side 10-11, kapittel 6.2.2]

## Filtre og oppdatering

Alias og søkeord: Rekvirent, Institusjon, Veterinær, Bandasjist, filter, staging  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Veiledningen beskriver filtrene Rekvirent, Institusjon, Veterinær, Bandasjist, NAV og Farmalogg. Grensesnittdokumentasjonen viser at 2.5.1-tjenesten tilbyr Institusjon, Rekvirent, Bandasjist og Veterinær, og at inkrementell henting støttes for Institusjon og Rekvirent. Ordinære oppdateringer skjer hver 14. dag. DMP anbefaler automatisk nattlig kontroll og rutinemessig innlasting av staging-filer i et testmiljø før publisering. [DMP-IMPL-3.6, PDF-side 13-14, kapittel 2.4.4-2.4.6; DMP-GRENSESNITT-2024-05-13, PDF-side 4-5, kapittel 3]
