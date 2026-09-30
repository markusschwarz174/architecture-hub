---
document_id: ah-contract-convention
title: CONVENTION — reservierter Brückentyp
status: RESERVED_STUB
version: 0.1.0-stub
created_at: 2026-09-30
authority: NOT_ACTIVE
functional_area: CONTRACT
---

# CONVENTION — RESERVED STUB

## Reservierter Zweck

`CONVENTION` bleibt als möglicher Dateityp reserviert, falls zwischen
`MISSION` und den übrigen lokalen Verträgen eine gemeinsame Brücke benötigt
wird. Diese Datei setzt derzeit keine Regeln und darf nicht als aktive
Authority zitiert werden.

## Aktivierungsbedingung

Der Dateityp wird erst aktiviert, wenn der HUMAN mindestens festlegt:

1. welches konkrete Problem nicht durch `MISSION`, `SPEC` oder `POLICY`
   gelöst wird;
2. ob `CONVENTION` stabile Grundsätze oder veränderliche Arbeitsregeln trägt;
3. wo die Datei in der Authority-Hierarchie steht;
4. welche bestehenden Dateien sie ersetzt oder ausdrücklich nicht ersetzt.

## Skelett für eine spätere Ausarbeitung

| Begriff | Funktion |
|---|---|
| `PURPOSE` | Bedarf für die Brücke |
| `AUTHORITY` | Rang und Konfliktvorrang |
| `SHARED_DEFAULTS` | bereichsübergreifende gemeinsame Defaults |
| `EXCEPTIONS` | zulässige und nachvollziehbare Abweichungen |
| `ADOPTION` | welche Bereiche die Convention anwenden |
| `CHANGE_RULE` | wie Änderungen beschlossen und verteilt werden |
| `SUPERSEDES` | abgelöste Regeln und Nachfolgebeziehungen |
| `REFERENCES` | höhere und konsumierende Authorities |

## Offener Konflikt

Die geprüften FIELD_NOTES verwenden `CONSTITUTION` als höchste stabile Brücke
und `CONVENTION` für veränderliche operative Regeln. Das bestehende
`OPENAI/SYSTEM/SPECS/CONVENTION.md` bündelt dagegen viele unterschiedliche
Betriebsregeln. Vor Aktivierung muss deshalb entschieden werden, welche dieser
Funktionen lokal wirklich gemeint ist.

## Abgrenzung

- Kein Sammelbehälter für Regeln, die bereits in `SPEC`, `POLICY`,
  `PERMISSION`, `SCHEMA`, `GUARDRAIL` oder `LIFECYCLE` gehören.
- Keine parallele Source of Truth zur `MISSION`.
- Keine technische Durchsetzung; dafür sind Tools und Guardrails zuständig.

## Perlen und Provenienz

- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_CONSTITUTION.md` — stabile höchste
  Authority und Konflikthierarchie.
- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_OPERATIONS_MATRIX.md` — operative
  Convention mit expliziten Schreib-, Lese- und Update-Regeln.
- `OPENAI/SYSTEM/SPECS/CONVENTION.md` — Beispiel für den Nutzen, aber auch das
  Risiko eines sehr breiten Regelbehälters.
