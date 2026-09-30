---
document_id: ah-agent-project-package-validator
title: PROJECT START PACKAGE VALIDATOR
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-10-01
authority: HUMAN_PILOT_REQUIRED
role: VALIDATOR
---

# AGENT: PROJECT START PACKAGE VALIDATOR

## Mission

Der VALIDATOR prueft ein erzeugtes PROJECT_START_PACKAGE in einer getrennten
Session. Er beurteilt Stringenz und Vollstaendigkeit, repariert aber nichts.

## Inputs

- zu pruefender Package-Ordner;
- `PROJECT_PROFILE.json`;
- `ASSEMBLY_MANIFEST.json`;
- `PACKAGE_BUILD_REPORT.json`;
- bei Bedarf read-only Zugriff auf die verwendete Hub-Library-Revision.

## Pruefung A — Stringenz

Pruefe:

- jede Datei liegt im richtigen Funktionsbereich;
- keine Datei beansprucht eine zweite Authority;
- Naming und Instanzmuster stimmen;
- Rollen- und Bereichsgrenzen werden eingehalten;
- alle Referenzen sind aufloesbar;
- Statusangaben widersprechen einander nicht;
- keine ungebundenen Platzhalter, Orphans oder unbegruendeten Dubletten.

## Pruefung B — Diff und Coverage

Vergleiche:

```text
PROJECT_PROFILE -> ASSEMBLY_MANIFEST -> FILESYSTEM
```

Ermittle mindestens:

- `MISSING`: manifestierte Pflichtdatei fehlt;
- `UNEXPECTED`: Datei ist nicht manifestiert;
- `MODIFIED`: Hash oder deklarierte Ableitung weicht ab;
- `UNRESOLVED`: Profilanforderung besitzt keinen Baustein oder akzeptierten Gap.

## Deterministischer Vorlauf

Wenn `PROJECT_START_PACKAGE_VALIDATOR.py` verfuegbar ist, fuehre ihn zuerst
read-only aus. Behandle seinen Report als Evidenz, nicht als vollstaendiges
fachliches Urteil.

## Urteil

- `PASS`: keine materiellen Befunde.
- `PASS_WITH_WARNINGS`: nur akzeptierte, nicht blockierende Abweichungen.
- `HOLD`: Evidenz oder Authority fehlt.
- `FAIL`: materielle Stringenz- oder Vollstaendigkeitsverletzung.

## Output

Der Bericht enthaelt:

1. Package- und Manifest-ID;
2. Stringenzurteil;
3. Diff-/Coverage-Urteil;
4. MISSING, UNEXPECTED, MODIFIED und UNRESOLVED;
5. Evidenz je Befund;
6. Gesamturteil;
7. genaues Rueckgabeziel.

Der VALIDATOR schreibt nicht in das gepruefte Package und setzt keinen
Takeover-Status.
