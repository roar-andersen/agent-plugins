# Lokale FEST 2.5.1-filer

Denne delen beskriver pluginens implementasjon, ikke nye FEST-krav.

## Oppsett og filer

Kjør skriptet `../scripts/fest_catalog.py` med lokal Python 3.10+. Det krever SQLite FTS5, som følger med vanlige Python-installasjoner. Pluginen leverer ingen Python-runtime. Hvis nødvendig runtime mangler, forklar det og bruk dokumentasjonsdelen; ikke påstå at filstøtten virker.

På Windows ligger brukerens innstillinger i `%LOCALAPPDATA%/Fest251Expert/settings.json`. På andre plattformer brukes `~/.config/Fest251Expert/settings.json`. På alle plattformer kan `--config <fil>` brukes før kommandoen for et separat oppsett. Del aldri denne filen eller søkeindeksen som del av pluginen.

Målmappen inneholder en undermappe per uttrekk og et snapshot per SHA-256-hash og indeksversjon. Snapshot inneholder `catalog.xml`, `index.sqlite` og, ved ZIP-import, `download.zip`. Gamle snapshots beholdes. Aktivt snapshot velges gjennom innstillingsfilen; det skiftes først etter vellykket innlasting. Ved endringer av målmappe kan tidligere uttrekk fortsatt være registrert fra den gamle mappen. Kontroller `status` og registrer/hent hvert uttrekk til ønsket mappe.

## Kommandoer

Eksempler viser argumentene etter `python <absolutt skriptsti>`:

```text
status
setup --directory <valgt-mappe> --datasets rekvirent institusjon veterinaer
refresh
refresh --datasets institusjon
register --directory <valgt-mappe> --file <XML-eller-ZIP> --dataset institusjon --environment production
search --dataset institusjon --query "paracetamol" --limit 10
search --dataset institusjon --query "paracetamol" --catalog KatLegemiddelMerkevare
get --dataset institusjon --id <oppførings-ID-eller-faglig-ID>
related --dataset institusjon --id <faglig-ID> --limit 10
```

`setup` og `refresh` laster ned fulle produksjonsuttrekk fra de tre åpne adressene. `refresh` uten valg oppdaterer bare allerede registrerte åpne uttrekk. Ingen bakgrunnsjobb er installert; oppdatering kjøres på brukerens forespørsel. Behold godkjenninger fra samme samtale. Ved feil beholdes tidligere registrert uttrekk; kontroller `errors` og `complete` i svaret. Adresser som slutter å virke skal verifiseres på DMPs side, ikke erstattes med en gjettet adresse.

`register` importerer brukerens eksisterende XML/ZIP. Brukeren må identifisere uttrekkstype og miljø. Miljø er `production`, `staging`, `test` eller `unknown`; ukjent er standard. Registrering kopierer og indekserer filen, og endrer ikke originalen. Tilgangsbegrensede uttrekk må leveres av brukeren; ingen autentisert Farmalogg/NAV-nedlasting er implementert. Bandasjist har heller ingen automatisk nedlasting i denne versjonen.

## Velg relevant uttrekk

- Eksplisitt uttrekk i brukerens spørsmål går foran andre regler.
- Veterinær bruk: `veterinaer`.
- Sykehus, sykehjem, ompakkede endoser, bulkpakninger eller legemiddeldoser: `institusjon`.
- Human forskrivning uten institusjonskontekst: start med `rekvirent` og oppgi dette valget.
- Handelsvarer: `bandasjist` hvis brukeren har valgt det; ellers relevante registrerte Rekvirent-/Institusjonsfiler, med kilde oppgitt.
- Oppgjørskontroll eller Farmalogg: bruk bare tilsvarende registrert uttrekk.
- Er flere uttrekk relevante, bruk `--dataset all` eller separate søk. Treff fra ulike uttrekk skal ikke slås sammen til ett kildegrunnlag. Ikke erstatt et manglende uttrekk med et annet uten å forklare det.

## Søk og sporbarhet

`search` søker i tekst og attributtverdier, med bokstavnormalisering og prefikssøk på alle ordene. Resultatet viser antall treff, begrensning, katalog, oppførings-ID, faglig ID og kilde. Søk kan treffe oppføringer som refererer til søkt ID; bruk `get` for eksakt identifikator. Bruk `get` for å lese XML-en til det konkrete treffet før du svarer om detaljer. XML-navnenes namespace beholdes, men serialisering kan vise `ns0`/`ns1`-prefikser.

`related` følger `Ref...`-elementer og viser også inngående referanser innenfor samme uttrekk. Uløste referanser merkes. Funksjonen dekker ikke alle mulige relasjoner representert på andre måter i modellen. Følg dokumentert mapping fra kunnskapsgrunnlaget der det trengs, og hent de konkrete oppføringene med `get`. Utfør flere oppslag ved kjeder over flere nivåer.

Skill mellom «ikke funnet i valgt uttrekk» og «finnes ikke i FEST». Oppgi kildens miljø og `HentetDato`, som gjelder datagrunnlaget og ikke faktisk nedlastingstid. `imported_at` er lokalt importtidspunkt. SHA-256 identifiserer eksakt kildeinnhold. Skill oppførings-ID fra faglig ID og varenummer.

## Størrelse, validering og begrensninger

Nedlasting, utpakking og XML-lesing skjer i strømmer. Bare én oppføring holdes i XML-minnet om gangen. Hele filen sendes ikke til språkmodellen; bare søketreff og valgte oppføringer returneres. ZIP og utpakket XML beholdes, og indeksen tar ekstra diskplass. Eksakt størrelse rapporteres i status. Snapshot per endret fil gjør at lagringsbehovet vokser; ingen automatisk sletting er implementert.

Grensen er 2 GiB per ZIP/XML-fil og et komprimeringsforhold på høyst 2000. ZIP må inneholde én XML-fil, som pakkes til et fast navn uten å følge ZIP-stier. DTD og entity-deklarasjoner avvises. Namespace, rot, dato, oppførings-ID og status kontrolleres. Dette er **ikke full XSD-validering**. Rapporter ikke filen som skjemavalidert.

Inkrementelle filer med utgåtte oppføringer avvises som fullt datagrunnlag. Sammenslåing av inkrementer er ikke implementert. Fravær av utgåtte oppføringer beviser ikke alene at en manuelt levert fil er full; spør brukeren ved usikkert opphav. En full fil må ikke erstattes av et inkrement. Produksjonsnedlasting som er eldre enn aktivt datagrunnlag avvises. Innholdsidentiske registreringer gjenbruker indeksen.

## Kilder til de åpne 2.5.1-uttrekkene

Verifisert 2026-10-02 fra DMPs nedlastingsside:

- https://www.dmp.no/om-oss/distribusjon-av-legemiddeldata/fest/nedlasting-av-fest-og-safest
- Rekvirent: https://www.dmp.no/globalassets/documents/om-oss/distribusjon-av-legemiddeldata/fest/festfiler/fest251.zip
- Institusjon: https://www.dmp.no/globalassets/documents/om-oss/distribusjon-av-legemiddeldata/fest/festfiler/fest251_inst.zip
- Veterinær: https://www.dmp.no/globalassets/documents/om-oss/distribusjon-av-legemiddeldata/fest/festfiler/fest251_vet.zip

Filstøtten er lokal og krever at agentverten kan kjøre Python og lese brukerens filer. En delt plugin bruker mottakerens oppsett. Nettleser- og mobilverter uten lokal prosesskjøring kan bruke dokumentasjonen, men ikke denne nedlastings- og søkefunksjonen.
