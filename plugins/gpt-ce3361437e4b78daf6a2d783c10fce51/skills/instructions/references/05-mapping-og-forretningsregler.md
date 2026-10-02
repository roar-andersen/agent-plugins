# Mapping og forretningsregler

## Virkestoff til merkevare og pakning

Alias og søkeord: mapping, `RefLegemiddelMerkevare`, `RefPakning`, virkestoffrekvirering  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Fra `LegemiddelVirkestoff` kan mottakeren følge `RefLegemiddelMerkevare` direkte til relevante `LegemiddelMerkevare`-forekomster og `RefPakning` direkte til relevante `Legemiddelpakning`-forekomster. Referanseverdiene er `IDREF` i skjemaet for fullt uttrekk. Ved virkestoffrekvirering gir disse koblingene hvilke merkevarer og pakninger som representeres av kombinasjonen av virkestoff, form og styrke. [DMP-IMPL-3.6, PDF-side 25-27, kapittel 3.3.1 og 3.3.5; XSD-FORSKRIVNING-FULL-2014-12-01, `LegemiddelVirkestoff/RefLegemiddelMerkevare` og `RefPakning`]

For å fylle valg av mengdeenhet kan systemet hente `Pakningsinfo/EnhetPakning` fra alle relevante pakninger og aggregere verdiene. Alternativt kan systemet vise tilgjengelige pakningsstørrelser. Ved Farmalogg-uttrekk skal humane og veterinære ATC-koder skilles, slik at veterinære pakninger ikke blir foreslått ved human ekspedering. [DMP-IMPL-3.6, PDF-side 26-27, kapittel 3.3.5]

## Merkevare til pakning

Alias og søkeord: merkevare pakning, `Pakningsinfo`, `RefLegemiddelMerkevare`, flerstyrkepakning  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Koblingen går fra pakningen til merkevaren: finn `Legemiddelpakning` der en `Pakningsinfo/RefLegemiddelMerkevare` matcher ønsket merkevare-ID. XSD-en tillater `0..*`, mens veiledningen sier at det i faktisk FEST-innhold er `1..*`: en pakning hører alltid til minst én merkevare, og flerstyrkepakninger kan peke til flere. Ikke modeller dette som en fysisk fremmednøkkel; det er en XML-referanse mellom identifikatorer. [DMP-IMPL-3.6, PDF-side 26 og 28, kapittel 3.3.2 og 3.4; XSD-FORSKRIVNING-FULL-2014-12-01, `Pakningsinfo/RefLegemiddelMerkevare`]

## Merkevare til dose og dose til pakning

Alias og søkeord: `Legemiddeldose`, LMR-nummer, minste plukkbare enhet, `RefPakning`  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

`Legemiddeldose` representerer en bestemt minste plukkbare enhet, for eksempel én tablett eller én ampulle. `RefLegemiddelMerkevare` er obligatorisk (`1`), mens `RefPakning` er `1..*` i XSD. Fra merkevare til dose søker man derfor etter doser med matchende `RefLegemiddelMerkevare`; fra dose til pakning følger man `RefPakning`. `Pakningskomponent` kan beskrive delene i et sett. [DMP-IMPL-3.6, PDF-side 21-22 og 26, kapittel 3.2.4 og 3.3.3-3.3.4; XSD-FORSKRIVNING-FULL-2014-12-01, `Legemiddeldose`; visuelt kontrollert figur 12 og 21]

Ved visning av en dose må detaljer som ikke finnes på dosen, hentes gjennom relasjonene. Veiledningen nevner at detaljert styrkeinformasjon kan hentes fra `SortertVirkestoffMedStyrke` på merkevaren. [DMP-IMPL-3.6, PDF-side 27-28, kapittel 3.3.5]

## Styrke og virkestoff

Alias og søkeord: `Virkestoff`, `VirkestoffMedStyrke`, `SortertVirkestoffMedStyrke`, alternativ styrke  
FEST-versjon: 2.5.1  
Påstandsstatus: AVLEDET_XSD

`VirkestoffMedStyrke` inneholder obligatorisk `Id`, `Styrke`, `RefVirkestoff` og `Styrkeoperator`. `StyrkeNevner`, `AlternativStyrke`, `AlternativStyrkeNevner`, `StyrkeOvreVerdi` og `AtcKombipreparat` er valgfrie. `SortertVirkestoffMedStyrke` gir obligatorisk `Sortering` og `RefVirkestoffMedStyrke`; `SortertVirkestoffUtenStyrke` gir `Sortering` og `RefVirkestoff`. [XSD-FORSKRIVNING-FULL-2014-12-01, de tre globale elementene]

Flytende preparater uttrykker ofte styrke som konsentrasjon. For enkeltdoser kan styrken angis per totalvolum. Pulver oppgis normalt som mengde virkestoff i vekt; væskevolum for oppløsning må ikke forveksles med selve styrken. Alternativ styrke brukes i dokumenterte tilfeller, blant annet når prosentstyrke suppleres med vekt/vekt eller vekt/volum. [DMP-IMPL-3.6, PDF-side 33-35, kapittel 5.5]

## Reseptgyldighet, vilkår og perioder

Alias og søkeord: reseptgyldighet, `Vilkår`, `StrukturertVilkar`, gyldig fra, gyldig til  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Ved virkestoffrekvirering kan reseptgyldighet hentes fra en tilhørende `LegemiddelMerkevare`, fordi veiledningen beskriver den som lik når ATC-koden er den samme. Flerstyrkepakninger er et teoretisk særtilfelle, men veiledningen oppgir at de aktuelle forekomstene ikke avviker fra normal ettårs gyldighet. [DMP-IMPL-3.6, PDF-side 27, kapittel 3.3.5]

`Vilkår` kan inneholde gjentatte `StrukturertVilkar`-elementer. Den lesbare teksten skal beholdes for visning selv når en strukturert variant finnes. Visuelt kontrollert figur 15 viser forholdet mellom katalogoppføring, `Vilkar`, strukturerte vilkår og referanser fra legemiddel, vare og refusjonsgruppe. Eksemplene i figur 16-18 viser strukturerte verdier for blant annet kjønn, alder, spesialist/sykehus og maksimalt antall. [DMP-IMPL-3.6, PDF-side 35-38, kapittel 5.7-5.8 og visuelt kontrollert figur 15-18; XSD-M30-FULL-2014-12-01, `Vilkar` og `StrukturertVilkar`]

## Regel for fravær og usikkerhet

Alias og søkeord: manglende felt, valgfritt, null, ukjent  
FEST-versjon: 2.5.1  
Påstandsstatus: TOLKNING

Et valgfritt XML-element som mangler, dokumenterer bare at elementet ikke er levert i den aktuelle forekomsten. Det bør ikke uten en uttrykkelig kilde oversettes til `false`, «ingen», «ikke relevant» eller en standardverdi. Denne regelen er en forsiktig implementasjonstolkning basert på XSD-kardinalitet og skal oppgis som `TOLKNING` når den brukes.
