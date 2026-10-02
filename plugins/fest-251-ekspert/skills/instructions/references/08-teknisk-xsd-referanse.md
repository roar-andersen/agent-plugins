# Teknisk XSD-referanse for FEST 2.5.1

Denne referansen er generert programmatisk fra M30- og Forskrivning-XSD-ene datert 2014-12-01. Bare globale elementer som kan nås fra M30-roten `FEST`, er med. Kardinaliteter er avledet direkte fra XSD; `maxOccurs="unbounded"` vises som `*`.

Kilderolle: `XML_STRUKTUR`  
Påstandsstatus for strukturelle opplysninger: `AVLEDET_XSD`

## Namespaces og skjemaer

| Prefiks i kildene | Namespace | Fil | Rolle |
|---|---|---|---|
| `m30` | `http://www.kith.no/xmlstds/eresept/m30/2014-12-01` | `er-m30-2014-12-01.xsd` | M30-struktur og kataloger |
| `fs` | `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01` | `forskrivning-2014-12-01.xsd` | Gjenbrukte Forskrivning-elementer |
| `kith` | `http://www.kith.no/xmlstds` | `kith.xsd` | Felles datatyper som `CV`, `CS`, `PQ` og `MO` |
| `xs` | `http://www.w3.org/2001/XMLSchema` | XML Schema | Primitive datatyper |

Kilder: `XSD-M30-FULL-2014-12-01` `/schema/import`; `XSD-FORSKRIVNING-FULL-2014-12-01` `/schema/import`.

## FEST

XML-navn: `FEST`  
Alias og søkeord: fest, FEST FEST  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST` (rot)  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`FEST` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `HentetDato` | `dateTime` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[1]` |
| `GyldigFradatoHelfo` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[2]` |
| `KatLegemiddelMerkevare` | `ref:m30:KatLegemiddelMerkevare` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[3]` |
| `KatLegemiddelpakning` | `ref:m30:KatLegemiddelpakning` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[4]` |
| `KatVirkestoff` | `ref:m30:KatVirkestoff` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[5]` |
| `KatOrdineringVirkestoff` | `ref:m30:KatOrdineringVirkestoff` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[6]` |
| `KatLegemiddelVirkestoff` | `ref:m30:KatLegemiddelVirkestoff` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[7]` |
| `KatHandelsvare` | `ref:m30:KatHandelsvare` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[8]` |
| `KatDiagnose` | `ref:m30:KatDiagnose` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[9]` |
| `KatRefusjon` | `ref:m30:KatRefusjon` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[10]` |
| `KatVilkar` | `ref:m30:KatVilkar` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[11]` |
| `KatVarselSlv` | `ref:m30:KatVarselSlv` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[12]` |
| `KatKodeverk` | `ref:m30:KatKodeverk` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[13]` |
| `KatByttegruppe` | `ref:m30:KatByttegruppe` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[14]` |
| `KatLegemiddeldose` | `ref:m30:KatLegemiddeldose` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[15]` |
| `KatInteraksjon` | `ref:m30:KatInteraksjon` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[16]` |
| `KatStrDosering` | `ref:m30:KatStrDosering` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[3]/*/*/*[17]` |

### Relasjoner

- `KatLegemiddelMerkevare` knytter strukturen til `m30:KatLegemiddelMerkevare` med kardinalitet `0..1`.
- `KatLegemiddelpakning` knytter strukturen til `m30:KatLegemiddelpakning` med kardinalitet `0..1`.
- `KatVirkestoff` knytter strukturen til `m30:KatVirkestoff` med kardinalitet `0..1`.
- `KatOrdineringVirkestoff` knytter strukturen til `m30:KatOrdineringVirkestoff` med kardinalitet `0..1`.
- `KatLegemiddelVirkestoff` knytter strukturen til `m30:KatLegemiddelVirkestoff` med kardinalitet `0..1`.
- `KatHandelsvare` knytter strukturen til `m30:KatHandelsvare` med kardinalitet `0..1`.
- `KatDiagnose` knytter strukturen til `m30:KatDiagnose` med kardinalitet `0..1`.
- `KatRefusjon` knytter strukturen til `m30:KatRefusjon` med kardinalitet `0..1`.
- `KatVilkar` knytter strukturen til `m30:KatVilkar` med kardinalitet `0..1`.
- `KatVarselSlv` knytter strukturen til `m30:KatVarselSlv` med kardinalitet `0..1`.
- `KatKodeverk` knytter strukturen til `m30:KatKodeverk` med kardinalitet `0..1`.
- `KatByttegruppe` knytter strukturen til `m30:KatByttegruppe` med kardinalitet `0..1`.
- `KatLegemiddeldose` knytter strukturen til `m30:KatLegemiddeldose` med kardinalitet `0..1`.
- `KatInteraksjon` knytter strukturen til `m30:KatInteraksjon` med kardinalitet `0..1`.
- `KatStrDosering` knytter strukturen til `m30:KatStrDosering` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `FEST`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[3]`.

## AdministreringLegemiddel

XML-navn: `AdministreringLegemiddel`  
Alias og søkeord: administreringlegemiddel, FEST AdministreringLegemiddel  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatOrdineringVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`AdministreringLegemiddel` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Blandingsveske` | `boolean` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[1]` |
| `RefBlandingsveske` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[2]` |
| `Administrasjonsvei` | `kith:CV` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[3]` |
| `KanKnuses` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[4]` |
| `KanApnes` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[5]` |
| `Bolus` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[6]` |
| `InjeksjonshastighetBolus` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[7]` |
| `Deling` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[8]` |
| `EnhetDosering` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[9]` |
| `Kortdose` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[10]` |
| `ForhandsregelInntak` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[11]` |
| `BruksomradeEtikett` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[25]/*/*/*[12]` |

### Relasjoner

- `RefBlandingsveske` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `AdministreringLegemiddel`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[25]`.

## BestanddelMatr

XML-navn: `BestanddelMatr`  
Alias og søkeord: bestanddelmatr, FEST BestanddelMatr  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `MedForbMatr`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`BestanddelMatr` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[34]/*/*/*[1]` |
| `Materiale` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[34]/*/*/*[2]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `BestanddelMatr`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[34]`.

## Brystprotese

XML-navn: `Brystprotese`  
Alias og søkeord: brystprotese, FEST Brystprotese  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatHandelsvare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Brystprotese` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Nr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[1]` |
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[2]` |
| `ProduktInfoVare` | `ref:fs:ProduktInfoVare` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[3]` |
| `Leverandor` | `ref:fs:Leverandor` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[4]` |
| `PrisVare` | `ref:fs:PrisVare` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[5]` |
| `Refusjon` | `ref:fs:Refusjon` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[6]` |

### Relasjoner

- `ProduktInfoVare` knytter strukturen til `fs:ProduktInfoVare` med kardinalitet `0..1`.
- `Leverandor` knytter strukturen til `fs:Leverandor` med kardinalitet `0..1`.
- `PrisVare` knytter strukturen til `fs:PrisVare` med kardinalitet `0..*`.
- `Refusjon` knytter strukturen til `fs:Refusjon` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Brystprotese`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[36]`.

## DoseEtterBehov

XML-navn: `DoseEtterBehov`  
Alias og søkeord: doseetterbehov, FEST DoseEtterBehov  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeDose`  
Brukes fra: `Dosering`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`DoseEtterBehov` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `DoseDognMaks` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[10]/*/*/*/*/*[1]` |
| `DoseTidsromMaks` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[10]/*/*/*/*/*[2]` |
| `Tidsrom` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[10]/*/*/*/*/*[3]` |
| `DoseIntervallMin` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[10]/*/*/*/*/*[4]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `DoseEtterBehov`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[10]`.

## DoseFastTidspunkt

XML-navn: `DoseFastTidspunkt`  
Alias og søkeord: dosefasttidspunkt, FEST DoseFastTidspunkt  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeDose`  
Brukes fra: `Dosering`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`DoseFastTidspunkt` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Klokkeslett` | `time` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[9]/*/*/*/*/*[1]` |
| `Tidsomrade` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[9]/*/*/*/*/*[2]` |
| `GisEksakt` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[9]/*/*/*/*/*[3]` |
| `FastDose` | `ref:fs:FastDose` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[9]/*/*/*/*/*[4]` |

### Relasjoner

- `FastDose` knytter strukturen til `fs:FastDose` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `DoseFastTidspunkt`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[9]`.

## Dosering

XML-navn: `Dosering`  
Alias og søkeord: dosering, FEST Dosering  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelforbruk`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Dosering` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Starttidspunkt` | `kith:TS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[5]/*/*/*[1]` |
| `Sluttidspunkt` | `kith:TS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[5]/*/*/*[2]` |
| `Doseringsregel` | `ref:fs:Doseringsregel` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[5]/*/*/*[3]` |

### Relasjoner

- `Doseringsregel` knytter strukturen til `fs:Doseringsregel` med kardinalitet `0..1`.
- `DoseFastTidspunkt` knytter strukturen til `fs:DoseFastTidspunkt` med kardinalitet `1..*`.
- `DoseEtterBehov` knytter strukturen til `fs:DoseEtterBehov` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Dosering`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[5]`.

## Doseringsregel

XML-navn: `Doseringsregel`  
Alias og søkeord: doseringsregel, FEST Doseringsregel  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Dosering`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Doseringsregel` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `DoseresEtter` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[6]/*/*/*[1]` |
| `Merknad` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[6]/*/*/*[2]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Doseringsregel`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[6]`.

## FastDose

XML-navn: `FastDose`  
Alias og søkeord: fastdose, FEST FastDose  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `DoseFastTidspunkt`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`FastDose` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `FasteUkedager` | `kith:CS` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[11]/*/*/*[1]` |
| `DagerPa` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[11]/*/*/*[2]` |
| `DagerAv` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[11]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `FastDose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[11]`.

## Hjelpestoff

XML-navn: `Hjelpestoff`  
Alias og søkeord: hjelpestoff, FEST Hjelpestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Hjelpestoff` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[17]/*/*/*` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Hjelpestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[17]`.

## Infusjonshastighet

XML-navn: `Infusjonshastighet`  
Alias og søkeord: infusjonshastighet, FEST Infusjonshastighet  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Ikke dokumentert  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Infusjonshastighet` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Volum` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[8]/*/*/*[1]` |
| `Tidsenhet` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[8]/*/*/*[2]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Infusjonshastighet`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[8]`.

## LegemiddelMerkevare

XML-navn: `LegemiddelMerkevare`  
Alias og søkeord: legemiddelmerkevare, FEST LegemiddelMerkevare  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `KatLegemiddelMerkevare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`LegemiddelMerkevare` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[1]` |
| `Varenavn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[2]` |
| `LegemiddelformLang` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[3]` |
| `SortertVirkestoffMedStyrke` | `ref:fs:SortertVirkestoffMedStyrke` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[4]` |
| `SortertVirkestoffUtenStyrke` | `ref:fs:SortertVirkestoffUtenStyrke` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[5]` |
| `Smak` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[6]` |
| `ProduktInfo` | `ref:fs:ProduktInfo` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[7]` |
| `Reseptgyldighet` | `ref:fs:Reseptgyldighet` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[8]` |
| `Hjelpestoff` | `ref:fs:Hjelpestoff` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[9]` |
| `Preparatomtaleavsnitt` | `ref:fs:Preparatomtaleavsnitt` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[12]/*/*/*/*/*[10]` |

### Relasjoner

- `SortertVirkestoffMedStyrke` knytter strukturen til `fs:SortertVirkestoffMedStyrke` med kardinalitet `0..*`.
- `SortertVirkestoffUtenStyrke` knytter strukturen til `fs:SortertVirkestoffUtenStyrke` med kardinalitet `0..*`.
- `ProduktInfo` knytter strukturen til `fs:ProduktInfo` med kardinalitet `0..1`.
- `Reseptgyldighet` knytter strukturen til `fs:Reseptgyldighet` med kardinalitet `0..*`.
- `Hjelpestoff` knytter strukturen til `fs:Hjelpestoff` med kardinalitet `0..*`.
- `Preparatomtaleavsnitt` knytter strukturen til `fs:Preparatomtaleavsnitt` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `LegemiddelMerkevare`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[12]`.

## LegemiddelVirkestoff

XML-navn: `LegemiddelVirkestoff`  
Alias og søkeord: legemiddelvirkestoff, FEST LegemiddelVirkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `KatLegemiddelVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`LegemiddelVirkestoff` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[1]` |
| `SortertVirkestoffMedStyrke` | `ref:fs:SortertVirkestoffMedStyrke` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[2]` |
| `SortertVirkestoffUtenStyrke` | `ref:fs:SortertVirkestoffUtenStyrke` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[3]` |
| `RefLegemiddelMerkevare` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[4]` |
| `RefPakning` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[5]` |
| `ForskrivningsenhetResept` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[28]/*/*/*/*/*[6]` |

### Relasjoner

- `SortertVirkestoffMedStyrke` knytter strukturen til `fs:SortertVirkestoffMedStyrke` med kardinalitet `0..*`.
- `SortertVirkestoffUtenStyrke` knytter strukturen til `fs:SortertVirkestoffUtenStyrke` med kardinalitet `0..*`.
- `RefLegemiddelMerkevare` knytter strukturen til `IDREF` med kardinalitet `0..*`.
- `RefPakning` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `LegemiddelVirkestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[28]`.

## Legemiddeldose

XML-navn: `Legemiddeldose`  
Alias og søkeord: legemiddeldose, FEST Legemiddeldose  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `KatLegemiddeldose`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Legemiddeldose` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[1]` |
| `LmrLopenr` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[2]` |
| `Mengde` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[3]` |
| `Pakningstype` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[4]` |
| `RefLegemiddelMerkevare` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[5]` |
| `RefPakning` | `IDREF` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[6]` |
| `Pakningskomponent` | `ref:fs:Pakningskomponent` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[7]` |
| `EnhetOrdinering` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[24]/*/*/*/*/*[8]` |

### Relasjoner

- `Pakningskomponent` knytter strukturen til `fs:Pakningskomponent` med kardinalitet `0..*`.
- `RefLegemiddelMerkevare` knytter strukturen til `IDREF` med kardinalitet `1`.
- `RefPakning` knytter strukturen til `IDREF` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Legemiddeldose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[24]`.

## Legemiddelpakning

XML-navn: `Legemiddelpakning`  
Alias og søkeord: legemiddelpakning, FEST Legemiddelpakning  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeLegemiddel`  
Brukes fra: `KatLegemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Legemiddelpakning` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[1]` |
| `Varenr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[2]` |
| `Ean` | `string` | `0..*` | Strekkode | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[3]` |
| `IkkeKonservering` | `boolean` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[4]` |
| `Oppbevaring` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[5]` |
| `Pakningsinfo` | `ref:fs:Pakningsinfo` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[6]` |
| `PakningsinfoResept` | `ref:fs:PakningsinfoResept` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[7]` |
| `PrisVare` | `ref:fs:PrisVare` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[8]` |
| `Markedsforingsinfo` | `ref:fs:Markedsforingsinfo` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[9]` |
| `Preparatomtaleavsnitt` | `ref:fs:Preparatomtaleavsnitt` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[14]/*/*/*/*/*[10]` |

### Relasjoner

- `Pakningsinfo` knytter strukturen til `fs:Pakningsinfo` med kardinalitet `0..*`.
- `PakningsinfoResept` knytter strukturen til `fs:PakningsinfoResept` med kardinalitet `0..*`.
- `PrisVare` knytter strukturen til `fs:PrisVare` med kardinalitet `0..*`.
- `Markedsforingsinfo` knytter strukturen til `fs:Markedsforingsinfo` med kardinalitet `0..1`.
- `Preparatomtaleavsnitt` knytter strukturen til `fs:Preparatomtaleavsnitt` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Legemiddelpakning`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[14]`.

## Lenke

XML-navn: `Lenke`  
Alias og søkeord: lenke, FEST Lenke  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Preparatomtaleavsnitt`, `VarselSlv`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Lenke` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Beskrivelse` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[41]/*/*/*[1]` |
| `Www` | `kith:URL` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[41]/*/*/*[2]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Lenke`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[41]`.

## Leverandor

XML-navn: `Leverandor`  
Alias og søkeord: leverandor, FEST Leverandor  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Ikke dokumentert  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Leverandor` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[39]/*/*/*[1]` |
| `Adresse` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[39]/*/*/*[2]` |
| `Telefon` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[39]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Leverandor`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[39]`.

## Markedsforingsinfo

XML-navn: `Markedsforingsinfo`  
Alias og søkeord: markedsforingsinfo, FEST Markedsforingsinfo  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Markedsforingsinfo` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `VarenrUtgaende` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[19]/*/*/*[1]` |
| `Markedsforingsdato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[19]/*/*/*[2]` |
| `AvregDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[19]/*/*/*[3]` |
| `MidlUtgattDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[19]/*/*/*[4]` |
| `OmpakkerAvEndose` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[19]/*/*/*[5]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Markedsforingsinfo`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[19]`.

## MedForbMatr

XML-navn: `MedForbMatr`  
Alias og søkeord: medforbmatr, FEST MedForbMatr  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeVare`  
Brukes fra: `KatHandelsvare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`MedForbMatr` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `BestanddelMatr` | `ref:fs:BestanddelMatr` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[33]/*/*/*/*/*` |

### Relasjoner

- `BestanddelMatr` knytter strukturen til `fs:BestanddelMatr` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `MedForbMatr`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[33]`.

## Naringsmiddel

XML-navn: `Naringsmiddel`  
Alias og søkeord: naringsmiddel, FEST Naringsmiddel  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeVare`  
Brukes fra: `KatHandelsvare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Naringsmiddel` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `StyrkeFormStoff` | `ref:fs:StyrkeFormStoff` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[35]/*/*/*/*/*` |

### Relasjoner

- `StyrkeFormStoff` knytter strukturen til `fs:StyrkeFormStoff` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Naringsmiddel`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[35]`.

## PakningByttegruppe

XML-navn: `PakningByttegruppe`  
Alias og søkeord: pakningbyttegruppe, FEST PakningByttegruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Ikke dokumentert  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`PakningByttegruppe` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `RefByttegruppe` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[20]/*/*/*[1]` |
| `GyldigFraDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[20]/*/*/*[2]` |
| `GyldigTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[20]/*/*/*[3]` |

### Relasjoner

- `RefByttegruppe` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `PakningByttegruppe`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[20]`.

## Pakningsinfo

XML-navn: `Pakningsinfo`  
Alias og søkeord: pakningsinfo, FEST Pakningsinfo  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Pakningsinfo` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `RefLegemiddelMerkevare` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[1]` |
| `Pakningsstr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[2]` |
| `EnhetPakning` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[3]` |
| `Pakningstype` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[4]` |
| `Multippel` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[5]` |
| `Antall` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[6]` |
| `Mengde` | `decimal` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[7]` |
| `Sortering` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[8]` |
| `DDD` | `kith:PQ` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[9]` |
| `Statistikkfaktor` | `decimal` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[10]` |
| `Pakningskomponent` | `ref:fs:Pakningskomponent` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[21]/*/*/*[11]` |

### Relasjoner

- `Pakningskomponent` knytter strukturen til `fs:Pakningskomponent` med kardinalitet `0..*`.
- `RefLegemiddelMerkevare` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Pakningsinfo`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[21]`.

## PakningsinfoResept

XML-navn: `PakningsinfoResept`  
Alias og søkeord: pakningsinforesept, FEST PakningsinfoResept  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`PakningsinfoResept` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Varenavn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[23]/*/*/*[1]` |
| `Pakningsstr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[23]/*/*/*[2]` |
| `EnhetPakning` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[23]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `PakningsinfoResept`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[23]`.

## Pakningskomponent

XML-navn: `Pakningskomponent`  
Alias og søkeord: pakningskomponent, FEST Pakningskomponent  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddeldose`, `Pakningsinfo`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Pakningskomponent` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Pakningstype` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[22]/*/*/*[1]` |
| `Mengde` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[22]/*/*/*[2]` |
| `Antall` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[22]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Pakningskomponent`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[22]`.

## Preparatomtaleavsnitt

XML-navn: `Preparatomtaleavsnitt`  
Alias og søkeord: preparatomtaleavsnitt, FEST Preparatomtaleavsnitt  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`, `Legemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Preparatomtaleavsnitt` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Avsnittoverskrift` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[13]/*/*/*[1]` |
| `Lenke` | `ref:fs:Lenke` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[13]/*/*/*[2]` |

### Relasjoner

- `Lenke` knytter strukturen til `fs:Lenke` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Preparatomtaleavsnitt`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[13]`.

## PrisVare

XML-navn: `PrisVare`  
Alias og søkeord: prisvare, FEST PrisVare  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelpakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`PrisVare` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Type` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[15]/*/*/*[1]` |
| `Pris` | `kith:MO` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[15]/*/*/*[2]` |
| `GyldigFraDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[15]/*/*/*[3]` |
| `GyldigTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[15]/*/*/*[4]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `PrisVare`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[15]`.

## ProduktInfo

XML-navn: `ProduktInfo`  
Alias og søkeord: produktinfo, FEST ProduktInfo  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`ProduktInfo` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Varseltrekant` | `boolean` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[16]/*/*/*[1]` |
| `Referanseprodukt` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[16]/*/*/*[2]` |
| `Vaksinestandard` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[16]/*/*/*[3]` |
| `Produsent` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[16]/*/*/*[4]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `ProduktInfo`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[16]`.

## ProduktInfoVare

XML-navn: `ProduktInfoVare`  
Alias og søkeord: produktinfovare, FEST ProduktInfoVare  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Ikke dokumentert  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`ProduktInfoVare` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `ProduktNr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[1]` |
| `Volum` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[2]` |
| `EnhetStorrelse` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[3]` |
| `AntPerPakning` | `int` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[4]` |
| `RefVilkar` | `IDREF` | `0..*` | Referanse til vilkår | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[5]` |
| `TillattMerMakspris` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[38]/*/*/*[6]` |

### Relasjoner

- `RefVilkar` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `ProduktInfoVare`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[38]`.

## Refusjon

XML-navn: `Refusjon`  
Alias og søkeord: refusjon, FEST Refusjon  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Virkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Refusjon` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `RefRefusjonsgruppe` | `IDREF` | `1..*` | Referanse til refusjonsgruppe | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[4]/*/*/*[1]` |
| `GyldigFraDato` | `date` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[4]/*/*/*[2]` |
| `ForskrivesTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[4]/*/*/*[3]` |
| `UtleveresTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[4]/*/*/*[4]` |

### Relasjoner

- `RefRefusjonsgruppe` knytter strukturen til `IDREF` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Refusjon`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[4]`.

## Reseptgyldighet

XML-navn: `Reseptgyldighet`  
Alias og søkeord: reseptgyldighet, FEST Reseptgyldighet  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Reseptgyldighet` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Kjonn` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[18]/*/*/*[1]` |
| `Varighet` | `duration` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[18]/*/*/*[2]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Reseptgyldighet`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[18]`.

## SortertVirkestoffMedStyrke

XML-navn: `SortertVirkestoffMedStyrke`  
Alias og søkeord: sortertvirkestoffmedstyrke, FEST SortertVirkestoffMedStyrke  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`, `LegemiddelVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`SortertVirkestoffMedStyrke` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Sortering` | `int` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[31]/*/*/*[1]` |
| `RefVirkestoffMedStyrke` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[31]/*/*/*[2]` |

### Relasjoner

- `RefVirkestoffMedStyrke` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `SortertVirkestoffMedStyrke`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[31]`.

## SortertVirkestoffUtenStyrke

XML-navn: `SortertVirkestoffUtenStyrke`  
Alias og søkeord: sortertvirkestoffutenstyrke, FEST SortertVirkestoffUtenStyrke  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `LegemiddelMerkevare`, `LegemiddelVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`SortertVirkestoffUtenStyrke` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Sortering` | `int` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[32]/*/*/*[1]` |
| `RefVirkestoff` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[32]/*/*/*[2]` |

### Relasjoner

- `RefVirkestoff` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `SortertVirkestoffUtenStyrke`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[32]`.

## StyrkeFormStoff

XML-navn: `StyrkeFormStoff`  
Alias og søkeord: styrkeformstoff, FEST StyrkeFormStoff  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Naringsmiddel`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`StyrkeFormStoff` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Styrke` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[40]/*/*/*[1]` |
| `Form` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[40]/*/*/*[2]` |
| `Stoff` | `string` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[40]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `StyrkeFormStoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[40]`.

## Virkestoff

XML-navn: `Virkestoff`  
Alias og søkeord: virkestoff, FEST Virkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Virkestoff` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[29]/*/*/*[1]` |
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[29]/*/*/*[2]` |
| `NavnEngelsk` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[29]/*/*/*[3]` |
| `RefVirkestoff` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[29]/*/*/*[4]` |
| `Refusjon` | `ref:fs:Refusjon` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[29]/*/*/*[5]` |

### Relasjoner

- `Refusjon` knytter strukturen til `fs:Refusjon` med kardinalitet `0..*`.
- `RefVirkestoff` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Virkestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[29]`.

## VirkestoffMedStyrke

XML-navn: `VirkestoffMedStyrke`  
Alias og søkeord: virkestoffmedstyrke, FEST VirkestoffMedStyrke  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatVirkestoff`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`VirkestoffMedStyrke` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[1]` |
| `Styrke` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[2]` |
| `StyrkeNevner` | `kith:PQ` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[3]` |
| `RefVirkestoff` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[4]` |
| `AlternativStyrke` | `kith:PQ` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[5]` |
| `AlternativStyrkeNevner` | `kith:PQ` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[6]` |
| `Styrkeoperator` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[7]` |
| `StyrkeOvreVerdi` | `double` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[8]` |
| `AtcKombipreparat` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[30]/*/*/*[9]` |

### Relasjoner

- `RefVirkestoff` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `VirkestoffMedStyrke`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[30]`.

## Behandling

XML-navn: `Behandling`  
Alias og søkeord: behandling, FEST Behandling  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Diagnose`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Behandling

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Beskrivelse` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[21]/*[2]/*/*[1]` |
| `Legemiddelforslag` | `ref:m30:Legemiddelforslag` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[21]/*[2]/*/*[2]` |

### Relasjoner

- `Legemiddelforslag` knytter strukturen til `m30:Legemiddelforslag` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Behandling`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[21]`.

## Byttegruppe

XML-navn: `Byttegruppe`  
Alias og søkeord: byttegruppe, FEST Byttegruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatByttegruppe`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Byttegruppe` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[1]` |
| `Kode` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[2]` |
| `MerknadTilByttbarhet` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[3]` |
| `BeskrivelseByttbarhet` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[4]` |
| `GyldigFraDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[5]` |
| `GyldigTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[37]/*/*/*[6]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Byttegruppe`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[37]`.

## Diagnose

XML-navn: `Diagnose`  
Alias og søkeord: diagnose, FEST Diagnose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatDiagnose`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Diagnose

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[20]/*[2]/*/*[1]` |
| `Diagnosekode` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[20]/*[2]/*/*[2]` |
| `Bruksomrade` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[20]/*[2]/*/*[3]` |
| `Behandling` | `ref:m30:Behandling` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[20]/*[2]/*/*[4]` |

### Relasjoner

- `Behandling` knytter strukturen til `m30:Behandling` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Diagnose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[20]`.

## Doseringsforslag

XML-navn: `Doseringsforslag`  
Alias og søkeord: doseringsforslag, FEST Doseringsforslag  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Legemiddelforslag`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Doseringsforslag

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Behandlingsfase` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[1]` |
| `MinTidForrigeDosering` | `duration` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[2]` |
| `Varighet` | `duration` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[3]` |
| `Doseringsregel` | `ref:m30:Doseringsregel` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[4]` |
| `GodkjentNormaldose` | `ref:m30:GodkjentNormaldose` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[5]` |
| `GodkjentMaksimaldose` | `ref:m30:GodkjentMaksimaldose` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[23]/*[2]/*/*[6]` |

### Relasjoner

- `Doseringsregel` knytter strukturen til `m30:Doseringsregel` med kardinalitet `0..*`.
- `GodkjentNormaldose` knytter strukturen til `m30:GodkjentNormaldose` med kardinalitet `1..*`.
- `GodkjentMaksimaldose` knytter strukturen til `m30:GodkjentMaksimaldose` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Doseringsforslag`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[23]`.

## Doseringsregel

XML-navn: `Doseringsregel`  
Alias og søkeord: doseringsregel, FEST Doseringsregel  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Doseringsforslag`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Doseringsregel

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `DoseresEtter` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[24]/*[2]/*/*[1]` |
| `OvreGrense` | `decimal` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[24]/*[2]/*/*[2]` |
| `NedreGrense` | `decimal` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[24]/*[2]/*/*[3]` |
| `Enhet` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[24]/*[2]/*/*[4]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Doseringsregel`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[24]`.

## Element

XML-navn: `Element`  
Alias og søkeord: element, FEST Element  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatKodeverk`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Element` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[34]/*/*/*[1]` |
| `ParentId` | `IDREF` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[34]/*/*/*[2]` |
| `Kode` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[34]/*/*/*[3]` |
| `Term` | `ref:m30:Term` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[34]/*/*/*[4]` |

### Relasjoner

- `Term` knytter strukturen til `m30:Term` med kardinalitet `0..*`.
- `ParentId` knytter strukturen til `IDREF` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Element`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[34]`.

## GodkjentMaksimaldose

XML-navn: `GodkjentMaksimaldose`  
Alias og søkeord: godkjentmaksimaldose, FEST GodkjentMaksimaldose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Doseringsforslag`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Godkjent maksimaldose

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Maksimaldose` | `decimal` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[26]/*[2]/*/*[1]` |
| `Enhet` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[26]/*[2]/*/*[2]` |
| `Periode` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[26]/*[2]/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `GodkjentMaksimaldose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[26]`.

## GodkjentNormaldose

XML-navn: `GodkjentNormaldose`  
Alias og søkeord: godkjentnormaldose, FEST GodkjentNormaldose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Doseringsforslag`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Godkjent normaldose

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OvreNormaldose` | `decimal` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[1]` |
| `NedreNormaldose` | `decimal` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[2]` |
| `Enhet` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[3]` |
| `MinAntDoser` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[4]` |
| `MaksAntDoser` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[5]` |
| `Periode` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[25]/*[2]/*/*[6]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `GodkjentNormaldose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[25]`.

## Info

XML-navn: `Info`  
Alias og søkeord: info, FEST Info  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatKodeverk`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Info` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `kith:oid` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[33]/*/*/*[1]` |
| `Betegnelse` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[33]/*/*/*[2]` |
| `Kortnavn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[33]/*/*/*[3]` |
| `AnsvarligUtgiver` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[33]/*/*/*[4]` |
| `Merknad` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[33]/*/*/*[5]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Info`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[33]`.

## Interaksjon

XML-navn: `Interaksjon`  
Alias og søkeord: interaksjon, FEST Interaksjon  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatInteraksjon`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Interaksjon` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[1]` |
| `Relevans` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[2]` |
| `Situasjonskriterium` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[3]` |
| `KliniskKonsekvens` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[4]` |
| `Interaksjonsmekanisme` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[5]` |
| `Kildegrunnlag` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[6]` |
| `Handtering` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[7]` |
| `Visningsregel` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[8]` |
| `Referanse` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[9]` |
| `Substansgruppe` | `ref:m30:Substansgruppe` | `2..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[38]/*/*/*[10]` |

### Relasjoner

- `Substansgruppe` knytter strukturen til `m30:Substansgruppe` med kardinalitet `2..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Interaksjon`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[38]`.

## InteraksjonIkkeVurdert

XML-navn: `InteraksjonIkkeVurdert`  
Alias og søkeord: interaksjonikkevurdert, FEST InteraksjonIkkeVurdert  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatInteraksjon`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`InteraksjonIkkeVurdert` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Atc` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[39]/*/*/*` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `InteraksjonIkkeVurdert`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[39]`.

## KatByttegruppe

XML-navn: `KatByttegruppe`  
Alias og søkeord: katalog byttegruppe, FEST KatByttegruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog byttegruppe

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfByttegruppe` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[15]/*[2]/*/*` |

### Relasjoner

- `Byttegruppe` knytter strukturen til `m30:Byttegruppe` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatByttegruppe`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[15]`.

## KatDiagnose

XML-navn: `KatDiagnose`  
Alias og søkeord: katalog diagnose, FEST KatDiagnose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog diagnose

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfDiagnose` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[17]/*[2]/*/*` |

### Relasjoner

- `Diagnose` knytter strukturen til `m30:Diagnose` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatDiagnose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[17]`.

## KatHandelsvare

XML-navn: `KatHandelsvare`  
Alias og søkeord: katalog handelsvare, FEST KatHandelsvare  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog handelsvare

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfHandelsvare` | `anonym complexType` | `0..*` | Oppført handelsvare | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[6]/*[2]/*/*` |

### Relasjoner

- `Brystprotese` knytter strukturen til `fs:Brystprotese` med kardinalitet `1`.
- `MedForbMatr` knytter strukturen til `fs:MedForbMatr` med kardinalitet `1`.
- `Naringsmiddel` knytter strukturen til `fs:Naringsmiddel` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatHandelsvare`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[6]`.

## KatInteraksjon

XML-navn: `KatInteraksjon`  
Alias og søkeord: katalog interaksjon, FEST KatInteraksjon  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog interaksjon

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfInteraksjon` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[18]/*[2]/*/*` |

### Relasjoner

- `Interaksjon` knytter strukturen til `m30:Interaksjon` med kardinalitet `1`.
- `InteraksjonIkkeVurdert` knytter strukturen til `m30:InteraksjonIkkeVurdert` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatInteraksjon`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[18]`.

## KatKodeverk

XML-navn: `KatKodeverk`  
Alias og søkeord: katalog kodeverk, FEST KatKodeverk  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog kodeverk

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfKodeverk` | `anonym complexType` | `0..*` | Oppført kodeverk | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[14]/*[2]/*/*` |

### Relasjoner

- `Info` knytter strukturen til `m30:Info` med kardinalitet `1`.
- `Element` knytter strukturen til `m30:Element` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatKodeverk`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[14]`.

## KatLegemiddelMerkevare

XML-navn: `KatLegemiddelMerkevare`  
Alias og søkeord: katalog legemiddelmerkevare, FEST KatLegemiddelMerkevare  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog legemiddel merkevare

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfLegemiddelMerkevare` | `anonym complexType` | `0..*` | Oppført medisinsk produkt | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[5]/*[2]/*/*` |

### Relasjoner

- `LegemiddelMerkevare` knytter strukturen til `fs:LegemiddelMerkevare` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatLegemiddelMerkevare`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[5]`.

## KatLegemiddelVirkestoff

XML-navn: `KatLegemiddelVirkestoff`  
Alias og søkeord: katalog legemiddelvirkestoff, FEST KatLegemiddelVirkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog legemiddel virkestoff

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfLegemiddelVirkestoff` | `anonym complexType` | `0..*` | Oppført legemiddel virkestoff | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[8]/*[2]/*/*` |

### Relasjoner

- `LegemiddelVirkestoff` knytter strukturen til `fs:LegemiddelVirkestoff` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatLegemiddelVirkestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[8]`.

## KatLegemiddeldose

XML-navn: `KatLegemiddeldose`  
Alias og søkeord: katalog legemiddeldose, FEST KatLegemiddeldose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog legemiddeldose

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfLegemiddeldose` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[16]/*[2]/*/*` |

### Relasjoner

- `Legemiddeldose` knytter strukturen til `fs:Legemiddeldose` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatLegemiddeldose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[16]`.

## KatLegemiddelpakning

XML-navn: `KatLegemiddelpakning`  
Alias og søkeord: katalog legemiddelpakning, FEST KatLegemiddelpakning  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog legemiddelpakning merkevare

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfLegemiddelpakning` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[10]/*[2]/*/*` |

### Relasjoner

- `Legemiddelpakning` knytter strukturen til `fs:Legemiddelpakning` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatLegemiddelpakning`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[10]`.

## KatOrdineringVirkestoff

XML-navn: `KatOrdineringVirkestoff`  
Alias og søkeord: katalog ordineringvirkestoff, FEST KatOrdineringVirkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog ordinasjon virkestoff

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfOrdineringVirkestoff` | `anonym complexType` | `0..*` | Oppført ordinasjon virkestoff | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[9]/*[2]/*/*` |

### Relasjoner

- `AdministreringLegemiddel` knytter strukturen til `fs:AdministreringLegemiddel` med kardinalitet `0..1`.
- `RefByttegruppe` knytter strukturen til `IDREF` med kardinalitet `0..1`.
- `RefLegemiddelVirkestoff` knytter strukturen til `IDREF` med kardinalitet `1..*`.
- `RefLegemiddelDose` knytter strukturen til `IDREF` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatOrdineringVirkestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[9]`.

## KatRefusjon

XML-navn: `KatRefusjon`  
Alias og søkeord: katalog refusjon, FEST KatRefusjon  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog refusjon

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfRefusjon` | `anonym complexType` | `0..*` | Oppført refusjon | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[12]/*[2]/*/*` |

### Relasjoner

- `Refusjonshjemmel` knytter strukturen til `m30:Refusjonshjemmel` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatRefusjon`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[12]`.

## KatStrDosering

XML-navn: `KatStrDosering`  
Alias og søkeord: katalog strdosering, FEST KatStrDosering  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog strukturert dosering

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfStrDosering` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[19]/*[2]/*/*` |

### Relasjoner

- `Kortdose` knytter strukturen til `m30:Kortdose` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatStrDosering`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[19]`.

## KatVarselSlv

XML-navn: `KatVarselSlv`  
Alias og søkeord: katalog varselslv, FEST KatVarselSlv  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog Varsel fra SLV

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfVarselSlv` | `anonym complexType` | `0..*` | Oppført Varsel fra SLV | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[11]/*[2]/*/*` |

### Relasjoner

- `VarselSlv` knytter strukturen til `m30:VarselSlv` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatVarselSlv`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[11]`.

## KatVilkar

XML-navn: `KatVilkar`  
Alias og søkeord: katalog vilkar, FEST KatVilkar  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog vilkår

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfVilkar` | `anonym complexType` | `0..*` | Oppført vilkår | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[13]/*[2]/*/*` |

### Relasjoner

- `Vilkar` knytter strukturen til `m30:Vilkar` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatVilkar`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[13]`.

## KatVirkestoff

XML-navn: `KatVirkestoff`  
Alias og søkeord: katalog virkestoff, FEST KatVirkestoff  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `FEST`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Katalog virkestoff

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `OppfVirkestoff` | `anonym complexType` | `0..*` | Oppført virkestoff | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[7]/*[2]/*/*` |

### Relasjoner

- `Virkestoff` knytter strukturen til `fs:Virkestoff` med kardinalitet `1`.
- `VirkestoffMedStyrke` knytter strukturen til `fs:VirkestoffMedStyrke` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `KatVirkestoff`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[7]`.

## Kortdose

XML-navn: `Kortdose`  
Alias og søkeord: kortdose, FEST Kortdose  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatStrDosering`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Kortdose` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Kortdose` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[41]/*/*/*[1]` |
| `BeskrivelseTerm` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[41]/*/*/*[2]` |
| `Legemiddelforbruk` | `ref:m30:Legemiddelforbruk` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[41]/*/*/*[3]` |

### Relasjoner

- `Legemiddelforbruk` knytter strukturen til `m30:Legemiddelforbruk` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Kortdose`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[41]`.

## Legemiddelforbruk

XML-navn: `Legemiddelforbruk`  
Alias og søkeord: legemiddelforbruk, FEST Legemiddelforbruk  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Kortdose`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Legemiddelforbruk` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Lopenr` | `int` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[42]/*/*/*[1]` |
| `Mengde` | `decimal` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[42]/*/*/*[2]` |
| `Periode` | `duration` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[42]/*/*/*[3]` |
| `Iterasjoner` | `int` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[42]/*/*/*[4]` |
| `Dosering` | `ref:fs:Dosering` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[42]/*/*/*[5]` |

### Relasjoner

- `Dosering` knytter strukturen til `fs:Dosering` med kardinalitet `0..1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Legemiddelforbruk`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[42]`.

## Legemiddelforslag

XML-navn: `Legemiddelforslag`  
Alias og søkeord: legemiddelforslag, FEST Legemiddelforslag  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Behandling`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Legemiddelforslag

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `VirkestoffnavnForm` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[22]/*[2]/*/*[1]` |
| `RefLegemiddelVirkestoff` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[22]/*[2]/*/*[2]` |
| `RefLegemiddelMerkevare` | `IDREF` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[22]/*[2]/*/*[3]` |
| `Oppmerksomhet` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[22]/*[2]/*/*[4]` |
| `Doseringsforslag` | `ref:m30:Doseringsforslag` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[22]/*[2]/*/*[5]` |

### Relasjoner

- `Doseringsforslag` knytter strukturen til `m30:Doseringsforslag` med kardinalitet `0..*`.
- `RefLegemiddelVirkestoff` knytter strukturen til `IDREF` med kardinalitet `0..*`.
- `RefLegemiddelMerkevare` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Legemiddelforslag`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[22]`.

## Refusjonsgruppe

XML-navn: `Refusjonsgruppe`  
Alias og søkeord: refusjonsgruppe, FEST Refusjonsgruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Refusjonshjemmel`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Refusjonsgruppe

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[1]` |
| `GruppeNr` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[2]` |
| `Atc` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[3]` |
| `KreverRefusjonskode` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[4]` |
| `RefusjonsberettighetBruk` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[5]` |
| `RefVilkar` | `IDREF` | `0..*` | Referanse vilkår (refusjonsberettighet bruk) | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[6]` |
| `Refusjonskode` | `ref:m30:Refusjonskode` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[28]/*[2]/*/*[7]` |

### Relasjoner

- `Refusjonskode` knytter strukturen til `m30:Refusjonskode` med kardinalitet `0..*`.
- `RefVilkar` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Refusjonsgruppe`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[28]`.

## Refusjonshjemmel

XML-navn: `Refusjonshjemmel`  
Alias og søkeord: refusjonshjemmel, FEST Refusjonshjemmel  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatRefusjon`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Refusjonshjemmel

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Refusjonshjemmel` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[27]/*[2]/*/*[1]` |
| `KreverVarekobling` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[27]/*[2]/*/*[2]` |
| `KreverVedtak` | `boolean` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[27]/*[2]/*/*[3]` |
| `Refusjonsgruppe` | `ref:m30:Refusjonsgruppe` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[27]/*[2]/*/*[4]` |

### Relasjoner

- `Refusjonsgruppe` knytter strukturen til `m30:Refusjonsgruppe` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Refusjonshjemmel`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[27]`.

## Refusjonskode

XML-navn: `Refusjonskode`  
Alias og søkeord: refusjonskode, FEST Refusjonskode  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Refusjonsgruppe`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Refusjonskode

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Refusjonskode` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[1]` |
| `Underterm` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[2]` |
| `GyldigFraDato` | `date` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[3]` |
| `ForskrivesTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[4]` |
| `UtleveresTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[5]` |
| `Refusjonsvilkar` | `ref:m30:Refusjonsvilkar` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[29]/*[2]/*/*[6]` |

### Relasjoner

- `Refusjonsvilkar` knytter strukturen til `m30:Refusjonsvilkar` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Refusjonskode`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[29]`.

## Refusjonsvilkar

XML-navn: `Refusjonsvilkar`  
Alias og søkeord: refusjonsvilkar, FEST Refusjonsvilkar  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Refusjonskode`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Refusjonsvilkår

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `RefVilkar` | `IDREF` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[30]/*[2]/*/*[1]` |
| `FraDato` | `date` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[30]/*[2]/*/*[2]` |
| `TilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[30]/*[2]/*/*[3]` |

### Relasjoner

- `RefVilkar` knytter strukturen til `IDREF` med kardinalitet `1`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Refusjonsvilkar`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[30]`.

## StrukturertVilkar

XML-navn: `StrukturertVilkar`  
Alias og søkeord: strukturertvilkar, FEST StrukturertVilkar  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Vilkar`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Strukturert vilkår

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Type` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[32]/*[2]/*/*[1]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `StrukturertVilkar`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[32]`.

## Substansgruppe

XML-navn: `Substansgruppe`  
Alias og søkeord: substansgruppe, FEST Substansgruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Interaksjon`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Substansgruppe` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Navn` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[40]/*/*/*[1]` |
| `Substans` | `anonym complexType` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[40]/*/*/*[2]` |

### Relasjoner

- `RefVirkestoff` knytter strukturen til `IDREF` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Substansgruppe`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[40]`.

## Term

XML-navn: `Term`  
Alias og søkeord: term, FEST Term  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `Element`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`Term` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Term` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[35]/*/*/*[1]` |
| `BeskrivelseTerm` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[35]/*/*/*[2]` |
| `Sprak` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[35]/*/*/*[3]` |

### Relasjoner

Ingen direkte `xs:element ref`- eller `IDREF`-relasjoner er deklarert i denne elementtypen.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Term`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[35]`.

## VarselSlv

XML-navn: `VarselSlv`  
Alias og søkeord: varselslv, FEST VarselSlv  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatVarselSlv`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`VarselSlv` er et XML-element i den delen av FEST 2.5.1-modellen som er nåbar fra `FEST`. Formålet utover plasseringen i XML-strukturen er ikke dokumentert i XSD-en.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Type` | `kith:CV` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[1]` |
| `Overskrift` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[2]` |
| `Varseltekst` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[3]` |
| `Visningsregel` | `kith:CV` | `1..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[4]` |
| `KodetInfo` | `kith:CV` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[5]` |
| `FraDato` | `date` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[6]` |
| `Lenke` | `ref:fs:Lenke` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[7]` |
| `Referanseelement` | `anonym complexType` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[36]/*/*/*[8]` |

### Relasjoner

- `Lenke` knytter strukturen til `fs:Lenke` med kardinalitet `0..1`.
- `RefElement` knytter strukturen til `IDREF` med kardinalitet `1..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `VarselSlv`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[36]`.

## Vilkar

XML-navn: `Vilkar`  
Alias og søkeord: vilkar, FEST Vilkar  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `KatVilkar`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

Vilkår

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Vilkårs-id | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[1]` |
| `VilkarNr` | `string` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[2]` |
| `Gruppe` | `kith:CV` | `1` | Vilkårsgruppe | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[3]` |
| `GjelderFor` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[4]` |
| `Tekst` | `string` | `1` | Vilkårstekst | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[5]` |
| `GyldigFraDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[6]` |
| `GyldigTilDato` | `date` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[7]` |
| `StrukturertVilkar` | `ref:m30:StrukturertVilkar` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[31]/*[2]/*/*[8]` |

### Relasjoner

- `StrukturertVilkar` knytter strukturen til `m30:StrukturertVilkar` med kardinalitet `0..*`.

### Regler og begrensninger

Kardinalitetene ovenfor er skjemakardinaliteter. Forretningsmessige innstramminger kan finnes i implementeringsveiledningen og må ikke utledes fra XSD alene.

### Praktisk bruk

Bruk namespace sammen med det eksakte XML-navnet `Vilkar`. Ved inkrementelle uttrekk må referanser valideres med loose-variantene; se `06-fullt-og-inkrementelt-uttrekk.md`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[31]`.

## CS

XML-navn: `CS`  
Alias og søkeord: XML-type CS, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`CS` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `CS`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[17]`.

## CV

XML-navn: `CV`  
Alias og søkeord: XML-type CV, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`CV` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `CV`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[18]`.

## MO

XML-navn: `MO`  
Alias og søkeord: XML-type MO, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`MO` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `MO`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[21]`.

## PQ

XML-navn: `PQ`  
Alias og søkeord: XML-type PQ, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`PQ` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `PQ`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[20]`.

## TS

XML-navn: `TS`  
Alias og søkeord: XML-type TS, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`TS` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `TS`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[6]`.

## URL

XML-navn: `URL`  
Alias og søkeord: XML-type URL, complexType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`URL` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer.

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `URL`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[7]`.

## oid

XML-navn: `oid`  
Alias og søkeord: XML-type oid, simpleType  
Namespace: `http://www.kith.no/xmlstds`  
Definert i: `kith.xsd`  
Arver fra: `token`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`oid` er en navngitt `simpleType` som brukes av FEST 2.5.1-strukturen.

### Innhold

Ingen direkte underelementer. Begrensninger: `pattern=(\d+\.?)*\d+`.

### Relasjoner

Basetype: `token`.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds` og eksakt navn `oid`.

### Kilder

- `XSD-KITH-COMMON` – `kith.xsd`, `/*/*[19]`.

## typeDose

XML-navn: `typeDose`  
Alias og søkeord: XML-type typeDose, complexType  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`typeDose` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Mengde` | `kith:PQ` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[7]/*/*[1]` |
| `Intervall` | `kith:PQ` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[7]/*/*[2]` |
| `Infusjonshastighet` | `ref:fs:Infusjonshastighet` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[7]/*/*[3]` |

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01` og eksakt navn `typeDose`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[7]`.

## typeLegemiddel

XML-navn: `typeLegemiddel`  
Alias og søkeord: XML-type typeLegemiddel, complexType  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`typeLegemiddel` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Atc` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[1]` |
| `NavnFormStyrke` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[2]` |
| `Reseptgruppe` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[3]` |
| `LegemiddelformKort` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[4]` |
| `RefVilkar` | `IDREF` | `0..*` | Referanse til vilkår | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[5]` |
| `Preparattype` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[6]` |
| `TypeSoknadSlv` | `kith:CS` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[7]` |
| `Opioidsoknad` | `boolean` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[8]` |
| `Refusjon` | `ref:fs:Refusjon` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[9]` |
| `PakningByttegruppe` | `ref:fs:PakningByttegruppe` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[10]` |
| `AdministreringLegemiddel` | `ref:fs:AdministreringLegemiddel` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[11]` |
| `SvartTrekant` | `kith:CV` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[26]/*/*[12]` |

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01` og eksakt navn `typeLegemiddel`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[26]`.

## typeVare

XML-navn: `typeVare`  
Alias og søkeord: XML-type typeVare, complexType  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`typeVare` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Nr` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[1]` |
| `Navn` | `string` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[2]` |
| `ProduktInfoVare` | `ref:fs:ProduktInfoVare` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[3]` |
| `Leverandor` | `ref:fs:Leverandor` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[4]` |
| `PrisVare` | `ref:fs:PrisVare` | `0..*` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[5]` |
| `Refusjon` | `ref:fs:Refusjon` | `0..1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-FORSKRIVNING-FULL-2014-12-01:/*/*[37]/*/*[6]` |

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01` og eksakt navn `typeVare`.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01` – `forskrivning-2014-12-01.xsd`, `/*/*[37]`.

## typeEnkeltoppforingFest

XML-navn: `typeEnkeltoppforingFest`  
Alias og søkeord: XML-type typeEnkeltoppforingFest, complexType  
Namespace: `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`  
Definert i: `er-m30-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: Elementer eller typer som angir denne typen i `type` eller `base`; se strukturmodellen for alle brukssteder.  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`typeEnkeltoppforingFest` er en navngitt `complexType` som brukes av FEST 2.5.1-strukturen.

### Innhold

| Element | Type | Kardinalitet | Beskrivelse | Status | Kilde |
|---|---|---:|---|---|---|
| `Id` | `ID` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[4]/*/*[1]` |
| `Tidspunkt` | `dateTime` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[4]/*/*[2]` |
| `Status` | `kith:CS` | `1` | Ikke dokumentert i XSD. | AVLEDET_XSD | `XSD-M30-FULL-2014-12-01:/*/*[4]/*/*[3]` |

### Relasjoner

Ingen basetype er deklarert.

### Regler og begrensninger

Regler følger de deklarerte elementene, attributtene og eventuelle restriction-fasetter i XSD-en.

### Praktisk bruk

Bruk typen med namespace `http://www.kith.no/xmlstds/eresept/m30/2014-12-01` og eksakt navn `typeEnkeltoppforingFest`.

### Kilder

- `XSD-M30-FULL-2014-12-01` – `er-m30-2014-12-01.xsd`, `/*/*[4]`.

## Forskrivning-elementer utelatt fra FEST-referansen

Disse globale elementene finnes i Forskrivning-XSD-en, men er ikke nåbare fra M30-roten `FEST` og presenteres derfor ikke som FEST-innhold:

`AdministreringForskrivning`, `Forskrivning`, `Legemiddelblanding`, `MengdeBestanddel`, `Styrke`, `Utblanding`.

Påstandsstatus: AVLEDET_XSD  
Kilde: programmatisk graftraversering fra `XSD-M30-FULL-2014-12-01:/schema/element[@name='FEST']` gjennom alle `xs:element/@ref`.
