# Legemiddel, pakning, refusjon og bytte

## `LegemiddelVirkestoff`

XML-navn: `LegemiddelVirkestoff`  
Alias og søkeord: legemiddelvirkestoff, virkestoffrekvirering, katalog virkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `OppfLegemiddelVirkestoff` i `KatLegemiddelVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`LegemiddelVirkestoff` er hovednivået for virkestoffrekvirering. Det arver felles legemiddelinformasjon og har `Id` samt listene `SortertVirkestoffMedStyrke`, `SortertVirkestoffUtenStyrke`, `RefLegemiddelMerkevare`, `RefPakning` og `ForskrivningsenhetResept`. De to direktereferansene gjør det mulig å finne relevante merkevarer og pakninger for en gitt virkestoffrekvirering. [DMP-IMPL-3.6, PDF-side 16-17 og 25-27, kapittel 3.2.1 og 3.3.1; XSD-FORSKRIVNING-FULL-2014-12-01, `/schema/element[@name='LegemiddelVirkestoff']`; visuelt kontrollert figur 6]

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `xs:ID` | `1` | Identifikator for legemiddelvirkestoffet. | AVLEDET_XSD | XSD-FORSKRIVNING-FULL-2014-12-01 |
| `SortertVirkestoffMedStyrke` | `fs:SortertVirkestoffMedStyrke` | `0..*` (`1..*` i praksis) | Ordnet referanse til virkestoff med styrke. | AVLEDET_XSD / DIREKTE_KILDE | XSD; DMP-IMPL-3.6 side 28 |
| `RefLegemiddelMerkevare` | `xs:IDREF` | `0..*` | Direktereferanse til relevante merkevarer. | AVLEDET_XSD | XSD-FORSKRIVNING-FULL-2014-12-01 |
| `RefPakning` | `xs:IDREF` | `0..*` | Direktereferanse til relevante pakninger. | AVLEDET_XSD | XSD-FORSKRIVNING-FULL-2014-12-01 |
| `ForskrivningsenhetResept` | `kith:CV` | `0..*` | Enheter som kan brukes ved rekvirering. | AVLEDET_XSD | XSD-FORSKRIVNING-FULL-2014-12-01 |

### Relasjoner

`LegemiddelVirkestoff` kobles til `VirkestoffMedStyrke` via `SortertVirkestoffMedStyrke/RefVirkestoffMedStyrke` og til merkevare/pakning via direktereferansene. 

### Regler og begrensninger

Humane og veterinære ATC-koder må skilles i Farmalogg-kontekst slik at veterinære pakninger ikke vises ved ekspedering av human virkestoffresept. [DMP-IMPL-3.6, PDF-side 26, kapittel 3.3.5]

### Praktisk bruk

Bruk `RefLegemiddelMerkevare` og `RefPakning` når målet er å finne hvilke produkter som representeres av virkestoffrekvireringen. For detaljer om styrke følges `SortertVirkestoffMedStyrke` til `VirkestoffMedStyrke`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01`, globalt element `LegemiddelVirkestoff`.
- `DMP-IMPL-3.6`, side 16-17 og 25-28.

## `LegemiddelMerkevare`

XML-navn: `LegemiddelMerkevare`  
Alias og søkeord: merkevare, varenavn, legemiddelform, reseptgyldighet  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `OppfLegemiddelMerkevare` og `Pakningsinfo/RefLegemiddelMerkevare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`LegemiddelMerkevare` beskriver en navngitt merkevare med blant annet `Varenavn`, `LegemiddelformLang`, sorterte virkestoffreferanser, `Smak`, `ProduktInfo`, `Reseptgyldighet`, `Hjelpestoff` og `Preparatomtaleavsnitt`, i tillegg til arvede legemiddelfelter. Veiledningen anbefaler ikke rekvirering direkte på merkevarenivå, men nivået brukes sentralt ved mapping og visning. [DMP-IMPL-3.6, PDF-side 18-19, kapittel 3.2.2; XSD-FORSKRIVNING-FULL-2014-12-01, globalt element `LegemiddelMerkevare`; visuelt kontrollert figur 8]

### Innhold

Se `08-teknisk-xsd-referanse.md` for komplett elementliste og eksakte kardinaliteter.

### Relasjoner

Pakninger peker til merkevaren via `Pakningsinfo/RefLegemiddelMerkevare`. `Legemiddeldose` peker direkte med `RefLegemiddelMerkevare`.

### Regler og begrensninger

`Id` er `0..1` i XSD. Ikke gjør den obligatorisk uten eksplisitt forretningsgrunnlag.

### Praktisk bruk

Bruk merkevaren for detaljert produktnavn, lang legemiddelform, reseptgyldighet og grunnlag for mapping til dose og pakning.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01`, globalt element `LegemiddelMerkevare`.
- `DMP-IMPL-3.6`, side 18-19 og 25-28.

## `Legemiddelpakning`

XML-navn: `Legemiddelpakning`  
Alias og søkeord: pakning, varenummer, EAN, pris, markedsføring, pakningsinformasjon  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `OppfLegemiddelpakning` i `KatLegemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Legemiddelpakning` beskriver en bestemt pakning. Egne elementer er `Id`, obligatorisk `Varenr`, `Ean`, `IkkeKonservering`, `Oppbevaring`, `Pakningsinfo`, `PakningsinfoResept`, `PrisVare`, `Markedsforingsinfo` og `Preparatomtaleavsnitt`. `Pakningsinfo` gir pakningsstørrelse, enhet, pakningstype og referanse til merkevare. [XSD-FORSKRIVNING-FULL-2014-12-01, globale elementer `Legemiddelpakning` og `Pakningsinfo`; DMP-IMPL-3.6, PDF-side 20-21 og 45-50; visuelt kontrollert figur 10]

### Innhold

I `Pakningsinfo` er `RefLegemiddelMerkevare` `0..*` i XSD, men `1..*` i faktisk FEST-innhold. Flere enn én brukes ved flerstyrkepakninger. `Pakningsstr` og `EnhetPakning` skal forstås sammen; `Antall` beskriver flere beholdere i samme pakning, og `Multippel` brukes ved flere pakninger under samme varenummer. [DMP-IMPL-3.6, PDF-side 28 og 45-49, kapittel 3.4 og 6.2.1; visuelt kontrollert figur 19-21]

### Relasjoner

`Pakningsinfo/RefLegemiddelMerkevare` kobler pakningen til én eller flere merkevarer. `PakningByttegruppe/RefByttegruppe` kobler til en byttegruppe. `Refusjon/RefRefusjonsgruppe` kobler til refusjonsgruppen.

### Regler og begrensninger

Datoene i `Markedsforingsinfo` og pris-/refusjonsstrukturene har egne betydninger. Oppføringsstatus må ikke brukes som erstatning for disse faglige gyldighetsperiodene.

### Praktisk bruk

Bruk `Varenr` ved identifikasjon av handelsført pakning, men bruk stabile FEST-ID-er og oppføringsmetadata korrekt ved oppdatering.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01`, `Legemiddelpakning`, `Pakningsinfo`, `Markedsforingsinfo`.
- `DMP-IMPL-3.6`, side 45-54.

## Refusjon og byttegruppe

Alias og søkeord: `Refusjon`, `Refusjonshjemmel`, `Refusjonsgruppe`, `Refusjonskode`, `Byttegruppe`  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`Refusjon` på vare eller legemiddel inneholder én eller flere `RefRefusjonsgruppe`, obligatorisk `GyldigFraDato` og valgfrie `ForskrivesTilDato` og `UtleveresTilDato`. Katalogen `KatRefusjon` inneholder `Refusjonshjemmel`, som igjen har én eller flere `Refusjonsgruppe`. En `Refusjonsgruppe` inneholder blant annet `GruppeNr`, eventuell `Atc`, `KreverRefusjonskode`, eventuell `RefusjonsberettighetBruk`, `RefVilkar` og `Refusjonskode`. [XSD-FORSKRIVNING-FULL-2014-12-01, `Refusjon`; XSD-M30-FULL-2014-12-01, `Refusjonshjemmel` og `Refusjonsgruppe`; HIS-3020-2018, PDF-side 21-23, kapittel 6.2.8]

Bytteinformasjon knytter en pakning til `Byttegruppe` gjennom `PakningByttegruppe`, med egne gyldighetsdatoer. Ikke anta at selve referansen alene avgjør om byttet er gyldig på en bestemt dato; datoene må vurderes. [DMP-IMPL-3.6, PDF-side 53-54, kapittel 6.5; XSD-FORSKRIVNING-FULL-2014-12-01, globalt element `PakningByttegruppe`; XSD-M30-FULL-2014-12-01, `Byttegruppe`]
