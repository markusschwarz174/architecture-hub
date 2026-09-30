---
document_id: ah-development-template-communication-concept
title: COMMUNICATION_CONCEPT — Library-Vorlage
status: TEMPLATE
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: DEVELOPMENT
instance_pattern: "[PROJECT]_COMMUNICATION_CONCEPT.md"
tags: [development, communication, postbox, decision_page, multi_model]
---

# [PROJECT] — COMMUNICATION CONCEPT

## Funktion

Das COMMUNICATION_CONCEPT beschreibt, wer mit wem, über welchen Kanal, in welchem Format, zu welchem Zeitpunkt und mit welcher Bestätigung kommuniziert. Es umfasst HUMAN–AI-, Agenten- und LLM/Provider-Kommunikation. Operative HO/TO-Artefakte bleiben in WORKFLOW/TOOLING.

## Begriffsskelett

| Kapitel | Funktion | Status |
|---|---|---|
| Kommunikationsakteure | Rollen, Autoritäten und Eskalation | Pflicht |
| Kommunikationsmatrix | Sender, Empfänger, Anlass, Vertrag und ACK | Pflicht |
| POSTBOX | asynchrones Agentenmuster | Pflicht ab D3, wenn eingesetzt |
| DECISION PAGE | HUMAN-Interface, Persistenz und Übergabe | Pflicht ab D4, wenn eingesetzt |
| Unabhängige Provider-Prüfung | sichtbare Review-/Repair-Pipeline | Pflicht ab D4, wenn eingesetzt |
| Wiederaufnahme und Fehlerfälle | persistenter Zustand und Recovery | Pflicht |
| HUMAN-Gates | nicht automatisierbare Entscheidungen | Pflicht |
| Abgrenzung | Trennung von Workflow, Tooling und Contract | Pflicht |

## 1. Kommunikationsakteure

| Akteur | Verantwortung | Darf entscheiden | Muss eskalieren |
|---|---|---|---|
| HUMAN | `[RESPONSIBILITY]` | `[DECISIONS]` | `[CONDITIONS]` |
| ARCHITEKT | Verbindung zum HUMAN, Agentenauswahl, kleine Erstkontrolle, Bereichsverbindung | `[LIMITED_DECISIONS]` | `[HUMAN_GATES]` |
| `[AGENT/PROVIDER]` | `[RESPONSIBILITY]` | `[DECISIONS]` | `[CONDITIONS]` |

## 2. Kommunikationsmatrix

| Von | An | Anlass | Kanal/Muster | Payload/Vertrag | Empfangsnachweis | Timeout/Eskalation |
|---|---|---|---|---|---|---|
| `[SENDER]` | `[RECIPIENT]` | `[TRIGGER]` | `[POSTBOX/API/UI]` | `[SCHEMA/SPEC]` | `[ACK]` | `[RULE]` |

## 3. POSTBOX ab D3

Jeder beteiligte Agent kann eine adressierte Inbox besitzen. Nachrichten werden als strukturierte Artefakte abgelegt und im nächsten Turn des Empfängers verarbeitet.

Mindestfelder einer Nachricht:

- `message_id`, `created_at`, `sender`, `recipient`;
- `message_type`, `subject`, `payload_ref` oder eingebetteter Payload;
- `reply_to`, `requires_ack`, `status`;
- optional `expires_at`, `correlation_id`, `contract_ref`.

Zustände: `CREATED → DELIVERED → READ → ACCEPTED|REJECTED|NEEDS_CLARIFICATION → CLOSED`.

Die POSTBOX ist Transport und Nachweis, nicht die Autorität des transportierten Inhalts. Empfang, Annahme und fachliche Zustimmung sind getrennte Ereignisse.

## 4. Webbasierte DECISION PAGE

Die Decision Page ist ein HUMAN-Interface, das einen komplizierten Entscheidungsraum verständlich und bedienbar macht. Sie ist weder die Entscheidung noch der Vertrag. Sie erzeugt oder bestätigt ein strukturiertes JSON, das anschließend zum autoritativen Entscheidungsartefakt werden kann.

### Betriebsart A — expliziter Export

1. Seite lädt einen versionierten Input.
2. HUMAN beantwortet Fragen und erfasst Annotationen.
3. Browser speichert Zwischenstände lokal.
4. HUMAN exportiert JSON und übergibt es bewusst an das System.
5. Das System validiert Schema, Herkunft und Input-Version und bestätigt den Import.

### Betriebsart B — automatische Übermittlung

1. Die Seite authentifiziert HUMAN und Zielprojekt.
2. Änderungen werden als versionierte Entwürfe serverseitig gespeichert.
3. HUMAN führt einen expliziten Submit aus.
4. Das System validiert, quittiert und schreibt eine unveränderliche Empfangs-ID.
5. Erst ein erfolgreicher, sichtbarer ACK macht die Übergabe vollständig.

### Verlustschutz

- Autosave nach jeder Änderung, zusätzlich manueller Save;
- lokaler Entwurf plus optionaler serverseitiger Entwurf;
- sichtbarer Status `UNSAVED`, `SAVED_LOCAL`, `SAVED_SERVER`, `SUBMITTED`, `ACKNOWLEDGED`;
- versionierter Input-Fingerprint und Schema-Version;
- Export jederzeit, auch vor Abschluss;
- Wiederaufnahme über stabile Session-/Decision-ID;
- kein Leeren des Entwurfs vor bestätigtem Import;
- Warnung bei veralteter Input-Version oder konkurrierender Bearbeitung.

Die belegte frühere REVISION-Variante war eine read-only Projektion des Ausgangstextes: Markierter Text öffnete Annotationseingaben, ohne den Ursprungstext live zu verändern. Möglich bleibt, dass Korrekturen parallel direkt in DOCX vorgenommen wurden. Beide Wege müssen im Projekt explizit unterschieden werden.

## 5. Unabhängige Provider-Prüfung ab D4

```text
PRODUCE
→ INDEPENDENT REVIEW
→ GATE
→ TARGETED REPAIR
→ FINALIZE
```

- Der Produzent liefert ein strukturiertes Artefakt mit Version/Hash.
- Ein unabhängiger Provider erhält nur den definierten Prüfinput und liefert strukturierte Findings.
- Ein Gate entscheidet, welche Findings bestätigt werden; bei Bedarf entscheidet HUMAN.
- Der ursprüngliche Produzent erhält nur bestätigte Findings und repariert gezielt.
- Finalisierung prüft Schema, Hash, offene Findings und Nachweise.

Freier, versteckter Agentenchat ist nicht erforderlich. Jeder Pass ist sichtbar, austauschbar, einzeln prüfbar und wiederaufnehmbar.

## 6. Wiederaufnahme und Fehlerfälle

| Prozess | Persistenter Zustand | Wiederaufnahmeschlüssel | Fehlerbehandlung |
|---|---|---|---|
| POSTBOX | Nachricht + Status + ACK | `message_id` | Retry ohne Doppelverarbeitung |
| DECISION PAGE | Entwurf + Input-Fingerprint | `decision_id` | Recovery/Export vor Reset |
| Provider-Pipeline | Pass-Outputs + Hashes + Findings | `run_id` | Wiederholung nur des fehlgeschlagenen Passes |
| HUB-Lernen | Kandidat + Empfangsstatus | `candidate_id` | Deduplizierung und idempotenter ACK |

## 7. HUMAN-Gates

`[Welche Entscheidungen dürfen nicht automatisch weitergegeben oder umgesetzt werden?]`

## 8. Abgrenzung

Dieses Dokument plant die Kommunikationsarchitektur. Konkrete Übergabekarten, operative Queues, Scheduler und Provider-SDKs gehören in WORKFLOW/TOOLING beziehungsweise CONTRACT.
