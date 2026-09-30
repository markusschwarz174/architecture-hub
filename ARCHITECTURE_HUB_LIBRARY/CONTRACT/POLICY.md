---
document_id: ah-contract-policy
title: POLICY — bedingte Entscheidungsregel
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# POLICY

## Zweck

Eine `POLICY` legt fest, welche Entscheidung unter welchen Bedingungen gilt.
Sie ist eigenständig, weil weder eine beschreibende SPEC noch ein SCHEMA noch
eine einzelne Permission eine veränderliche Regelmenge mit Prioritäten,
Ausnahmen und Lebenszyklus vollständig ausdrückt.

## Dateifamilie

```text
[SUBJECT]_POLICY.md
[SUBJECT]_POLICY.yaml
[SUBJECT]_POLICY.json
```

Markdown erklärt Zweck und Begründung. YAML oder JSON wird verwendet, wenn ein
Tool die Regeln deterministisch auswertet. Bei mehreren Darstellungen werden
Authority und Ableitungsrichtung festgelegt.

## Begriffsskelett

| Begriff | Funktion | Status |
|---|---|---|
| `POLICY_ID` | stabile Kennung | Pflicht |
| `STATUS` | `DRAFT`, `ACTIVE`, `SUSPENDED`, `SUPERSEDED` oder `RETIRED` | Pflicht |
| `VERSION` | geltende Version | Pflicht |
| `PURPOSE` | zu regelnder Entscheidungsbereich | Pflicht |
| `SCOPE` | Geltungsbereich | Pflicht |
| `AUTHORITY` | Entscheidungsquelle und Konfliktvorrang | Pflicht |
| `RULES` | Bedingungen und resultierende Entscheide | Pflicht |
| `PRIORITY` | Auflösung mehrerer passender Regeln | Pflicht, wenn Überschneidungen möglich sind |
| `DEFAULT` | Entscheidung ohne passende Regel | Pflicht |
| `EXCEPTIONS` | eng begrenzte Abweichungen | falls vorhanden |
| `ESCALATION` | Weg bei unentscheidbaren oder gesperrten Fällen | Pflicht |
| `ENFORCEMENT` | konsumierendes Tool oder Guardrail | falls maschinell wirksam |
| `EFFECTIVE_FROM` | Beginn der Geltung | Pflicht für `ACTIVE` |
| `REVIEW_TRIGGER` | Ereignisse für erneute Prüfung | Pflicht |
| `EXPIRES` | Ablauf oder ausdrücklich `NO_EXPIRY` | Pflicht |
| `SUPERSEDES` / `SUPERSEDED_BY` | nachvollziehbare Ablösung | falls vorhanden |
| `RETIREMENT` | Stilllegung, Archivierung und Verhalten der Konsumenten | Pflicht |
| `AUDIT` | Entscheidungs- und Änderungsnachweis | falls wirksam |
| `QUALITY_REFERENCE` | Tests und Prüfevidenz | falls maschinell wirksam |

`RESPONSIBILITY` und `OWNER` des ausführenden Policy-Konsumenten gehören nach
`TOOLING`. Die Policy nennt nur ihre Authority und referenziert den Konsumenten.

## Lifecycle-Regel

Eine neue Policy-Version überschreibt ihre Vorgängerin nicht still. Sie nennt
den Geltungsbeginn, den abgelösten Stand und den Umgang mit bereits begonnenen
Fällen. Historische Entscheide dürfen als Genealogie erhalten bleiben, setzen
aber keine aktuelle Norm.

## Abgrenzung

- `SPEC` beschreibt Anforderungen und zugesichertes Verhalten.
- `POLICY` entscheidet anhand von Bedingungen.
- `PERMISSION` bindet eine konkrete Fähigkeit.
- `SCHEMA` validiert Struktur.
- `GUARDRAIL` setzt die Policy an einem Kontrollpunkt durch.
- `LIFECYCLE` regelt Outputs, nicht die fachliche Entscheidung selbst.

## Perlen und Provenienz

- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_DECISION_LIFECYCLE.md` — Status,
  Schreiber, Leser, Update-Trigger und nachvollziehbare Ablösung.
- `MY_AI_PROJECTS/2026-08 MAIL_ORGANIZER/VERSION_260923/config/`
  `SECURITY_POLICY.yaml` und `AUTOMATION_POLICY.yaml` — getrennte
  Policy-Funktionen mit maschinenlesbaren Regeln.
- zugehörige Schemas und `config_loader.py` — formale Prüfung und
  Cross-Checks vor Ausführung.
- `FIELD_NOTES_DRAFT/0_C_CONVENTION/REVIEW_TO_MARKER/RTM_AUTOFIX.yaml` —
  Priorität, Bedingungen, Default und blockierende Regeln.
