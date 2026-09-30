---
document_id: ah-workflow-subject-spec-md-template
title: "[SUBJECT]_SPEC — Markdown-Vorlage"
status: ACTIVE
version: 1.0.0
created_at: 2026-09-30
updated_at: 2026-09-30
authority: HUMAN_CONFIRMED_LIBRARY_TEMPLATE
functional_area: WORKFLOW
canonical: true
template_target: "[SUBJECT]_SPEC.md"
source_check: WORKFLOW_SOURCE_CHECK.md
---

# [SUBJECT]_SPEC

## SUBJECT

`<Gegenstand dieser Spec>`

## PURPOSE

<Weshalb wird dieser Gegenstand spezifiziert?>

## AUTHORITY

| Feld | Wert |
|---|---|
| `decision_authority` | `<HUMAN oder belegte Authority>` |
| `representation_role` | `<SINGLE|PRIMARY|DERIVED>` |
| `primary_representation` | `<SELF oder relativer Pfad>` |
| `derived_from` | `<NONE oder relativer Pfad>` |
| `conflict_rule` | `PRIMARY_REPRESENTATION_WINS` |
| `effective_from` | `<ISO-8601 oder NOT_ACTIVE>` |
| `supersedes` | `<Referenz oder NONE>` |

Bei nur einer Repräsentation gilt `SINGLE`. Bei mehreren Repräsentationen
existiert genau eine `PRIMARY`; jede `DERIVED`-Datei verweist mit
`derived_from` auf sie. Bei Widerspruch gilt ausschliesslich die `PRIMARY`.

## SCOPE

- <Geltungsbereich>

## OUT_OF_SCOPE

- <ausgeschlossene Verantwortung, falls eine Verwechslung möglich ist>

## REQUIREMENTS

- <überprüfbare Anforderung>

## INPUTS

- <Input oder Vorbedingung, falls vorhanden>

## OUTPUTS

- <zugesichertes Ergebnis, falls vorhanden>

## FAILURE_BEHAVIOR

- <Verhalten bei nicht erfüllbarer Bedingung, falls ausführbar>

## LIMITS

- `DEFERRED`: <bewusst später>
- `KNOWN_LIMIT`: <im Scope, derzeit begrenzt>

## REFERENCES

- <Quelle oder abhängiger Vertrag>
