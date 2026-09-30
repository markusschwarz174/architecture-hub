---
document_id: ah-workflow-automation-template
title: AUTOMATION — wiederverwendbare Vorlage
status: ACTIVE
version: 1.0.0
created_at: 2026-09-30
updated_at: 2026-09-30
authority: HUMAN_CONFIRMED_LIBRARY_TEMPLATE
functional_area: WORKFLOW
canonical: true
template_target: AUTOMATION.md
source_check: WORKFLOW_SOURCE_CHECK.md
---

# AUTOMATION

## Verwendung der Vorlage

Diese Vorlage beschreibt den kleinsten bestätigten Vertrag einer Automation.
Bei der Instanziierung werden nur tatsächlich vorhandene Passes, Gates,
Limits und Übergänge materialisiert. Fehlende Sachverhalte werden nicht mit
plausiblen Annahmen aufgefüllt.

Die Überschriften sind ein Begriffsskelett, keine Pflicht zu leeren Kapiteln.

## Instanz-Metadaten

```yaml
document_id: "<automation-id>"
title: "<Name der Automation>"
status: "<DRAFT|ACTIVE|DEPRECATED|SUPERSEDED>"
version: "<SemVer>"
authority: "<entscheidende HUMAN- oder System-Authority>"
functional_area: WORKFLOW
```

## Zweck und Abgrenzung

- `PURPOSE`: <Weshalb existiert diese Automation?>
- `ENTRY`: <Welcher bestätigte Startpunkt eröffnet den Ablauf?>
- `END`: <Welches bestätigte Output-Signal beendet den Ablauf?>
- `OUT_OF_SCOPE`: <Was gehört ausdrücklich nicht zu dieser Automation?>

## Flow und Passes

Der verbindliche innere Kern eines Passes lautet:

```text
ENTRY -> ACTION -> EXIT
```

Für jeden real vorhandenen Pass wird der folgende Minimalvertrag verwendet:

| Begriff | Inhalt |
|---|---|
| `TRIGGER` | auslösendes HUMAN-Wort oder ausdrücklich autorisiertes Ereignis |
| `ENTRY` | benötigte Inputs und belegte Vorbedingungen; kein Actor |
| `ACTION` | innerhalb dieses Passes ausgeführte Tätigkeiten |
| `EXIT` | geregelter Abschluss: Output, Rückgabeziel und nächster zulässiger Übergang |
| `ACTOR` | handelndes Subjekt: HUMAN, AI-Rolle oder Script-Actor |
| `WERKZEUG` | Script, UI, Prompt-Vertrag oder andere konkrete Ausführungshilfe |
| `HUMAN-STOPP` | Stelle, an der kein selbständiger Entscheid oder Übergang zulässig ist |
| `SPEICHERORT` | Authority-konforme Heimat des Outputs |

### Pass-Vorlage

Zeilen ohne belegten Inhalt werden in der konkreten Instanz entfernt.

```yaml
pass_id: "<ID>"
trigger: "<vorhandener Auslöser>"
entry: "<Inputs und Vorbedingungen>"
action: "<Tätigkeit>"
exit: "<Output, Rückgabeziel, nächster Übergang>"
actor: "<HUMAN|AI-Rolle|Script-Actor>"
werkzeug: "<konkretes Werkzeug>"
human_stopp: "<belegte Bedingung; sonst Zeile entfernen>"
speicherort: "<belegter Pfad oder System; sonst Zeile entfernen>"
```

## Gates in zwei Sichten

### Sicht 1 — einzelne Gate-Spec

Eine Gate-Spec hält nur belegte Angaben fest. In den geprüften Quellen wurden
folgende Felder tatsächlich verwendet:

```yaml
id: "<Gate-ID>"
name: "<Gate-Name>"
check: "<Prüfung>"
source: "<Prüfquelle>"
tool: "<Prüfwerkzeug>"
pass_condition: "<Bedingung für PASS>"
fail_action: "<Aktion bei FAIL>"
severity: "<belegte Einstufung>"
```

### Sicht 2 — Gate-Übersicht

Die Übersicht zeigt dieselben Gates quer über die tatsächlich relevanten
Phasen, Dimensionen und Verantwortungen. Sie ist eine Sicht auf die
Einzel-Gates und keine zweite Authority.

| Gate | Phase/Übergang | Dimension | Verantwortung | Einzel-Spec |
|---|---|---|---|---|
| `<ID>` | `<Phase>` | `<Dimension>` | `<Actor/Owner>` | `<Referenz>` |

## Output als Endsignal

Ein `OUTPUT` ist nicht primär ein Dateiformat. Er ist das bestätigte Signal,
dass ein Turn, ein Pass oder eine Operation beendet ist. Der Output nennt den
erreichten Zustand, seinen Speicher- oder Rückgabeort und den nächsten
zulässigen Übergang.

Ein bestätigter Output bildet den sicheren Wiederaufnahmepunkt. `CHECKPOINT`
und `MILESTONE` werden dafür synonym verwendet und erzeugen keine getrennten
Konzepte.

## Wiederaufnahme, Idempotenz und Self-Healing

- Bei einem Unterbruch zwischen `ENTRY` und bestätigtem `OUTPUT` wird auf den
  letzten bestätigten Output zurückgefallen. Der Gesamtworkflow startet nicht
  am Anfang neu.
- Ein erneuter Lauf bewahrt bereits gültige Ergebnisse und erzeugt keinen
  unnötigen zweiten Effekt.
- Self-Healing bleibt innerhalb des definierten Vertrags: bekannte Zustände
  erkennen, gültiges Vorhandenes bewahren, Fehlendes ergänzen und bekannte
  Defekte reparieren.
- Ein unbekannter Zustand führt zu Stopp, HUMAN-Entscheid oder geregelter
  Eskalation. Er erlaubt keine freie Änderung des Lösungswegs.

## Limits

| Begriff | Bedeutung |
|---|---|
| `OUT_OF_SCOPE` | gehört nicht zur Verantwortung dieser Automation |
| `DEFERRED` | wäre relevant, wird aber bewusst später behandelt |
| `KNOWN_LIMIT` | gehört zum Scope, ist derzeit jedoch nur begrenzt gelöst |

Concurrency und Locking sind für Multi-Agent- und Multi-LLM-Systeme
`DEFERRED`; sie gehören nicht zur allgemeinen AUTOMATION-Grundvorlage.

## Abgrenzungen

- Wahl von Dateityp und Ausführungsart gehört zu `DEVELOPMENT`.
- Fachliche Verträge, Package- und Rollenverträge gehören zu `CONTRACT`.
- Nachweise, `FILESYS`, Systemüberwachung und INSPECTOR gehören zu `QUALITY`.
- Ein allgemeiner Dateityp `WORKFLOW.md`, `RUNBOOK.md`, `PLAYBOOK.md`,
  `ROUTING.md` oder `DIALOGFLOW.md` wird aus dieser Vorlage nicht abgeleitet.

## Verknüpfte Specs

Fachliche Details können in `[SUBJECT]_SPEC.md`, `[SUBJECT]_SPEC.json` oder
`[SUBJECT]_SPEC.yaml` liegen. Bei mehreren Repräsentationen gilt die in diesen
Vorlagen festgelegte Authority-Regel.

## Provenienz

Siehe `WORKFLOW_SOURCE_CHECK.md`. Der Entwicklungsstand
`ARCHITECTURE_HUB_DEVELOPMENT/WORKFLOW_FUNCTIONAL_AREA_DRAFT.MD` bleibt als
nicht-kanonischer Entwicklungsnachweis erhalten.
