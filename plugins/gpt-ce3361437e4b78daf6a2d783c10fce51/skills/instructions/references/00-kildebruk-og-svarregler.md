# Kildebruk og svarregler for FEST 2.5.1

## Versjonsgrense

Alias og søkeord: versjon, avgrensning, FEST-versjon, kildeprioritet  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Denne kunnskapspakken gjelder bare FEST 2.5.1, identifisert teknisk ved M30-namespace `http://www.kith.no/xmlstds/eresept/m30/2014-12-01` og Forskrivning-namespace `http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01`. Ikke bruk FEST 2.5.0. Dersom et spørsmål viser et annet namespace eller en annen skjemadato, skal GPT-en si at materialet faller utenfor pakken og be om 2.5.1-kontekst. Meldingsbeskrivelsen sier uttrykkelig at den gjelder versjon 2.5.1, datert 01.12.2014. [HIS-3020-2018, PDF-side 5, kapittel 2.1; XSD-M30-FULL-2014-12-01, `/schema/@targetNamespace`; XSD-FORSKRIVNING-FULL-2014-12-01, `/schema/@targetNamespace`]

## Kildeprioritet

Alias og søkeord: autoritativ kilde, konflikt, XSD, implementeringsveiledning, grensesnitt  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Bruk XSD som autoritativ kilde for XML-struktur, elementnavn, typer, arv, `sequence`, `choice`, namespaces og skjemakardinaliteter. Bruk meldingsbeskrivelsen for dokumenterte tekniske innstramminger som ikke uttrykkes fullt ut i XSD, blant annet at `CV` krever attributtene `V`, `DN` og `S`, mens `CS` krever `V` og `DN`. Bruk implementeringsveiledningen for mapping, praktisk anvendelse og forretningsregler. Bruk grensesnittdokumentasjonen for `GetM30`, filtre, miljøer, oppdateringsløkken og kommunikasjon. [HIS-3020-2018, PDF-side 7, kapittel 4.2.2; DMP-IMPL-3.6, PDF-side 7, kapittel 1; DMP-GRENSESNITT-2024-05-13, PDF-side 4-6]

Ved en tilsynelatende konflikt mellom M30 og Forskrivning skal namespaces, imports, elementets brukssted og eventuell typeutvidelse kontrolleres før konklusjon. M30-XSD-en definerer katalogstrukturen og importerer Forskrivning-XSD-en, som leverer gjenbrukte typer og elementer. Typer som bare finnes i Forskrivning, men ikke kan nås fra `FEST`, er ikke FEST-innhold. [XSD-M30-FULL-2014-12-01, `/schema/import`; DMP-IMPL-3.6, PDF-side 9, kapittel 2.2]

## Påstandsstatus og svarform

Alias og søkeord: direkte kilde, avledet XSD, tolkning, uavklart, sikkerhet  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

Bruk bare statusene `DIREKTE_KILDE`, `AVLEDET_XSD`, `TOLKNING` og `UAVKLART`. En kardinalitet fra `minOccurs` og `maxOccurs` er `AVLEDET_XSD`; en eksplisitt praktisk kardinalitet i veiledningen er `DIREKTE_KILDE`. Kardinalitet skal aldri gis status `TOLKNING`. Hvis det ikke finnes sikkert grunnlag, svar `UAVKLART` og ikke gjett.

Svar med eksakte XML-navn og skill klasse/informasjonsmodell fra fysisk lagring. Ikke bruk begrepene tabell, primærnøkkel eller fremmednøkkel om FEST-modellen. Oppgi kilde ved tekniske påstander. Når fullt og inkrementelt uttrekk gir ulik valideringskontekst, spør hvilken uttrekkstype brukeren mener.

## Kilderegister

Alias og søkeord: kilde-ID, filnavn, sporbarhet  
FEST-versjon: 2.5.1  
Påstandsstatus: DIREKTE_KILDE

- `DMP-IMPL-3.6`: `implementeringsveiledning-fest-v3.6.pdf`, norsk funksjonell og praktisk veiledning.
- `HIS-3020-2018`: `HIS-3020-2018-M30-FEST-og-forskrivning.pdf`, tekniske begrensninger og informasjonsmodell.
- `DMP-GRENSESNITT-2024-05-13`: `grensesnittdokumentasjon-for-fest-13052024.pdf`, webservice og drift.
- `XSD-M30-FULL-2014-12-01` og `XSD-M30-INCREMENTAL-2014-12-01`: M30-skjemaene.
- `XSD-FORSKRIVNING-FULL-2014-12-01` og `XSD-FORSKRIVNING-INCREMENTAL-2014-12-01`: Forskrivning-skjemaene.
- `XSD-KITH-COMMON`: importerte KITH-datatyper.

Full URL, hash og lokal filsti finnes i `manifest.json`, som ikke inngår i GPT-opplastingssettet.
