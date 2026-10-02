# FEST 2.5.1-ekspert: brukerveiledning

Pluginen hjelper deg med FEST 2.5.1, DMPs legemiddeldata for eResept. Den har tre deler:

| Del | Hva du får | Krever |
|---|---|---|
| Kunnskap | Informasjonsmodell, XML/XSD, mapping og forretningsregler, med kildehenvisninger | Ingenting |
| Lokale FEST-filer | Søk og oppslag i faktiske legemidler, pakninger, refusjoner og interaksjoner | Engangsnedlasting, se under |
| Webservice | Veiledning og testede C#/.NET-klienter for `FestService251.svc` (`GetM30`) | Ingenting |

## Kom i gang

1. **Installer pluginen** (én gang):
   - Claude Code: `claude plugin marketplace add roar-andersen/agent-plugins`, deretter `claude plugin install fest-251-ekspert@roar-agent-plugins`
   - Codex: `codex plugin marketplace add roar-andersen/agent-plugins`
   - Har du den eldre `gpt-ce3361437e4b78daf6a2d783c10fce51`: avinstaller den først. Den oppdateres ikke til det nye navnet.
2. **Sjekk Python**: Kjør `python --version` (eller `py --version` på Windows). Du trenger 3.10 eller nyere. Mangler Python, installer det fra python.org.
3. **Last ned FEST-filene**: Skriv «Kom i gang med FEST-pluginen». Agenten foreslår en mappe (for eksempel `Dokumenter/FEST`) og hvilke uttrekk som skal hentes. Svar «ja» eller velg selv. Nedlasting og indeksering av alle tre uttrekkene tok rundt ett minutt i test.
4. **Prøv et søk**: For eksempel «Finn pakninger med paracetamol i Institusjon-uttrekket».

Første gang du bruker pluginen, sier agenten fra om at filene mangler, og tilbyr å laste dem ned.

## Hvilke uttrekk skal jeg velge?

| Uttrekk | Bruk når du jobber med | Nedlasting | Diskplass med indeks |
|---|---|---:|---:|
| Rekvirent | Forskrivning utenfor institusjon (journalsystem, eResept) | ca. 15 MB | ca. 400 MB |
| Institusjon | Sykehus og sykehjem, inkludert legemiddeldoser og bulk | ca. 15 MB | ca. 400 MB |
| Veterinær | Veterinær forskrivning | ca. 1 MB | ca. 30 MB |

Velg det uttrekket systemet ditt bruker. Er du usikker, ta Institusjon og Rekvirent. Bandasjist, NAV og Farmalogg lastes ikke ned automatisk. Har du slike filer, be agenten registrere dem («registrer denne FEST-filen …»).

## Holde filene oppdatert

DMP publiserer ny FEST hver 14. dag. Skriv «oppdater FEST-filene». Gamle versjoner beholdes, så et søk kan alltid knyttes til datagrunnlaget det ble gjort i (`HentetDato`). Ingen bakgrunnsjobb installeres.

## Eksempler på spørsmål

- «Hvordan henger legemiddelpakning, refusjon og byttegruppe sammen?»
- «Hva er forskjellen på fullt og inkrementelt uttrekk?»
- «Finn pakningen med varenummer 123456 i Rekvirent.»
- «Hvilke endepunkter har FestService251 i test og produksjon?»
- «Vis en C#-klient som henter inkrementelle oppdateringer med GetM30.»
- «Hvorfor får jeg Returkode 5 fra FEST?»

## Webservice-integrasjon i C#/.NET

Referansen `skills/instructions/references/10-webservice-integrasjon-dotnet.md` beskriver kontrakten, oppdateringsløkken, returkoder, meldingsstørrelser og feilbehandling. Den skiller mellom DMP-krav, WSDL-kontrakt, testet oppførsel og implementasjonsråd. Kjørbare eksempler for .NET 10 ligger i `skills/instructions/examples/dotnet/`:

```text
dotnet run --project skills/instructions/examples/dotnet/HttpClient -- full Veterinær
dotnet run --project skills/instructions/examples/dotnet/HttpClient -- update Rekvirent
```

Eksemplene kaller testmiljøet på internett som standard. Sett miljøvariabelen `FEST_ENDPOINT` for et annet endepunkt.

## Begrensninger

- Filstøtten krever en agentvert som kan kjøre Python lokalt (Codex eller Claude Code). I nettleser og mobil virker bare kunnskaps- og webservicedelen.
- Lokale filer kontrolleres, men XSD-valideres ikke.
- Pluginen kaller ikke webservicen selv. Den hjelper deg med å lage klienten.
- Gjelder bare FEST 2.5.1.

Feil i FEST-data meldes til DMP på `fest@dmp.no`. Feil i pluginen meldes som issue i GitHub-repoet.
