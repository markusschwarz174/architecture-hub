---
document_id: ah-development-template-bauplan
title: BAUPLAN — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[CHANGE]_BAUPLAN.md"
tags: [development, bauplan, planning, implementation]
---

# [CHANGE] — BAUPLAN

## Funktion

Der BAUPLAN wird vom PLANNER erstellt und ist die nachvollziehbare Anleitung für den IMPLEMENTOR. Er zerlegt eine freigegebene Änderung in prüfbare Bauschritte. Der IMPLEMENTOR dokumentiert die tatsächliche Ausführung anschließend im BUILD_RECORD.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Auftrag | Change, Ziel, Rollen und Grundlagen | Pflicht |
| Scope und Nicht-Ziele | Grenze der Umsetzung | Pflicht |
| Vorbedingungen | notwendiger Startzustand | Pflicht |
| Bauschritte | geordnete prüfbare Umsetzung | Pflicht |
| Prüf- und Rückfallpunkte | sichere Gates und Wiederaufnahme | Pflicht |
| Risiken und offene Entscheide | Eskalationen vor Ausführung | falls vorhanden |
| Abschlusskriterien | objektiver Zielzustand | Pflicht |
| Abgrenzung | Trennung vom tatsächlichen Bauverlauf | Pflicht |

## 1. Auftrag

| Feld | Wert |
|---|---|
| Change-ID | `[CHANGE]` |
| Ziel | `[GOAL]` |
| Grundlage | `[CONCEPT_OR_ARCHITECTURE_REF]` |
| Verbindliche SPECS | `[SPEC_REFS_OR_NONE]` |
| Planner | `[PLANNER]` |
| Implementor | `[IMPLEMENTOR_OR_UNASSIGNED]` |
| Freigabe/Gate | `[GATE_REF]` |

## 2. Scope und Nicht-Ziele

- In Scope: `[IN_SCOPE]`
- Out of Scope: `[OUT_OF_SCOPE]`

## 3. Vorbedingungen

- `[PRECONDITION]`

## 4. Bauschritte

| ID | Aktion | Betroffene Artefakte | Erwartetes Ergebnis | Nachweis | Status |
|---|---|---|---|---|---|
| BP-01 | `[ACTION]` | `[PATHS]` | `[EXPECTED_RESULT]` | `[CHECK]` | PLANNED |

Zulässige Statuswerte: `PLANNED`, `READY`, `IN_PROGRESS`, `BLOCKED`, `DONE`, `SKIPPED`, `SUPERSEDED`.

## 5. Prüf- und Rückfallpunkte

| Nach Schritt | Prüfung | HUMAN-Gate | Rückfall/Wiederaufnahme |
|---|---|---|---|
| BP-01 | `[CHECK]` | `[YES/NO]` | `[RECOVERY_POINT]` |

## 6. Risiken und offene Entscheide

| ID | Typ | Beschreibung | Owner | Behandlung |
|---|---|---|---|---|
| R-001 | `[RISK/HUMAN_DECISION]` | `[DESCRIPTION]` | `[OWNER]` | `[ACTION_OR_GATE]` |

## 7. Abschlusskriterien

- `[VERIFIABLE_EXIT_CRITERION]`

## Abgrenzung

Der BAUPLAN ist keine Baudokumentation. Fortschritt und Wiederaufnahme stehen im BUILD_RECORD; chronologische Entscheidungen und Lernkandidaten im DEVELOPMENT_LOG.
