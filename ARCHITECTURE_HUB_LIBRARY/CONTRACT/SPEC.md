---
document_id: ah-contract-spec
title: SPEC — beschreibender Vertrag
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# SPEC

## Zweck

Eine `SPEC` beschreibt überprüfbar, was ein System, Baustein, Interface oder
Artefakt leisten muss und welche Grenzen gelten. Sie ist der allgemeine
beschreibende Vertrag im Funktionsbereich `CONTRACT`.

`SPECIFICATION` ist ein `ALIAS`, kein zweiter lokaler Dateityp.

## Dateifamilie

```text
[SUBJECT]_SPEC.md
[SUBJECT]_SPEC.yaml
[SUBJECT]_SPEC.json
```

Das Format folgt dem tatsächlichen Leser:

- Markdown für HUMAN und AI;
- YAML oder JSON für deterministische Konsumenten;
- mehrere Darstellungen nur mit benannter Authority und Ableitungsrichtung.

## Begriffsskelett

Nur für den Gegenstand relevante Kapitel werden materialisiert.

| Begriff | Funktion | Status |
|---|---|---|
| `PURPOSE` | Zweck des spezifizierten Gegenstands | Pflicht |
| `SCOPE` | Geltungsbereich | Pflicht |
| `OUT_OF_SCOPE` | ausdrücklich ausgeschlossene Verantwortung | Pflicht, wenn eine Verwechslung möglich ist |
| `AUTHORITY` | Entscheidungsquelle, Konfliktvorrang und Geltungsstatus | Pflicht |
| `REQUIREMENTS` | überprüfbare Anforderungen | Pflicht |
| `INPUTS` | akzeptierte Eingaben und Vorbedingungen | falls vorhanden |
| `OUTPUTS` | zugesicherte Ergebnisse | falls vorhanden |
| `INTERFACES` | Übergaben und externe Verträge | falls vorhanden |
| `INVARIANTS` | Bedingungen, die immer gelten müssen | falls vorhanden |
| `FAILURE_BEHAVIOR` | Verhalten bei nicht erfüllbaren Bedingungen | Pflicht bei ausführbaren Gegenständen |
| `LIFECYCLE` | Referenz auf den geltenden Output-Lebenszyklus | Pflicht, wenn Outputs entstehen |
| `QUALITY_REFERENCE` | Verweis auf Prüfung und Evidenz in `QUALITY` | falls Prüfung erforderlich ist |
| `REFERENCES` | Quellen und abhängige Verträge | Pflicht |

## Authority-Minimum

```yaml
status: <DRAFT|ACTIVE|DEPRECATED|SUPERSEDED>
decision_authority: <HUMAN oder belegte Authority>
conflict_precedence: <höhere Quelle oder Regel>
effective_from: <ISO-8601 oder NOT_ACTIVE>
supersedes: <Referenz oder NONE>
update_trigger: <konkreter Auslöser>
```

`RESPONSIBILITY` und `OWNER` werden nicht in dieser Datei definiert. Sie
gehören zum ausführenden Tool in `TOOLING`. Eine SPEC referenziert das Tool,
wenn dessen Zuständigkeit für die Ausführung relevant ist.

## Abgrenzung

- `POLICY` entscheidet regelbasiert unter Bedingungen.
- `PERMISSION` erlaubt oder blockiert eine konkrete Aktion auf einer Ressource.
- `SCHEMA` definiert maschinenlesbare Struktur.
- `GUARDRAIL` setzt Grenzen an einem realen Kontrollpunkt durch.
- `LIFECYCLE` regelt den Lebensweg erzeugter Outputs.
- Validation und Prüfevidenz gehören zu `QUALITY`.

`OpenAPI` ist ein Spezialfall für HTTP-APIs und Interfaces. Es ersetzt nicht
die allgemeine SPEC und erzeugt keinen zusätzlichen universellen Dateityp.

## Perlen und Provenienz

- `FIELD_NOTES_DRAFT/0_MISSION_CONTROL/PACKAGES/PACKAGE_CORE.md` — minimaler
  Arbeitsvertrag mit Trigger, Entry, Actor, Action, Exit und Speicherort.
- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_OPERATIONS_MATRIX.md` — eine führende
  Quelle pro Konzept sowie explizite Authority bei Konflikten.
- `ARCHITECTURE_HUB_DEVELOPMENT/WORKFLOW_FUNCTIONAL_AREA_DRAFT.MD` —
  Formatwahl nach Leser und Ausführung; Authority bei mehreren Darstellungen.
- ISO/IEC/IEEE 29148 — externe Referenz für Requirements Engineering; keine
  automatisch übernommene lokale Pflichtstruktur.
