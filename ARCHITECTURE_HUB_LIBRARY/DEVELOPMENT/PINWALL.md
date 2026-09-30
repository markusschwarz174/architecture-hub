---
document_id: ah-development-template-pinwall
title: PINWALL — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "PINWALL.md"
tags: [development, pinwall, human_input, untriaged]
---

# PINWALL

## Funktion

Die PINWALL ist der bewusst unreflektierte HUMAN-Eingang. Ideen, Zweifel, Fundstücke und spontane Aufträge dürfen ohne Vorprüfung abgelegt werden. Ein Eintrag ist weder Entscheidung noch Vertrag noch Arbeitsfreigabe.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Eingangsregeln | Schutz der rohen HUMAN-Eingabe | Pflicht |
| Untriagierte Einträge | unverarbeiteter Eingang mit stabiler ID | Pflicht |
| Triage-Protokoll | nachvollziehbares Schicksal jedes Eintrags | Pflicht |
| Abgrenzung | verhindert Autoritätsverwechslung | Pflicht |

## Eingangsregeln

- HUMAN-Einträge werden inhaltlich nicht stillschweigend umgeschrieben.
- Jeder Eintrag erhält eine stabile ID und einen Zeitstempel.
- Triage verschiebt oder kopiert einen Eintrag erst nach sichtbarer Kennzeichnung in das zuständige Artefakt.
- Erledigte oder verworfene Einträge bleiben mit ihrem Ergebnis nachvollziehbar.

## Untriagierte Einträge

### PW-001 — [TIMESTAMP]

- Eingabe: `[RAW_HUMAN_INPUT]`
- Herkunft: `[SOURCE_OR_HUMAN]`
- Anhänge/Referenzen: `[REFS_OR_NONE]`
- Triage: `UNTRIAGED`

## Triage-Protokoll

| PINWALL-ID | Ergebnis | Zielartefakt | Ziel-ID | Bearbeitet am |
|---|---|---|---|---|
| PW-001 | `[ACCEPTED/DEFERRED/REJECTED/DUPLICATE]` | `[TARGET_OR_NONE]` | `[ID_OR_NONE]` | `[TIMESTAMP]` |

## Abgrenzung

Die PINWALL ist kein Backlog, keine SPEC, kein DEVELOPMENT_LOG und keine SSOT für Entscheidungen. `BOARD` ist höchstens ein verständlicher Alias, aber kein paralleler Dateityp.
