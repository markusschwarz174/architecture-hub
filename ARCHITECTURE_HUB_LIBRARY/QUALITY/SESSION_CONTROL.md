# SESSION_CONTROL

## Zweck

SESSION_CONTROL prüft die Qualität einer laufenden HUMAN-AI-Session. Es ist kein neuer Agent, sondern ein von SENTINEL aufrufbares Prüfmodul. Es überwacht Kontextintegrität, Bias-Risiken, unbelegte Behauptungen und Reaktionen von HUMAN.

## Grenze der Messbarkeit

Kontextfenster-Auslastung darf nur als Messwert angegeben werden, wenn die Laufzeit sie tatsächlich liefert. Ohne direkten Messwert werden nur beobachtbare Proxys protokolliert: Compaction oder Zusammenfassung, wiederholte Rückfragen, verlorene Entscheide, widersprüchliche Quellen, Quellenwechsel, Wiederholungen und Abweichungen vom gebundenen Auftrag.

HUMAN-Reaktionen sind wichtige Sensoren, aber kein Wahrheitsautomat. Zustimmung kann einen Fehler übersehen; Ablehnung kann eine Präferenz statt einen Faktenfehler ausdrücken. Bias und Halluzination werden deshalb zusätzlich am AI-Output und an gebundener Evidenz geprüft.

## Checkpoints

Ein Checkpoint wird mindestens ausgelöst:

- am Start eines material verändernden Auftrags;
- nach Compaction, Summary, Handover oder neu zusammengesetztem Kontext;
- vor einer irreversiblen oder schwer rückgängig zu machenden Aktion;
- nach einer HUMAN-Korrektur, einem Widerspruch oder wiederholter Rückfrage;
- vor Abschluss oder Übergabe eines längeren Auftrags.

## Vier Prüfbereiche

### 1. Kontextintegrität

- Sind Ziel, Scope, aktueller Auftrag und Nicht-Ziele noch gebunden?
- Sind verwendete Quellen, Versionen und offene HUMAN-Entscheide sichtbar?
- Wurden geplante, ausgeführte und bestätigte Zustände getrennt?
- Gibt es Hinweise auf Kontextverlust, veraltete Erinnerung oder eine unbelegte Zusammenfassung?

### 2. Bias-Kontrolle

Geprüft werden mindestens Bestätigungs-/Sycophancy-Bias, Anchoring auf die erste Hypothese, Recency-Bias, Selection-Bias und Automation-Bias. Die Gegenprobe lautet: Welche plausible Alternative oder welche Evidenz würde das aktuelle Urteil widerlegen?

### 3. Grounding- und Halluzinationskontrolle

- Stichprobe materieller Aussagen gegen Quellen oder reale Systemzustände;
- erfundene Dateien, IDs, Toolresultate, Zitate und abgeschlossene Aktionen suchen;
- Behauptung, Schlussfolgerung und Unsicherheit trennen;
- `PASS` nur bei ausreichender Evidenz, sonst `HOLD` oder `INCONCLUSIVE`.

### 4. HUMAN-Signale

Erfasst werden Korrekturen, abgelehnte Empfehlungen, wiederholte Fragen, Scope-Rücknahmen, Hinweise auf Informationsüberlastung und ausdrücklich positive Referenzentscheide. Das Signal wird mit dem betroffenen AI-Output und dessen Quellen verbunden.

Vor einem materiellen AI-Output dürfen bestätigte, zum Scope passende Einträge aus `HUMAN_PATTERNS.json` und freigegebene Golden Examples als Referenz geladen werden. Kandidaten oder widersprochene Muster bleiben draussen. Nach dem Output wird die Reaktion erneut gebunden, damit Anpassung und Fehlentwicklung unterscheidbar bleiben.

## Output und Routing

Jeder Checkpoint folgt `QUALITY_DATA.schema.json#/$defs/session_checkpoint` und wird in `QUALITY_LOG.jsonl` protokolliert.

- `PASS`: Session kann im gebundenen Scope weiterlaufen.
- `WARN`: Risiko sichtbar; nächste Antwort muss die Gegenmassnahme zeigen.
- `HOLD`: Kontext oder Grounding reicht für den nächsten materiellen Schritt nicht.
- `INCONCLUSIVE`: Messung oder Evidenz fehlt; HUMAN oder unabhängiger Review entscheidet das weitere Vorgehen.

Ein SESSION-CONTROL-Befund verändert das produktive Verhalten nicht selbst. Er kann einen Retry, eine neue Kontext-Assembly, einen unabhängigen Review oder einen Incident auslösen.
