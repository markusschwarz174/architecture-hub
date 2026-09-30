---
document_id: ah-contract-permission
title: PERMISSION — deklarierte und wirksame Berechtigung
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# PERMISSION

## Zweck

Eine `PERMISSION` legt fest, welcher Actor oder welches Tool welche Aktion an
welcher Ressource unter welchen Bedingungen ausführen darf oder nicht darf.

Eine Markdown-Datei dokumentiert die Berechtigung, erteilt technisch jedoch
noch keine Fähigkeit. Ohne belegte Durchsetzungsstelle trägt eine Permission
den Zustand `DECLARATIVE_ONLY`.

## Wirksamkeitskette

```text
HUMAN- oder System-Authority
-> PERMISSION
-> maschinenlesbare POLICY oder CONFIG
-> SCHEMA
-> Hook, Tool, API-, App- oder Betriebssystemkontrolle
-> QUALITY-Evidenz und Audit
```

Nur die tatsächlich verdrahtete Schnittmenge dieser Ebenen ist wirksam.

## Begriffsskelett

| Begriff | Funktion | Status |
|---|---|---|
| `PERMISSION_ID` | stabile Kennung | Pflicht |
| `STATUS` | `DECLARATIVE_ONLY`, `ENFORCED`, `SUSPENDED`, `REVOKED` oder `EXPIRED` | Pflicht |
| `SUBJECT` | Actor oder Tool, für das die Regel gilt | Pflicht |
| `ACTION` | erlaubte oder blockierte Operation | Pflicht |
| `RESOURCE` | betroffenes Ziel | Pflicht |
| `EFFECT` | `ALLOW` oder `DENY` | Pflicht |
| `SCOPE` | sachliche und technische Reichweite | Pflicht |
| `CONDITIONS` | notwendige Zustände und Vorbedingungen | falls vorhanden |
| `AUTHORITY` | erteilende oder entziehende Entscheidungsquelle | Pflicht |
| `BINDING` | Version, Request, Fall, Transaktion oder Hash | bei veränderlichen oder riskanten Vorgängen |
| `ENFORCEMENT_POINTS` | konkrete Hooks, Tools, APIs, ACLs oder App-Rechte | Pflicht für `ENFORCED` |
| `DEFAULT` | Verhalten ohne passende Regel; für Berechtigungen grundsätzlich `DENY` | Pflicht |
| `VALID_FROM` / `EXPIRES` | zeitliche Geltung | falls zeitlich begrenzt |
| `REVOCATION` | Widerrufsweg und Wirkung | Pflicht |
| `AUDIT` | protokollierte Entscheidung und Ausführung | Pflicht bei Seiteneffekten |
| `LIFECYCLE` | Verweis auf erzeugte oder veränderte Outputs | falls Outputs betroffen sind |
| `QUALITY_REFERENCE` | Nachweis der technischen Durchsetzung | Pflicht für `ENFORCED` |

Die Zuständigkeit des Subjects oder Tools wird in `TOOLING` festgelegt. Diese
Datei dupliziert weder `RESPONSIBILITY` noch `OWNER`.

## Finanz-Spezialfall

Finanzielle Operationen werden nicht pauschal freigegeben. Die Permission wird
an den realen Vorgang und dessen Domain-Schema gebunden. Welche Attribute
dafür erforderlich sind, bestimmt die konkrete Finanz-SPEC; diese Library
erfindet keine Betragsgrenzen oder Freigabestufen.

## Abgrenzung

- Eine Allowlist ist nicht automatisch eine Permission.
- Eine inhaltliche HUMAN-Zustimmung ist nicht automatisch eine
  Ausführungsberechtigung.
- `POLICY` enthält allgemeine Entscheidungsregeln; `PERMISSION` bindet die
  konkrete Fähigkeit an Subject, Aktion, Ressource und Bedingungen.
- `GUARDRAIL` kontrolliert die Ausführung an einem realen Laufzeitpunkt.

## Perlen und Provenienz

- `MY_AI_PROJECTS/2026-08 MAIL_ORGANIZER/VERSION_260923/config/SECURITY_POLICY.yaml`
  — maschinenlesbare erlaubte Aktionen und verbotene Fähigkeiten.
- zugehörige Schemas, `config_loader.py`, `thunderbird_executor.py` und
  Contract-Tests — Durchsetzung über mehrere Ebenen statt nur Dokumentation.
- `config/WHITELIST.yaml` — Routingreferenz ausdrücklich ohne
  Sicherheitsfreigabe.
- `tests/test_gateway_finance.py` — fall-, Request-, Response- und
  Hash-Bindung bei Finanzübergaben.
- `OPENAI/SYSTEM/SPECS/HOOK_CAPTURE.md` und `SYSTEM/HOOKS/README.md` — reale
  Aktivierung erst über Plugin, Hook-Konfiguration, Marker, Lock und Runtime.
