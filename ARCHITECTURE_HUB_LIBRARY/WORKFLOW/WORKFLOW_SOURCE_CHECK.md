---
document_id: ah-workflow-source-check
title: WORKFLOW — Source-Check, Provenienz und Grenzen
status: ACTIVE
version: 1.0.0
created_at: 2026-09-30
updated_at: 2026-09-30
authority: HUMAN_CONFIRMED_SOURCE_CHECK
functional_area: WORKFLOW
canonical: true
---

# WORKFLOW — Source-Check

## Ergebnisstand

Der Source-Check ist für den gegenwärtig bestätigten WORKFLOW-Stand
abgeschlossen. Kanonisch in der Library sind:

- `AUTOMATION.md` als wiederverwendbare Vorlage;
- `[SUBJECT]_SPEC.md`, `[SUBJECT]_SPEC.json` und `[SUBJECT]_SPEC.yaml` als
  eine Dateifamilie mit gemeinsamer Authority-Regel.

Der Entwicklungs-Draft bleibt unverändert als Genealogie erhalten und ist
nicht selbst die kanonische Library-Datei.

## Provenienzkette

```text
FIELD_NOTES-Quellen
  -> Source-Analyse und HUMAN-Entscheide im Chat „WORKFLOW-Dateitypen prüfen“
  -> ARCHITECTURE_HUB_DEVELOPMENT/WORKFLOW_FUNCTIONAL_AREA_DRAFT.MD
  -> HUMAN-Auftrag zur Überführung
  -> ARCHITECTURE_HUB_LIBRARY/WORKFLOW/
```

## Geprüfte lokale Quellen

- `FIELD_NOTES_DRAFT/0_MISSION_CONTROL/PACKAGES/PACKAGE_CORE.md`, §3:
  `ENTRY -> ACTION -> EXIT` sowie `TRIGGER`, `ACTOR`, `WERKZEUG`,
  `HUMAN-STOPP` und `SPEICHERORT`.
- `FIELD_NOTES_DRAFT/0_W_WORKFLOW/P5_WEB_PREVIEW/W_P5_GATE_BUILD.md`:
  ausführbare Gate-Spec mit ENTRY-, EXIT- und Handover-Verhalten.
- `FIELD_NOTES_DRAFT/0_W_WORKFLOW/_archive/`
  `GATES_MATRIX_260530_PRE_HOG_RENAME_260614.md`:
  phasen- und dimensionsübergreifende Gate-Sicht.
- `FIELD_NOTES_DRAFT/0_W_WORKFLOW/W_WRITING_ROOM/`
  `_agents_WRITING_ROOM/W_WRITING_ROOM_LAYOUTER_GATE_260612.yaml`:
  strukturierte Gate-Felder wie `source`, `tool`, `pass_condition`,
  `fail_action` und `severity`.
- `ARCHITECTURE_HUB_DEVELOPMENT/WORKFLOW_FUNCTIONAL_AREA_DRAFT.MD`:
  provisorische Normalisierung der Quellen und bestätigten HUMAN-Entscheide.

## Bestätigte HUMAN-Entscheide

1. `AUTOMATION.md` bleibt allgemeiner WORKFLOW-Dateityp.
2. `[SUBJECT]_SPEC.{md|json|yaml}` ist eine Dateifamilie.
3. Passes verwenden nur belegte Bestandteile des Minimalvertrags.
4. Gates werden als Einzel-Spec und als Quersicht geführt.
5. `OUTPUT` signalisiert das Ende eines Turns oder einer Operation.
6. `CHECKPOINT` und `MILESTONE` sind Synonyme.
7. Wiederaufnahme erfolgt vom letzten bestätigten Output, nicht durch
   Neustart des gesamten Workflows.
8. Idempotenz und vertragsgebundenes Self-Healing sind Grundprinzipien.
9. `OUT_OF_SCOPE`, `DEFERRED` und `KNOWN_LIMIT` bleiben unterscheidbar.

## Authority-Regel der SPEC-Dateifamilie

Eine einzelne Repräsentation trägt `SINGLE`. Bei mehreren Repräsentationen
gibt es genau eine `PRIMARY`; jede `DERIVED`-Repräsentation verweist auf
diese Quelle. Bei Drift oder Widerspruch gilt `PRIMARY_REPRESENTATION_WINS`.
Mehrere gleichrangige Wahrheiten sind unzulässig.

## Nicht aufgenommen

Es werden keine allgemeinen Vorlagen für `WORKFLOW.md`, `RUNBOOK.md`,
`PLAYBOOK.md`, `ROUTING.md` oder `DIALOGFLOW.md` geführt. Projektspezifische
Dateien mit solchen Namen bleiben möglich, begründen aber keinen allgemeinen
Library-Dateityp.

Ebenfalls nicht in WORKFLOW normalisiert werden:

- Dateityp- und Werkzeugwahl: `DEVELOPMENT`;
- Package- und Rollenverträge: `CONTRACT`;
- Nachweise, `FILESYS`, Systemüberwachung und INSPECTOR: `QUALITY`;
- Concurrency und Locking: `DEFERRED` für Multi-Agent-/Multi-LLM-Systeme;
- die verworfene Regel «Status nicht überladen».

## Grenzen des Source-Checks

- Die Quellen belegen verwendete und bewährte Muster, nicht deren universelle
  Pflicht für jeden Workflow.
- Die archivierte Gate-Matrix belegt das Zwei-Sichten-Modell; ihre damaligen
  Fachkriterien werden nicht als aktuelle universelle Kriterien übernommen.
- Leere oder nicht belegte Template-Felder dürfen bei einer Instanz entfernt
  werden. Es werden keine Inhalte erfunden, nur um die Vorlage zu füllen.
- Neue Projekt-Lessons gelangen erst nach Prüfung und positivem Entscheid in
  diese Library.
