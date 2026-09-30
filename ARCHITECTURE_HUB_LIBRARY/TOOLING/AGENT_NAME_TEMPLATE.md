---
document_id: ah-tooling-template-agent-name
title: AGENT_<NAME>.md — Vertrag eines eigenständigen Akteurs
status: TEMPLATE
version: 1.0.0
created_at: 2026-09-30
functional_area: TOOLING
canonical_file_family: "AGENT_<NAME>.md"
target_filename: "AGENT_<AUSSAGEKRÄFTIGER_NAME>.md"
authority: HUMAN_CONFIRMED_FILE_TYPE
agent_class: "<AGENT|MASTER_AGENT|SUBAGENT>"
aliases:
  SUBAGENT:
    - HELFER
tags:
  - agent
  - master-agent
  - subagent
  - helfer
  - responsibility
  - owner
provenance:
  local_authority: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling
  decision_context: TOOLING-Dateitypen prüfen, HUMAN-confirmed on 2026-09-30
  source_check: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#provenienz-und-source-check-für-tooling
---

# AGENT: [AUSSAGEKRÄFTIGER NAME]

<!--
MASTER_AGENT und SUBAGENT sind Klassen beziehungsweise Tags, keine eigenen
Dateitypen. Jeder Akteur erhält einen fachlich aussagekräftigen Namen.
ROLE_<NAME>.md wird nicht erzeugt. PERSONA bleibt ein reservierter Begriff.
-->

## MISSION

[PLATZHALTER: Welchen eigenständigen Auftrag erfüllt dieser Agent?]

## ACTIVATION

[PLATZHALTER: Trigger, Vorbedingungen und Ausschlüsse]

## AUTHORITY

[PLATZHALTER: Entscheidungsquellen, Vorrang und Grenzen]

## INPUTS

| Input | Quelle | Pflicht | Validierung |
|---|---|---|---|
| `[NAME]` | [PLATZHALTER] | JA/NEIN | [PLATZHALTER] |

## RESPONSIBILITY_AND_OWNER

[PLATZHALTER: Wofür steht der Agent ein, welche Outputs besitzt er während
ihres Lebenszyklus, und wann endet seine Verantwortung?]

## TOOLS_AND_PERMISSIONS

| Tool oder Fähigkeit | Zweck | Authority | HUMAN-Gate |
|---|---|---|---|
| [PLATZHALTER] | [PLATZHALTER] | [PLATZHALTER] | JA/NEIN |

## STATE_AND_CONTEXT

[PLATZHALTER: Welche Zustände, Sessions, Checkpoints oder Referenzen werden
benötigt? Keine Chatgeschichte als einzige dauerhafte Authority verwenden.]

## WORKFLOW

1. [PLATZHALTER: Inspect]
2. [PLATZHALTER: Plan]
3. [PLATZHALTER: Execute]
4. [PLATZHALTER: Validate]
5. [PLATZHALTER: Handoff]

## SUPERVISION_AND_DELEGATION

[PLATZHALTER: Beaufsichtigt dieser Agent andere Agenten? Als MASTER_AGENT
Roster, Übergabevertrag und Abbruchrecht nennen. Als SUBAGENT/HELFER den
beaufsichtigenden Agenten und die autonome Arbeitsgrenze nennen.]

## OUTPUT_CONTRACT

[PLATZHALTER: zugesicherte Outputs, Format, Zielpfad und Abschlusszustand]

## FAILURE_AND_ESCALATION

[PLATZHALTER: Fehlerzustände, Retry-Grenze, HOLD und Eskalationsziel]

## BOUNDARIES

- [PLATZHALTER: ausdrücklich nicht erlaubte Verantwortung]
- [PLATZHALTER: benachbarter Agent oder Funktionsbereich]

## VALIDATION

[PLATZHALTER: reproduzierbare Evidenz für Verhalten und Output]

## HANDOFF

[PLATZHALTER: Empfänger, übergebener Zustand, Evidenz und offene Risiken]

## PROVENANCE

- Lokale Authority:
  `ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling`
- HUMAN-Entscheid: „TOOLING-Dateitypen prüfen“, 30. September 2026
- Source-Check: gezielt, nicht vollständig; Grenzen stehen in der lokalen
  Authority.
