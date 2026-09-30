---
document_id: ah-naming-local
title: Architecture Hub — Local Naming
status: DRAFT_FOR_HUMAN_REVIEW
version: 0.3.0-draft
created_at: 2026-09-30
updated_at: 2026-09-30T23:53:00+02:00
authority: HUMAN_APPROVAL_REQUIRED
scope: ARCHITECTURE_HUB and connected local workspaces
---

# NAMING_LOCAL — unser technischer Sprachvertrag

## Zweck

`NAMING_LOCAL.md` ist die technische Single Source of Truth für die einheitliche
Verwendung von Namen und Begriffen im lokalen Workspace — sobald die jeweiligen
Einträge durch den HUMAN bestätigt wurden.

Diese Datei beansprucht keine allgemeingültige Wahrheit. Sie beschreibt einen
bewusst gewählten AI-Mikrokosmos, damit HUMAN und AI innerhalb dieses Systems
vom Gleichen sprechen. Die Einteilung darf weiterentwickelt werden; Änderungen
werden versioniert und nicht still umgedeutet.

Unbekannte oder externe Begriffe werden zuerst in `NAMING_LIBRARY.md`
eingeordnet. Erst ein HUMAN-Entscheid macht daraus einen lokalen kanonischen
Begriff.

## Einfache Suchlogik

Jeder Eintrag verwendet nur zwei zusätzliche Felder:

- `ALIAS`: andere Bezeichnungen, unter denen derselbe lokale Begriff gefunden
  werden soll;
- `TAGS`: verwandte Themen und Suchbegriffe, ohne zu behaupten, dass sie
  Synonyme sind.

Es gibt hier keine zusätzliche Ontologie für „enger“, „weiter“, „ähnlich“ oder
„abgeleitet“. Falls eine Abgrenzung wichtig ist, steht sie in einem normalen
Satz.

## Status

Die sechs Funktionsbereiche sind gemeinsam bestätigt. Die darunter genannten
Gefässe und Begriffe sind teilweise erst Kandidaten. Bis zum Abschluss des
Terminologie-Reviews gilt deshalb:

```text
PROPOSED -> HUMAN REVIEW -> CANONICAL
```

# Die sechs lokalen Funktionsbereiche

Die folgende Einteilung ist bewusst **subjektiv und zweckgebunden**. Sie ist
keine Taxonomie der AI-Community und kein Naturgesetz. Ihr Wert liegt darin,
dass sie den lokalen Architekturraum einfach und vollständig genug gliedert.

| Bereich | Leitfrage | Funktion |
|---|---|---|
| `MISSION` | Was und warum wollen wir erreichen? | Auftrag, Zweck, Ziel, Scope und Erfolg festhalten |
| `DEVELOPMENT` | Wie entwerfen, bauen und verändern wir das System? | Architektur, Planung, Implementierung und Entwicklungssteuerung führen |
| `WORKFLOW` | Wie arbeitet das gebaute System? | Ablauf, Zustände, Übergänge, Automationen und Ausführung ordnen |
| `CONTRACT` | Was gilt — und was gilt nicht? | Anforderungen, Grenzen, Regeln, Verantwortungen und Datenverträge definieren |
| `TOOLING` | Womit und durch wen wird gearbeitet? | Prompts, Scripts, Tools, Rollen, Agenten, Hooks und Module bereitstellen |
| `QUALITY` | Wie schützen, prüfen und verbessern wir das Ganze? | Validation, Review, Evals, Security, Datenschutz, Performance, Versionierung und Lernen verankern |

## 1. MISSION

**Funktion:** Definiert die stabile Ausrichtung eines Vorhabens: seine
Ausgangslage, seinen Existenzgrund, seinen Zielzustand und den grundsätzlichen
Abschluss der Mission. Sie beschreibt weder den detaillierten Bauweg noch den
vollständigen Vertrag.

**Kanonischer Dateityp:** `MISSION.md`

- `ALIAS`: Auftrag, Mission Statement
- `TAGS`: AI_HUM_COWORK, CONTEXT, PURPOSE, GOAL, MISSION_COMPLETE

Die `TAGS` sind für diesen Dateityp zugleich die vereinbarten
Kapitelüberschriften:

| Kapitel | Inhalt |
|---|---|
| `AI_HUM_COWORK` | Grundprinzip der Zusammenarbeit von HUMAN und AI; keine detaillierten Rollen-, Authority- oder Prozessregeln |
| `CONTEXT` | Ausgangslage, Anlass und das zu lösende Grundproblem |
| `PURPOSE` | Weshalb das Vorhaben existiert |
| `GOAL` | Welcher grundsätzliche Zielzustand erreicht werden soll |
| `MISSION_COMPLETE` | Grundsätzlicher Abschluss der Mission nach Durchlauf des Systems; keine mikrometergenaue Prüfspezifikation |

**Abgrenzung:** `MILESTONES` gehören zu `WORKFLOW`. `SCOPE`, `OUT_OF_SCOPE`
und `SUCCESS_CRITERIA` gehören zu `CONTRACT`. Die Mission darf darauf
verweisen, dupliziert sie aber nicht.

## 2. DEVELOPMENT

**Funktion:** Steuert, wie etwas entworfen, gebaut, geändert und ausgeliefert
wird. DEVELOPMENT endet nicht beim Coding; Entscheidungen, Planung,
Implementierung, Migration und Entwicklungsstatus gehören ebenfalls dazu.

- `ALIAS`: Entwicklung
- `TAGS`: concept, architecture, planning, bauplan, construction,
  implementation, build_record, development_log, pinwall, discovery,
  inventory, communication, learning, versioning

**Bestätigte Dateitypen:**

| Dateityp | Instanzmuster | Alias / Suchbegriffe | Abgrenzung |
|---|---|---|---|
| `CONCEPT` | `[PROJECT]_CONCEPT.md` | Konzept, Systemkonzept | fachliche geltende Beschreibung; kein BAUPLAN und keine SPEC |
| `ARCHITECTURE` | `[PROJECT]_ARCHITECTURE.md` | Architektur, Systemarchitektur | technische Struktur; kein BUILD_RECORD |
| `BUILD_RECORD` | `[PROJECT]_BUILD_RECORD.md` | Baudokumentation, Baubericht, Baufortschritt, Wiederaufnahme | dokumentiert den tatsächlichen Bau; plant ihn nicht |
| `DEVELOPMENT_LOG` | `DEVELOPMENT_LOG.json` | Entwicklungslog, Entscheidungs- und Lernverlauf | strukturierte Chronik; ersetzt die frühere Benennung `DECISIONS_LOG` in DEVELOPMENT |
| `PINWALL` | `PINWALL.md` | Pinwand; Board nur als Suchalias | unreflektierter HUMAN-Eingang; keine Entscheidung und kein Backlog |
| `BAUPLAN` | `[CHANGE]_BAUPLAN.md` | Umsetzungsplan, Implementierungsplan | PLANNER-Anleitung an IMPLEMENTOR; kein Fortschrittsbericht |
| `DISCOVERY` | `[CHANGE]_DISCOVERY.md` | Bestandsanalyse, Ermittlungsakte | lesbarer EXPLORER-Output |
| `DISCOVERY_INVENTORY` | `[CHANGE]_DISCOVERY_INVENTORY.json` | Discovery-Inventar, Bestandsinventar | maschinenlesbarer Output derselben Discovery; nie ohne gemeinsame `discovery_id` |
| `COMMUNICATION_CONCEPT` | `[PROJECT]_COMMUNICATION_CONCEPT.md` | Kommunikationskonzept | Kommunikationsarchitektur; keine operative HO/TO-Datei |

`CONCEPT` und `ARCHITECTURE` sind in den einfachen Stufen eine
Entweder-oder-Wahl. Beide werden nur mit begründetem Trennungsnutzen geführt.

**Mitbenutzter CONTRACT-Dateityp:** Die Familie `SPEC` mit dem Muster
`[SUBJECT]_SPEC.md|yaml|json` wird ab DEVELOPMENT-Stufe D2 ausgewählt und
verwendet, bleibt aber kanonisch in `CONTRACT`. `SPECIFICATION` ist ihr Alias.
Es wird keine zweite DEVELOPMENT-SSOT dafür angelegt.

**Bestätigte Muster ohne eigenen DEVELOPMENT-Dateityp:** `POSTBOX` ab D3,
webbasierte `DECISION_PAGE` ab D4 und der Ablauf
`PRODUCE → INDEPENDENT_REVIEW → GATE → TARGETED_REPAIR → FINALIZE` ab D4.
HO/TO-Cards und HANDOFF-Dateien gehören nach WORKFLOW/TOOLING. Ein
eigenständiger `DEVELOPER`-Agent und `[PROJECT]_ACTORS.md` sind nicht aktiv.

**Library-Ort:** Begriffsskelette, Vorlagen, EXPLORER-Vertrag, Daten-Schema und
Provenienz liegen unter `ARCHITECTURE_HUB_LIBRARY/DEVELOPMENT/`. Konkrete
Projektinstanzen werden daraus kopiert und im Projekt geführt.

**Abgrenzung:** DEVELOPMENT beschreibt, wie wir das System bauen und ändern.
WORKFLOW beschreibt, wie das gebaute System arbeitet. QUALITY validiert;
CONTRACT hält verbindliche Anforderungen und Schemas. Der ARCHITEKT ist die
Verbindung zum HUMAN und zu anderen Bereichen, wählt Agenten aus und führt
eine kleine Erstkontrolle durch; er ersetzt keine QUALITY-Validierung.

## 3. WORKFLOW

**Funktion:** Beschreibt ausführbare oder nachvollziehbare Abläufe mit Schritten,
Zuständen, Übergängen, Inputs, Outputs und Fehlerwegen.

- `ALIAS`: Ablauf, Prozess
- `TAGS`: workflow, pipeline, automation, pass, gate, entry, exit, output,
  checkpoint, milestone, resume, recovery, idempotency, self-healing, loop,
  graph, orchestration, state, transition

**Lokale Verwendung:** `WORKFLOW` ist der technische Begriff in Tools.
`Pipeline` darf in Chats als anschauliches Ablaufwort verwendet werden, erzeugt
aber kein zweites Architekturkonzept.

**Bestätigte Dateitypen und Vorlagen:**

- `AUTOMATION.md` — allgemeiner Vertrag eines ausgeführten Ablaufs;
- `[SUBJECT]_SPEC.md`, `[SUBJECT]_SPEC.json` und `[SUBJECT]_SPEC.yaml` — eine
  Dateifamilie für einen konkret benannten Gegenstand. Bei mehreren
  Repräsentationen gibt es genau eine `PRIMARY`; alle anderen sind `DERIVED`.

`SPECIFICATION` bleibt Alias von `SPEC`. `CHECKPOINT` und `MILESTONE` werden
lokal synonym verwendet; beide bezeichnen einen durch bestätigten `OUTPUT`
gesicherten Wiederaufnahmepunkt und sind keine eigenen Dateitypen.

**Nicht als allgemeine Dateitypen zugeordnet:** `WORKFLOW.md`, `RUNBOOK.md`,
`PLAYBOOK.md`, `ROUTING.md` und `DIALOGFLOW.md`. Solche Namen dürfen in einem
Fachprojekt begründet vorkommen, erzeugen aber weder einen universellen Typ
noch eine Library-Vorlage.

## 4. CONTRACT

**Funktion:** Legt überprüfbar fest, was ein System, Baustein oder Beteiligter
leisten muss, darf und nicht darf. Hier liegen Anforderungen, Grenzen,
Authorities, Regeln, Policies, Schemas und Schnittstellenvereinbarungen.

- `ALIAS`: Vertrag
- `TAGS`: spec, requirement, convention, constitution, authority, policy,
  permission, lifecycle, constraint, schema, interface, guardrail

**Bestätigte Dateitypen:** `SPEC`, `PERMISSION`, `LIFECYCLE`, `SCHEMA`,
`GUARDRAIL` und `POLICY`. `CONVENTION` bleibt als nicht aktive Reserve
erhalten. Die Begriffsskelette und Quellenbindungen liegen unter
`ARCHITECTURE_HUB_LIBRARY/CONTRACT/`.

**Abgrenzung:** `SPECIFICATION` ist ein Alias von `SPEC`. Eine SPEC kann je
nach realem Leser als Markdown, YAML oder JSON vorliegen. `CONTRACT` ist der
Funktionsbereich und kein zusätzlicher Dateityp. `AUTHORITY` ist Pflichtinhalt
normativer Verträge, aber kein eigener Dateityp. `OPENAPI` ist ein Spezialfall
für API- und Interface-Verträge. `RESPONSIBILITY` und `OWNER` gehören zu
`TOOLING`; Validation gehört zu `QUALITY`.

## 5. TOOLING

**Funktion:** Enthält die Mittel und ausführenden Einheiten, mit denen Mission,
Development, Workflow und Contract praktisch umgesetzt werden.

- `ALIAS`: Tools, Werkzeugkasten
- `TAGS`: prompt, script, source-code, agent, master-agent, subagent, helfer,
  persona, role, hook, module, harness, skill, command, responsibility, owner,
  mcp, plugin, connector, extension, a2a, sandbox, executor, agent-framework,
  tool-search, model-router

**Bestätigte Dateitypen und Dateifamilien:**

| Dateityp oder Familie | Lokale Funktion | Verbindlicher Zielname | Wiederverwendbares Skelett |
|---|---|---|---|
| `PROMPT*.md` | eigenständige, versionierte Modellinstruktion | etablierter, aussagekräftiger Promptname mit `.md`; die Familiennotation ist kein strikter Dateisystem-Glob | `TOOLING/PROMPT_TEMPLATE.md` |
| `SCRIPT` | ausführbare oder implementierende Python-Logik | aussagekräftiger Name mit `.py` | `TOOLING/SCRIPT_TEMPLATE.py` |
| `AGENTS.md` | geltende Projektinstruktionen für OpenAI/Codex-Agenten | exakt `AGENTS.md` | `TOOLING/AGENTS_TEMPLATE.md` |
| `CLAUDE.md` | geltende Projektinstruktionen für Anthropic/Claude | exakt `CLAUDE.md` | `TOOLING/CLAUDE_TEMPLATE.md` |
| `SKILL.md` | Einstieg eines wiederverwendbaren Skill-Pakets | exakt `SKILL.md` im Root des Skill-Pakets | `TOOLING/SKILL_TEMPLATE.md` |
| `AGENT_<NAME>.md` | Vertrag eines eigenständigen, aussagekräftig benannten Akteurs | `AGENT_` plus fachlicher Name und `.md` | `TOOLING/AGENT_NAME_TEMPLATE.md` |

Die Template-Dateien für `AGENTS.md`, `CLAUDE.md` und `SKILL.md` tragen
absichtlich nicht selbst den aktiven Zielnamen. Dadurch werden sie in der
Library nicht versehentlich als geltende Host-Instruktion oder installierter
Skill erkannt. Erst eine bewusst angelegte Kopie erhält den exakten Zielnamen.

**Lokale Unterscheidung:**

- `TOOL` ist der breite Oberbegriff. Ein Prompt, Python-Script, Agent, Skill,
  Connector oder eine Automation kann lokal als Tool bezeichnet werden.
- `SCRIPT` bezeichnet lokal ein Python-Script. Andere implementierende Dateien
  sind `SOURCE CODE`, aber nicht automatisch ein weiterer lokaler Dateityp.
- `AGENT` ist eine selbstständig ausführende Einheit mit Auftrag, Zustand und
  gegebenenfalls Tools.
- `MASTER_AGENT` ist eine Agentenklasse beziehungsweise ein `TAG` für einen
  Agenten, der mehrere Agenten beaufsichtigt. Es entsteht kein zusätzlicher
  Dateityp.
- `SUBAGENT` ist eine Agentenklasse beziehungsweise ein `TAG` für einen
  selbstständig arbeitenden Agenten unter Aufsicht eines Agenten.
  `HELFER` ist der bestätigte lokale `ALIAS`.
- `PERSONA` bleibt als Begriff reserviert. Sie prägt Stimme, Perspektive oder
  Verhaltensstil, erzeugt gegenwärtig aber keinen eigenen Dateityp.
- `ROLE` beschreibt eine Funktion innerhalb eines Prompts oder Workflows.
  Der Kandidat `ROLE_<NAME>.md` wurde ausdrücklich verworfen.
- `RESPONSIBILITY` beschreibt, wofür eine ausführende Einheit während und nach
  ihrer Arbeit einstehen muss.
- `OWNER` benennt die für ein Tool und seine Pflichten zuständige Instanz. Bei
  erzeugten Dateien umfasst dies auch die im referenzierten `LIFECYCLE`
  festgelegte Verschiebung, Archivierung oder Bereinigung.

Die Begriffe bleiben auffindbar, sind aber keine Synonyme.

**Lokale Promptfunktionen:** `STARTPROMPT`, `MASTERPROMPT`, `BRÜCKENPROMPT`
und `ÜBERGABEPROMPT` bleiben zulässige Funktionsnamen innerhalb der Familie
`PROMPT*.md`. Sie bilden keine zusätzlichen allgemeinen Dateitypen.

**Auslagerungsregel für Skills:** Mehr als 300 Zeilen sind ein Prüftrigger,
aber keine Definition eines Skills. Ein Skill wird früher als eigenes Paket
mit `SKILL.md` gespeichert, wenn er wiederverwendet wird, eigene Scripts oder
Referenzen besitzt, unabhängig versioniert werden muss oder von mehreren
Agenten geladen werden soll. Kleine, nur für einen Agenten relevante
Anweisungen dürfen in `AGENT_<NAME>.md` integriert bleiben.

**Technologiebegriffe ohne neuen Dateityp:** `MCP`, `PLUGIN`, `CONNECTOR`,
`EXTENSION`, `A2A`, `SANDBOX`, `EXECUTOR`, `AGENT FRAMEWORK`, `TOOL SEARCH`,
`PROGRAMMATIC TOOL CALLING`, `MODEL ROUTER`, `WEBMCP`, `AGENT UI` und
`AGENT IDENTITY` sind Auswahl- oder Entwicklungswissen. Sie werden nur bei
einem realen Trigger eingesetzt und erzeugen ohne neuen HUMAN-Entscheid keinen
allgemeinen lokalen Dateityp. `LOCAL INFERENCE SERVER` ist durch den vom HUMAN
benannten Bestand `HERMES AGENTS` abgedeckt. Reifeprüfung und Auswahlregeln
stehen im DEVELOPER-Vertrag.

### Provenienz und Source-Check für TOOLING

- `ENTSCHEIDUNG`: HUMAN-bestätigte Diskussion „TOOLING-Dateitypen prüfen“ am
  30. September 2026.
- `LOKALE BASIS`: `AH_MISSION.MD`, `NAMING_LIBRARY.md`, dieser lokale
  Sprachvertrag, `AH_AGENT_ARCHITEKT.MD`, `AH_AGENT_DEVELOPER.MD` und der
  Startprompt für Funktionsbereiche.
- `MECHANISCHER CHECK`: Markdown, Python, PowerShell, JSON, JSONL, YAML und YML
  wurden mit einem breiten TOOLING-Suchmuster geprüft. In
  `FIELD_NOTES_DRAFT` waren 21'375 Dateien im Format-Scope und 13'322
  Trefferdateien; in `AI_PROJECTS` 374 und 203; im lokalen Codex-Bestand 1'236
  und 1'109. Die hohen Trefferzahlen sind wegen allgemeiner Begriffe wie
  Prompt, Agent und Script bewusst nur Suchindikatoren, keine Qualitätszählung.
- `SEMANTISCHE STICHPROBE`: zentrale `AGENTS.md`- und `CLAUDE.md`-Instruktionen,
  aktive Agentenverträge, ein produktiver MASTERPROMPT, ein Python-Prompt-
  Builder, eine installierte `SKILL.md` sowie die zentralen Architecture-Hub-
  Verträge wurden gezielt gelesen beziehungsweise in ihren relevanten
  Abschnitten geprüft.
- `EXTERNE PRIMÄRQUELLEN`: aktuelle Dokumentation von OpenAI, Anthropic,
  QwenLM, MCP, A2A, OpenTelemetry, OWASP, WebMCP und aktuellen Model-Routern;
  die Quellenliste ist im DEVELOPER-Vertrag dauerhaft gebunden.
- `FEHLENDE QUELLE`: Ein eigener Root `MY_AI_PROJECTS` wurde am erwarteten Ort
  nicht gefunden. `HERMES AGENTS` wurde als HUMAN-Angabe übernommen, aber im
  durchsuchten `AI_PROJECTS`-Root nicht lokalisiert.
- `GRENZEN`: Der Check war mechanisch breit und semantisch gezielt, nicht
  semantisch vollständig. Archive und generierte Bestände erzeugen Dubletten;
  Binärformate wurden nicht vollständig ausgewertet. Der Check beweist nicht,
  dass jede wiederverwendbare Perle gefunden wurde.

## 6. QUALITY

**Funktion:** Schützt das System, prüft seine Ergebnisse und macht es durch
Evidenz, Fehlerbehandlung und Lessons Learned besser.

- `ALIAS`: Qualität
- `TAGS`: validation, verification, review, eval, audit, test, security,
  privacy, performance, reliability, observability, versioning,
  lessons-learned

**Lokale Entscheidung:** `VALIDATION` und `VERIFICATION` werden synonym
verwendet. `VALIDATION` ist der bevorzugte Oberbegriff. Die in Fachdomänen
übliche V&V-Trennung bleibt in `NAMING_LIBRARY.md` dokumentiert, wird lokal aber
nicht erzwungen.

Lokale Prüfbezeichnungen:

- `VALIDATION`: Oberbegriff für eine geplante Prüfung;
- `REVIEW`: Prüfung eines konkreten Artefakts oder Ergebnisses;
- `EVAL`: messbare, wiederholbare Bewertung, häufig mit Datensatz und Metrik;
- `AUDIT`: breitere, nachvollziehbar dokumentierte Prüfung eines Systems oder
  Projekts.

# Bestätigte lokale Einzelbegriffe

## ONE-WAY TOOL

Ein `ONE-WAY TOOL` verantwortet ein Ergebnis, aber nicht die weitere Steuerung
des Ablaufs. Der HUMAN validiert das Ergebnis und korrigiert bei Bedarf Prompt
oder Script.

- `ALIAS`: Quick Tool, One Shot Tool
- `TAGS`: a1, prompt, script, human-validation, bounded-output

## AUTOMATION

Eine `AUTOMATION` verantwortet einen Ablauf. Sie steuert mindestens einen
Folgeschritt und enthält eine einfache, eingebaute Validation.

- `ALIAS`: automatisierter Ablauf
- `TAGS`: a2, workflow, entry, pass, gate, output, checkpoint, milestone,
  resume, recovery, idempotency, self-healing, validation

## PROMPT-FUNKTIONEN

`PROMPT` ist das Gefäss; der Präfix benennt seine Funktion. Aktuell bekannte
Funktionsnamen sind unter anderem `STARTPROMPT`, `MASTERPROMPT`,
`BRÜCKENPROMPT` und `ÜBERGABEPROMPT`.

- `ALIAS`: Promptvorlage
- `TAGS`: start, bridge, handoff, master, instruction, context

`CONSTRUCTION` ist kein Prompt-Typ, sondern ein historisch gewählter Name für
einen Bereich, in dem geplant, entwickelt und gebaut wurde.

# Noch nicht kanonisch entschieden

Diese Punkte werden in Schritt C gegen `NAMING_LIBRARY.md` geprüft:

- Benennung und Abgrenzung von `PINWALL`, `BOARD` und `DECISIONS`;
- kanonische Namen für Packages, Module, Blueprints und Templates;
- endgültige Namen der Architekturstufen A3 und A4;
- konkrete Dateinamenssyntax und zulässige Separatoren;
- Name und Artefakte des heute noch zu veröffentlichenden Lernkonzepts.

# Dateinamenssystematik

Die eigentlichen Naming-Specs werden nach dem Terminologie-Review ergänzt.
Bis dahin gilt nur die minimale Zwischenregel:

- technische Bezeichner in `UPPER_SNAKE_CASE`;
- Markdown-Endung einheitlich `.md`;
- ein kanonischer Name pro Funktion;
- alternative Begriffe ausschliesslich als `ALIAS` auffindbar halten;
- Bedeutung nie still ändern, sondern versionieren.

# Visualisierungen

Die Stadt- und Ökolandschaft ist eine Orientierungshilfe für Einsteiger und
Diskussionen. Sie ist **keine** Source of Truth. Jede Darstellung nennt die
Version von `NAMING_LOCAL.md`, auf der sie basiert.
