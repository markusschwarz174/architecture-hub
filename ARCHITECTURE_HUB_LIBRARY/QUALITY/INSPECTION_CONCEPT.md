# INSPECTION_CONCEPT

## Zweck

INSPECTION behandelt den Fall, dass ein System nicht erwartungsgemäss funktioniert. QUALITY besitzt die Fallverantwortung vom ersten Befund bis zur bestätigten Schliessung; DEVELOPMENT besitzt Analyse und Bau der Reparatur.

## Aktivierung

| Modus | Auslöser | Regel |
|---|---|---|
| `MANUAL` | HUMAN oder Drittperson meldet einen Fehler | SENTINEL eröffnet oder ergänzt den Fall und bindet die Meldung als Evidenz. |
| `EVENT_DRIVEN` | Output, Zustand oder Übergabe weicht vom SOLL ab | Der betroffene Prozess ruft SENTINEL mit Prüfling, SOLL und beobachteter Abweichung auf. |
| `CONTINUOUS` | SENTINEL startet gekoppelt mit dem überwachten System | Nur bei expliziter Konfiguration; Intervall, Scope und Kostenlimit gehören zur Systemkonfiguration. |

Ohne explizite Konfiguration gilt `MANUAL + EVENT_DRIVEN`. Dauerüberwachung ist eine verfügbare Betriebsart, aber kein pauschaler Standard.

## Präventive INSPECTOR-Prüfung

Der INSPECTOR kann vor einem Incident oder im Rahmen einer vereinbarten
periodischen Prüfung nach strukturellen Warnzeichen suchen. Er prüft
read-only, ob eine Datei zu viele voneinander unabhängige Regeln bündelt,
mehrere Funktionsbereiche vermischt, eine zweite Authority erzeugt, veraltete
Referenzen enthält oder Regeln am falschen Ort trägt. `FILESYS` liefert dafür
Inventar-, Pfad- und Strukturbeobachtungen; die semantische Entscheidung
bleibt bei QUALITY, DEVELOPMENT und HUMAN.

Der INSPECTOR liefert Befund, Quelle, Auswirkung und vorgeschlagenen
Zielbereich. Er repariert oder verschiebt nichts still. Bestätigter
Änderungsbedarf geht als begrenzter Auftrag an DEVELOPMENT und danach zurück
an QUALITY zur unabhängigen Prüfung. So sollen überladene Architekturdateien
und unkontrollierte Regelsammlungen früh erkannt werden.

## Verantwortungsfluss

```text
QUALITY  DETECT → TRIAGE → STABILIZE (falls nötig) → HANDOVER
DEVELOPMENT                     TAKEOVER → ANALYSE → BUILD → RETURN FOR VALIDATION
QUALITY                                                         VALIDATE → CLOSE oder RETURN
```

QUALITY darf den Fall nicht an DEVELOPMENT „wegwerfen“. Bis zum bestätigten `TAKEOVER` bleibt die Aktionsverantwortung bei QUALITY; die Fallverantwortung bleibt während des gesamten Ablaufs bei QUALITY.

## Phasen

### 1. DETECT

- Beobachtung vom Schluss trennen.
- Prüfling, SOLL, Zeitpunkt, Quelle und erste Evidenz binden.
- In `QUALITY_LOG.jsonl` protokollieren.
- Bei echtem Arbeitsbedarf einen Eintrag in `ACTIVE_INCIDENTS.json` eröffnen.

### 2. TRIAGE

- Auswirkung, Reproduzierbarkeit und betroffene Grenze bestimmen.
- Fehlerbild gegen `LIST_OF_IMPROVEMENTS.json` abgleichen.
- Ein Treffer ist ein Diagnosehinweis, kein Beweis und keine automatische Reparaturfreigabe.
- Unzureichende Evidenz führt zu `HOLD` oder `INCONCLUSIVE`, nicht zu einer erfundenen Ursache.

### 3. STABILIZE

QUALITY darf Feuerwehr spielen: einen Prozess pausieren, einen betroffenen Output quarantänisieren, einen freigegebenen Retry auslösen, auf einen geprüften Checkpoint zurückrollen oder einen sicheren Betriebspfad sperren. Diese Aktionen müssen vorab erlaubt, reversibel und protokolliert sein. Freie Code-, Prompt- oder Architekturänderungen sind DEVELOPMENT-Arbeit.

### 4. HANDOVER / TAKEOVER

Die Übergabe ist eine Quittung, keine Nachricht ohne Empfangsnachweis:

1. QUALITY setzt `HANDOVER_OFFERED` und übergibt Incident-ID, Reproduktion, Evidenz, Auswirkung, bereits ausgeführte Stabilisierung und Abnahmekriterien.
2. DEVELOPMENT bestätigt dieselbe Incident-ID mit `TAKEOVER_ACCEPTED` oder weist die Übergabe begründet zurück.
3. Erst die Bestätigung wechselt den `action_owner` zu `DEVELOPMENT`.
4. DEVELOPMENT referenziert Reparatur und eigene Tests und setzt `RETURNED_FOR_VALIDATION`.
5. Nur QUALITY darf nach unabhängiger Revalidierung `CLOSED` setzen; andernfalls folgt `RETURNED_TO_DEVELOPMENT`.

## Datenhaltung

| Datei | Aufgabe | Schreibregel |
|---|---|---|
| `QUALITY_LOG.jsonl` | append-only Evidenzjournal aller guten und schlechten Prüfereignisse | Korrekturen sind neue Ereignisse; alte Zeilen werden nicht überschrieben. |
| `ACTIVE_INCIDENTS.json` | aktueller, kompakter Arbeitszustand offener Fälle | Projektion bis zu einer angegebenen Log-Sequenz; atomar ersetzen, nie als zweite Historie behandeln. |
| `LIST_OF_IMPROVEMENTS.json` | bestätigtes, wiederverwendbares Wissen nach Reparatur und erfolgreicher Revalidierung | kein Backlog und keine Sammlung unbestätigter Vermutungen. |
| `GOLDEN_EXAMPLES.json` | versionierte, HUMAN-bestätigte Referenzfälle je Gate | Beispiele kalibrieren ein Urteil, ersetzen aber weder SOLL noch Kontextprüfung. |
| `HUMAN_PATTERNS.json` | abgeleitete HUMAN-Präferenzen und Entscheidungsmuster | Kandidaten, Gegenbelege und Geltungsbereich bleiben sichtbar; keine stille Aktivierung. |
| externe Evidenz | grosse Reports, Snapshots und Rohdaten | stabile Referenz und Hash im Journal. |

IDs verbinden alle Dateien. Für dieselbe Tatsache gibt es nicht mehrere konkurrierende Texte.

## Schliessen und Lernen

Ein Incident wird nur geschlossen, wenn der ursprüngliche Fehlerfall und das definierte SOLL erfolgreich geprüft wurden. Erst danach darf ein wiederverwendbarer Eintrag in `LIST_OF_IMPROVEMENTS.json` entstehen. Der Eintrag beschreibt Fehler-Signatur, bestätigte Ursache, Reparatur, Geltungsbereich, Gegenanzeigen und Validierungsreferenzen. Allgemeine Entwicklungs-Lessons und Release-Historie verbleiben bei DEVELOPMENT.

## Konsistenzregel

Für jede Datendatei gibt es genau einen kontrollierten Writer. JSON-Dokumente werden in einer temporären Datei erzeugt, gegen `QUALITY_DATA.schema.json` geprüft und atomar ersetzt. JSONL-Ereignisse werden unter Schreibsperre angehängt. Fehlt diese Kontrolle, wird nicht geschrieben und der Fall geht auf `HOLD`.

Jede Journalzeile trägt eine eindeutige, monoton steigende `sequence`. Schemaänderungen erhalten eine neue `schema_version` und einen ausdrücklich beschriebenen Migrationspfad; bestehende Daten werden nicht still umgedeutet.
