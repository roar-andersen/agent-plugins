# agent-plugins

Roars Agent Plugins: en felles GitHub-katalog for pluginer til Claude Code, ChatGPT/Codex og andre kompatible agentverter.

## Marketplace

- Codex: `.agents/plugins/marketplace.json`
- Claude Code: `.claude-plugin/marketplace.json`
- Felles plugininnhold: `plugins/<plugin-navn>/`

Katalogene er foreløpig tomme. Marketplace kan registreres, men ingen plugin kan installeres før en faktisk plugin er lagt til. Se [veiledningen](plugins/README.md).

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
claude plugin install min-plugin@roar-agent-plugins
```

## ChatGPT

I arbeidsområder med GitHub-import kan en administrator velge Admin → Plugins → Add → Import marketplace og bruke `https://github.com/roar-andersen/agent-plugins`. Tilgjengelighet avhenger av arbeidsområdet. Lokalt oppsett for Codex er en separat installasjonsvei.

## Andre agenter

Det finnes ingen universell marketplace-installasjon som er dokumentert for alle agentverter. Verter som støtter Claude-pluginformatet kan bruke Claude-katalogen. Andre kan gjenbruke skills eller portable Agent Plugins-pakker dersom verten støtter dem. Test kompatibilitet per vert.

## Vedlikehold

Bruk PR-er til `main`, øk pluginens versjon ved endringer, og bruk Git-tagger for utgivelser. Hold begge marketplace-katalogene oppdatert når pluginer legges til eller fjernes.

## Dokumentasjon

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: GitHub import og sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Claude Code: Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code: Plugin manifest](https://code.claude.com/docs/en/plugins-reference)
