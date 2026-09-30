---
document_id: ah-skeleton-v1-audit
title: Audit Architecture Skeleton 1.0 Draft
status: REVIEWED
version: 1.0.0
created_at: 2026-09-30T01:01:37+02:00
authority: HUMAN_REVIEW_REQUIRED
---

# AUDIT ARCHITECTURE SKELETON 1.0 — DRAFT

## Auftrag

Prüfung des A1-A4-Skeletts auf Konflikte, Widersprüche, Redundanzen und
Abdeckung realer Dateifunktionen aus vorhandenen Projekten.

## Prüfumfang

Inventarisiert wurden:

1. `AI_PROJECTS/OPENAI` mit 236 sichtbaren Dateien;
2. `FIELD_NOTES_DRAFT` mit 99'171 sichtbaren Pfaden, davon 9'492
   kontrollierte source-nahe Dateien nach Ausschluss offensichtlicher
   `tmp`-, Archiv-, Cache- und Runtime-Bestände;
3. `MY_AI_PROJECTS` mit 6'011 sichtbaren Dateien, davon 2'691 source-nahe
   Dateien nach Ausschluss vendorter Abhängigkeiten und Caches;
4. die im aktuellen `SYSTEM/CONSTRUCTION/SOURCES_FOR_V0` ausgewählten Quellen
   aus FIELDNOTES, LERNCOCKPIT und MAIL_ORGANIZER.

Die Prüfung war eine vollständige Pfad-, Namens- und Dateityp-Inventur mit
inhaltlicher Prüfung repräsentativer Steuerdateien. Sie war keine semantische
Volllektüre jedes generierten Runtime-, Medien- oder Vendor-Files. Einige
vendorte Python-Verzeichnisse im MAIL_ORGANIZER waren für die Inventur nicht
lesbar; sie sind Fremdabhängigkeiten und keine Architekturquellen.

## Beobachtete Dateifamilien

| Beobachtete alte Dateien | Funktion im Skelett 1.0 |
|---|---|
| `0_M_MISSION.md`, `MISSION_CONTROL.md`, `META_ROLE_AND_VISION.md` | `MISSION.md` oder stufenspezifische Systemspezifikation |
| Prompts, Prompt Cards, Startprompts, Correction Prompts | `PROMPT*.md` / `STARTPROMPT.md` |
| Python, PowerShell, JavaScript, CMD, Module | `SCRIPT.*` / Source Code |
| `ARCHITECTURE.md`, `PACKAGE.md`, `*_CONTROL.md`, `DIALOGFLOW.md` | `AUTOMATION.md`, `AGENT_SYSTEM.md` oder zusätzliche `SPECS` |
| `SPEC_*.md`, `ROOM_*_SPEC.md`, `SPECS/` | zusätzliche `SPECS/*.md` |
| `C_NAMING.md`, PDF-Naming und Pfadregeln | `NAMING_LOCAL.md` |
| `CONVENTION.md`, `CONSTITUTION.md`, Operations Matrix | `CONVENTIONS.md` |
| `AGENTS.md`, `CLAUDE.md` | Werkzeug- und Providerinstruktionen |
| `PLANNER.md`, `IMPLEMENTOR.md`, `VALIDATOR.md`, `REVIEWER.md`, `OBSERVER.md` | `AGENT_<NAME>.md` oder `ROLE_<NAME>.md` |
| Persona-Dateien | `ROLE_<NAME>.md` |
| Output Schemas, JSON Schema, YAML Schema | `SCHEMA.*` |
| `GUARDRAIL`, Policy-, Allowlist- und Operations-Dateien | `GUARDRAILS.yaml`, `CONFIG.*` oder `SECURITY.md` |
| JSON/YAML-Konfigurationen | `CONFIG.*` |
| `DATA`, Fixtures, Corpora, Mail- und Chat-Payloads | `DATA`, `INPUT`, `SOURCE` oder `FIXTURE` |
| SQL-Schema und Migrationsdateien | `DATABASE_SCHEMA.sql` / `migrations/*.sql` |
| `PIN_WALL.md`, `BOARD.md`, `BUILD_STATUS.md`, Roadmaps | `PINWALL.md` beziehungsweise funktionales `BOARD.md` |
| `HANDOFF.md` | `HANDOFF.md` |
| JSONL-Logs, Journal, Experiment Logs | `LOG.jsonl` / `JOURNAL.md` |
| Tests, Smoke Tests, Canary Checks | `tests/*` / `TEST_*.md` |
| Quality Audits, Reviews, Validationsberichte | `VALIDATION.md`, `EVALS`, `REPORT` oder Validation Report |
| `DECISIONS_LOG.md`, Version Decisions | `ADR_*.md` / `DECISIONS_LOG.md` |
| Baupläne, Plans, Work Tickets, Backlogs | `BAUPLAN.md`, `PLAN.md`, `WORK_TICKET.md` |
| `README`, `INSTALL`, `CONTRIBUTING`, `LICENSE` | gleichnamige Governance- und Einstiegsfamilien |
| `LESSONS_LEARNED`, Perlenkatalog | `LESSONS_LEARNED.md`, `SOURCES.md` oder Library-Kandidat |
| Indexe und Manifeste | `INDEX.*` / `MANIFEST.*` |
| Hooks, Plugins, Scheduler, Browser Bridges | technische Entry-Point- und Deployment-Dateien |
| Reports, HTML, DOCX, Bilder, Audio, Video | `OUTPUT`, `ARTIFACT`, `REPORT` oder `ASSET` |
| Checkpoints, Locks, Runtime-State, Backup | Runtime-, Recovery-, Snapshot- oder Archivfamilie |

## Abdeckungsergebnis

Alle beobachteten **autorisierten und projektgesteuerten Dateifunktionen**
lassen sich einer Dateifamilie des Skeletts zuordnen. Nicht jede historische
Datei braucht eine eigene Matrixspalte. Generierte Payloads, Medien,
Runtime-State, Caches, virtuelle Umgebungen, Binaries und vendorte Libraries
sind Betriebs-, Fach- oder Fremdartefakte und keine Grundarchitektur.

`SPECS` wurden nicht verworfen. Der scheinbare Konflikt wurde so aufgelöst:

- `AUTOMATION.md` ist die primäre A2-Spec;
- `AGENT_SYSTEM.md` ist die primäre A3-Spec;
- `MULTI_PROVIDER.md` ist die primäre A4-Spec;
- zusätzliche `SPECS/*.md` bleiben auf allen Stufen möglich.

## Gefundene Konflikte und Auflösung

### 1. A1-A4 war als Umfangsskala beschrieben

**Konflikt:** Die alte Fassung mischte Einmaligkeit, Wiederholung,
Wissensbasis, Multi-Agent und Produktstatus.

**Auflösung:** A1-A4 beschreibt jetzt Verantwortung und Validationsgrenze.
Laufzeit, Lebensdauer, Wiederverwendung und Öffentlichkeit sind orthogonal.

### 2. Ein Repository sollte genau eine A-Stufe erhalten

**Konflikt:** Reale Projekte enthalten Systeme verschiedener Stufen. Das
OPENAI-Projekt besitzt beispielsweise deterministische Hook-Automation und
providerübergreifende Entwicklungsvalidation nebeneinander.

**Auflösung:** Klassifiziert wird der konkrete Workflow oder die konkrete
Systemgrenze, nicht pauschal der Repository-Ordner.

### 3. `PINWALL.md` widerspricht bestehenden `BOARD.md`-Konventionen

**Konflikt:** FIELDNOTES verwendet `PIN_WALL.md`; das OPENAI-System verbietet
zusätzliche Pinwalls und verwendet Boards.

**Auflösung:** `PINWALL.md` bezeichnet die Funktion der aktuellen
Entwicklungssteuerung. Ein `BOARD.md` darf diese Funktion erfüllen. Es gibt nie
zwei parallele aktuelle Wahrheiten.

### 4. `MISSION.md` und `README.md` überlappten

**Auflösung:** Mission = Warum, Grenzen und Erfolg. README = Einstieg,
Bedienung und Installation.

### 5. Validation, Tests, Evals und Reports wurden vermischt

**Auflösung:** `VALIDATION.md` definiert den Vertrag; Tests und Evals führen
ihn aus; Reports speichern die Evidenz.

### 6. Schema, Config, Guardrails und Data wurden vermischt

**Auflösung:** Schema definiert Struktur; Config setzt Verhalten; Guardrails
setzen Grenzen; Data enthält Payload oder ungefährliche Beispiele.

### 7. `AGENTS.md`, `AGENT_<NAME>.md` und `ROLE_<NAME>.md` wurden vermischt

**Auflösung:** `AGENTS.md`/`CLAUDE.md` steuern Werkzeuge im Projekt. Ein
Agentenfile beschreibt einen Akteur mit Authority und Vertrag. Ein Rollenfile
beschreibt eine begrenzte Funktion oder Perspektive. Separate Agenten- und
Rollenfiles bleiben optional.

### 8. `STARTPROMPT` war als universeller Startpunkt vorgesehen

**Konflikt:** Reale Automationen starten auch über Hooks, Zeitplan, API,
Browser-Bridge, CLI oder Dateiereignis.

**Auflösung:** `AUTOMATION.md` dokumentiert den Entry Point. `STARTPROMPT.md`
bleibt optional; eine generische `HOOK.md` wird nicht eingeführt.

### 9. Self-Healing drohte A2 und A3 zu vermischen

**Auflösung:** A2 besitzt begrenzte, vorgegebene RECOVERY. A3 darf innerhalb
seiner Grenzen Self-Correction betreiben. Autonome Veränderung von Code,
Guardrails oder Authorities ist keine Grundbefugnis.

### 10. Gleiches Modell, neues Modell und neuer Provider waren unklar

**Auflösung:** A3 bleibt innerhalb desselben Provider-Ökosystems und trennt
Sessions. A4 überschreitet eine Provider- beziehungsweise unabhängige
Modellfamiliengrenze.

## Verbleibende bewusste Offenheiten

1. Die Datei-Normalformen `AGENT_SYSTEM.md` und `MULTI_PROVIDER.md` sind neue
   Zielnamen. Alte `PACKAGE`, `CONTROL`, `PIPELINE` und `P7`-Dateien lassen sich
   funktional darauf abbilden, müssen aber nicht rückwirkend umbenannt werden.
2. Ob `GUARDRAILS.yaml`, `SECURITY.md`, `EVALS` und `HANDOFF.md` in jeder A3-
   beziehungsweise A4-Variante wirklich Pflicht bleiben, muss im Praxistest
   gegen kleine rein beratende Systeme geprüft werden.
3. Zentral versionierte `NAMING`- und `CONVENTIONS`-Dateien dürfen zuverlässig
   verlinkt werden. Ein Projekt muss nicht dieselbe Datei duplizieren, muss
   aber die verwendete Version eindeutig binden.
4. Echtdaten werden nicht durch `DATA.example.*` repräsentiert. Für öffentliche
   Repositories ist weiterhin ein eigener Public-Readiness-Check notwendig.

## Urteil

Das Skelett 1.0 ist als **arbeitsfähiger Draft** vollständig genug, um die
anschliessende Library-Arbeit zu strukturieren. Es ist noch kein final
freigegebener Standard. Die grössten früheren Widersprüche sind aufgelöst;
die verbleibenden Offenheiten sind bewusst markiert und im Praxistest
entscheidbar.
