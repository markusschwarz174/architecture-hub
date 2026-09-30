---
document_id: ah-development-functional-area-draft
title: Provisorischer Freeze — Funktionsbereich DEVELOPMENT
status: DRAFT
version: 0.1.0-draft
created_at: 2026-09-30T23:29:00+02:00
updated_at: 2026-09-30T23:29:00+02:00
authority: HUMAN_APPROVAL_REQUIRED
canonical: false
---

# Provisorischer Freeze — DEVELOPMENT

Dieser Entwurf dokumentiert den gemeinsam bestätigten Zwischenstand für den
Funktionsbereich `DEVELOPMENT`. Er beschreibt, wie ein System entworfen,
untersucht, geplant, gebaut, verändert und für spätere Arbeit nachvollziehbar
gemacht wird. Er ist noch kein kanonischer Library-Standard und schreibt noch
nichts in `NAMING_LOCAL.md` um.

Die zentrale Entscheidung lautet: DEVELOPMENT soll klein beginnen und nur mit
zunehmender Systemkomplexität zusätzliche Dateifamilien, Agenten und
Kommunikationsmuster aktivieren. Die Library darf mehr Bausteine anbieten, als
ein einzelnes Projekt auswählt. Ein Projekt kann beispielsweise sechs
Agentenverträge vorfinden und davon nur drei einsetzen.

## Vier Ausbaustufen

| Stufe | Zweck | Dateifamilien und Werkzeuge |
|---|---|---|
| `D1` | Einen kleinen Entwicklungsstand nachvollziehbar bauen und fortsetzen | `[PROJECT]_CONCEPT.MD` **oder** `[PROJECT]_ARCHITECTURE.MD`; `[PROJECT]_BUILD_RECORD.MD`; `DEVELOPMENT_LOG.JSON`; `PINWALL.MD` |
| `D2` | Eine abgegrenzte Änderung vor der Umsetzung planen und bei Bedarf spezifizieren | D1 plus `[CHANGE]_BAUPLAN.MD` und die Spec-Familie `[SUBJECT]_SPEC.MD`, `[SUBJECT]_SPEC.JSON` oder `[SUBJECT]_SPEC.YAML` |
| `D3` | Arbeit auf getrennte Kontexte und Agenten verteilen | D2 plus `ARCHITEKT`, `EXPLORER`, `PLANNER`, `IMPLEMENTOR`, optionale `FACHSPEZIALISTEN`, das DISCOVERY-Dateipaar und `POSTBOX` |
| `D4` | Komplexe HUMAN-AI- und providerübergreifende Zusammenarbeit planen | D3 plus `[PROJECT]_COMMUNICATION_CONCEPT.MD`, webbasierte `DECISION PAGE` und `INDEPENDENT REVIEW LOOP` |

Die Stufen sind Auswahlhilfen und keine Pflicht zur Vollausstattung. Ein
kleines Projekt soll nicht vorsorglich D4-Strukturen erhalten.

## Bestätigte Dateifamilien

### Konzept oder Architektur

`[PROJECT]_CONCEPT.MD` und `[PROJECT]_ARCHITECTURE.MD` beschreiben den
geltenden Systemstand. Sie sind ein bewusstes Entweder-oder: Das Projekt wählt
die Bezeichnung, die seiner Komplexität und seinem Leser entspricht, und führt
nicht zwei parallele Beschreibungen derselben Wahrheit.

- `CONCEPT` erklärt das System fachlich und funktional.
- `ARCHITECTURE` beschreibt zusätzlich relevante Komponenten, Grenzen,
  Abhängigkeiten und technische Struktur.
- Für WORKFLOW, TOOLING, CONTRACT und QUALITY dürfen darin die geplanten
  Zusammenhänge beschrieben oder auf zuständige Verträge verwiesen werden.

### Build Record

`[PROJECT]_BUILD_RECORD.MD` dokumentiert den tatsächlichen Bauverlauf. Er ist
kein Bauplan. Er hält fest, was gebaut, geändert, verworfen, unterbrochen,
wiederaufgenommen und nachgewiesen wurde. Damit trennt DEVELOPMENT zwei
unterschiedliche Funktionen:

- `[CHANGE]_BAUPLAN.MD`: Wie eine konkrete Änderung gebaut werden soll.
- `[PROJECT]_BUILD_RECORD.MD`: Wie der Bau tatsächlich verlief und wo er
  steht.

Der Build Record kann Checkpoints, offene Arbeiten, Abweichungen vom Bauplan,
reale Ergebnisse und Wiederaufnahmehinweise enthalten. Er ersetzt weder den
aktuellen Auftrag in der PINWALL noch den maschinenlesbaren Verlauf im
DEVELOPMENT_LOG.

### Development Log

`DEVELOPMENT_LOG.JSON` ist der strukturierte Entwicklungsverlauf. Der frühere
Name `DECISIONS_LOG.JSON` wird nicht weitergeführt, weil der Log mehr als
Entscheide enthalten darf und zum bereits vorhandenen Begriff `QUALITY_LOG`
passt.

Mögliche Ereignisse sind Entscheidungen, Planfreigaben, Baufortschritte,
Abbrüche, Wiederaufnahmen, belegte Abweichungen und `LESSON_CANDIDATE`.
Ereignistypen und endgültiges Schema sind noch als Contract zu bestätigen.

### Pinwall

`PINWALL.MD` ist das bewusst niederschwellige Gefäss für ungeordnete Gedanken,
Beobachtungen, Fragen, Ideen und HUMAN-Pendenzen. Ein Projekt führt nicht
gleichzeitig eine zweite aktuelle Wahrheit unter `BOARD.md`. Ein funktional
bereits bestehendes Board kann die Rolle der PINWALL übernehmen.

Die PINWALL ist keine Authority für Architektur, kein Entscheidungslog und
kein Agentenbriefkasten. Verarbeitete Inhalte werden in den zuständigen
Dateityp überführt oder sichtbar abgeschlossen.

### Bauplan

`[CHANGE]_BAUPLAN.MD` ist der begrenzte Plan für eine konkrete Änderung. Der
PLANNER schreibt ihn; der IMPLEMENTOR setzt ihn um. Der Bauplan beschreibt
Ziel, Ausgangslage, betroffene Artefakte, Reihenfolge, Grenzen,
Abnahmekriterien, Rückweg und bekannte Risiken. Der tatsächliche Fortschritt
gehört in den Build Record und in Laufartefakte, nicht als fortlaufende
Umschreibung in den ursprünglichen Plan.

### Spec-Familie

`[SUBJECT]_SPEC.MD`, `[SUBJECT]_SPEC.JSON` und `[SUBJECT]_SPEC.YAML` bilden
eine logische Dateifamilie. Das Format folgt dem tatsächlichen Leser:

- Markdown für HUMAN-lesbare fachliche und technische Verträge;
- JSON oder YAML für maschinenlesbare Strukturen und Konfigurationen.

Mehrere Darstellungen desselben Vertrags benötigen eine eindeutig benannte
Authority und eine dokumentierte Ableitungsrichtung. Das blosse Vorhandensein
mehrerer Formate erlaubt keine parallelen Sources of Truth.

### Communication Concept

`[PROJECT]_COMMUNICATION_CONCEPT.MD` plant bei D4 die Kommunikationswege des
Systems. Es beschreibt, wer mit wem kommuniziert, über welchen Kanal, in
welchem Format, mit welcher Authority, zu welchem Zeitpunkt und mit welchem
Beleg. Es darf POSTBOX, DECISION PAGE und INDEPENDENT REVIEW LOOP auswählen,
ohne deren Tool- oder Workflow-Verträge zu duplizieren.

## Agenten und getrennte Kontextfenster

### Architekt

Der `ARCHITEKT` ist die Verbindung zum HUMAN und zu den anderen
Funktionsbereichen. Er übersetzt den Auftrag in eine sinnvolle
Entwicklungsarchitektur, wählt die benötigten Agenten und Werkzeuge aus und
setzt sie ein. Er führt eine erste kleine Kontrolle auf Vollständigkeit,
Scope und offensichtliche Widersprüche durch. Diese Kontrolle ersetzt keine
unabhängige QUALITY-Validation.

Der ARCHITEKT entscheidet nicht anstelle des HUMAN über wertungsabhängige
Fragen. Er bereitet sie verständlich auf und sorgt dafür, dass bestätigte
Entscheide in den zuständigen Artefakten landen.

### Explorer

Der `EXPLORER` ist der forensische Bestandsanalyst von DEVELOPMENT. Er ist der
Sherlock Holmes des Systems: Er rekonstruiert den tatsächlichen Zustand,
bevor geplant, entschieden oder gebaut wird.

Er sucht nicht nur dort, wo ihm etwas gezeigt wird. Er untersucht auch Orte,
Dateitypen, Abhängigkeiten und Spuren, die gewöhnliche Agenten übersehen:
Archive, temporäre Verzeichnisse, generierte Artefakte, Logs, Tests,
Konfigurationen, alte Versionen, tote Referenzen, unreferenzierte Dateien,
verdeckte Schreiber, unbekannte Konsumenten und widersprüchliche Authorities.

Er beobachtet zuerst und bildet danach Hypothesen. Jede wesentliche Aussage
wird als `FACT`, `INFERENCE`, `HYPOTHESIS` oder `UNKNOWN` gekennzeichnet und
mit ihrer Evidenz verbunden. Archive dürfen historische Evidenz liefern, aber
nicht still als aktueller Stand gelten.

Der EXPLORER verändert den untersuchten Originalbestand nicht. Wenn eine
Zerlegung notwendig ist, arbeitet er auf einer abgegrenzten, hashgebundenen
Untersuchungskopie. Dort darf er Artefakte extrahieren, nummerieren,
vergleichen, aufteilen und neu anordnen.

Sein Ziel ist nicht, möglichst viele Dateien aufzulisten, sondern den
tatsächlichen Zusammenhang zu rekonstruieren:

- Was existiert, und was sollte existieren?
- Was fehlt, ist doppelt, veraltet oder widersprüchlich?
- Welche Referenz zeigt auf nichts, und welche Datei besitzt keine Referenz?
- Welcher Producer schreibt welches Artefakt, und welche Konsumenten lesen es?
- Welche Outputs haben keinen bekannten Producer?
- Welche Producer erzeugen den erwarteten Output nicht?
- Welche Fehler werden verschluckt, Tests deaktiviert oder Warnungen
  übergangen?
- Welche zeitliche Abfolge und welche unscheinbare Spur erklären das
  beobachtete Verhalten?

Der EXPLORER dokumentiert auch negative Evidenz: wo und wie gesucht wurde,
ohne einen erwarteten Fund zu machen. Er benennt unzugängliche Bereiche und
erfindet dort keinen Befund. Er versucht seine eigenen Hypothesen zu
widerlegen und ordnet verbleibende Hypothesen nach Evidenzstärke und
Konfidenz.

Der EXPLORER entwickelt keine Lösung und baut keinen Fix. Er liefert die
belegte Grundlage für ARCHITEKT und PLANNER.

#### Discovery-Dateipaar

| Datei | Funktion |
|---|---|
| `[CHANGE]_DISCOVERY.MD` | HUMAN-lesbare Untersuchung, Befunde, Zusammenhänge und Diagnosehypothesen |
| `[CHANGE]_DISCOVERY_INVENTORY.JSON` | Maschinenlesbares Inventar, Referenzen, Klassifikationen und Evidenz |

Beide Dateien tragen dieselbe `discovery_id` und verweisen aufeinander. Sie
bilden gemeinsam ein logisches `DISCOVERY_BUNDLE`, ohne einen weiteren
obligatorischen Dateityp zu erzeugen.

Das Inventory kann untersuchte und ausgeschlossene Bereiche, Pfade, Versionen,
Hashes, Authorities, Producer, Konsumenten, Referenzen, Duplikatgruppen,
Divergenzen, Orphans, Stale Files, tote Referenzen, zeitliche Spuren,
Evidenzlücken sowie Befunde mit stabilen IDs enthalten.

### Planner

Der `PLANNER` übersetzt den bestätigten Auftrag und die belegte
Bestandsaufnahme in einen ausführbaren `[CHANGE]_BAUPLAN.MD`. Er plant; er
implementiert nicht. Bei fehlender Grundlage gibt er den Auftrag an ARCHITEKT
oder EXPLORER zurück, statt Annahmen als Tatsachen in den Bauplan zu schreiben.

### Implementor

Der `IMPLEMENTOR` baut den bestätigten Bauplan. Er verändert nicht gleichzeitig
den Auftrag oder das Ziel. Notwendige Abweichungen werden sichtbar gestoppt,
belegt und an PLANNER beziehungsweise ARCHITEKT zurückgegeben. Der Name
`DEVELOPER` wird für diese Rolle nicht verwendet, weil der gesamte
Funktionsbereich bereits DEVELOPMENT heisst.

### Fachspezialist

`FACHSPEZIALIST_[DOMAIN]` ist eine optionale Rollenfamilie. Es gibt keine feste
Liste obligatorischer Fachagenten. Der ARCHITEKT wählt Fachspezialisten nur,
wenn Fachwissen oder ein eigenes Kontextfenster die Arbeit materiell
verbessert. Mögliche Domänen entstehen aus dem realen Projekt und werden nicht
vorsorglich erfunden.

Ein Fachspezialist untersucht oder bearbeitet seinen abgegrenzten Gegenstand
und liefert ein strukturiertes Artefakt zurück. Er übernimmt weder die
Gesamtarchitektur noch die unabhängige QUALITY-Validation.

## Postbox in D3

`POSTBOX` ist das asynchrone Kommunikationsmuster zwischen Agenten. Jeder
Agent kann einen eigenen Briefkasten besitzen. Andere Agenten hinterlegen dort
schemafähige Nachrichten, die der Empfänger beim nächsten zuständigen Turn
liest und verarbeitet.

Eine POSTBOX ist kein freier Agentenchat und keine zweite PINWALL. Nachrichten
sind sichtbare, prüfbare Artefakte mit mindestens Absender, Empfänger,
Nachrichtentyp, Zeitpunkt, Payload oder Artefaktverweisen, gewünschter Aktion,
Authority-Scope und Status.

Der empfohlene Lebenszyklus lautet:

```text
PENDING -> ACKNOWLEDGED -> COMPLETED
```

Dabei gelten folgende Regeln:

- Der Absender darf senden, aber nicht für den Empfänger quittieren.
- Nur der Empfänger bestätigt Bearbeitung und Abschluss.
- Eine Nachricht ist nicht automatisch eine Ausführungsberechtigung.
- Autorisierte und HUMAN-pflichtige Aktionen sind ausdrücklich getrennt.
- `COMPLETED` benötigt Abschlussbelege.
- Wiederholtes Senden derselben `message_id` darf keine Duplikate erzeugen.
- Jeder Agent liest nur seine eigene, für den Auftrag relevante POSTBOX.
- Dauerhafte Fachinformation bleibt im zuständigen Artefakt; die Nachricht
  verweist darauf.

DEVELOPMENT nimmt das Muster in D3 auf. WORKFLOW legt konkrete Übergabepunkte
fest, TOOLING implementiert Transport und Statusübergänge, und Rollenverträge
bestimmen Schreib-, Lese- und Quittierrechte.

## Webbasierte Decision Page in D4

Die `DECISION PAGE` ist ein HUMAN-Interface, das einen komplizierten
Entscheidungsraum verständlich und bedienbar macht.

> Die HTML-Seite ist nicht die Entscheidung und nicht der Vertrag. Sie ist die
> Benutzeroberfläche, mit der der HUMAN den Vertrag beziehungsweise die
> Entscheidung erzeugt.

Das strukturierte Ergebnis ist ein JSON-Artefakt. Je nach Einsatz kann es eine
Entscheidung, Konfiguration, Planfreigabe, Agentenauswahl, Triage, Freigabe,
Ablehnung oder Liste offener HUMAN-Entscheide darstellen.

### Zwei Betriebsarten

| Modus | Verhalten |
|---|---|
| `STANDALONE` | HUMAN arbeitet selbständig in der Seite. Entwürfe werden automatisch gespeichert; der Abschluss erzeugt das verbindliche JSON. |
| `AI_GUIDED` | AI führt durch den Entscheidungsraum. HUMAN entscheidet; ein deterministischer Builder persistiert jeden eindeutigen Entscheid sofort. |

Im `AI_GUIDED`-Modus gilt `DIALOGFUEHRUNG: AI` und
`ENTSCHEIDUNGSAUTORITAET: HUMAN`. AI darf erläutern, vergleichen, nachfragen
und einen Vorschlag formulieren. Sie darf den HUMAN-Entscheid nicht ersetzen.

### Zwei beobachtete Interaktionsformen

Die Sources und die HUMAN-Erinnerung belegen zwei kombinierbare Formen:

1. In einer Browseransicht kann HUMAN eine Textstelle markieren. Darauf
   erscheint ein Eingabefeld für Befund oder Korrekturvorschlag. Der
   dargestellte Quelltext selbst wird dadurch nicht live verändert; die
   Eingabe ist eine Annotation beziehungsweise ein Entscheidungsartefakt.
2. Die Browseransicht kann als reine Prüffläche dienen, während HUMAN die
   eigentliche Änderung direkt in der DOCX-Quelle vornimmt.

Welche Form im konkreten historischen Lauf verwendet wurde, ist noch nicht
vollständig mechanisch aufgelöst. Der aktive QUALITY-REVISION-Vertrag kennt
zuletzt eine read-only Browserprojektion, während der REVISER bestätigte
HUMAN-Entscheide über einen deterministischen Builder in
`REVISION_LIST_DRAFT.json` persistierte. Die frühere beziehungsweise
darunterliegende P5-Klicktool-Oberfläche unterstützt zusätzlich interaktive
Annotationen. Diese Varianten dürfen nicht rückwirkend zu einer einzigen
behaupteten Implementierung vermischt werden.

### Speicherung und Wiederaufnahme

Eine robuste DECISION PAGE benötigt:

- lokale Sofortspeicherung nach jeder Eingabe;
- einen atomar geschriebenen Workspace-Draft;
- eine stabile `decision_run_id`;
- sichtbare Zustände `GESPEICHERT`, `NICHT SYNCHRONISIERT` und `FEHLER`;
- eine Speicherbestätigung, bevor `GESPEICHERT` angezeigt wird;
- einen Hash des Fragen- oder Entscheidungssets;
- Wiederaufnahme des letzten bestätigten Stands;
- Archivierung ersetzter Drafts;
- manuellen JSON-Download als Notausgang;
- Warnung vor dem Schliessen bei unbestätigten Änderungen;
- Trennung zwischen Draft und finalem Entscheidungsartefakt.

Das FIELD_NOTES-Muster zeigt eine zusätzliche Recovery-Perle:
Ein unterbrochener Lauf kann einen vollständig gespeicherten und pro Karte
HUMAN-bestätigten Entscheidungsstand in einen neuen Draft übernehmen. Pfad und
SHA-256 der alten Entscheidevidenz werden festgehalten. Offene,
`BORDERLINE`- oder nicht bestätigte Karten blockieren das Healing. Recovery
umgeht niemals die anschliessenden Freigabe- und Validation-Gates.

### Automatische Übergabe

Eine statische HTML-Seite kann aus Sicherheitsgründen nicht beliebig in den
Workspace schreiben. Für automatische Übergabe braucht sie einen kleinen
lokalen Decision-Service oder einen deterministischen Orchestrator:

```text
DECISION PAGE
  -> Draft an lokalen Service
  -> Schema-Validation
  -> atomarer Write
  -> Speicherquittung an die Seite
  -> FINAL SUBMIT
  -> finales Decision-JSON mit Hash
  -> Nachricht an die POSTBOX des Empfängers
```

Der HUMAN muss damit nicht mehr als manueller JSON-Briefträger dienen. Ein
Entscheid darf dennoch nur diejenigen Folgeaktionen automatisch auslösen, die
sein Authority-Scope ausdrücklich erlaubt.

## Independent Review Loop in D4

Das P7-Translator-Tool aus FIELD_NOTES wird als universelles Muster
`INDEPENDENT REVIEW LOOP` aufgenommen:

```text
PRODUCE
-> INDEPENDENT REVIEW
-> GATE
-> TARGETED REPAIR
-> FINALIZE
```

Ein produzierendes Modell erzeugt ein strukturiertes Artefakt. Ein
unabhängiger Provider oder eine unabhängige Modellfamilie prüft dieses
Artefakt. Ein Gate bestätigt, verwirft oder eskaliert Findings. Der
ursprüngliche Provider erhält nur bestätigte Findings zurück und repariert
gezielt die betroffenen Einheiten.

Die Modelle führen keinen freien, verborgenen Agentenchat. Ein
deterministischer Orchestrator übergibt versionierte Artefakte zwischen den
Pässen. Dadurch bleiben Inputs, Outputs, Fehler, Kosten, Zeiten und
Verantwortung pro Pass sichtbar.

Ein wiederverwendbarer Loop benötigt:

- austauschbare Provider und getrennte Kontexte;
- JSON-Schema pro Übergang;
- stabile Objekt- oder Block-IDs;
- unveränderliche Pass-Artefakte;
- definierte Gate-Regeln;
- Retry nur für die betroffene Einheit;
- HUMAN-Eskalation bei kritischen oder mehrdeutigen Findings;
- ein Run-Manifest mit Modellen, Prompts, Hashes, Kosten und Laufzeiten;
- eine finale Vollständigkeitsprüfung.

Der Orchestrator ist TOOLING und kein zusätzlicher Agent. `PRODUCER`,
`REVIEWER` und `REPAIRER` sind Laufzeitrollen. Ein zweiter Kontext desselben
Providers kann eine getrennte Prüfung liefern; eine andere Modellfamilie oder
ein anderer Provider bietet jedoch die stärkere methodische Unabhängigkeit.

## Vertikaler Lernfluss zum Hub

Projektbezogene Verbesserungslisten, Build Records und Logs teilen das
Schicksal ihres Projekts. Übertragbare Lehren werden deshalb als
eigenständige Kandidaturen an den Hub übergeben.

```text
PROJECT DEVELOPMENT_LOG
  -> LESSON_CANDIDATE exportieren
  -> PROJECT HUB_OUTBOX
  -> Transport in die HUB LEARNING INBOX
  -> Schema-, Provenienz- und Dublettenprüfung
  -> HUB LEARNING_REGISTER
  -> ACKNOWLEDGEMENT zurück an das Projekt
```

Dies kombiniert zwei Verantwortungen:

- Das Projekt sendet beziehungsweise veröffentlicht eine ausdrücklich
  ausgewählte Lernkandidatur.
- Der Hub sammelt nur diese Kandidaturen ein und übernimmt sie nach Prüfung in
  seine eigene SSOT.

Das Projekt schreibt nie direkt in das `LEARNING_REGISTER`. Der Hub durchsucht
umgekehrt nicht ungefragt das gesamte Projekt nach vermeintlichen Lehren. Die
Kandidatur wird kopiert, nicht verschoben. Dadurch bleibt ihre Projektherkunft
erhalten, während die übertragbare Lehre auch nach Projektabschluss im Hub
verfügbar bleibt.

Jede Kandidatur benötigt mindestens eine stabile `candidate_id`, Projekt und
Quellartefakt, ursprüngliche Event-ID, Content-Hash, Evidenz, Schemasversion
und Übertragungsstatus. Idempotenz verhindert eine doppelte Aufnahme bei
wiederholtem Versand.

### Zwei getrennte Lebenszyklen

Problembehebung und Lernen bleiben getrennt:

| Lebenszyklus | Leitfrage |
|---|---|
| Problembehebung | Ist der konkrete Fehler oder Rückschlag im Projekt behoben? |
| Lernen | Ist daraus eine belegte und übertragbare Lehre entstanden? |

Ein Problem kann behoben sein, ohne eine allgemeine Lehre zu erzeugen. Eine
wertvolle Lehre kann bereits feststehen, obwohl das ursprüngliche Problem noch
nicht vollständig gelöst ist.

Der Lernlebenszyklus ist provisorisch:

```text
CAPTURED -> TRIAGED -> VALIDATED -> PROMOTED
                         |-> PROJECT_ONLY
                         |-> REJECTED
                         |-> SUPERSEDED
```

Erfolge, Fehler, Rückschläge, Near Misses und gemischte Ergebnisse können
Lernkandidaten liefern. Der gemeinsame JSON-Kern soll Quelle, Ergebnisart,
Beobachtung, Evidenz, Lehre, Anwendbarkeit, empfohlene Änderung, betroffene
Library-Bausteine und Lernstatus enthalten.

Die im Projekt liegende `LIST_OF_IMPROVEMENTS` bleibt projektbezogen. Sie ist
keine dauerhafte Hub-SSOT und wird nicht allein aufgrund ihres Namens mit dem
globalen Lernregister gleichgesetzt.

## Auswahl aus der Local Library

Die Local Library stellt Tools, Templates, Rollenverträge und Muster zur
Auswahl bereit. Ein konkretes Projekt übernimmt nur die tatsächlich benötigten
Bausteine. Auswahl, Version und projektspezifische Abweichung bleiben
nachvollziehbar.

Beispiele:

- Ein D1-Projekt benötigt keine Agentenorganisation.
- Ein D3-Projekt kann ARCHITEKT, EXPLORER und IMPLEMENTOR verwenden, aber
  keinen eigenen Fachspezialisten.
- Ein D4-Projekt kann den INDEPENDENT REVIEW LOOP verwenden, ohne jede
  Nachricht über eine POSTBOX zu routen.
- Ein Projekt darf ein Library-Template instanziieren, ohne das Template
  selbst zur Projekt-SSOT zu machen.

## Bewusste Nicht-Zuordnungen und Konflikte

- `HO_TO_CARD`, `HANDOFF` und konkrete Übergabeprotokolle werden nicht als
  DEVELOPMENT-Dateityp geführt. DEVELOPMENT plant ihre Verwendung;
  WORKFLOW, TOOLING und Rollenverträge regeln die konkrete Übergabe.
- `[PROJECT]_ACTORS.MD` wird nicht aufgenommen.
- Ein unabhängiger `VALIDATOR` gehört zu QUALITY und nicht in die
  DEVELOPMENT-Agentenliste.
- `DEVELOPER` wird als DEVELOPMENT-Rolle verworfen. Der bestehende lokale
  Vertrag `AH_AGENT_DEVELOPER.MD` steht damit in einem offenen
  Migrationskonflikt. Dieser Draft ändert oder löscht ihn nicht still.
- `DISCOVERY` ist eine bedarfsabhängige D3-Output-Familie und keine
  obligatorische D1-Datei.
- POSTBOX transportiert Nachrichten; sie ersetzt weder PINWALL noch
  Fachartefakte.
- DECISION PAGE ist Oberfläche; das erzeugte und persistierte JSON ist der
  strukturierte Entscheidungsstand.

## Quellenbindung

Semantisch gelesene FIELD_NOTES-Quellen:

- `0_MISSION_CONTROL/PACKAGES/PACKAGE_CONSTRUCTION/EXPLORER.MD` für belegten
  Ist-Zustand, Diagnose, vertikale Abläufe und horizontale Abhängigkeiten;
- `0_MISSION_CONTROL/AGENTS/SYSTEM_SENTINEL/03_AGENT_FILESY/FILESY.md` für
  Cross-Refs, Orphans, Stale Files, Naming- und Location-Drift;
- `0_MISSION_CONTROL/AGENTS/SYSTEM_SENTINEL/05_AGENT_DUPLO/DUPLO.md` für
  exakte und semantische Duplikate sowie divergierende Kopien;
- `0_MISSION_CONTROL/AGENTS/SYSTEM_SENTINEL/02_AGENT_KOMPASS/KOMPASS.md` für
  Mission-Drift und Obsoleszenz;
- `LESSONS_LEARNED.md` und
  `SYSTEM_SENTINEL/08_SENTINEL_QUALITY/LIST_OF_IMPROVEMENTS.json` für die
  Trennung von Problembehebung, Verbesserung und übertragbarer Lehre;
- `0_W_WORKFLOW/P6_PUBLISH/INBOX/` für POSTBOX-Schema, atomisches Schreiben,
  Statusübergänge, Quittierung und begrenzte Autorisierung;
- `0_W_WORKFLOW/P7_TRANSLATOR/TRANSLATOR_SDK_CLD_GPT_CLD_260810/` für den
  providerübergreifenden Produce-Review-Gate-Repair-Loop;
- `0_MISSION_CONTROL/PACKAGES/PACKAGE_QUALITY_REVISION/` für AI-geführte
  HUMAN-Entscheide, `REVISION_LIST_DRAFT`, Browserprojektion, atomische
  Persistenz, Recovery und Healing;
- `0_W_WORKFLOW/P5_WEB_PREVIEW/P5_TICKET_SYSTEM/` sowie das Writing-Room-HITL-
  Template für interaktive Annotationen, Browser-State und JSON-Export.

## Stand und Grenzen des Source-Checks

Durchsucht wurden die aktiven Teile von `FIELD_NOTES_DRAFT`, insbesondere
MISSION_CONTROL, SYSTEM_SENTINEL, PACKAGE_CONSTRUCTION,
PACKAGE_QUALITY_REVISION, P5, P6, P7 und die zentralen Lessons-Learned-Dateien.
Markdown, JSON, JSON-Schemas, Python-Builder, Tests und ausgewählte HTML-
Oberflächen wurden einbezogen. Relevante Archive und Snapshots wurden als
historische Evidenz punktuell gelesen, nicht als aktuelle Authority.

Der Check war für die oben gebundenen Kernquellen semantisch, für den gesamten
Workspace jedoch weder dateivollständig noch als Beweis gedacht, dass jede
historische Perle gefunden wurde. Insbesondere die genaue historische
Browserfassung mit den beim Markieren aufploppenden Textfeldern ist noch nicht
eindeutig auf eine einzelne Implementierung zurückgeführt. Die HUMAN-
Erinnerung wird deshalb als eigene Evidenz bewahrt und nicht durch die zuletzt
aktive read-only UX-Regel überschrieben.

## Noch offene Entscheide

- endgültige Schemas und Speicherorte für `LESSON_CANDIDATE`, Hub-Inbox und
  `LEARNING_REGISTER`;
- endgültige Dateiendung beziehungsweise Eventstruktur des
  `DEVELOPMENT_LOG`;
- POSTBOX-Speicherform für mehrere gleichzeitige Absender;
- kanonischer lokaler Name des `INDEPENDENT REVIEW LOOP`;
- konkrete Implementierung des lokalen Decision-Service;
- Auflösung oder Migration des bestehenden `AH_AGENT_DEVELOPER.MD`;
- Identifikation der genauen historischen interaktiven Browserfassung, falls
  sie als eigenes Golden Example übernommen werden soll.

Dieser Entwurf darf erst nach weiterer HUMAN-Prüfung in `NAMING_LOCAL.md` oder
in kanonische Library-Templates überführt werden.
