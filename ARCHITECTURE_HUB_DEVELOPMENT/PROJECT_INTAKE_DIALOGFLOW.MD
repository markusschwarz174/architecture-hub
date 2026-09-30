---
document_id: ah-project-intake-dialogflow
title: PROJECT INTAKE DIALOGFLOW
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-10-01
authority: HUMAN_PILOT_REQUIRED
---

# PROJECT INTAKE DIALOGFLOW

## Zweck

Dieser Dialogflow fuehrt einen fachlichen Laien von einer Projektidee zu einem
bestaetigten `PROJECT_PROFILE`. Er ist eine Gespraechssteuerung, keine zweite
fachliche Authority.

## Zustaende

```text
OPEN
  -> ORIENT
  -> BLOCK_1_INTENT
  -> BLOCK_2_SCOPE
  -> BLOCK_3_OPERATION
  -> BLOCK_4_CONFIRMATION
  -> PROFILE_DRAFT
  -> HUMAN_CONFIRM
  -> PROFILE_FINAL
  -> HANDOVER_TO_HUB_ARCHITEKT
```

Rueckspruenge sind nur zum betroffenen Block erlaubt. Bereits bestaetigte
Antworten werden bewahrt und bei Aenderungen sichtbar ersetzt.

## OPEN und ORIENT

Der ADVISOR erklaert in wenigen Saetzen:

- Ziel des Interviews;
- dass noch nichts gebaut wird;
- dass der HUMAN jeden tragenden Entscheid bestaetigt;
- dass jederzeit `STOP`, `ZURUECK` oder `WEISS ICH NICHT` moeglich ist.

## BLOCK 1 — Vorhaben und Nutzen

Pflichtklaerung:

1. Was soll am Ende fuer wen besser oder moeglich sein?
2. Welches konkrete Problem soll geloest werden?
3. Woran erkennt der HUMAN ein brauchbares Ergebnis?

Ausgabe: Titel, Kurzbeschreibung, HUMAN-Nutzen, Nutzer und erste
Erfolgskriterien.

## BLOCK 2 — Scope und Material

Pflichtklaerung:

1. Welche Inputs, Dateien, Daten oder Systeme sind betroffen?
2. Welche Outputs werden erwartet?
3. Was gehoert ausdruecklich nicht zum Projekt?

Nur bei Relevanz: bestehende Implementierung, externe Dienste, Zielpfade,
Formate, Mengen und zeitliche Vorgaben.

## BLOCK 3 — Schutz und Betriebsweise

Pflichtklaerung:

1. Darf das System nur lesen, Vorschlaege erstellen oder selbst veraendern?
2. Welche Daten oder Aktionen sind empfindlich beziehungsweise riskant?
3. Wo muss der HUMAN pruefen oder entscheiden?

Nur bei Relevanz: wiederholter Start, Idempotenz, Recovery, Rollback,
Parallelitaet, Providergrenzen und Offlinebetrieb.

## BLOCK 4 — Grenzen und Bestaetigung

Der ADVISOR zeigt eine kompakte Zusammenfassung mit:

- bestaetigten Fakten;
- verwendeten Defaults;
- Annahmen;
- Risiken;
- offenen Entscheiden;
- bewussten Nicht-Zielen.

Er fragt genau:

```text
Soll dieses Profil so als Grundlage fuer die Architektur- und
Bausteinauswahl bestaetigt werden?
```

## Umgang mit Unsicherheit

- `WEISS ICH NICHT`: als offene Entscheidung oder konservativer Default.
- Widerspruch: beide Aussagen zeigen und gezielt klaeren.
- Sicherheitsrelevante Luecke: `HOLD` statt Annahme.
- Fachliche Detailfrage ohne Einfluss auf die Auswahl: fuer spaeter vormerken.

## PROFILE DRAFT

Vor der Bestaetigung wird das JSON als `DRAFT` gezeigt oder gespeichert. Der
ADVISOR nennt alle Felder, die er aus HUMAN-Aussagen abgeleitet hat.

## PROFILE FINAL

Nach HUMAN-Bestaetigung:

- Status auf `CONFIRMED` setzen;
- Zeitpunkt und Bestaetigungsart binden;
- Schema pruefen;
- keine Antworten still umformulieren;
- Uebergabe an den HUB-ARCHITEKTEN ausgeben.

## Stopbedingungen

- `COMPLETED`: Profil bestaetigt und schema-valide.
- `HOLD`: tragender Entscheid oder erlaubte Authority fehlt.
- `STOPPED_BY_HUMAN`: Zwischenstand bewahren, keine finale Uebergabe.
