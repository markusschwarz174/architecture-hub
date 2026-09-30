---
document_id: ah-contract-lifecycle
title: LIFECYCLE — Lebensweg erzeugter Outputs
status: DRAFT
version: 0.1.0
created_at: 2026-09-30
authority: HUMAN_CONFIRMED_FILE_TYPE
functional_area: CONTRACT
---

# LIFECYCLE

## Zweck

`LIFECYCLE` hält fest, welches Tool welchen Output erzeugt und was mit diesem
Output während und nach der Ausführung geschieht. Der Vertrag endet nicht bei
`CREATE`, sondern erst bei einem belegten Endzustand.

`RESPONSIBILITY` und `OWNER` des erzeugenden Tools werden in `TOOLING`
festgelegt. Diese Datei referenziert das Tool und regelt den Lebensweg seiner
Outputs; sie erzeugt keine zweite Owner-Authority.

## Anwendungsregel

Der Dateityp ist verfügbar, aber nicht als eigene Datei für jedes kleine Tool
Pflicht. Ein eigener Lifecycle-Vertrag ist sinnvoll, wenn Outputs persistent,
zahlreich, sicherheitsrelevant, wiederaufnehmbar oder über mehrere Orte und
Zustände verteilt sind. Ein trivialer Lifecycle darf direkt im Toolvertrag
stehen und auf dieses Skelett verweisen.

## Begriffsskelett pro Output-Familie

| Begriff | Funktion | Status |
|---|---|---|
| `LIFECYCLE_ID` | stabile Kennung des Lebenszyklusvertrags | Pflicht |
| `AUTHORITY` | Quelle und Konfliktvorrang für Aufbewahrung und Abschlussaktionen | Pflicht |
| `TOOL_REFERENCE` | erzeugendes Tool und dessen Authority in `TOOLING` | Pflicht |
| `OUTPUT` | Output-Typ, Format und Identität | Pflicht |
| `CREATE_TRIGGER` | auslösendes Ereignis | Pflicht |
| `FIRST_WRITE_TARGET` | korrekter Zielort beim ersten Schreiben | Pflicht |
| `CLASS` | `CANONICAL`, `WORKING`, `EVIDENCE` oder `TEMPORARY` | Pflicht |
| `ACTIVE_USE` | zulässige Verwendung und Konsumenten | falls vorhanden |
| `SUCCESS_STATE` | Zustand nach erfolgreicher Verwendung | Pflicht |
| `FAILURE_STATE` | Verhalten bei Fehler oder Abbruch | Pflicht |
| `SUPERSEDED_STATE` | Verhalten nach Ablösung durch einen Nachfolger | falls versioniert |
| `RETENTION` | Dauer oder sachliche Aufbewahrungsbedingung | Pflicht |
| `TERMINAL_ACTION` | `KEEP`, `MOVE`, `ARCHIVE` oder `DELETE` | Pflicht |
| `ACTION_TRIGGER` | Ereignis, das die Abschlussaktion auslöst | Pflicht |
| `PERMISSION_REFERENCE` | Berechtigung für Verschieben, Archivieren oder Löschen | bei Seiteneffekten |
| `RECOVERY` | Wiederaufnahme und geschützte Evidenz | falls Wiederaufnahme möglich ist |
| `ORPHAN_HANDLING` | Erkennung und Behandlung verwaister Outputs | Pflicht bei Serienerzeugung |
| `AUDIT_EVIDENCE` | Beleg der ausgeführten Abschlussaktion | falls protokollierungspflichtig |

## Grundregeln

1. Der korrekte Zielort wird vor der Erzeugung bestimmt; ein Projekt-Root ist
   kein temporärer Ablagekorb.
2. Das erzeugende Tool beseitigt seine eigenen temporären und abgelösten
   Outputs entsprechend diesem Vertrag.
3. Bei Fehlern bleiben die für Recovery notwendigen Inputs und Belege
   erhalten.
4. `DELETE` braucht eine ausdrückliche Permission und ein eindeutig belegtes
   Ziel. Ohne Löschfreigabe gilt `MOVE` oder `ARCHIVE`, sofern vorgesehen.
5. Ein fremdes Aufräumwerkzeug übernimmt Outputs nur über eine explizite
   Übergabe in `TOOLING`; es erhält kein pauschales Janitor-Recht.
6. Verwaiste Outputs werden nicht anhand blosser Vermutung gelöscht.

## Abgrenzung

- `TOOLING` bestimmt Tool, Responsibility und Owner.
- `WORKFLOW` bestimmt Reihenfolge, Übergänge und Wiederaufnahme des Ablaufs.
- `PERMISSION` bestimmt, ob die Abschlussaktion ausgeführt werden darf.
- `QUALITY` prüft, ob der Lebenszyklus eingehalten wurde.
- `LIFECYCLE` bleibt die führende Quelle für den Lebensweg des Outputs.

## Perlen und Provenienz

- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_PRODUCER_OWNS_ARTEFACT.md` — Producer
  bleibt bis zum Lebenszyklusende verantwortlich; korrekter Zielort beim
  ersten Schreiben; Cleanup-Tail und Recovery-Regel.
- `FIELD_NOTES_DRAFT/0_C_CONVENTION/C_CONSTITUTION.md` — nur notwendige
  Artefakte erzeugen und nach Verwendung über Löschen oder Archivieren
  entscheiden.
- `FIELD_NOTES_DRAFT/0_MISSION_CONTROL/PACKAGES/PACKAGE_CORE.md` — Output,
  Rückgabe und Speicherort als Teil des Pass-Vertrags.
- `OPENAI/SYSTEM/CONSTRUCTION/JOBS/260929_quellen-kontrollcheck/PERLENKATALOG.md`
  — Run-Eigentum temporärer Artefakte, isolierte Temp-Orte und Rückführung nur
  verifizierter Outputs.
