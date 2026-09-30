---
document_id: ah-naming-local
title: Architecture Hub — Local Naming
status: DRAFT_FOR_HUMAN_REVIEW
version: 0.1.0-draft
created_at: 2026-09-30
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
- `TAGS`: architecture, planning, construction, implementation, build, adr,
  decisions, pinwall, versioning

**Abgrenzung:** DEVELOPMENT beschreibt, wie wir das System bauen und ändern.
WORKFLOW beschreibt, wie das gebaute System arbeitet.

## 3. WORKFLOW

**Funktion:** Beschreibt ausführbare oder nachvollziehbare Abläufe mit Schritten,
Zuständen, Übergängen, Inputs, Outputs und Fehlerwegen.

- `ALIAS`: Ablauf, Prozess
- `TAGS`: workflow, pipeline, automation, loop, graph, orchestration, state,
  transition

**Lokale Verwendung:** `WORKFLOW` ist der technische Begriff in Tools.
`Pipeline` darf in Chats als anschauliches Ablaufwort verwendet werden, erzeugt
aber kein zweites Architekturkonzept.

## 4. CONTRACT

**Funktion:** Legt überprüfbar fest, was ein System, Baustein oder Beteiligter
leisten muss, darf und nicht darf. Hier liegen Anforderungen, Grenzen,
Authorities, Regeln, Policies, Schemas und Schnittstellenvereinbarungen.

- `ALIAS`: Vertrag
- `TAGS`: spec, requirement, convention, constitution, authority, policy,
  constraint, schema, interface, guardrail

**Abgrenzung:** `SPEC` ist ein lokaler Sammelbegriff für beschreibende
Markdown-Artefakte. Nicht jede Spec ist jedoch ein Contract, und ein
maschinenlesbares Schema kann Teil eines Contracts sein.

## 5. TOOLING

**Funktion:** Enthält die Mittel und ausführenden Einheiten, mit denen Mission,
Development, Workflow und Contract praktisch umgesetzt werden.

- `ALIAS`: Tools, Werkzeugkasten
- `TAGS`: prompt, script, agent, persona, role, hook, module, harness, skill,
  command

**Lokale Unterscheidung:**

- `AGENT` ist eine ausführende Einheit mit Auftrag, Zustand und gegebenenfalls
  Tools.
- `PERSONA` prägt Stimme, Perspektive oder Verhaltensstil.
- `ROLE` beschreibt eine Funktion innerhalb eines Prompts oder Workflows.

Die drei Begriffe bleiben auffindbar, sind aber keine Synonyme.

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
- `TAGS`: a2, workflow, startpoint, validation, pinwall,
  development-control

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
