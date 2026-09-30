---
document_id: ah-development-template-discovery
title: DISCOVERY — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[CHANGE]_DISCOVERY.md"
tags: [development, discovery, investigation, evidence]
---

# [CHANGE] — DISCOVERY

## Funktion

Die DISCOVERY ist die lesbare Ermittlungsakte des EXPLORER. Sie erklärt Suchraum, Vorgehen, Befunde, Beweise, Unsicherheiten und Hypothesen. Das gleichnamige `DISCOVERY_INVENTORY.json` enthält das maschinenlesbare Inventar derselben Untersuchung.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Identität | koppelt Auftrag, Agent und Inventory | Pflicht |
| Ausgangslage | Frage und bekannte Voraussetzungen | Pflicht |
| Suchstrategie | erwartete und unerwartete Suchräume | Pflicht |
| Bestandsbild | verdichtete Gesamtsicht | Pflicht |
| Befunde | evidenzgebundene Beobachtungen | Pflicht |
| Referenz- und Duplikatbild | Beziehungen, Varianten und Leichen | Pflicht |
| Hypothesen und Einschätzung | begründete, nicht als Fakt getarnte Deutung | falls vorhanden |
| Evidenzlücken | nicht geprüfte oder unbelegte Bereiche | Pflicht |
| Empfehlung | nächste Schritte, getrennt von Befunden | falls ableitbar |

## Identität

| Feld | Wert |
|---|---|
| Discovery-ID | `[DISCOVERY_ID]` |
| Change-ID | `[CHANGE]` |
| Auftrag | `[QUESTION_OR_SCOPE]` |
| Explorer | `[AGENT_INSTANCE]` |
| Beginn/Stand | `[TIMESTAMP]` |
| Inventory | `[CHANGE]_DISCOVERY_INVENTORY.json` |

## 1. Ausgangslage

`[Was ist bekannt, was wird nicht vorausgesetzt und was soll untersucht werden?]`

## 2. Suchstrategie

| Suchraum | Warum relevant | Methode | Status |
|---|---|---|---|
| `[PATH/SYSTEM/ARCHIVE]` | `[REASON]` | `[SEARCH/GRAPH/COMPARE/INSPECT]` | `[DONE/PARTIAL/NOT_SEARCHED]` |

Explizit zu berücksichtigen sind bei Relevanz: versteckte oder unerwartete Ablagen, Archive, Generatoren, Schemas, Logs, Referenzketten, Duplikate, Dateileichen, veraltete Varianten und nicht offensichtliche Abhängigkeiten.

## 3. Bestandsbild

`[Verdichtete Beschreibung der gefundenen Artefakte, Beziehungen, Varianten und Lücken.]`

## 4. Befunde

### F-001 — [TITLE]

- Einordnung: `[FACT/INFERENCE/HYPOTHESIS/UNKNOWN]`
- Kategorie: `[DUPLICATE/ORPHAN/STALE/BROKEN_REF/CONFLICT/GAP/PATTERN/OTHER]`
- Aussage: `[FINDING]`
- Evidenz: `[PATHS/IDS/EXCERPTS]`
- Auswirkung: `[IMPACT]`
- Konfidenz: `[HIGH/MEDIUM/LOW]`

## 5. Referenz- und Duplikatbild

`[Wichtige eingehende/ausgehende Referenzen, kanonische Kandidaten, Dubletten und Abweichungen.]`

## 6. Hypothesen und fachliche Einschätzung

| ID | Hypothese | Begründung | Gegenbelege | Nächste Prüfung |
|---|---|---|---|---|
| H-001 | `[HYPOTHESIS]` | `[REASONING]` | `[COUNTEREVIDENCE]` | `[NEXT_CHECK]` |

## 7. Evidenzlücken und nicht untersuchte Räume

- `[GAP_OR_LIMIT]`

## 8. Empfehlung an PLANNER/ARCHITEKT/HUMAN

`[Priorisierte nächste Schritte; klar getrennt von den Befunden.]`

## Abschluss

Die Discovery ist abgeschlossen, wenn Suchraum, Inventory, Referenzen, Duplikate, verwaiste/veraltete Artefakte, Befunde, Hypothesen und Grenzen so dokumentiert sind, dass ein anderer Agent ohne versteckten Kontext weiterarbeiten kann.

## Abgrenzung

Die DISCOVERY untersucht und empfiehlt. Sie ersetzt weder den BAUPLAN noch die Implementierung oder eine QUALITY-Validierung und autorisiert keine Löschung oder Migration.
