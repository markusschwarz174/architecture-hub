---
document_id: ah-contract-schema
title: SCHEMA — dezentraler Strukturvertrag
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# SCHEMA

## Zweck

Ein `SCHEMA` definiert maschinenlesbar die zulässige Struktur eines konkreten
Inputs, Outputs, Zustands oder Interfaces. Schemas entstehen dezentral dort,
wo ein realer Konsument sie benötigt. Es gibt keine globale `SCHEMA.json`.

## Dateifamilie

```text
[SUBJECT].schema.json
[SUBJECT].schema.yaml
```

Die Dateiendung folgt der eingesetzten Schemasprache. Ein beliebiges Beispiel-
JSON ist noch kein Schema.

## Begriffsskelett

| Begriff | Funktion | Status |
|---|---|---|
| `SCHEMA_ID` | eindeutige Schema-Kennung | Pflicht |
| `SCHEMA_VERSION` | Version der Schemasprache und des lokalen Vertrags | Pflicht |
| `SUBJECT` | strukturierter Gegenstand | Pflicht |
| `AUTHORITY` | führende Quelle und Ableitungsrichtung | Pflicht |
| `TYPE` | Grundtyp oder Dokumentform | Pflicht |
| `REQUIRED` | verpflichtende Felder | Pflicht |
| `PROPERTIES` | Felder, Typen und Bedeutungen | Pflicht |
| `ENUMS` / `CONSTRAINTS` | zulässige Werte und strukturelle Grenzen | falls vorhanden |
| `ADDITIONAL_PROPERTIES` | Umgang mit unbekannten Feldern | Pflicht |
| `REFERENCES` | wiederverwendete Teil-Schemas | falls vorhanden |
| `COMPATIBILITY` | Umgang mit älteren und neueren Versionen | Pflicht bei langlebigen Daten |
| `CONSUMERS` | Validatoren, Tools und Interfaces | Pflicht |
| `SUPERSEDES` | abgelöstes Schema | falls vorhanden |

## OpenAPI-Spezialfall

`OpenAPI` wird einmalig als standardisierte Interface-Spezifikation für
HTTP-APIs aufgenommen. Eine OpenAPI-Datei kann Daten-Schemas enthalten und
zugleich Operationen, Parameter und Responses beschreiben. Sie ist deshalb
ein spezialisierter Interface-Vertrag, keine globale Ersatzform für jede SPEC.

## Grundregeln

1. Das Schema liegt bei seinem realen Subject oder Konsumenten.
2. Menschliche Begründung und maschinenlesbarer Vertrag bleiben verbunden,
   aber nicht als zwei widersprüchliche Authorities.
3. Mehrere Repräsentationen nennen, welche führend und welche abgeleitet ist.
4. Strukturprüfung ersetzt weder Policy-Entscheidung noch Permission-Check.
5. Die Ausführung der Prüfung und deren Evidenz gehören zu `QUALITY`.

## Abgrenzung

- `SPEC` beschreibt Bedeutung und Anforderungen.
- `SCHEMA` begrenzt Form, Typen und strukturelle Werte.
- `POLICY` entscheidet anhand von Inhalt und Kontext.
- `GUARDRAIL` setzt Regeln zur Laufzeit durch.

## Perlen und Provenienz

- `MY_AI_PROJECTS/2026-08 MAIL_ORGANIZER/VERSION_260923/schemas/` — getrennte
  Schemas für Security Policy, Automation Policy, Whitelist und Blacklist.
- `MY_AI_PROJECTS/.../src/mail_manager/config_loader.py` — Laden, Validieren
  und domänenübergreifende Konsistenzprüfungen.
- `OPENAI/SYSTEM/SCHEMAS/` — dezentrale Schemas für Hook-, Event- und
  Workspace-Artefakte.
- JSON Schema Draft 2020-12 und OpenAPI Specification — externe
  Standardreferenzen; konkrete Version wird pro Instanz festgelegt.
