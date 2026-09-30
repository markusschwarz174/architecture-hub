---
document_id: ah-naming-library
title: Architecture Hub — Naming Library
status: LIVING_REFERENCE
version: 0.1.0
created_at: 2026-09-30
authority: EXTERNAL_REFERENCE_NOT_LOCAL_STANDARD
scope: AI community, professional software practice, vendors and standards
---

# NAMING_LIBRARY — Brücke in die grosse, weite Welt

## Zweck

`NAMING_LIBRARY.md` sammelt Begriffe und **Systematiken** aus der AI-Community,
der professionellen Softwareentwicklung, Grossunternehmen, Forschung,
Standards und Herstellerdokumentation.

Die Datei ist keine lokale Sprach-Authority und keine allgemeingültige
Wahrheit. Sie ist eine Übersetzungs- und Rechercheebene: Neue oder unbekannte
Begriffe werden hier eingeordnet, bevor der HUMAN entscheidet, ob und wie sie
in `NAMING_LOCAL.md` übernommen werden.

Die subjektive lokale Einteilung in sechs Funktionsbereiche gehört ausdrücklich
nicht in diese Datei.

## Einfache Erfassung

Jeder Begriff erhält neben einer kurzen Bedeutung nur:

- `ALIAS`: andere Namen, Schreibweisen oder etablierte Abkürzungen;
- `TAGS`: verwandte Themen für Suche und Gruppierung.

`ALIAS` behauptet keine universelle Synonymie. Die Bedeutung gilt immer im
genannten Kontext. Falls eine wichtige Abgrenzung nötig ist, genügt ein klarer
Satz.

Neue Einträge nennen nach Möglichkeit eine Primärquelle, den beobachteten
Kontext und das Aufnahmedatum. Ein externer Begriff wird niemals automatisch
zum lokalen Standard.

# Externe Systematiken

## 1. Entwicklungsschichten rund um AI-Systeme

Die Community beschreibt die Entwicklung nicht mehr nur als
Prompt-Engineering. Mehrere Schichten ergänzen sich; sie sind keine allgemein
anerkannte lineare Reifeleiter.

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `PROMPT ENGINEERING` | Gestaltung einzelner Instruktionen, Beispiele und Ausgabevorgaben | Prompt Design | prompt, instruction, few-shot, output |
| `CONTEXT ENGINEERING` | Auswahl, Strukturierung und Aktualisierung des gesamten Modellkontexts | Context Design | context-window, retrieval, memory, tools, state |
| `HARNESS ENGINEERING` | Bau der Laufzeitumgebung, die ein Modell mit Tools, Regeln, Zuständen und Feedback umgibt | Agent Harness | runtime, tools, guardrails, orchestration, observability |
| `LOOP ENGINEERING` | Gestaltung wiederholter Plan–Act–Observe–Evaluate-Zyklen und ihrer Stopregeln | Agent Loop Design | iteration, feedback, stopping, retry, reflection |
| `GRAPH ENGINEERING` | Modellierung verzweigter, zustandsbehafteter Agent- und Workflow-Abläufe als Graph | Agent Graph Design | nodes, edges, routing, state-machine, orchestration |
| `AGENT ENGINEERING` | Übergreifende Praxis für zuverlässige agentische Systeme über Prompt, Kontext, Tools, Laufzeit und Evaluation | Agentic Engineering | agents, reliability, deployment, evals, operations |
| `AGENTOPS` | Betrieb, Beobachtung und Verbesserung von Agentensystemen in Produktion | LLMOps for Agents | tracing, monitoring, cost, latency, incidents |

## 2. Agenten und Workflows

Eine verbreitete Systematik unterscheidet zwischen `WORKFLOW` und `AGENT`:
Beim Workflow ist der Pfad weitgehend im Voraus festgelegt; beim Agenten
entscheidet das Modell dynamisch über Schritte und Tool-Nutzung. In realen
Systemen kommen Mischformen vor.

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `AGENT` | Modellgesteuerte ausführende Einheit, die Schritte und Tools innerhalb eines Auftrags auswählt | AI Agent | autonomy, tools, state, goal |
| `WORKFLOW` | Orchestrierter Ablauf mit definierten Schritten oder Übergängen | Flow | sequence, state, orchestration, deterministic |
| `MULTI-AGENT SYSTEM` | System mehrerer interagierender Agenten oder Rollen | MAS | delegation, handoff, coordination, authority |
| `ORCHESTRATOR` | Komponente, die Aufgaben, Zustände oder Übergaben koordiniert | Coordinator | routing, scheduling, handoff, workflow |
| `HANDOFF` | Übergabe von Verantwortung und Kontext an eine andere ausführende Einheit | Transfer | agent, context, authority, session |
| `TOOL` | aufrufbare Fähigkeit mit definiertem Interface | Function, Action | schema, input, output, side-effect |
| `SKILL` | paketierte, wiederverwendbare Anleitung oder Fähigkeit; Bedeutung ist plattformabhängig | Capability | instructions, package, tool, reusable |
| `GUARDRAIL` | Laufzeitkontrolle für Eingaben, Ausgaben oder Aktionen | Safety Rail | validation, policy, boundary, runtime |

## 3. Spezifikations- und Entwicklungsansätze

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `SPEC-DRIVEN DEVELOPMENT` | Entwicklung, bei der eine überprüfbare Spezifikation das zentrale Bau- und Abnahmeartefakt ist | SDD | spec, requirements, implementation, tests |
| `TEST-DRIVEN DEVELOPMENT` | Tests werden vor oder gemeinsam mit der Implementierung formuliert und steuern den Bau | TDD | tests, red-green-refactor, acceptance |
| `BEHAVIOR-DRIVEN DEVELOPMENT` | Verhalten wird in fachnahen Beispielen und Szenarien beschrieben | BDD | scenarios, given-when-then, acceptance |
| `ARCHITECTURE DECISION RECORD` | kompakter Datensatz eines Architekturentscheids mit Kontext und Folgen | ADR | decision, alternatives, consequences, architecture |
| `REQUEST FOR COMMENTS` | Vorschlag zur strukturierten Diskussion und Entscheidung | RFC | proposal, review, governance, decision |
| `TECHNICAL SPIKE` | begrenzte Untersuchung einer technischen Unsicherheit mit dokumentiertem Erkenntnisgewinn | Spike | exploration, risk-reduction, prototype, learning |

## 4. Qualitäts- und Sicherheitssystematiken

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `VALIDATION` | Prüfung, ob das System für den beabsichtigten Zweck geeignet ist | — | fitness-for-purpose, acceptance, quality |
| `VERIFICATION` | Prüfung, ob eine Umsetzung definierte Anforderungen erfüllt | — | conformance, requirements, quality |
| `EVALUATION` | systematische Bewertung mit Fällen, Kriterien und möglichst Metriken | Eval | benchmark, dataset, metric, regression |
| `REVIEW` | fachliche oder technische Prüfung eines Artefakts durch Menschen oder Systeme | Inspection | feedback, approval, artifact, code |
| `AUDIT` | nachvollziehbare Prüfung von System, Prozess oder Kontrollen gegen einen Bezugsrahmen | Assessment | evidence, compliance, controls, traceability |
| `RED TEAMING` | gezielte Suche nach Missbrauchs-, Sicherheits- und Robustheitsschwächen | Adversarial Testing | security, safety, abuse, robustness |
| `THREAT MODELING` | strukturierte Ermittlung von Schutzgütern, Angreifern, Bedrohungen und Massnahmen | Threat Analysis | security, trust-boundary, risk, mitigation |
| `OBSERVABILITY` | Fähigkeit, internen Systemzustand aus Traces, Logs und Metriken zu verstehen | — | tracing, logging, metrics, debugging |

**Wichtige Übersetzungsnotiz:** Fachnormen trennen häufig `VALIDATION` und
`VERIFICATION`. Lokal werden beide bewusst unter `VALIDATION` zusammengeführt.
Die externe Unterscheidung bleibt hier erhalten, damit Quellen korrekt gelesen
werden können.

## 5. Protokolle, Daten und Integrationen

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `MODEL CONTEXT PROTOCOL` | offenes Protokoll, mit dem AI-Anwendungen Tools, Ressourcen und Prompts von Servern beziehen | MCP | protocol, tools, resources, prompts, integration |
| `RETRIEVAL-AUGMENTED GENERATION` | Abruf externer Informationen zur Anreicherung des Modellkontexts | RAG | retrieval, embeddings, vector-store, context |
| `KNOWLEDGE GRAPH` | Wissen als Entitäten und Beziehungen mit expliziter Semantik | KG | graph, ontology, entities, relations |
| `SCHEMA` | maschinenlesbare Definition zulässiger Struktur und Datentypen | Data Schema | json-schema, sql, validation, contract |
| `STRUCTURED OUTPUT` | Modellausgabe, die einer vorgegebenen Struktur oder einem Schema folgt | Constrained Output | json, schema, parsing, reliability |

## 6. Lernen während der Arbeit

Für das lokale Lernkonzept existiert kein einzelner externer Begriff mit exakt
demselben Umfang. Relevante Nachbarn sind:

| Begriff | Kurzbedeutung | ALIAS | TAGS |
|---|---|---|---|
| `LEARNING IN THE FLOW OF WORK` | Lernen wird nahe an der aktuellen Arbeit verfügbar gemacht | Workflow Learning | workplace-learning, performance-support, just-in-time |
| `JUST-IN-TIME LEARNING` | Wissen wird genau dann erschlossen, wenn es für eine Aufgabe gebraucht wird | JIT Learning | need-driven, microlearning, workplace-learning |
| `TECHNICAL SPIKE` | zeitlich begrenzte Untersuchung, um technische Unsicherheit zu reduzieren | Spike | exploration, prototype, decision, risk |
| `CONTEXT SWITCHING` | Wechsel zwischen Aufgaben oder mentalen Kontexten mit möglichem Wiederanlaufverlust | Task Switching | interruption, cognitive-load, focus, state |

Das lokale Konzept ergänzt diese Nachbarn um einen bewussten Checkpoint, einen
isolierten AI-geführten Lernzweig, eine verdichtete Lernkapsel, einen
Merge-Entscheid und die Rückkehr zur Hauptarbeit. Sein öffentlicher Name wird
vor der Publikation separat festgelegt.

# Aufnahme- und Übersetzungsprozess

1. Unbekannten Begriff mitsamt Fundstelle und Kontext erfassen.
2. Nach `TERM`, `ALIAS` und `TAGS` suchen.
3. Falls nötig, Bedeutung anhand einer Primärquelle ergänzen.
4. Zugehörige externe Systematik dokumentieren — nicht nur das Einzelwort.
5. Eine lokale Zuordnung als Vorschlag markieren.
6. Erst nach HUMAN-Entscheid den kanonischen Eintrag in `NAMING_LOCAL.md`
   anlegen oder ändern.

# Primäre Startquellen

- Anthropic: *Building effective agents* — Workflow/Agent und agentische
  Muster: <https://www.anthropic.com/research/building-effective-agents>
- OpenAI: *A practical guide to building agents* — Agenten, Tools,
  Instruktionen und Guardrails:
  <https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/>
- Model Context Protocol: Architektur und Kernkonzepte:
  <https://modelcontextprotocol.io/docs/learn/architecture>
- GitLab: *Technical Spike*:
  <https://handbook.gitlab.com/handbook/engineering/development/growth/technical_spikes/>
- Microsoft Engineering Playbook: *Technical Spike*:
  <https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/technical-spike/>
- Josh Bersin: *Learning in the Flow of Work*:
  <https://joshbersin.com/2018/06/a-new-paradigm-for-corporate-training-learning-in-the-flow-of-work/>

Die Liste ist ein Startpunkt, keine abgeschlossene Bibliografie.
