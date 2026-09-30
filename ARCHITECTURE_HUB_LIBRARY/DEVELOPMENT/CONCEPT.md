---
document_id: ah-development-template-concept
title: CONCEPT — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[PROJECT]_CONCEPT.md"
tags: [development, concept, system_description]
---

# [PROJECT] — CONCEPT

## Funktion

Das CONCEPT beschreibt den aktuell geltenden fachlichen Entwurf eines Systems: Zweck, erwartetes Verhalten, Bestandteile und Grenzen. In D1/D2 ist es die einfachere Alternative zur ARCHITECTURE.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Status | Geltung, Version und Authority | Pflicht |
| Zweck und Zielbild | Problem und gewünschter Zustand | Pflicht |
| Geltungsbereich | In Scope und Out of Scope | Pflicht |
| Fachliches Modell | Begriffe, Objekte und Beziehungen | Pflicht |
| Hauptabläufe | wesentliches Verhalten und HUMAN-Gates | Pflicht |
| Regeln und Invarianten | immer geltende fachliche Regeln | falls vorhanden |
| Schnittstellen und Abhängigkeiten | Nachbarsysteme und Voraussetzungen | falls vorhanden |
| Offene Punkte | noch nicht entschiedene Fragen | falls vorhanden |

## Status

| Feld | Wert |
|---|---|
| Projekt | `[PROJECT]` |
| Version | `[VERSION]` |
| Gültig ab | `[DATE]` |
| Autorität | `[HUMAN/PROJECT]` |
| Ersetzt | `[DOCUMENT_OR_NONE]` |

## 1. Zweck und Zielbild

`[Welches Problem löst das System und welcher Zustand soll gelten?]`

## 2. Geltungsbereich

- Enthalten: `[IN_SCOPE]`
- Nicht enthalten: `[OUT_OF_SCOPE]`

## 3. Fachliches Modell

`[Begriffe, Akteure, Objekte und Beziehungen in verständlicher Sprache.]`

## 4. Hauptabläufe

`[Wesentliche Abläufe, Entscheidungen und HUMAN-Gates.]`

## 5. Regeln und Invarianten

- `[RULE]`

## 6. Schnittstellen und Abhängigkeiten

`[Benachbarte Bereiche, Quellen, Senken und externe Voraussetzungen.]`

## 7. Offene Punkte

| ID | Frage | Owner | Status |
|---|---|---|---|
| C-001 | `[QUESTION]` | `[OWNER]` | OPEN |

## Abgrenzung

Das CONCEPT ist kein BAUPLAN, kein Fortschrittsbericht und keine verbindliche SPEC. Technische Strukturdetails gehören bei Bedarf in eine ARCHITECTURE.
