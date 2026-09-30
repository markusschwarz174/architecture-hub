---
document_id: ah-workflow-functional-area-draft
title: Provisorischer Freeze — Funktionsbereich WORKFLOW
status: DRAFT
version: 0.2.0-draft
created_at: 2026-09-30T21:43:00+02:00
updated_at: 2026-09-30T21:43:00+02:00
authority: HUMAN_APPROVAL_REQUIRED
canonical: false
---

# Provisorischer Freeze — WORKFLOW

Dieser Stand hält bestätigte Begriffe und Dateifamilien fest. Er ist kein
endgültiger Standard und noch nicht für einen Commit freigegeben.

## Bestätigte Dateifamilien

- `AUTOMATION.md` bleibt bestätigt.
- `[SUBJECT]_SPEC.MD`, `[SUBJECT]_SPEC.JSON` und `[SUBJECT]_SPEC.YAML` bilden
  eine Dateifamilie. Das Format folgt Empfänger und Ausführung; bei mehreren
  Darstellungen müssen Authority und Ableitung klar sein.
- `WORKFLOW.md`, `RUNBOOK.md`, `PLAYBOOK.md`, `ROUTING.md` und
  `DIALOGFLOW.md` werden keine allgemeinen Dateitypen.

## Schlankes Begriffsskelett

Ein Workflow beschreibt nur, was für eine sichere Ausführung und
Wiederaufnahme tatsächlich vorhanden ist:

1. `ENTRY`
2. `FLOW` mit seinen vorhandenen Passes
3. `GATES` sowie synonyme `CHECKPOINTS` / `MILESTONES`
4. Unterbruch, Wiederaufnahme, Idempotenz und Self-Healing
5. bestätigter `OUTPUT` als Ende des Turns oder der Operation
6. verknüpfte `[SUBJECT]_SPEC.*`, sofern fachliche Detailverträge nötig sind

Das ist ein Begriffsskelett, keine Pflicht zu sechs Kapiteln oder zu leeren
Feldern.

## Minimalvertrag eines Passes

Es werden nur Felder verlangt, die in der übernommenen FIELD_NOTES-Quelle
tatsächlich vorhanden und für den konkreten Pass relevant sind:

- `TRIGGER`
- `ENTRY`
- `ACTION`
- `EXIT`
- `ACTOR`
- `WERKZEUG`
- `HUMAN-STOPP`
- `SPEICHERORT`

Nicht vorhandene Informationen werden nicht ergänzt. `EXIT` bezeichnet den
erzeugten Output, sein Übergabeziel und den nächsten zulässigen Übergang.

## Gates in zwei Sichten

1. Eine Gate-Spec beschreibt ein einzelnes Gate mit den in der Quelle
   tatsächlich vorhandenen Angaben wie ID, Name, Check, Quelle, Werkzeug,
   Pass-Bedingung, Fail-Aktion und Schweregrad.
2. Eine Gate-Übersicht zeigt die Gates quer über Phasen, Dimensionen und
   Verantwortungen.

Die Einzelsicht macht ein Gate ausführbar. Die Quersicht macht Lücken,
Doppelungen und Abdeckung sichtbar.

## Output, Wiederaufnahme und Self-Healing

Ein Output ist vor allem ein bestätigtes Endsignal. Er schliesst den Turn
oder die Operation ab und bildet damit einen sicheren Wiederaufnahmepunkt.
`CHECKPOINT` und `MILESTONE` sind dafür Synonyme; eine zusätzliche
Begriffsunterscheidung wird nicht eingeführt.

Wird eine Operation zwischen `ENTRY` und bestätigtem `OUTPUT` unterbrochen,
fällt sie auf den letzten gültigen Output zurück. Sie startet nicht den
gesamten Workflow neu. Self-Healing bleibt vertragsgebunden: vorhandene
gültige Teile bewahren, Fehlendes ergänzen, bekannte Defekte reparieren und
bei unbekannten Zuständen stoppen oder eskalieren. Wiederholte Ausführung
darf keinen unnötigen zweiten Effekt erzeugen.

## Limits

- `OUT_OF_SCOPE`: gehört nicht zur Verantwortung dieses Funktionsbereichs
  oder Artefakts.
- `DEFERRED`: wäre relevant, wird aber bewusst später behandelt.
- `KNOWN_LIMIT`: gehört zum Scope, ist derzeit jedoch nur begrenzt gelöst.

Locking und Concurrency werden als `DEFERRED` für Multi-Agent- oder
Multi-LLM-Systeme festgehalten. Die frühere Idee «Status nicht überladen» wird
nicht übernommen; `MAIL_Organizer` dient dafür nicht als positives Muster.

## Zuständige Empfänger ausserhalb von WORKFLOW

| Thema | Empfänger | Ablage in diesem Stand |
|---|---|---|
| Wahl von Dateityp und Werkzeug; Script oder AI-Pass | `DEVELOPMENT` | `AH_AGENT_DEVELOPER.MD`, Abschnitt «Artefakt- und Ausführungswahl» |
| Nachweise, `FILESYS`, Systemüberwachung und präventiver INSPECTOR | `QUALITY` | `INSPECTION_CONCEPT.md`, Abschnitt «Präventive INSPECTOR-Prüfung» |
| Zentraler Paketvertrag und spezialisierte Rollen | `CONTRACT` | Warteschlange; noch kein CONTRACT-Artefakt angelegt |

Die CONTRACT-Zeile ist absichtlich nur eine adressierte Warteschlange. Ein
neuer kanonischer CONTRACT-Bereich wird nicht vor dem entsprechenden
Funktionsentscheid erfunden.

## LOCAL als lernende Auswahl

Der Funktionsbereich WORKFLOW in `LOCAL` soll eine orchestrierte
All-Star-Auswahl bewährter Dateien bereitstellen. Universelle und fachlich
spezifische Bausteine bleiben unterscheidbar. Lessons Learned aus realen
Projekten fliessen über einen Entwicklungs-Briefkasten ein, werden geprüft
und nur bei positivem Entscheid aufgenommen. Bestehende Bausteine werden
regelmässig und ereignisgetrieben überprüft und kuratiert.

## Quellenbindung

Der Pass-Minimalvertrag und das Zwei-Sichten-Gate-Modell stammen aus den
geprüften FIELD_NOTES-Bausteinen:

- `0_MISSION_CONTROL/PACKAGES/PACKAGE_CORE.md`, §3 «Minimaler Pass-Vertrag»;
- `0_W_WORKFLOW/P5_WEB_PREVIEW/W_P5_GATE_BUILD.md` als Gate-Spec;
- `0_W_WORKFLOW/_archive/GATES_MATRIX_260530_PRE_HOG_RENAME_260614.md` als
  phasen- und dimensionsübergreifende Gate-Matrix;
- `0_W_WORKFLOW/W_WRITING_ROOM/_agents_WRITING_ROOM/`
  `W_WRITING_ROOM_LAYOUTER_GATE_260612.yaml` als strukturierte Gate-Sicht.

Ergänzungen dieses Drafts normalisieren die bestätigten HUMAN-Entscheide; sie
dürfen nicht als rückwirkender Inhalt der Quellen ausgegeben werden.
