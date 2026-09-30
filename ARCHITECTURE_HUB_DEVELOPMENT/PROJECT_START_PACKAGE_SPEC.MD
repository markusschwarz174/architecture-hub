---
document_id: ah-project-start-package-spec
title: PROJECT START PACKAGE — Vertrag
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-10-01
authority: HUMAN_PILOT_REQUIRED
---

# PROJECT START PACKAGE

## Name

Der kanonische Arbeitsname lautet `PROJECT_START_PACKAGE`, auf Deutsch
`Projekt-Startpaket`. Der Begriff ersetzt das unspezifische Wort `SET`.

## Zweck

Ein PROJECT_START_PACKAGE ist ein projektbezogener, manifestgebundener und
uebergabefaehiger Startbestand. Es enthaelt genau die fuer das konkrete
Vorhaben ausgewaehlten Library-Bausteine sowie den naechsten Agenten.

Es ist weder eine Kopie der gesamten Library noch bereits das fertige Projekt.

## Erzeugungsweg

```text
HUMAN
  -> ADVISOR-Interview
  -> PROJECT_PROFILE.json
  -> HUB-ARCHITEKT: A-/D-Stufe und Bausteinauswahl
  -> ASSEMBLY_MANIFEST.json
  -> PROJECT_START_PACKAGE_BUILDER.py
  -> Stringenz- und Diff-Pruefung
  -> HANDOVER_OFFERED
  -> externer PROJECT-ARCHITEKT
  -> TAKEOVER_ACCEPTED oder TAKEOVER_REJECTED
```

## Mindestinhalt

```text
[PROJECT]_START_PACKAGE/
├── PROJECT_PROFILE.json
├── ASSEMBLY_MANIFEST.json
├── PACKAGE_BUILD_REPORT.json
├── HANDOVER.md
├── STARTPROMPT_PROJECT.md
├── AGENT_PROJECT_ARCHITEKT.md
├── MISSION.md
├── PROJECT_CONCEPT.md oder PROJECT_ARCHITECTURE.md
├── PROJECT_BUILD_RECORD.md
├── DEVELOPMENT_LOG.json
├── PINWALL.md
└── ausgewaehlte CONTRACT-, WORKFLOW-, TOOLING- und QUALITY-Bausteine
```

Eine README ist nicht Bestandteil des Vertrags. Einstieg und Uebergabe leben
in `STARTPROMPT_PROJECT.md` und `HANDOVER.md`.

## Verantwortungen

### ADVISOR

Ermittelt das bestaetigte Projektprofil. Keine Bausteinauswahl.

### HUB-ARCHITEKT

Bestimmt A1–A4 und D1–D4, waehlt Bausteine, begruendet Ein- und Ausschluesse
und erstellt das Manifest. HUMAN bestaetigt die wirksame Auswahl.

### PACKAGE BUILDER

Kopiert ausschliesslich manifestierte Quellen, prueft Pfadgrenzen, ersetzt
explizit angegebene Platzhalter und schreibt einen Build-Report. Er trifft
keine fachlichen Entscheide.

### PACKAGE VALIDATOR

Prueft Stringenz, Vollstaendigkeit, Hashes, Referenzen und Profile-Coverage in
einer unabhaengigen Session. Er repariert nicht.

### PROJECT-ARCHITEKT

Fuehrt das Takeover durch und begleitet danach den HUMAN durch Planung und
Entwicklung. Er veraendert die Hub-Library nicht.

## Build-Gates

1. `PROFILE_CONFIRMED`: Profil schema-valide und HUMAN-bestaetigt.
2. `SELECTION_CONFIRMED`: Auswahl und Ausschluesse bestaetigt.
3. `MANIFEST_BUILDABLE`: Quellen und Zielpfade eindeutig.
4. `PACKAGE_BUILT`: Builder ohne fehlende Pflichtquelle abgeschlossen.
5. `STRINGENCY_PASS`: Inhalte und Pfade liegen im richtigen Bereich.
6. `DIFF_PASS`: Profil, Manifest und Filesystem sind vollstaendig verbunden.
7. `READY_FOR_HANDOVER`: keine unakzeptierte materielle Luecke.

## Abnahme

Das Package ist brauchbar, wenn ein PROJECT-ARCHITEKT in einer neuen Session
nur mit diesem Ordner:

- Auftrag, Scope und Authority versteht;
- die Auswahl nachvollziehen kann;
- fehlende oder veraenderte Dateien erkennt;
- das Takeover korrekt akzeptiert oder ablehnt;
- den ersten Entwicklungsschritt eindeutig benennen kann.
