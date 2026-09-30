---
document_id: ah-development-template-architecture
title: ARCHITECTURE — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[PROJECT]_ARCHITECTURE.md"
tags: [development, architecture, components, interfaces]
---

# [PROJECT] — ARCHITECTURE

## Funktion

Die ARCHITECTURE beschreibt die aktuell geltende technische Struktur eines Systems. In D1/D2 ist sie die technisch detaillierte Alternative zum CONCEPT.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Status | Geltung, Version und Authority | Pflicht |
| Architekturziele | technische Zielgrössen | Pflicht |
| Systemgrenze und Kontext | Nachbarschaft und Verantwortung | Pflicht |
| Komponenten und Verantwortlichkeiten | Struktur und Ownership | Pflicht |
| Daten- und Kontrollfluss | Abläufe, Zustände und Gates | Pflicht |
| Schnittstellen und Verträge | Bindung an SPECS/SCHEMAS | falls vorhanden |
| Entscheidungen und Begründungen | Referenz auf gültigen Verlauf | Pflicht |
| Risiken, Annahmen und offene Fragen | Unsicherheit sichtbar halten | falls vorhanden |

## Status

| Feld | Wert |
|---|---|
| Projekt | `[PROJECT]` |
| Version | `[VERSION]` |
| Gültig ab | `[DATE]` |
| Autorität | `[HUMAN/PROJECT]` |
| Ersetzt | `[DOCUMENT_OR_NONE]` |

## 1. Architekturziele

- `[GOAL]`

## 2. Systemgrenze und Kontext

`[System, Nachbarsysteme, HUMAN, Quellen und Senken.]`

## 3. Komponenten und Verantwortlichkeiten

| Komponente | Verantwortung | Input | Output | Owner |
|---|---|---|---|---|
| `[COMPONENT]` | `[RESPONSIBILITY]` | `[INPUT]` | `[OUTPUT]` | `[OWNER]` |

## 4. Daten- und Kontrollfluss

`[Reihenfolge, Zustände, Gates, Fehler- und Wiederaufnahmepfade.]`

## 5. Schnittstellen und Verträge

| Schnittstelle | Vertrag/SPEC | Produzent | Konsument |
|---|---|---|---|
| `[INTERFACE]` | `[SPEC_REF]` | `[PRODUCER]` | `[CONSUMER]` |

## 6. Entscheidungen und Begründungen

`[Verweise auf DEVELOPMENT_LOG-Ereignisse und gültige Verträge.]`

## 7. Risiken, Annahmen und offene Fragen

| ID | Typ | Aussage | Evidenz/Owner | Status |
|---|---|---|---|---|
| A-001 | `[RISK/ASSUMPTION/QUESTION]` | `[STATEMENT]` | `[REF/OWNER]` | OPEN |

## Abgrenzung

Die ARCHITECTURE ist keine Implementierungscheckliste, kein BUILD_RECORD und keine QUALITY-Validierung. Verbindliche Feld- oder Schnittstellenanforderungen gehören in eine SPEC.
