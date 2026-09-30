---
document_id: ah-development-template-build-record
title: BUILD_RECORD — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[PROJECT]_BUILD_RECORD.md"
tags: [development, build_record, progress, resume]
---

# [PROJECT] — BUILD RECORD

## Funktion

Der BUILD_RECORD ist die fortlaufende Baudokumentation: tatsächlich ausgeführte Arbeit, aktueller Bauzustand, Abweichungen und verlässlicher Wiederaufnahmepunkt. Er vereint Baubericht, Baufortschritt und Wiederaufnahme, nicht jedoch die vorgängige Planung.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Aktueller Bauzustand | kompakter verlässlicher Stand | Pflicht |
| Wiederaufnahme | exakter Einstieg nach Unterbruch | Pflicht |
| Bauchronik | tatsächlich ausgeführte Schritte und Evidenz | Pflicht |
| Offene Baustellen | Blocker und nächste Aktionen | falls vorhanden |
| Abgrenzung | Trennung von BAUPLAN und Log | Pflicht |

## Aktueller Bauzustand

| Feld | Wert |
|---|---|
| Stand | `[TIMESTAMP]` |
| Letzter abgeschlossener Schritt | `[STEP_ID]` |
| Nächster sicherer Schritt | `[NEXT_STEP]` |
| Aktive Blocker | `[BLOCKERS_OR_NONE]` |
| Zugehöriger BAUPLAN | `[BAUPLAN_REF_OR_NONE]` |
| Geltendes CONCEPT/ARCHITECTURE | `[REF]` |

## Wiederaufnahme

1. Lies: `[REQUIRED_REFS]`
2. Prüfe: `[PRECONDITIONS]`
3. Starte bei: `[EXACT_RESUME_POINT]`
4. Nicht wiederholen: `[COMPLETED_OR_INVALIDATED_WORK]`

## Bauchronik

### [TIMESTAMP] — [STEP_ID]

- Ausgeführt: `[ACTION]`
- Ergebnis: `[RESULT]`
- Evidenz: `[FILES/TESTS/OUTPUT_REFS]`
- Abweichung vom BAUPLAN: `[NONE_OR_DESCRIPTION]`
- Entscheidung/Log-Referenz: `[EVENT_ID_OR_NONE]`
- Status: `[DONE/PARTIAL/BLOCKED/REVERTED]`

## Offene Baustellen

| ID | Beschreibung | Ursache | Nächste Aktion | Owner |
|---|---|---|---|---|
| B-001 | `[ITEM]` | `[CAUSE]` | `[ACTION]` | `[OWNER]` |

## Abgrenzung

Der BUILD_RECORD ersetzt weder den BAUPLAN noch das DEVELOPMENT_LOG. Der BAUPLAN sagt voraus, wie gebaut werden soll; der BUILD_RECORD hält fest, was tatsächlich geschah.
