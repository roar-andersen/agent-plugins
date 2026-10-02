# Informasjonsmodell og XML-struktur

## Skjemaer og namespaces

Alias og søkeord: namespace, M30, Forskrivning, import, XSD  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

M30 bruker target namespace `http://www.kith.no/xmlstds/eresept/m30/2014-12-01`. Forskrivning bruker `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`. Begge importerer `http://www.kith.no/xmlstds` fra `kith.xsd`; M30 importerer i tillegg Forskrivning. `elementFormDefault` er `qualified`, mens `attributeFormDefault` er `unqualified`. Prefixene i XSD er praktiske aliaser; namespace-URI-en, ikke prefixet, avgjør identiteten. [XSD-M30-FULL-2014-12-01, `/schema`; XSD-FORSKRIVNING-FULL-2014-12-01, `/schema`; XSD-KITH-COMMON, `/schema`]

## Roten `FEST`

Alias og søkeord: `FEST`, `HentetDato`, `GyldigFradatoHelfo`, rot, toppstruktur  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

`FEST` begynner med obligatorisk `HentetDato` av typen `xs:dateTime`, fulgt av valgfri `GyldigFradatoHelfo` av typen `xs:date`. Deretter følger de valgfrie katalogelementene i en fast `xs:sequence`; hver har skjemakardinalitet `0..1`. `GyldigFradatoHelfo` brukes bare i HELFO-uttrekk. Den tekniske meldingsbeskrivelsen presiserer at klienten skal bruke mottatt `HentetDato` nøyaktig ved neste inkrementelle henting. [XSD-M30-FULL-2014-12-01, `/schema/element[@name='FEST']`; HIS-3020-2018, PDF-side 9-10, kapittel 6.2.1]

M30 pakkes ikke i standard Hodemelding. Den visuelt kontrollerte pakkeoversikten skiller M30-delen fra den gjenbrukte Forskrivning-delen, og katalogdiagrammet viser de 15 valgfrie katalogene rundt `FEST`. [HIS-3020-2018, PDF-side 8-9, figur 1-3 og kapittel 6.1-6.2]

## `typeEnkeltoppforingFest` og oppføringer

Alias og søkeord: enkeltoppføring, `typeEnkeltoppforingFest`, `Id`, `Tidspunkt`, `Status`, arv  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`typeEnkeltoppforingFest` er abstrakt og inneholder obligatorisk `Id` (`xs:string`), `Tidspunkt` (`xs:dateTime`) og `Status` (`kith:CS`). De konkrete `Oppf...`-strukturene utvider typen med `xs:extension`. Et eksempel er `OppfLegemiddelpakning`, som arver oppføringsmetadata og kan inneholde `fs:Legemiddelpakning` med `0..1`. At innholdet er valgfritt er nødvendig fordi en utgått oppføring i et inkrement kan bestå bare av status og tidspunkt. [XSD-M30-FULL-2014-12-01, `/schema/complexType[@name='typeEnkeltoppforingFest']` og katalogelementene; HIS-3020-2018, PDF-side 10-13, kapittel 6.2.2-6.2.3]

## Arv og felles legemiddelinformasjon

Alias og søkeord: `typeLegemiddel`, arv, abstrakt klasse, fellesklasse  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

Den navngitte XSD-typen `fs:typeLegemiddel` samler felles elementer som `Atc`, `NavnFormStyrke`, `Reseptgruppe`, `LegemiddelformKort`, `RefVilkar`, `Preparattype`, `TypeSoknadSlv`, `Opioidsoknad`, `Refusjon`, `PakningByttegruppe`, `AdministreringLegemiddel` og `SvartTrekant`. `LegemiddelMerkevare`, `Legemiddelpakning`, `Legemiddeldose` og `LegemiddelVirkestoff` utvider denne typen. Veiledningen omtaler dette funksjonelt som den abstrakte fellesklassen Legemiddel. [XSD-FORSKRIVNING-FULL-2014-12-01, `/schema/complexType[@name='typeLegemiddel']` og relevante globale elementer; DMP-IMPL-3.6, PDF-side 14-15, kapittel 3.1 og visuelt kontrollert figur 4]

## Referanser og kardinalitet

Alias og søkeord: ID, IDREF, referanse, kardinalitet, `minOccurs`, `maxOccurs`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

`xs:ID` identifiserer forekomster i et fullt XML-dokument, og `xs:IDREF` refererer til en slik ID. Eksempler er `RefLegemiddelMerkevare`, `RefPakning`, `RefVilkar`, `RefVirkestoff` og `ParentId`. Kardinalitet kommer fra `minOccurs` og `maxOccurs`; manglende attributter betyr `1`. `maxOccurs="unbounded"` betyr `*`, ikke en bestemt øvre grense. I inkrementelle loose-skjemaer er berørte `IDREF` endret til `xs:string` fordi målet kan ligge utenfor deluttrekket. [XSD-M30-FULL-2014-12-01 og XSD-FORSKRIVNING-FULL-2014-12-01, alle `element[@type='IDREF']`; inkrementelle XSD-er, innledende kommentar og tilsvarende elementer]

Skjemakardinalitet er ikke alltid lik praktisk innhold. Veiledningen sier at `Legemiddelpakning/Pakningsinfo/RefLegemiddelMerkevare` og `LegemiddelVirkestoff/SortertVirkestoffMedStyrke` brukes som `1..*` i praksis selv om modellen åpner for `0..*`. Slike innstramminger skal merkes `DIREKTE_KILDE`, ikke endre den rapporterte XSD-kardinaliteten. [DMP-IMPL-3.6, PDF-side 28, kapittel 3.4]

## KITH-datatyper

Alias og søkeord: `CV`, `CS`, `PQ`, `MO`, kode, mengde, beløp  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

FEST bruker blant annet KITH-typene `CS` (Coded Simple value), `CV` (Coded Value), `PQ` (Physical Quantity) og `MO` (Monetary). Meldingsbeskrivelsen stiller strengere krav enn selve `kith.xsd`: for `CV` er `V`, `DN` og `S` obligatoriske, og for `CS` er `V` og `DN` obligatoriske. Denne dokumenterte innstrammingen skal brukes ved implementasjon selv om attributter ser valgfrie ut i felles-XSD-en. [HIS-3020-2018, PDF-side 7, kapittel 4.2.2; XSD-KITH-COMMON, globale typer]
