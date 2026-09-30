---
document_id: ah-tooling-template-prompt
title: PROMPT — wiederverwendbares Begriffsskelett
status: TEMPLATE
version: 1.0.0
created_at: 2026-09-30
functional_area: TOOLING
canonical_file_family: "PROMPT*.md"
authority: HUMAN_CONFIRMED_FILE_TYPE
aliases:
  - PROMPTVORLAGE
tags:
  - prompt
  - instruction
  - versioned
  - startprompt
  - masterprompt
  - brueckenprompt
  - uebergabeprompt
provenance:
  local_authority: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling
  decision_context: TOOLING-Dateitypen prüfen, HUMAN-confirmed on 2026-09-30
  source_check: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#provenienz-und-source-check-für-tooling
---

# [PROMPTNAME]

<!--
VERWENDUNG

Diese Vorlage wird kopiert und als eigenständige, versionierte
Modellinstruktion ausgefüllt. `PROMPT*.md` bezeichnet die lokale Familie und
keinen strikten Dateisystem-Glob. Bestehende Funktionsnamen wie STARTPROMPT,
MASTERPROMPT, BRÜCKENPROMPT und ÜBERGABEPROMPT bleiben zulässig.

Auftragsspezifische Daten werden nicht dauerhaft in eine allgemeine Vorlage
eingebrannt. Nicht benötigte optionale Kapitel werden entfernt.
-->

## PURPOSE

[PLATZHALTER: Welchen einen Zweck erfüllt dieser Prompt?]

## ACTIVATION

[PLATZHALTER: Wann wird der Prompt verwendet, und wann ausdrücklich nicht?]

## AUTHORITY

[PLATZHALTER: Welche Quellen und HUMAN-Entscheide sind verbindlich? Was gewinnt
bei einem Konflikt?]

## INPUTS

| Input | Bedeutung | Pflicht | Validierung |
|---|---|---|---|
| `[NAME]` | [PLATZHALTER] | JA/NEIN | [PLATZHALTER] |

## INSTRUCTIONS

1. [PLATZHALTER: kleinster vollständiger Arbeitsauftrag]
2. [PLATZHALTER: notwendige Reihenfolge oder Entscheidungsregel]
3. [PLATZHALTER: Abschlussbedingung]

## CONSTRAINTS

- [PLATZHALTER: verbotene oder begrenzte Handlung]
- [PLATZHALTER: Datenschutz-, Sicherheits- oder Freigaberegel]

## OUTPUT_CONTRACT

[PLATZHALTER: Format, Pflichtfelder, Zielpfad und beobachtbarer Zielzustand]

## FAILURE_AND_STOP

[PLATZHALTER: Wann wird mit HOLD, Rückfrage, Teilresultat oder Abbruch
reagiert?]

## VALIDATION

[PLATZHALTER: Wie wird das Ergebnis reproduzierbar geprüft?]

## REFERENCES

- [PLATZHALTER: kanonische Quelle oder abhängiger Vertrag]

## CHANGELOG

- `1.0.0` — [PLATZHALTER: initiale freigegebene Fassung]
