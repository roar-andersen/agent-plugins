# Administrering, interaksjoner, varsler og handelsvarer

## `AdministreringLegemiddel`

XML-navn: `AdministreringLegemiddel`  
Alias og søkeord: administrering, administrasjonsvei, knusing, deling, kortdose  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `Ingen`  
Brukes fra: `fs:typeLegemiddel` og legemiddelklassene som arver denne  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`AdministreringLegemiddel` samler informasjon for praktisk administrering. `Administrasjonsvei` er obligatorisk med `1..*`; `Blandingsveske`, `KanKnuses`, `KanApnes`, `Bolus`, `InjeksjonshastighetBolus` og `Deling` er valgfrie. `RefBlandingsveske`, `EnhetDosering`, `Kortdose`, `ForhandsregelInntak` og `BruksomradeEtikett` kan gjentas. [XSD-FORSKRIVNING-FULL-2014-12-01, `/schema/element[@name='AdministreringLegemiddel']`; DMP-IMPL-3.6, PDF-side 55-56, kapittel 7]

### Innhold

Veiledningen beskriver at kortdose er et kort, strukturert doseringsforslag, mens katalogen `KatStrDosering` inneholder mer detaljert strukturert dosering. Opplysninger må presenteres i riktig kontekst; fravær av et valgfritt element er ikke det samme som et negativt faglig svar.

### Relasjoner

`AdministreringLegemiddel` inngår i `typeLegemiddel`. `Kortdose` peker gjennom kodeverdi og kataloginnhold til doseringsinformasjon; `KatStrDosering` er en egen M30-katalog.

### Regler og begrensninger

Ikke utled at et legemiddel kan knuses eller åpnes dersom `KanKnuses` eller `KanApnes` mangler.

### Praktisk bruk

Bruk kodens `V`, `DN` og `S` ved visning og maskinell behandling av `CV`-verdier.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01`, `AdministreringLegemiddel`.
- `DMP-IMPL-3.6`, side 55-56.

## Interaksjoner

Alias og søkeord: `Interaksjon`, `Substansgruppe`, interaksjonsvarsel, interaksjonssøk  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Interaksjonskatalogen består av `OppfInteraksjon`-oppføringer med `Interaksjon` eller `InteraksjonIkkeVurdert`. `Interaksjon` knytter to eller flere `Substansgruppe`-referanser til faglig informasjon om interaksjonen, mens hver `Substansgruppe` inneholder ett eller flere substanselementer og kan knytte disse til `Virkestoff` gjennom `RefVirkestoff`. Interaksjonssøk bør derfor bygge fra et legemiddels virkestoffreferanser til relevante substansgrupper og deretter interaksjoner. [XSD-M30-FULL-2014-12-01, globale elementer `KatInteraksjon`, `Interaksjon`, `InteraksjonIkkeVurdert` og `Substansgruppe`; DMP-IMPL-3.6, PDF-side 57-60, kapittel 8]

`InteraksjonIkkeVurdert` betyr ikke automatisk «ingen interaksjon». Det representerer at kombinasjonen ikke er vurdert slik kilden beskriver. Visningen må skille dette fra en vurdert kombinasjon uten påvist problem. [DMP-IMPL-3.6, PDF-side 60, kapittel 8.5]

## Varsel fra DMP

Alias og søkeord: `VarselSlv`, varsel, gyldighetsperiode, referanse element  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

XML-navnet er historisk `VarselSlv`, selv om virksomheten nå heter DMP. Varsler ligger i `KatVarselSlv` og kan knyttes til elementer i hovedkatalogene gjennom en klasse-/referansestruktur. Varslets egne gyldighetsdatoer avgjør når det er relevant; oppføringsstatus og faglig gyldighetsperiode er forskjellige forhold. Dersom et varsel utløper, kan den tilknyttede referansen komme som utgått i et inkrement. [XSD-M30-FULL-2014-12-01, `KatVarselSlv` og `VarselSlv`; DMP-IMPL-3.6, PDF-side 61-63, kapittel 9]

## Handelsvarer

XML-navn: `MedForbMatr`, `Naringsmiddel`, `Brystprotese`  
Alias og søkeord: handelsvare, medisinsk forbruksmateriell, næringsmiddel, brystprotese, produktgruppe  
Namespace: `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`  
Definert i: `forskrivning-2014-12-01.xsd`  
Arver fra: `fs:typeVare`  
Brukes fra: `OppfHandelsvare` i `KatHandelsvare`  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

### Formål

`MedForbMatr` (medisinsk forbruksmateriell), `Naringsmiddel` og `Brystprotese` bygger på `typeVare`. Fellesinnholdet er `Nr`, `Navn`, valgfri `ProduktInfoVare`, valgfri `Leverandor`, gjentakbar `PrisVare` og valgfri `Refusjon`. `MedForbMatr` kan inneholde `BestanddelMatr`; `Naringsmiddel` kan inneholde `StyrkeFormStoff`. [XSD-FORSKRIVNING-FULL-2014-12-01, `typeVare` og de tre globale elementene; XSD-M30-FULL-2014-12-01, `KatHandelsvare`]

### Innhold og relasjoner

Produktgruppestrukturen finnes ikke som én ferdig katalog. Veiledningen sier at treet må bygges ved å kombinere kodeverk 7403 Produktgruppe med `Refusjonsgruppe` og handelsvareoppføringer. Koder med 1, 3, 5 og 7 siffer danner nivåer; konkrete varer kobles under 7-sifrede grupper gjennom refusjonsreferanser. [DMP-IMPL-3.6, PDF-side 67-69, kapittel 12.1 og visuelt kontrollert figur 22-23]

### Regler og begrensninger

Veiledningen anbefaler rekvirering på produktgruppenivå, ikke direkte varenummernivå. Strukturerte vilkår, blant annet alder, antallsbegrensning og krav om egen resept, må vurderes på gruppen. `Brystprotese` skal ignoreres ved rekvirering. [DMP-IMPL-3.6, PDF-side 68-71, kapittel 12.2]

### Praktisk bruk

Bygg visningstreet fra kodeverk 7403 og koble varer via refusjonsstrukturene. Ikke bruk eksempelbilder med eldre namespace som teknisk kilde; XML-navn og kardinaliteter skal alltid tas fra XSD-ene i denne pakken.

### Kilder

- `XSD-FORSKRIVNING-FULL-2014-12-01`, `typeVare`, `MedForbMatr`, `Naringsmiddel`, `Brystprotese`.
- `DMP-IMPL-3.6`, side 67-71.
