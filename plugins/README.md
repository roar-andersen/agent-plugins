# Pluginer

Legg hver plugin i `plugins/<plugin-navn>/`. FEST 2.5.1-ekspert finnes i `fest-251-ekspert/`, med dokumentasjon i skillens referanser.

For støtte i både Claude Code og ChatGPT/Codex, bruk `.claude-plugin/plugin.json` i pluginmappen og del `skills/<skill-navn>/SKILL.md`. OpenAI støtter Claude-kompatible pakker. Et portabelt `plugin.json` ved pluginroten kan legges til for verter som støtter Agent Plugins 1.0; dette gir ikke automatisk støtte i alle agenter.

Minimalt Claude-manifest:

```json
{"name":"min-plugin","version":"0.1.0","description":"Beskriv hva pluginen gjør","author":{"name":"Roar Andersen"}}
```

Legg denne oppføringen i `plugins` i `.claude-plugin/marketplace.json`:

```json
{"name":"min-plugin","source":"./plugins/min-plugin"}
```

Legg denne oppføringen i `plugins` i `.agents/plugins/marketplace.json`:

```json
{"name":"min-plugin","source":{"source":"local","path":"./plugins/min-plugin"},"policy":{"installation":"AVAILABLE","authentication":"ON_INSTALL"},"category":"Productivity"}
```

Hold navn og stier like i begge kataloger. Øk versjonen ved utgivelser. Test i hver vert; verktøynavn, MCP-konfigurasjon, hooks og appkoblinger kan kreve tilpasninger. Ikke legg hemmeligheter i repoet.

Kjør `python scripts/plugin_versions.py --plugin <navn> --bump patch` for å øke og samordne versjonen. Se rotens README for automatisk versjonsøkning etter merge.
