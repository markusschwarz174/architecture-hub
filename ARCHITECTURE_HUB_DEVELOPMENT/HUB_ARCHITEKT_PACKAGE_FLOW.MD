---
document_id: ah-hub-architekt-package-flow
title: HUB-ARCHITEKT — PROJECT START PACKAGE FLOW
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-10-01
authority: HUMAN_PILOT_REQUIRED
---

# HUB-ARCHITEKT — PACKAGE FLOW

## Zweck

Dieser Flow ergaenzt den aktiven `AH_AGENT_ARCHITEKT.MD` fuer genau einen
Auftrag: Aus einem bestaetigten `PROJECT_PROFILE.json` ein begruendetes,
baubares PROJECT_START_PACKAGE vorbereiten.

## Eingang

- schema-valides Profil mit Status `CONFIRMED`;
- ADVISOR-Handover;
- aktuelle Library und ihre Git-Revision;
- HUMAN-Authority fuer die Auswahl.

## 1. Profil uebernehmen

Pruefe Profil-ID, Status, offene Entscheide und Risiken. Materielle Luecken
fuehren zu `TAKEOVER_REJECTED` an den ADVISOR oder zu `HOLD` beim HUMAN.

## 2. A- und D-Stufe bestimmen

- A1–A4 folgt Verantwortung und Validationsgrenze aus `AH_MISSION.MD`.
- D1–D4 folgt dem bestaetigten DEVELOPMENT-Stand und dem real notwendigen
  Entwicklungsumfang.

Begruende beide Stufen getrennt. Waehle keine hoehere Stufe nur als Reserve.

## 3. Bausteine auswaehlen

Pruefe mindestens:

- MISSION: Projektzweck und Abschluss;
- DEVELOPMENT: Concept oder Architecture, Build Record, Log und Pinwall;
- CONTRACT: nur benoetigte Specs, Permissions, Policies, Schemas,
  Guardrails oder Lifecycles;
- WORKFLOW: Automation und Subject-Specs nur bei ausfuehrbarem Ablauf;
- TOOLING: nur tatsaechlich benoetigte Prompts, Scripts, Skills oder Agents;
- QUALITY: passende Validation, Review, Audit und Evidenz.

Jeder Kandidat erhaelt eines der Urteile `SELECTED`, `REJECTED`, `DEFERRED`
oder `GAP` samt Begruendung.

## 4. HUMAN-Gate

Zeige vor dem Dateibau:

| Punkt | Inhalt |
|---|---|
| A-Stufe | Auswahl und Begruendung |
| D-Stufe | Auswahl und Begruendung |
| SELECTED | Bausteine und Zielpfade |
| REJECTED | verworfene Alternativen |
| GAPS | offene Library-Luecken |
| HUMAN-Gates | nicht delegierte Entscheide |
| naechster Agent | PROJECT-ARCHITEKT |

Erzeuge das wirksame Manifest erst nach HUMAN-Bestaetigung.

## 5. Assembly Manifest

Erzeuge ein gegen `ASSEMBLY_MANIFEST.schema.json` gueltiges Manifest. Es muss
mindestens diese drei HUB_DEVELOPMENT-Quellen enthalten:

- `AGENT_PROJECT_ARCHITEKT_TEMPLATE.MD` -> `AGENT_PROJECT_ARCHITEKT.md`;
- `STARTPROMPT_PROJECT_TEMPLATE.MD` -> `STARTPROMPT_PROJECT.md`;
- `PROJECT_HANDOVER_TEMPLATE.MD` -> `HANDOVER.md`.

Alle Platzhalterersetzungen werden im Manifest ausdruecklich deklariert. Das
Manifest darf keine Quelle ausserhalb von `ARCHITECTURE_HUB_LIBRARY` oder
`ARCHITECTURE_HUB_DEVELOPMENT` adressieren.

## 6. Package bauen

Fuehre den Builder mit bestaetigtem Profil und Manifest aus:

```text
python ARCHITECTURE_HUB_DEVELOPMENT/PROJECT_START_PACKAGE_BUILDER.py
  --profile <PROJECT_PROFILE.json>
  --manifest <ASSEMBLY_MANIFEST.json>
  --library-root <ARCHITECTURE_HUB_LIBRARY>
  --hub-development-root <ARCHITECTURE_HUB_DEVELOPMENT>
  --output <PROJECT_START_PACKAGE>
```

Kein `--overwrite` beim ersten Build. Ein bestehendes Package wird nicht
stillschweigend ersetzt.

## 7. Interner Preflight

Fuehre den deterministischen Validator aus. Das ist noch keine unabhaengige
Endvalidation, sondern verhindert eine offensichtlich defekte Uebergabe.

Bei `FAIL` oder `HOLD` kein Handover anbieten.

## 8. Handover

Wenn Profil, Manifest, Build und Preflight tragfaehig sind:

```text
READY_FOR_HANDOVER
-> HANDOVER_OFFERED
```

Nenne dem HUMAN den absoluten Package-Pfad und verweise auf den externen
Validator-Startprompt. Der PROJECT-ARCHITEKT darf erst nach dessen Pruefung
das Takeover akzeptieren.
