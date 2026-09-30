---
document_id: ah-contract-guardrail
title: GUARDRAIL — durchgesetzte Laufzeitgrenze
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# GUARDRAIL

## Zweck

Ein `GUARDRAIL` kontrolliert Eingaben, Ausgaben, Tool-Aufrufe oder
Seiteneffekte an einem realen Durchsetzungspunkt. Er beschreibt nicht nur eine
Grenze, sondern bindet sie an ein Tool, einen Hook, eine API oder eine andere
ausführbare Kontrolle.

## Entscheidungssemantik

```text
ALLOW
BLOCK
ESCALATE
```

Eine spezifische `BLOCK`-Regel schlägt ein allgemeineres `ALLOW`. Ausnahmen
müssen den blockierten Fall enger begrenzen und ihre zusätzlichen Bedingungen
explizit nennen. Das Verhalten ohne passende oder auswertbare Regel wird pro
Guardrail festgelegt; bei riskanten Seiteneffekten darf Unklarheit nicht als
stillschweigendes `ALLOW` behandelt werden.

## Begriffsskelett

| Begriff | Funktion | Status |
|---|---|---|
| `GUARDRAIL_ID` | stabile Kennung | Pflicht |
| `STATUS` | Geltungszustand | Pflicht |
| `SCOPE` | geschützter Bereich | Pflicht |
| `SUBJECT` | kontrollierter Actor oder kontrolliertes Tool | Pflicht |
| `CONTROL_POINT` | Input, Output, Tool-Aufruf oder Seiteneffekt | Pflicht |
| `AUTHORITY` | Quelle der Grenze und Konfliktvorrang | Pflicht |
| `ALLOW` | eindeutig zulässige Fälle | falls vorhanden |
| `BLOCK` | unzulässige Fälle | falls vorhanden |
| `ESCALATE` | Fälle, die einen Entscheid benötigen | falls vorhanden |
| `PRECEDENCE` | Priorität bei mehreren Treffern | Pflicht |
| `EXCEPTIONS` | eng begrenzte Ausnahmen samt Zusatzbedingungen | falls vorhanden |
| `ENFORCEMENT` | Hook, Tool, API, Middleware oder andere Kontrolle | Pflicht |
| `FAILURE_MODE` | Verhalten bei Ausfall oder unklarer Auswertung | Pflicht |
| `AUDIT` | protokollierte Entscheidung und Evidenz | Pflicht bei Seiteneffekten |
| `POLICY_REFERENCE` | zugrunde liegende Entscheidungsregeln | falls vorhanden |
| `PERMISSION_REFERENCE` | erforderliche Berechtigung | falls eine Fähigkeit kontrolliert wird |
| `LIFECYCLE` | Geltung, Ablösung und Stilllegung | Pflicht |
| `QUALITY_REFERENCE` | Tests und Wirksamkeitsnachweis | Pflicht |

## Allowlist und Denylist

`ALLOWLIST` und `DENYLIST` sind mögliche Datenstrukturen innerhalb eines
Guardrails. Die historischen Bezeichnungen `WHITELIST` und `BLACKLIST` bleiben
als Such-Aliases auffindbar. Keine dieser Listen ist allein eine Permission.

## Abgrenzung

- `POLICY` formuliert die Entscheidungsregel.
- `PERMISSION` bindet eine Fähigkeit an Subject, Aktion und Ressource.
- `GUARDRAIL` trifft oder erzwingt die Kontrolle an einem realen Laufzeitpunkt.
- `QUALITY` prüft, ob das Guardrail korrekt und vollständig greift.

## Perlen und Provenienz

- `FIELD_NOTES_DRAFT/0_C_CONVENTION/REVIEW_TO_MARKER/RTM_AUTOFIX.yaml` —
  gemeinsame ALLOW-/BLOCK-Tabelle, Block-Vorrang, enge Ausnahme und Audit.
- `MY_AI_PROJECTS/2026-08 MAIL_ORGANIZER/VERSION_260923/config/SECURITY_POLICY.yaml`
  — erlaubte Aktionen und verbotene Fähigkeiten.
- `src/mail_manager/thunderbird_executor.py` und Contract-Tests — reale
  Action- und Zielkontrollen statt nur beschriebener Grenzen.
- OpenAI Agents SDK Guardrails und Open Policy Agent — externe Referenzen für
  Laufzeitkontrollen und Policy Enforcement; keine automatische lokale
  Produktbindung.
