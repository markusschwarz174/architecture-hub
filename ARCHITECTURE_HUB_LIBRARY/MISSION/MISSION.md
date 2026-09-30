---
document_id: ah-library-template-mission
title: MISSION — wiederverwendbare Vorlage
status: TEMPLATE
version: 1.0.0
created_at: 2026-09-30
functional_area: MISSION
canonical_file_type: MISSION.md
authority: HUMAN_APPROVAL_REQUIRED_PER_INSTANCE
aliases:
  - AUFTRAG
  - MISSION_STATEMENT
tags:
  - AI_HUM_COWORK
  - CONTEXT
  - PURPOSE
  - GOAL
  - MISSION_COMPLETE
boundaries:
  - MILESTONES belong to WORKFLOW.
  - SCOPE belongs to CONTRACT.
  - OUT_OF_SCOPE belongs to CONTRACT.
  - SUCCESS_CRITERIA belong to CONTRACT.
provenance:
  local_authority: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md
  decision_context: META_LIBRARY chat, HUMAN-confirmed on 2026-09-30
  concrete_source_not_copied: ARCHITECTURE_HUB_DEVELOPMENT/AH_MISSION.MD
source_check:
  status: TARGETED_NOT_EXHAUSTIVE
  checked_on: 2026-09-30
  searched_local_roots:
    - FIELD_NOTES_DRAFT including relevant archives
    - MY_AI_PROJECTS
    - AI_PROJECTS including OPENAI and ARCHITECTURE_HUB
  methods:
    - mechanical search of Markdown filenames and headings
    - semantic reading of central active MISSION documents
    - terminology comparison with selected primary professional sources
  evidence_summary: >-
    The focused check supported MISSION.md as the single local file type for
    this functional area. PURPOSE and GOAL were recurrent source concepts;
    AI_HUM_COWORK and MISSION_COMPLETE are explicit new local decisions.
  limitations:
    - Not every source file was read semantically from beginning to end.
    - Mechanical hit counts include historical and archived variants.
    - The check does not prove that every reusable source pearl was found.
---

# MISSION

<!--
VERWENDUNG

Diese Vorlage wird für ein konkretes Vorhaben kopiert und ausgefüllt. Die fünf
Kapitel sind das bestätigte Begriffsskelett von MISSION.md. Platzhalter werden
ersetzt; Ausfüllhinweise werden danach entfernt.

Die Mission bleibt grundsätzlich und stabil. Detaillierte Abläufe, Milestones,
Scope-Grenzen und messbare Erfolgskriterien werden nicht hier dupliziert.
-->

## AI_HUM_COWORK

<!--
Beschreibe in wenigen Sätzen das Grundprinzip der Zusammenarbeit. Halte hier
keine detaillierten Rollen, Authorities, Übergaben oder Prozessregeln fest.
-->

[PLATZHALTER: Wie arbeiten HUMAN und AI bei dieser Mission grundsätzlich
zusammen? Wer behält die verbindliche Entscheidungshoheit?]

## CONTEXT

<!--
Beschreibe die Ausgangslage, den Anlass und das grundlegende Problem. Nenne nur
Kontext, der zum Verständnis der Mission nötig ist.
-->

[PLATZHALTER: Welche Ausgangslage führt zu dieser Mission, und weshalb entsteht
sie jetzt?]

## PURPOSE

<!--
Formuliere den Existenzgrund. PURPOSE beantwortet das Warum, nicht den
detaillierten Lösungsweg.
-->

[PLATZHALTER: Weshalb existiert dieses Vorhaben? Welchen grundsätzlichen Nutzen
soll es schaffen?]

## GOAL

<!--
Beschreibe den angestrebten Zielzustand. Keine Milestones, Tasks oder
mikrometergenauen Prüfkriterien aufnehmen.
-->

[PLATZHALTER: Welcher grundsätzliche Zustand soll nach erfolgreichem Durchlauf
erreicht sein?]

## MISSION_COMPLETE

<!--
Schliesse die Mission mit einer grundsätzlichen Abschlussaussage ab. Dieser
Abschnitt folgt am Ende, wenn alles durchlaufen ist. Er ersetzt keine
detaillierten SUCCESS_CRITERIA. Falls ein CONTRACT existiert, darf auf dessen
verbindliche Kriterien verwiesen werden.
-->

[PLATZHALTER: Wann gilt diese Mission grundsätzlich als abgeschlossen, und wer
stellt den Abschluss fest?]
