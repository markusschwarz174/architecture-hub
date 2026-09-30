# VALIDATION_CONCEPT

## Zweck

QUALITY prüft planmässige Outputs gegen ein ausdrücklich benanntes SOLL. Das Konzept gilt für einzelne Artefakte sowie für Outputs eines mehrstufigen Workflows. Es beschreibt die Prüfung, nicht die Reparatur.

## Grenze

- QUALITY prüft, protokolliert, meldet und fordert bei `FAIL` den vorgesehenen Retry an.
- QUALITY verändert den geprüften Output nicht, ausser eine vorab freigegebene, reversible Stabilisierung ist Teil des Prüfauftrags.
- DEVELOPMENT analysiert und baut Reparaturen.
- Ein Output ist nicht bestanden, nur weil er plausibel wirkt. Das Urteil braucht prüfbare Evidenz.

## Vier modulare Prüfpositionen

| Modul | Prüffrage | Werkzeug | Ergebnis |
|---|---|---|---|
| `EXPERT_REVIEW` | Ist der Output fachlich richtig, vollständig und widerspruchsfrei? | Unabhängige Zweitbeurteilung; zuerst eigenes Urteil, dann Vergleich | Befunde mit Kriterien- und Evidenzbezug |
| `SIMULATION_TEST` | Würde der geplante Ablauf funktionieren, bevor er real ausgeführt wird? | Dry-run, Sandbox oder kontrollierte Simulation | beobachtete Zustände, Folgefehler und Abbruchpunkte |
| `DIFF_CHECK` | Was hat sich gegenüber dem gebundenen Ausgangszustand tatsächlich geändert? | deterministischer Snapshot-/Hash-/Strukturvergleich | maschinenlesbarer Diff; keine Plausibilitätsbehauptung |
| `FINAL_TEST` | Erfüllt das reale Ergebnis das SOLL und den ursprünglichen Fehlerfall? | Test am fertig erzeugten Output/Systemzustand | bestätigtes Endurteil |

Die Module werden passend zum Risiko aufgerufen. Nicht jeder Fall braucht alle vier. Weggelassene Module und der Grund dafür werden im Report genannt.

## Zwei-Hände-Prinzip

Das Zwei-Hände-Prinzip beginnt bei `LV2`. `LV1` ist bewusst eine Ein-LLM-Prüfung. Bei `LV2` und `LV3` sind Produzent und Validator nicht dieselbe Instanz. `EXPERT_REVIEW` wird dort ohne Vorprägung durch die Begründung des Produzenten begonnen. Kann die verlangte Unabhängigkeit nicht hergestellt werden, lautet das Ergebnis nicht `PASS`, sondern `INCONCLUSIVE` oder `HOLD`.

## Validierungsstufen

Die Stufe beschreibt die nachweisbare Unabhängigkeit der Prüfung, nicht die absolute Sicherheit des Ergebnisses.

| Level | Prüferaufbau | Typischer Einsatz | Ergänzungen |
|---|---|---|---|
| `LV1` | `SINGLE LLM` | einfache oder risikoarme Prüfung durch ein LLM | `+D`, `+G`, `+H`, `+MODEL`, `+WEB`, `+DATA` |
| `LV2` | `PARTNER LLM` | unabhängige Zweitprüfung durch ein weiteres LLM | `+D`, `+G`, `+H`, `+WEB`, `+DATA` |
| `LV3` | `MULTI LLM` | wichtige oder strittige Prüfung durch mehrere LLMs, bei Bedarf mit JUDGE | `+D`, `+G`, `+H`, `+WEB`, `+DATA` |

| Zusatz | Bedeutung |
|---|---|
| `+D` | deterministische Tests, Schema, Hash, Diff oder realer Wirkungsbeleg |
| `+G` | Prüfung gegen freigegebene Golden Examples im passenden Kontext |
| `+H` | HUMAN bestätigt das Ergebnis oder trifft den reservierten Entscheid |
| `+MODEL` | zusätzlicher Gegencheck durch ein anderes Modell; als vollständige unabhängige Zweitprüfung mindestens `LV2` |
| `+WEB` | Validierung durch aktuelle Internetrecherche mit Quellen- und Zeitbezug |
| `+DATA` | Validierung gegen einen bezeichneten Datenbestand über Retrieval/RAG |

Eine Validation benötigt keine Kopie des gesamten ursprünglichen Kontextfensters. Übergeben wird ein begrenztes Validation Package aus Prüfling, SOLL, Kriterien und Evidenz. Ein Fork oder Session-Export ist nur nötig, wenn ausnahmsweise der vollständige Entstehungskontext selbst Prüfgegenstand ist.

Bei `+WEB` werden Suchfrage, verwendete Quellen und Abrufzeit gebunden. Bei `+DATA` werden Datenbestand beziehungsweise Indexversion, Retrieval-Frage und verwendete Fundstellen gebunden. Ein fehlender Treffer beweist weder im Web noch im RAG die Nichtexistenz einer Information.

Jedes Gate legt in `VALIDATION_GATES.json` nur Mindestlevel und gewünschte Zusätze fest. Protokollierung ist Teil des Reportvertrags. Konfliktrouting und Eskalation liegen bei SENTINEL beziehungsweise INSPECTION und belasten diese Tabelle nicht.

## Datenfluss

```text
SOLL + gebundener Input/Snapshot
        ↓
Auswahl der Prüfmodule
        ↓
Evidenz je Modul
        ↓
ein VALIDATION_REPORT
        ↓
QUALITY_LOG.jsonl
        ↓
PASS → regulär beendet
FAIL → erlaubter RETRY oder INCIDENT-Eröffnung
HOLD / BORDERLINE / INCONCLUSIVE → HUMAN oder zuständige Stelle
```

## Reportvertrag

Jeder Lauf erzeugt genau einen Report gemäss `QUALITY_DATA.schema.json#/$defs/validation_report` mit:

- gebundenem Prüfling und SOLL;
- eingesetzten und bewusst ausgelassenen Modulen;
- Befunden und Evidenzreferenzen;
- Urteil `PASS`, `FAIL`, `HOLD`, `BORDERLINE` oder `INCONCLUSIVE`;
- eindeutigem nächsten Schritt.
- Gate-ID, gewählter LV-Stufe, verwendeten Zusätzen und der vollständigen Validierungskette.

Der Report wird als Ereignis oder als referenziertes Artefakt in `QUALITY_LOG.jsonl` festgehalten. Grosse Rohbelege bleiben ausserhalb des Logs und werden über stabile Referenz plus Hash gebunden.

Ein generischer Dateityp `VALIDATION_REPORT.md` ist deshalb bewusst nicht vorgesehen: kleine Reports sind strukturierte Reportobjekte, umfangreiche oder HUMAN-lesbare Prüfungen verwenden `REVIEW_<ID>.md` beziehungsweise `AUDIT_<ID>.md` und werden aus dem Journal referenziert.

Alle nachgelagerten Validatoren arbeiten auf derselben gebundenen Evidenzoberfläche. Ein Validator darf nicht still einen neuen Snapshot, ein anders gerendertes Dokument oder eine eigene Diff-Logik als vermeintlich gleichen Prüfling verwenden. Wird die Evidenz erneuert, beginnt ein neuer, klar referenzierter Prüflauf.

## Retry-Regel

`FAIL` bedeutet nicht unbegrenztes Wiederholen. Ein automatischer Retry ist nur zulässig, wenn eine Retry-Policy vorhanden, der Schritt idempotent oder sicher reversibel und die Ursache als transient klassifiziert ist. Fehlt eine dieser Bedingungen oder scheitert der freigegebene Retry, wechselt der Fall in `INSPECTION_CONCEPT`.

## Tool-Schnittstellen

Die fachlichen Positionen brauchen ausführbare Hände. Implementierungen dürfen wechseln, müssen aber dieselben Verträge erfüllen:

1. `observe` — read-only Zustand und Evidenz erfassen;
2. `preflight` — Voraussetzungen und Schemas prüfen, fehlende Voraussetzung als `HOLD` statt als Scheinerfolg melden;
3. `simulate` — geplante Wirkung ohne Produktivmutation prüfen;
4. `diff` — gebundene Snapshots deterministisch vergleichen;
5. `final_test` — den realen Endzustand gegen SOLL und Fehlerfall testen;
6. `write_report` — genau einen schema-validen Report erzeugen;
7. `append_event` — Reportereignis kontrolliert in das Journal schreiben.

Die konkreten Adapter sind systemabhängig und in diesem Bibliotheksstand bewusst noch nicht implementiert.

Security ist kein eigener QUALITY-Dateityp. Wo Sicherheit relevant ist, erscheint sie als ausdrückliches SOLL-Kriterium im Report; ein unabhängiger Security-Review kann als spezialisierter `EXPERT_REVIEW` eingebunden werden.

## Golden Examples pro Gate

Ein Gate darf neben abstrakten Kriterien ein versioniertes Referenzset aus `GOLDEN_EXAMPLES.json` verwenden. Ein brauchbares Set enthält nicht nur ideale Positivbeispiele, sondern auch bestätigte `NO_GO`-, `BORDERLINE`- und Grenzfälle. Jeder Eintrag ist an eine Gate-ID, einen Kontext, ein HUMAN-Verdikt und seine Herkunft gebunden.

Golden Examples sind Kalibrierungsbelege, keine universelle Wahrheit. Ein Beispiel ausserhalb seines dokumentierten Kontexts darf keinen automatischen Entscheid auslösen. Ein Widerspruch mit einer aktuellen HUMAN-Anweisung setzt das Beispiel auf Review.

### Gewinnung

1. AI bildet aus realen Fällen 20 unterschiedliche, konkrete Szenarien für genau ein Gate.
2. `GOLDEN_EXAMPLE_INTERVIEW.html` zeigt pro Szenario Input, AI-Vorschlag und die Auswahl `GO`, `NO_GO`, `BORDERLINE` oder `HOLD` mit Kommentar.
3. Die HTML-Instanz speichert Zwischenstände lokal und exportiert einen schema-validen JSON-Beleg.
4. AI wertet Antworten, Ausnahmen und noch unbesetzte Entscheidungsklassen aus und erzeugt den nächsten 20er-Satz.
5. Erst ein bestätigter Kandidat wird in `GOLDEN_EXAMPLES.json` übernommen.

Start und Abschluss jeder Runde werden in `QUALITY_LOG.jsonl` protokolliert; HTML-Instanz und JSON-Export werden dabei über Referenz und Hash gebunden.

Zwanzig Antworten sind eine Batchgrösse, kein Qualitätsbeweis. Das Interview endet, wenn die vorab benannten Entscheidungsdimensionen durch bestätigte Positiv-, Negativ- und relevante Grenzfälle abgedeckt sind und kein erforderlicher `HOLD` offen bleibt. „AI hat genug“ ohne ausgewiesene Abdeckung ist kein Stoppkriterium.

### Anwendung im Gate

Der Validator protokolliert die verwendete Version des Referenzsets und die IDs der nächstliegenden Beispiele. Ähnlichkeit ist nur Evidenz. Das eigentliche Urteil bleibt an SOLL, Kontext und Prüfkriterien gebunden.

## HUMAN-Entscheidungsmuster

HUMAN-Entscheide und Korrekturen werden als unveränderliche Ereignisse in `QUALITY_LOG.jsonl` erfasst. `HUMAN_PATTERNS.json` enthält daraus abgeleitete Kandidaten und bestätigte Muster mit Geltungsbereich, Gegenbelegen und Evidenz-IDs.

Ein Muster darf eine aktuelle HUMAN-Anweisung, Faktenlage oder Sicherheitsregel nie überschreiben. Eine direkte HUMAN-Korrektur erzeugt sofort einen Gegenbeleg; automatische Anwendung des betroffenen Musters bleibt bis zur Klärung gesperrt. QUALITY beobachtet und bewertet die Muster. Eine Änderung am produktiven AI-Verhalten wird als Entwicklungsauftrag an DEVELOPMENT übergeben.

Für den laufenden Dialog dürfen ausschliesslich bestätigte, zum aktuellen Scope passende Muster als zusätzlicher Kontext geladen werden. Kandidaten dienen der Analyse, nicht der Steuerung. Nach dem Output wird die HUMAN-Reaktion wieder als Evidenz erfasst; so entsteht ein überprüfbarer Regelkreis statt stiller Personalisierung.
