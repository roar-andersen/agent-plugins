# Vedlikehold av pluginer

- Gjør endringer gjennom PR til main. Ikke merge eller godkjenn PR-er automatisk.
- Behold samme pluginnavn ved oppdatering (navnet er pluginens identitet), og bevar øvrige pluginer/marketplace-oppføringer. Navnebytte krever eksplisitt beslutning og en migreringsmerknad i README.
- Bruk semantiske versjoner MAJOR.MINOR.PATCH uten datostempler eller build-suffiks.
- Ved pluginendringer, kjør `python scripts/plugin_versions.py --plugin <navn> --bump patch`. Bruk `minor` for nye funksjoner og `major` for brytende endringer. Verktøyet oppdaterer alle manifestene og begge marketplace-katalogene.
- Main-workflow øker automatisk patch når plugininnholdet er endret uten versjonsøkning. Eksplisitt høyere versjon beholdes. Ikke gjør en ekstra bump bare for CI-synkroniseringen.
- Kjør `python scripts/plugin_versions.py` og `python -m unittest discover -s tests -v` før PR.
- Ikke legg lokale FEST XML/ZIP-filer, indekser, innstillinger, personlige stier eller hemmeligheter i repoet.
- Endringer i FEST-dokumentasjon er kildepåstander. Hold dokumenterte krav atskilt fra implementasjonsvalg og faktiske data fra brukerens filer.
