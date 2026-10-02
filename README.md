# agent-plugins

Roars Agent Plugins: en felles GitHub-katalog for pluginer til Claude Code, ChatGPT/Codex og andre kompatible agentverter.

## Marketplace

- Codex: `.agents/plugins/marketplace.json`
- Claude Code: `.claude-plugin/marketplace.json`
- Felles plugininnhold: `plugins/<plugin-navn>/`

Katalogene inneholder **FEST 2.5.1-ekspert**, som forklarer FEST og kan laste ned og søke i lokale FEST-uttrekk. Filstøtten krever en lokal agentvert og Python 3.10+ med SQLite FTS5. Se [veiledningen](plugins/README.md).

## Codex CLI

```powershell
codex plugin marketplace add roar-andersen/agent-plugins
```

## Claude Code

```powershell
claude plugin marketplace add roar-andersen/agent-plugins
```

Etter at en plugin er publisert:

```powershell
claude plugin install gpt-ce3361437e4b78daf6a2d783c10fce51@roar-agent-plugins
```

## ChatGPT

I arbeidsområder med GitHub-import kan en administrator velge Admin → Plugins → Add → Import marketplace og bruke `https://github.com/roar-andersen/agent-plugins`. Tilgjengelighet avhenger av arbeidsområdet. Lokalt oppsett for Codex er en separat installasjonsvei.

## Andre agenter

Det finnes ingen universell marketplace-installasjon som er dokumentert for alle agentverter. Verter som støtter Claude-pluginformatet kan bruke Claude-katalogen. Andre kan gjenbruke skills eller portable Agent Plugins-pakker dersom verten støtter dem. Test kompatibilitet per vert.

## Vedlikehold

Bruk PR-er til `main`, øk pluginens versjon ved endringer, og bruk Git-tagger for utgivelser. Hold begge marketplace-katalogene oppdatert når pluginer legges til eller fjernes.

Pluginens navn beholdes fra den eksisterende kontopluginen slik at identiteten er stabil. Marketplace-installasjonen og kontoinstallasjonen har ulike distribusjonskilder; bruk én av dem for å unngå duplisert funksjonalitet.

### Semantisk versjonering og oppdateringer

Versjonen finnes i portable-, Codex- og Claude-manifestene og i begge marketplace-katalogene. Øk alle samlet:

```powershell
python scripts/plugin_versions.py --plugin gpt-ce3361437e4b78daf6a2d783c10fce51 --bump patch
```

Bruk `minor` for nye funksjoner og `major` for brytende endringer. GitHub Actions kontrollerer manifestene og kjører tester. Etter merge til `main` øker workflowen automatisk patch dersom plugininnholdet er endret uten en eksplisitt versjonsøkning, samordner katalogene og lager en tagg `<plugin-navn>-v<versjon>`. En eksplisitt høyere versjon beholdes. Workflowen trenger skrivetilgang til innhold; branch protection må tillate versjonscommit fra denne workflowen for automatisk bump. Hvis dette ikke er tillatt, øk versjonen i PR-en med kommandoen over.

Versjonering gjør oppdateringene identifiserbare, men aktiverer ikke automatisk oppdatering i alle agentverter. Marketplace må være registrert fra GitHub og oppdateringsfunksjonen aktivert der verten støtter det. Codex kan hente oppdatert marketplace med:

```powershell
codex plugin marketplace upgrade roar-agent-plugins
```

I Claude Code kan automatisk oppdatering aktiveres for marketplace i plugininnstillingene; egen marketplace har ikke nødvendigvis dette aktivert som standard. Lokal import fra en kopiert mappe følger ikke GitHub-oppdateringer automatisk. Nye versjoner blir tilgjengelige først etter at de er merget til `main` og klienten har oppdatert sin marketplace.

## Dokumentasjon

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: GitHub import og sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Claude Code: Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code: Plugin manifest](https://code.claude.com/docs/en/plugins-reference)
