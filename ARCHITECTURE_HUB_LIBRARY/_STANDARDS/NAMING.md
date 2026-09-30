---
document_id: ah-naming
title: Architecture Hub Naming Catalogue
status: DRAFT_FOR_HUMAN_REVIEW
version: 0.2.0-draft
created_at: 2026-09-30T01:24:00+02:00
updated_at: 2026-09-30T08:36:00+02:00
authority: HUMAN_APPROVAL_REQUIRED
scope: architecture-relevant terminology
---

# NAMING — Begriffskatalog und Konfliktübersicht

## Zweck und Status

Diese Datei ist noch **kein verbindlicher Namensstandard**. Sie ist die
Prüfgrundlage für den HUMAN-Entscheid. Sie trennt:

1. den verwendeten Begriff;
2. seine Bedeutung im jeweiligen Workspace;
3. seine gebräuchliche Bedeutung in der AI- und Software-Community;
4. Konflikte, Überlappungen und falsche Synonyme;
5. die empfohlene Verwendung im `ARCHITECTURE_HUB`.

Erst nach der gemeinsamen Bereinigung werden Einträge als verbindlich
freigegeben. Bis dahin sind alle Empfehlungen **Kandidaten**.

## Lebendes und versioniertes Register

Die Dateinamenssystematik und das Vokabular dürfen fortlaufend ergänzt und
angepasst werden. Anpassbarkeit bedeutet jedoch nicht, dass Namen still und
folgenlos umgedeutet werden. Für jeden Begriff wird einer dieser Zustände
geführt:

```text
PROPOSED -> CANONICAL -> DEPRECATED -> RETIRED
                |
                -> ALIAS
```

Änderungsregeln:

1. Neue Begriffe beginnen als `PROPOSED` und benötigen Bedeutung, Scope und
   Abgrenzung.
2. Ein `ALIAS` verweist auf den kanonischen Begriff und erzeugt keine zweite
   Bedeutung.
3. Eine Bedeutungsänderung erhält eine neue Version und wird nicht still in
   alte Dateien zurückgeschrieben.
4. `DEPRECATED` benennt Ersatz und Migrationsweg; bestehende Quellen bleiben
   weiterhin auffindbar.
5. Ergänzungen und Präzisierungen erhöhen die Minor-Version; inkompatible
   Bedeutungswechsel die Major-Version.
6. Jeder Änderungsentscheid nennt Datum, Begründung, betroffene Artefakte und
   HUMAN-Authority.

## Sichtungsraum

Die Übersicht erfasst architekturrelevante Begriffe aus Dateinamen,
Verzeichnisnamen, Überschriften und ausgewählten Verträgen in:

| Kürzel | Quelle |
|---|---|
| `H` | `ARCHITECTURE_HUB` |
| `O` | Workspace `OPENAI` und dessen `SYSTEM` |
| `F` | `FIELD_NOTES_DRAFT` einschliesslich Mission Control, Workflows und historischer Varianten |
| `M` | `MY_AI_PROJECTS`, insbesondere `MAIL_ORGANIZER` und Experimente |
| `C` | Community- und Herstellerterminologie aus Primärquellen |

`Alle Begriffe` bedeutet hier: alle bei der Sichtung erkannten
**architekturrelevanten Begriffsfamilien**. Fachwörter einzelner Projekte,
Dateinamen mit reinem Inhaltsthema sowie Abhängigkeiten in Vendor- und
Cache-Verzeichnissen gehören nicht in diesen Standard.

## Statuscodes

| Code | Bedeutung |
|---|---|
| `KEEP` | als bevorzugten Begriff übernehmen |
| `QUALIFY` | nur mit Präzisierung oder zusammengesetztem Namen verwenden |
| `ALIAS` | auffindbar halten, aber nicht als neuen kanonischen Namen verwenden |
| `LOCAL` | zulässiger Hub-eigener Begriff; keine etablierte Community-Bedeutung behaupten |
| `AVOID` | wegen Mehrdeutigkeit oder irreführender Wirkung vermeiden |
| `DECIDE` | HUMAN-Entscheid steht noch aus |

# 1. Auftrag, Regeln und dauerhafte Dokumente

| Begriff | Gefundene Verwendung | Präzise Bedeutung | Konflikt | Empfehlung |
|---|---|---|---|---|
| `MISSION.md` | `H`, `F`; in A2–A4 als Grunddatei | Warum etwas existiert, wofür es verantwortlich ist, was ausserhalb seines Scopes liegt und wann es erfüllt ist | Wird teilweise wie `README`, Vision oder vollständige Spec verwendet | `KEEP`: Zweck, Scope, Verantwortung, Nicht-Ziele und Erfolgskriterien; keine Bedienungsanleitung |
| `README.md` | `O`, `F`, `M` | Einstieg und Navigation für Leser: Was ist hier, wie starte ich, wohin gehe ich weiter? | Wird als Mission, Statusbericht oder Sammel-Spec überladen | `KEEP`: Onboarding und Wegweiser; darf auf `MISSION.md` verweisen, ersetzt sie nicht |
| `CONSTITUTION.md` | `F`, `M`; besonders in grösseren Systemen | Höchste, selten geänderte Grundprinzipien und nicht verhandelbare Governance | Oft bloss ein stärker klingendes Wort für Conventions | `QUALIFY`: nur verwenden, wenn tatsächlich übergeordnet, knapp und schwer änderbar; sonst `CONVENTIONS.md` |
| `CONVENTION.md` / `CONVENTIONS.md` | Singular in `O`, Varianten in `F`; Plural im Hub-Entwurf | Versionierte Arbeits-, Struktur- und Verhaltensregeln mit definiertem Geltungsbereich | Singular/Plural; vermischt teils Authority, Security und Stil | `DECIDE`, Empfehlung: `CONVENTIONS.md` im Plural; spezialisierte Regeln verlinken statt duplizieren |
| `NAMING.md` | häufig in `F`; im Hub vorgesehen | Kontrolliertes Vokabular, zulässige Namen, Aliase und Benennungsmuster | Kann reine Dateinamenregeln oder ein Glossar meinen | `KEEP`: beide Teile ausdrücklich trennen: **Terminologie** und **Namenssyntax** |
| `SPRACHREGELN.md` | `F`, Hub optional | Regeln für natürliche Sprache, Ton, Schreibweise, Übersetzung und verbotene Formulierungen | Wird mit technischem Naming vermischt | `KEEP`: nur Sprachproduktion; technische Bezeichner bleiben in `NAMING.md` |
| `POLICY` | `M`, Community | Durchsetzbare Regel für Entscheidungen oder Aktionen, oft maschinenprüfbar | Wird als loses Leitprinzip verwendet | `QUALIFY`: `SECURITY_POLICY`, `RETENTION_POLICY`, `AUTOMATION_POLICY`; Owner und Enforcement nennen |
| `RULE` | `F`, `M` | einzelne konkrete Regel | Kann Empfehlung, Constraint oder Policy bedeuten | `QUALIFY`: Muss/Soll, Scope, Owner und Prüfbarkeit angeben |
| `PRINCIPLE` / Leitprinzip | `H`, `F` | dauerhafte Orientierung für Entscheide, nicht zwingend direkt maschinenprüfbar | Wird als harte Regel missverstanden | `KEEP`: klar von `POLICY` und `CONSTRAINT` trennen |
| `CONSTRAINT` | `F`, `M`, `C` | harte Grenze, die eine Lösung nicht verletzen darf | Wird mit Präferenz oder Guardrail gleichgesetzt | `KEEP`: technisch oder organisatorisch überprüfbare Grenze |
| `AUTHORITY` | `H`, `F`, `M` | Recht, bei Konflikten verbindlich zu entscheiden oder eine Änderung freizugeben | Wird mit Berechtigung oder Quellenrang vermischt | `KEEP`: `DECISION_AUTHORITY`, `CHANGE_AUTHORITY`, `SOURCE_AUTHORITY` qualifizieren |
| `PERMISSION` | `M`, Community | technische Erlaubnis zu lesen, schreiben, ausführen oder kommunizieren | Kein Entscheidungsrecht | `KEEP`: nie als Synonym für Authority verwenden |
| `GUARDRAIL` / `GUARDRAILS` | `F`, `M`, Hub-Entwurf, Community | Mechanismus, der Eingaben, Ausgaben oder Aktionen zur Laufzeit prüft, begrenzt oder unterbricht | Wird als Sammelwort für alle Regeln benutzt | `QUALIFY`: nur für wirksame Laufzeitkontrollen; Dokumentname `GUARDRAILS.yaml`, wenn maschinenlesbar |
| `BOUNDARY` | `M`, Community | ausdrücklich gezogene System-, Scope-, Trust- oder Authority-Grenze | Ohne Präfix unklar | `QUALIFY`: `SYSTEM_BOUNDARY`, `SCOPE_BOUNDARY`, `TRUST_BOUNDARY`, `PROVIDER_BOUNDARY` |
| `CONTRACT` | `F`, `M`, `C` | beobachtbare Vereinbarung zu Input, Output, Fehlern und Verpflichtungen zwischen Komponenten | Wird mit vollständiger Spec oder Schema gleichgesetzt | `KEEP`: Verhalten und Verpflichtungen; Schema kann Teil eines Contracts sein |
| `ADR` | Hub-Meta-Gruppe, Community | ein einzelner Architecture Decision Record mit Kontext, Optionen, Entscheid und Folgen | Wird mit fortlaufendem Entscheidungslog verwechselt | `KEEP`: eine Datei oder ein Eintrag pro Architekturentscheid |
| `DECISIONS.md` / `DECISIONS_LOG.md` | `F`, `M` | dauerhaftes Register bestätigter Entscheide mit Datum, Status, Authority und Verweisen | Kann Pinwall-Einträge oder ADRs duplizieren | `KEEP`: `DECISIONS.md` als kanonischer Name; `DECISIONS_LOG.md` als Legacy-Alias; Details bei Bedarf in verlinkten ADRs |
| `LESSONS_LEARNED` | `H`, `F` | beobachtete Erfahrungen aus realen Durchläufen, inklusive Bedingungen und Evidenz | Wird zu früh als universeller Standard behandelt | `KEEP`: zunächst Evidenz; erst nach Review als Pattern, Standard oder Modul promoten |
| `INDEX` | `F`, `M` | Navigations- oder Registry-Datei mit Verweisen | Wird mit Manifest verwechselt | `KEEP`: für Auffindbarkeit; muss nicht maschinenlesbar oder vollständig ausführungsrelevant sein |
| `MANIFEST` | `M`, Community | maschinenlesbare, möglichst vollständige Deklaration von Bestandteilen und Metadaten | Wird als README benutzt | `KEEP`: nur wenn Vollständigkeit oder maschinelle Verarbeitung beabsichtigt ist |
| `PROJECT_INFO` | `O` | kompakte Projektmetadaten | Überschneidet README und Manifest | `ALIAS`: künftig Metadaten in Frontmatter/Manifest; Navigation in README |

# 2. Planung, Status und Übergaben

| Begriff | Gefundene Verwendung | Präzise Bedeutung | Konflikt | Empfehlung |
|---|---|---|---|---|
| `PINWALL.md` / `PIN_WALL.md` | prägend in `F`; `PINWALL.md` im Hub-Entwurf | lebendes Arbeitscockpit: aktueller Fokus, aktive Arbeiten, offene Fragen, Blocker, anstehende Entscheide und nächste Schritte | kein etablierter Community-Begriff; darf nicht zum Archiv für bestätigte Entscheide oder zum Ereignislog werden | `LOCAL + RECOMMENDED`: Schreibweise `PINWALL.md`; breiter und für den Hub passender als ein reines Taskboard |
| `BOARD.md` | `O`; generischer Community-Begriff | Aufgabenübersicht mit Status, Reihenfolge und gegebenenfalls Zuständigkeit | deckt nur einen Teil der Pinwall-Funktion ab | `ALIAS`: bestehende Boards zulassen; neue Hub-Projekte bevorzugen `PINWALL.md` |
| `PROJECT_BOARD.md` | `O`, `H` | Board auf Projektebene | Überschneidung mit Pinwall | `QUALIFY`: nur wenn mehrere Ebenen existieren; sonst kanonischen Einzelnamen verwenden |
| `SESSION_BOARD.md` | `O` | temporäre Steuerung einer Session | droht dauerhafte Wahrheit neben dem Projektboard zu erzeugen | `QUALIFY`: nach Sessionabschluss in Handoff/Log überführen; nicht zweite Source of Truth |
| `STATUS.md` | viele Varianten in `F` | Zeitpunktaufnahme des Zustands | Wird als Board, Log oder Build-Report verwendet | `QUALIFY`: `PROJECT_STATUS`, `BUILD_STATUS`, `RELEASE_STATUS`; Snapshot-Zeit nennen |
| `BUILD_STATUS.md` | `M` | Stand der Implementierung, Tests und offenen Bauarbeiten | kann zur zweiten Pinwall werden | `KEEP` nur als erzeugter oder eng begrenzter Bericht; aktive Steuerung bleibt im Board/Pinwall |
| `ROADMAP.md` | `M`, Community | geordnete zukünftige Vorhaben, Abhängigkeiten und Zielzustände | Wird mit aktuellem Taskboard vermischt | `KEEP`: Zukunftsrichtung, nicht Tagessteuerung |
| `PLAN.md` | `M`, SDD-Community | Lösungs- und Vorgehensplan für eine definierte Spec | Wird als Mission oder Taskliste genutzt | `KEEP`: erklärt das Wie; referenziert die Spec |
| `TASKS.md` / `WORK_TICKET` | `O`, `M`, Community | ausführbare Arbeitseinheiten mit Done-Kriterien | Ticket wird teils als vollständige Spec benutzt | `KEEP`: Umsetzungseinheiten; Anforderungen bleiben in der Spec |
| `HANDOFF` | `O`, `F`, Community | explizite Übergabe von Verantwortung, Artefakten, Status und offenen Risiken | wird mit Delegation oder bloss einer Nachricht gleichgesetzt | `KEEP`: Sender, Empfänger, Übergabegegenstand, Annahmekriterium und Restunsicherheit nennen |
| `LOG` | `O`, `F`, `M` | append-only Ereignis- oder Aktivitätsaufzeichnung | wird mit Status, Transcript und Audit verwechselt | `QUALIFY`: `EVENT_LOG`, `DECISIONS_LOG`, `RUN_LOG`; Zweck und Retention nennen |
| `REPORT` | `F`, `M` | zusammengefasste Auswertung für einen Adressaten | sagt ohne Präfix wenig | `QUALIFY`: `VALIDATION_REPORT`, `AUDIT_REPORT`, `RUN_REPORT`, `STATUS_REPORT` |
| `TRACE` | `C`, teilweise `M` | strukturierter End-to-End-Verlauf eines Runs über Modell-, Tool-, Guardrail- und Handoff-Schritte | nicht jedes Log ist eine Trace | `KEEP`: nur bei korrelierbarer Ausführungskette |
| `TRANSCRIPT` | `C`, Chat-Exporte in `O`/`M` | inhaltliche Folge von Nachrichten, Tool-Aufrufen und Antworten | enthält nicht zwingend Systemtelemetrie | `KEEP`: Gesprächs-/Interaktionsinhalt, nicht allgemeiner Log |
| `CHAT_EXPORT` | `O`, `M` | exportierte Rohdarstellung eines Chats | kein kuratierter Wissensbaustein | `KEEP`: Quelle mit Provenienz; erst danach extrahieren und kuratieren |
| `CHECKPOINT` | `M`, Community | definierter, wiederaufnehmbarer Zustand innerhalb eines Laufs | wird mit Backup oder Gate verwechselt | `KEEP`: Zustand + Wiederaufnahmeregel; ein Gate ist dagegen eine Entscheidungsschwelle |

## Empfehlung zur Steuerungsfamilie

Die Begriffe `PINWALL`, `BOARD`, `DECISIONS`, `STATUS` und `LOG` sind **nicht**
gleichbedeutend:

```text
PINWALL  = Was ist jetzt aktiv, offen, blockiert oder als Nächstes zu tun?
BOARD    = Welche Aufgaben haben welchen Bearbeitungsstatus?
DECISIONS = Was wurde verbindlich entschieden und warum?
STATUS   = Wo standen wir zu Zeitpunkt X?
LOG      = Was ist wann geschehen?
ROADMAP  = Wohin wollen wir später?
```

Empfehlung: Der Hub verwendet `PINWALL.md` als aktuelle Entwicklungssteuerung.
Sie darf Abschnitte `PENDING DECISIONS` und `RECENT DECISIONS` enthalten, führt
aber nur Links und Kurzstatus. Der dauerhafte Entscheid steht einmalig in
`DECISIONS.md` oder einem verlinkten ADR. `BOARD.md` bleibt Import-/Legacy-Alias
und wird nicht parallel als zweite aktuelle Wahrheit geführt.

# 3. Anforderungen, Struktur und Daten

| Begriff | Gefundene Verwendung | Präzise Bedeutung | Konflikt | Empfehlung |
|---|---|---|---|---|
| `SPEC` / `SPECS` | stark in `F`, `M`; im Hub diskutiert | **lokale Dateifamilie** für menschenlesbare Markdown-Verträge, Anleitungen und Steuerungsdokumente; auf Inhaltsebene kann `specification` enger eine normative Beschreibung meinen | Dateiformat und semantischer Dokumenttyp werden vermischt | `LOCAL + KEEP`: Ordner `SPECS/` als Gegenfamilie zu `SCRIPTS/`; zusätzlich `document_type` oder Funktionsname verwenden, damit Mission, Prompt, Review und Report unterscheidbar bleiben |
| `SYSTEM_SPEC` | implizit in A3/A4 | Spec des gesamten Systems und seiner Komponentenbeziehungen | kann zu monolithisch werden | `QUALIFY`: Systemgrenze nennen; Teil-Specs zulassen |
| `AUTOMATION.md` | Hub A2 | primäre A2-Spec: Entry Point, Ablauf, Zustände, Abbruch, Recovery und Ende | Name klingt nach Übersicht, ist aber normativ gemeint | `KEEP`, aber im Kopf als `document_type: specification` kennzeichnen |
| `SCHEMA` | häufig in `O`, `F`, `M` | formaler Strukturvertrag für Daten oder Nachrichten | ist keine fachliche Voll-Spec und keine Beispieldatei | `QUALIFY`: `OUTPUT_SCHEMA`, `EVENT_SCHEMA`, `DATABASE_SCHEMA`; Format/Version nennen |
| `OUTPUT_SCHEMA` | `F`, `O` | maschinenprüfbare Struktur eines Outputs | sagt nichts über inhaltliche Qualität | `KEEP`: mit semantischen Akzeptanzkriterien ergänzen |
| `DATABASE_SCHEMA.sql` | Hub-Entwurf, `M`-Migrationspraxis | Tabellen, Relationen, Constraints und gegebenenfalls Views | darf nicht mit Datenbestand verwechselt werden | `KEEP`: migrationsfähige Quelle bestimmen |
| `CONFIG` / `CONFIGURATION` | ältere Verwendung in `O`, `M`, Community | historischer lokaler Überbegriff; technisch veränderbare Betriebswerte, die Verhalten parametrisieren | als lokaler Oberbegriff zu unscharf und seit längerem kaum verwendet | `LEGACY`: nicht als neue Hub-Hauptfamilie; konkrete Funktion wie `POLICY`, `SETTINGS`, `GUARDRAILS` oder `DATA` benennen |
| `DATA` | `F`, `M`, Hub-Entwurf | konkrete Datensätze oder Ereignisse | Dateiformat wird mit Semantik verwechselt | `QUALIFY`: `DATA.example.json`, `EVENTS.example.jsonl`; JSON/YAML allein sind keine Architekturtypen |
| `EXAMPLE` | überall | nicht normative Demonstration eines gültigen Falls | wird als Default oder Testfixture missverstanden | `KEEP`: im Namen `.example.`; nicht als Produktionsquelle verwenden |
| `FIXTURE` | `M`, Community | kontrollierte Testdaten mit erwarteter Verwendung | nicht bloss Beispiel | `KEEP`: unter Tests; deterministische Erwartung angeben |
| `TEMPLATE` | `F`, `O`, Hub-Library | ausfüllbarer Startartefakt mit Platzhaltern und Regeln | wird mit Blueprint und Beispiel vermischt | `KEEP`: erzeugt eine Instanz eines Artefakttyps |
| `BLUEPRINT` / `BAUPLAN` | `O`, `F`, Hub | Kompositionsrezept für mehrere Dateien, Module und Entscheidungen eines Systemtyps | `BAUPLAN` und `BLUEPRINT` doppeln sich; teils als Implementierungsplan benutzt | `DECIDE`, Empfehlung: `BLUEPRINT` kanonisch, `BAUPLAN` als auffindbarer Alias |
| `PATTERN` | Community, `F` | wiederkehrende Lösung mit Kontext, Kräften, Folgen und Gegenanzeigen | wird als blosses Beispiel oder Regel bezeichnet | `KEEP`: erst nach mehreren Evidenzen; kein Zwangsstandard |
| `MODULE` | Hub, Software-Community | eigenständig verständlicher und kombinierbarer Funktionsbaustein mit Contract | wird mit Package und beliebigem Ordner gleichgesetzt | `KEEP`: klare Schnittstelle, Abhängigkeiten und Version |
| `PACKAGE` | häufig in `F`, technisch in `M` | entweder distributierbare Softwareeinheit **oder** lokales Bündel zusammengehöriger Agent-/Control-Dateien | zwei verschiedene Bedeutungen | `QUALIFY`: `SOFTWARE_PACKAGE` vs `ROLE_BUNDLE`; für neue Hub-Bausteine bevorzugt `MODULE` |
| `LIBRARY` | Hub | kuratierter Bestand freigegebener, wiederverwendbarer Bausteine | kann Softwarebibliothek oder Ablageordner bedeuten | `LOCAL`: im Hub klar als kuratierte Architektur-Library definiert |
| `CATALOG` / `PERLENKATALOG` | `O`, `F` | auffindbare Liste von Kandidaten oder Assets | Katalogeintrag ist nicht automatisch freigegeben | `KEEP`: Status und Provenienz pro Eintrag; `PERLE` ist ein Kandidat, kein Standard |
| `PLACEHOLDER` | Hub-Mission | ausdrücklich offener, noch zu füllender Slot | kann versehentlich als fertiger Inhalt gelten | `KEEP`: maschinen- oder visuell eindeutig markieren; vor Release prüfen |
| `ARTIFACT` | Community, Hub | dauerhaftes Arbeitsprodukt: Datei, Spec, Report, Code, Datensatz | sehr breit | `KEEP` als Oberbegriff, nicht als präziser Dateiname |
| `SOURCE OF TRUTH` | implizit in Workspaces | die für einen bestimmten Sachverhalt autoritative, aktuell editierbare Quelle | mehrere Dateien beanspruchen denselben Rang | `QUALIFY`: immer Sachverhalt und Scope nennen; Kopien sind keine zweite Source of Truth |
| `PROVENANCE` / Genealogie | Hub-Mission | nachvollziehbare Herkunft, Transformation und Freigabe eines Bausteins | wird mit Version allein verwechselt | `KEEP`: Quelle, Datum/Version, Transformationen und Entscheide |

# 4. Prompts, Scripts, Tools und Ausführung

| Begriff | Gefundene Verwendung | Präzise Bedeutung | Konflikt | Empfehlung |
|---|---|---|---|---|
| `PROMPT` | stark in allen Workspaces | Instruktion oder Eingabe an ein Modell | kann Systemregel, Startbefehl, Template oder einmalige Nutzereingabe meinen | `QUALIFY`: Funktion im Namen nennen |
| `SYSTEM_PROMPT` | Community | höchstrangige modellseitige Instruktion einer Laufzeit | wird mit Projektmission verwechselt | `KEEP`: nur für tatsächliche Runtime-Instruktion |
| `DEVELOPER_PROMPT` | OpenAI-Terminologie | Instruktionsebene des Anwendungsentwicklers unterhalb System-/Plattformvorgaben | nicht providerübergreifend identisch | `QUALIFY`: Providerkontext nennen |
| `USER_PROMPT` | Community | konkrete Eingabe des Nutzers | kann Startsignal oder Arbeitsauftrag sein | `KEEP` |
| `STARTPROMPT` | sehr häufig in `F`, `M`; optional in Hub A2 | gespeicherter Prompt, mit dem ein dokumentierter Arbeitslauf gestartet wird | nicht jeder Entry Point ist ein Prompt | `KEEP` als mögliche Entry-Point-Art; niemals als universelle Pflichtdatei |
| `MASTERPROMPT` / `MASTER_PROMPT` | `F` | Prompt mit übergeordneter Steuerungsfunktion für einen ausdrücklich abgegrenzten Ablauf | der Name sagt ohne Scope nicht, wofür er Master ist | `KEEP AS PROMPT SUBTYPE`: Scope im Titel oder Frontmatter nennen; kein automatisch höherer Authority-Rang |
| `BRÜCKENPROMPT` / `BRIDGE_PROMPT` | lokale Promptfamilie | überträgt ausgewählten Kontext oder Arbeitsstand zwischen Phasen, Sessions oder Systemen | kann mit Handoff oder Context Dump verwechselt werden | `KEEP AS PROMPT SUBTYPE`: Quelle, Ziel, Auswahlregel und Verlustgrenzen nennen |
| `ÜBERGABEPROMPT` / `HANDOFF_PROMPT` | lokale Promptfamilie | beauftragt den nächsten Akteur und übergibt Artefakte, Status, offene Risiken und Annahmekriterien | ein Handoff besteht nicht nur aus Prompttext | `KEEP AS PROMPT SUBTYPE`: Prompt ist Transportartefakt; Handoff bleibt der Gesamtvorgang |
| `PROMPT_CARD` | `F` | Dossier zu Zweck, Variablen, Inputs, Outputs, Risiken und Tests eines Prompts | kann Prompt selbst oder Metadokument meinen | `QUALIFY`: Prompttext und Begleitkarte trennen |
| `PROMPT_TEMPLATE` | Community, `F` | parametrisierter Prompt mit definierten Variablen | nicht mit Blueprint gleichsetzen | `KEEP` |
| `ONE-SHOT` | lokal bisher teils für einen einmaligen Lauf; Community zusätzlich für genau ein In-Context-Beispiel | in der ML-/Prompt-Literatur meist: ein Demonstrationsbeispiel im Kontext | gefährliche Doppelbedeutung | `ONE-SHOT` für die Prompttechnik reservieren; die A1-Klasse heisst unabhängig von ihrer Nutzungsdauer `ONE-WAY` |
| `ONE-WAY` / `ONE_WAY_TOOL` | Hub A1 | lokaler Klassifikationsbegriff: verantwortet ein Ergebnis und besitzt keinen autonomen Validations-/Korrekturloop | kein etablierter Community-Begriff; sagt nichts über einmalige oder wiederholte Nutzung | `LOCAL + CANONICAL`: sichtbarer Klassenname `ONE-WAY`; technischer Bezeichner `ONE_WAY_TOOL` |
| `SCRIPT` | alle Workspaces | direkt ausführbare Folge deterministischer oder API-aufrufender Schritte | nicht jedes Script ist ein Agent-Tool; kann intern nicht deterministisch sein | `KEEP`: Runtime, Inputs, Outputs und Seiteneffekte dokumentieren |
| `TOOL` | alle Workspaces, MCP/OpenAI/Anthropic | lokal und umgangssprachlich: alles, was eine Funktion ausführt; in Agentensystemen zusätzlich eine modellaufrufbare Funktion/Fähigkeit | erst in technischen Verträgen entsteht eine relevante Doppelbedeutung | `LOCAL + KEEP`: im Chat als Oberbegriff zulässig; in Specs bei Kollisionsgefahr `APPLICATION_TOOL`, `AGENT_TOOL` oder `MCP_TOOL` präzisieren |
| `MCP TOOL` | Community | vom MCP-Server angebotene, modellkontrollierte ausführbare Funktion | nicht mit MCP Resource oder Prompt verwechseln | `KEEP`: MCP-Primitiv exakt benennen |
| `MCP RESOURCE` | Community | anwendungsverwalteter Kontextinhalt | keine ausführbare Funktion | `KEEP` |
| `MCP PROMPT` | Community | vordefiniertes, vom Nutzer auswählbares Prompt-Template | kein Systemprompt | `KEEP` |
| `HOOK` | `O`, `F`, `M` | registrierter Callback an einem definierten Lifecycle-Ereignis | wird als Trigger, Script oder allgemeiner Einstieg bezeichnet | `KEEP`: Event, Zeitpunkt, Payload, Seiteneffekt und Fehlerverhalten nennen |
| `TRIGGER` | Hub-Diskussion, Community | Bedingung oder Ereignis, das einen Lauf auslöst oder eine Pflicht aktiviert | bisher auch für Architekturmerkmale genutzt | `QUALIFY`: `RUNTIME_TRIGGER` vs `REQUIREMENT_TRIGGER` |
| `ENTRY POINT` | Hub A2, Software-Community | dokumentierte Schnittstelle, über die ein Lauf beginnt | kann Prompt, Hook, API, Schedule oder Befehl sein | `KEEP` als Oberbegriff |
| `SCHEDULE` | Community | zeitbasierter Trigger | kein Hook und kein Workflow | `KEEP` |
| `RUN` | Community | eine konkrete Ausführung von Start bis Stop/Ergebnis | wird mit Session oder Thread gleichgesetzt | `KEEP`: stabile Run-ID verwenden |
| `SESSION` | `O`, `F`, Community | zeitlich oder kontextuell abgegrenzte Interaktion mit eigenem Laufzeitkontext | Provider definieren Persistenz unterschiedlich | `QUALIFY`: lokale Sessiongrenze explizit definieren |
| `THREAD` | OpenAI/Codex, Community | persistierbarer Gesprächs- und Ereignisstrang; kann mehrere Turns/Runs enthalten | nicht allgemein dasselbe wie Session | `QUALIFY`: Provider-/Produktkontext nennen |
| `TURN` | `O`, Community | ein Interaktionszyklus mit Nutzer-/Agenteninput und resultierenden Aktionen/Antworten | kann mehrere Modellaufrufe enthalten | `KEEP`: nicht mit Run gleichsetzen |
| `SANDBOX` | OpenAI/Anthropic, `M` | kontrollierte Ausführungsumgebung mit begrenzten Ressourcen und Berechtigungen | wurde mit Konto oder Modell verwechselt | `KEEP`: Umgebung, nicht Account und nicht Provider |

# 5. Workflow, Pipeline, Automation, Agent und Harness

| Begriff | Gefundene Verwendung | Präzise Bedeutung | Konflikt | Empfehlung |
|---|---|---|---|---|
| `WORKFLOW` | `O`, `F`, Community | kanonischer technischer Begriff für eine logische Folge von Schritten, Zuständen und Übergängen | wird in Chats häufig Pipeline genannt | `LOCAL + CANONICAL`: technische Verträge und Tools verwenden `WORKFLOW` |
| `PIPELINE` | `F`, `M`, Community | lokaler umgangssprachlicher Ausdruck für einen Workflow; technisch enger auch gerichtete Daten-, Build- oder Deploymentstufen | Chatbegriff und technischer Spezialbegriff überlagern sich | `ALIAS`: in Chats frei verwendbar; in Specs nur als eigener technischer Typ, wenn der Stufenfluss wesentlich ist |
| `AUTOMATION` | Hub A2, `M` | ausführendes System, das einen vorgegebenen Ablauf bis zum definierten Endzustand steuert und maschinell validiert | Community nutzt den Begriff breiter; nicht jeder Workflow ist automatisiert | `KEEP` als Hub-Klasse; lokale A2-Definition sichtbar halten |
| `SYSTEM` | überall | abgegrenzte Menge zusammenwirkender Komponenten mit gemeinsamer Verantwortung | wird als Verstärkungswort gebraucht | `QUALIFY`: Systemgrenze und Verantwortung nennen |
| `AGENT` | `O`, `F`, `M`, Community | eigenständiger ausführender Akteur beziehungsweise eine isoliert gestartete Agenteninstanz, die mit Modell, Instruktionen und gegebenenfalls Tools einen Auftrag bearbeitet | ein Agent kann eine Persona verkörpern und eine Rolle übernehmen; dadurch werden die drei Begriffe nicht synonym | `KEEP`: bei dauerhaften Agenten Mission, Input/Output, Tools, Rechte, Grenzen, Übergabe und Stop-Bedingung dokumentieren |
| `ASSISTANT` | Nutzerbeschreibung, Community | nutzerorientierte Interaktionsfunktion; kann nicht-agentisch oder agentisch implementiert sein | wird automatisch als Agent interpretiert | `QUALIFY`: beschreibt Beziehung zum Nutzer, nicht die technische Autonomie |
| `ROLE` | Hub, `F`, `M` | begrenzte Funktion oder Verantwortung, die in einem Prompt einem HUMAN, Agenten oder Script-Actor zugewiesen wird | braucht keine eigene Laufzeitidentität | `KEEP`: Rolle beschreibt **was jemand in diesem Ablauf tut** |
| `PERSONA` | stark in `F`, unter anderem Perspektiven wie Schüler, Lehrperson oder Professor | definierte fachliche oder menschliche Perspektive, Prüflinse, Stimme und gegebenenfalls Verhaltensprofil | kann durch einen Agenten ausgeführt werden, ist aber selbst noch keine Laufzeitinstanz | `KEEP`: Persona beschreibt **aus welcher Perspektive gearbeitet wird**; Rechte und Authority separat festlegen |
| `SUBAGENT` | Community | separat ausgeführter Agent für eine abgegrenzte delegierte Teilaufgabe | kann Rolle, Tool-Agent oder Child-Process meinen | `QUALIFY`: eigener Kontext, eigene Tools/Authority und Rückgabecontract nennen |
| `MULTI-AGENT SYSTEM` | Hub A4-Diskussion, Community | mehrere eigenständige Agenten mit Koordination, Delegation oder Handoffs | mehrere Rollen in einem Prompt sind noch kein Multi-Agent-System | `KEEP`: Anzahl Laufzeitakteure, nicht Anzahl Rollennamen, entscheidet |
| `SINGLE-PROVIDER AGENT SYSTEM` | Hub A3 | lokaler A3-Klassenname für Agentensystem innerhalb eines Provider-Ökosystems | kann mehrere Modelle und Agenten enthalten; „single“ wird leicht falsch gelesen | `LOCAL + DECIDE`: Definition beibehalten oder `INTRA-PROVIDER AGENT SYSTEM` prüfen |
| `MULTI-PROVIDER SYSTEM` | Hub A4 | lokaler A4-Klassenname, wenn Produktions-/Prüfpfad eine Provider- oder unabhängige Modellfamiliengrenze überschreitet | Providerwechsel garantiert keine Unabhängigkeit oder Wahrheit | `LOCAL + DECIDE`: besser als Eigenschaft `PROVIDER-DIVERSE VALIDATION` präzisieren |
| `ORCHESTRATOR` | Community, Hub späterer Assembler diskutiert | wählt, startet und koordiniert Worker/Agents sowie Zusammenführung | wird mit Router oder Assembler verwechselt | `KEEP`: Laufzeitkoordination |
| `ROUTER` | `O`, Community | klassifiziert Input und wählt einen nächsten Pfad oder Empfänger | plant nicht zwingend den ganzen Ablauf | `KEEP` |
| `DISPATCHER` | Community | weist bereits definierte Arbeit einem Worker zu | nicht zwingend inhaltliche Auswahl oder Aggregation | `QUALIFY` |
| `COORDINATOR` | Community | sorgt für Reihenfolge, Synchronisation und gemeinsamen Zustand | unpräziser als Orchestrator | `QUALIFY`: konkrete Mechanik nennen |
| `ASSEMBLER` | Hub-Meta-Gruppe als spätere Produktrolle | stellt aus Library-Bausteinen ein Projekt-Setup zusammen | kann mit Orchestrator verwechselt werden | `LOCAL`: Komposition zur Entwicklungszeit, nicht Laufzeitsteuerung |
| `HANDOFF` | Community | Übergabe der aktiven Zuständigkeit an einen anderen Agenten | nicht dasselbe wie Tool-Aufruf oder Delegation mit Rückkehr | `KEEP`: Ownership-Wechsel explizit machen |
| `DELEGATION` | Community | Vergabe einer Teilaufgabe mit erwartetem Ergebnis an den Auftraggeber | kann als Handoff implementiert sein, muss aber nicht | `KEEP`: Rückkehr- und Ergebniscontract nennen |
| `AGENT LOOP` | OpenAI/Anthropic | wiederholter Zyklus aus Modellentscheidung, Tool-/Umweltaktion, Beobachtung und nächstem Schritt bis zur Stopbedingung | wird pauschal „Loop Engineering“ genannt | `KEEP`: konkrete Loop-Art und Stopbedingungen benennen |
| `EVALUATOR-OPTIMIZER LOOP` | Anthropic | Generator erzeugt, Evaluator bewertet, Feedback führt zu iterativer Verbesserung | wird mit beliebigem Retry verwechselt | `KEEP`: klare Bewertungskriterien und Iterationslimit erforderlich |
| `HARNESS` | vereinzelt in `F`, stark in aktueller Community | Laufzeit- und Steuerungsschicht um das Modell: Agent Loop, Tools, Kontext, Persistenz, Policies, Sandbox und Observability | wird als Agent selbst oder bloss Testharness verstanden | `KEEP`, aber `AGENT_HARNESS` bzw. `EVALUATION_HARNESS` qualifizieren |
| `FRAMEWORK` | Nutzerziel, Community | wiederverwendbarer Satz von Konzepten, Verträgen und Erweiterungspunkten | wird als Library, Tool oder fertiges System bezeichnet | `QUALIFY`: Der Hub ist Framework **und** Library; die Begriffe beschreiben verschiedene Aspekte |
| `RUNTIME` | Community, `M` | die ausführende Umgebung und Logik während eines Runs | wird mit Harness oder Sandbox gleichgesetzt | `KEEP`: Harness ist Steuerungsschicht; Sandbox ist isolierte Umgebung; Runtime ist Ausführungskontext |

# 6. Rollen und ihre Abgrenzung

## Agent, Persona und Rolle

Die Begriffe sind kombinierbar, aber nicht synonym:

```text
AGENT   = Wer oder was läuft eigenständig?
PERSONA = Aus welcher Perspektive arbeitet dieser Akteur?
ROLE    = Welche Funktion erfüllt er in diesem Ablauf?
```

Beispiel: Eine isolierte AI-Instanz ist der `AGENT`. Sie verwendet die
`PERSONA_SCHUELER` und übernimmt im aktuellen Prompt die `ROLE REVIEWER`.
Dass eine Persona als eigener isolierter Subagent gestartet wird, macht den
konkreten Lauf zum Agentenlauf; die wiederverwendbare Perspektivdefinition
bleibt trotzdem eine Persona.

| Bevorzugter Begriff | Gefundene Varianten | Verantwortung | Nicht dasselbe wie | Empfehlung |
|---|---|---|---|---|
| `ARCHITEKT` | `ARCHY`, `ARCHITECT` | analysiert Optionen, Grenzen und Trade-offs; dokumentiert Architekturentscheide | Developer, Approver | `ARCHITEKT` lokal beibehalten; `ARCHY` als persönlicher Agentenname, nicht als Rollenbegriff |
| `DEVELOPER` | `IMPLEMENTOR`, `BUILDER`, teils `COOK` | baut oder ändert Bausteine nach freigegebenen Specs und Standards | Architect, Reviewer | `DEVELOPER` als Oberrolle; `IMPLEMENTOR` für eng spec-treue Umsetzungsphase; Metaphern nicht in Normdateien |
| `REVIEWER` | viele `REVIEWER`-Dateien in `F` | prüft ein Artefakt anhand expliziter Kriterien und gibt Befunde/Empfehlung ab | Validator, Auditor, Approver | `KEEP`: Review kann HUMAN oder AI sein und ist nicht automatisch Freigabe |
| `VALIDATOR` | `VALIDATOR`, Claude-Validationen | führt eine definierte Validationsprüfung aus | Reviewer oder Auditor als spezielle Prüfmodi | `KEEP`: kanonische Qualitätsrolle im Hub |
| `VERIFIER` | im Translator-Ablauf als weiterer Prüfpass | lokales Synonym zu `VALIDATOR` | kein eigener Prüfarttyp im Hub | `ALIAS`: darf in Bestandsprojekten bleiben; neue Verträge bevorzugen `VALIDATOR` |
| `EVALUATOR` | `F`, Community | führt eine community-typische `EVAL` mit Fällen, Gradern und Metriken aus | allgemeiner Validator oder einmaliger Reviewer | `KEEP` als spezialisierte Validationsrolle |
| `GRADER` | AI-Eval-Community | wendet Bewertungslogik auf einen Eval-Fall an | vollständiger Evaluator/Reviewer | `KEEP`: Code-, HUMAN- oder LLM-Grader qualifizieren |
| `AUDITOR` | selten als Rolle, häufig `AUDIT` | führt ein grösseres, eigenständig gescoptes Validationsprojekt mit systematischer Evidenzprüfung durch | einzelner Review-Pass | `KEEP` als spezialisierte Validationsrolle |
| `OBSERVER` | `O`, `F` | beobachtet Runs/Ereignisse und protokolliert, ohne operative Ownership | Reviewer oder Controller | `KEEP`: darf nicht stillschweigend Entscheidungen treffen |
| `ADVISOR` / `ADVISER` | Nutzerbeispiel, `F` | gibt Empfehlungen ohne Entscheidungs- oder Ausführungsauthority | Architect oder Approver | `KEEP`: Schreibweise festlegen; Empfehlung `ADVISOR` für Dateinamen |
| `CURATOR` | Hub-Meta-Gruppe | pflegt Taxonomie, Provenienz, Versionen, Dubletten und Promotion in die Library | Reviewer oder Archivist | `KEEP` |
| `APPROVER` | Community | besitzt Freigabeauthority für einen definierten Entscheid | Reviewer | `KEEP`: kann Review übernehmen, aber Authority muss ausdrücklich sein |
| `HUMAN` | Hub | menschliche Authority, Prüfer oder Nutzer je nach Contract | pauschal „Human-in-the-loop“ | `QUALIFY`: `HUMAN_OWNER`, `HUMAN_REVIEWER`, `HUMAN_APPROVER`, `HUMAN_USER` |

## Rollen-Metaphern

`COOK`, `WAITER`, `CASHIER` und ähnliche Namen können in einem konkreten
Anwendungsmodell anschaulich sein. Im universellen Naming sind sie jedoch
keine Architekturrollen. Die Normdatei sollte zuerst die Funktion nennen,
zum Beispiel `FULFILLMENT_AGENT (Metapher: COOK)`.

# 7. Qualität, Validation und Fehlerbehandlung

| Begriff | Präzise Bedeutung | Konflikt im Bestand | Empfehlung |
|---|---|---|---|
| `CHECK` | einzelne Prüfung einer Bedingung | wird als Test, Validation oder Review bezeichnet | `KEEP` als neutraler Oberbegriff auf kleiner Ebene |
| `TEST` | ausführbarer Versuch mit definiertem Setup und erwartbarem Ergebnis | AI-Qualität wird mit wenigen Unit Tests gleichgesetzt | `KEEP`: Testart nennen, etwa Unit, Integration, Acceptance oder Smoke |
| `SMOKE TEST` | schneller, breiter Minimaltest, ob Kernfunktion grundsätzlich läuft | beweist keine vollständige Qualität | `KEEP` |
| `ACCEPTANCE TEST` | prüft explizite Akzeptanzkriterien aus Nutzer-/Businesssicht | wird mit Validationsbericht verwechselt | `KEEP` |
| `VALIDATION` | lokaler Oberbegriff für geplante Qualitätsprüfung, Gegenprüfung und Abnahme eines Artefakts, Ablaufs oder Systems | Community-Quellen können Validation enger verwenden | `LOCAL + CANONICAL`: oberste Qualitätsfamilie und bevorzugter Hub-Begriff |
| `VERIFICATION` | im Hub gleichbedeutend mit `VALIDATION` | externe V&V-Normen unterscheiden die Wörter teilweise | `ALIAS`: keine eigene Hub-Prüfart und keine zusätzliche Pflichtstufe daraus bauen |
| `REVIEW` | verbreitete operative Form einer Validation: HUMAN oder AI betrachtet ein Artefakt anhand von Kriterien und erzeugt Findings | ohne Kriterien leicht subjektiv | `KEEP`: häufiger, verständlicher Passname innerhalb der Validation |
| `EVAL` / `EVALUATION` | Community-Form der Validation mit Fällen oder Dataset, Gradern, Metriken und wiederholbaren Runs | wird lokal seltener verwendet | `KEEP`: Community-Begriff und spezialisierter Subtyp von Validation |
| `LLM-AS-JUDGE` | LLM-Grader für subjektive oder schwer deterministisch messbare Kriterien | wird als unabhängige Wahrheit behandelt | `QUALIFY`: Rubrik, Kalibrierung und Stichproben durch HUMAN/deterministische Checks |
| `AUDIT` | grösseres, eigenständig gescoptes Validationsprojekt mit systematischer Evidenz, mehreren Prüfschritten und Abschlussbericht | im Bestand selten und für umfangreiche AI-Prüfaufträge verwendet | `KEEP`: Subtyp von Validation; Scope, Kriterien, Evidenz und Abschluss nennen |
| `GATE` | Entscheidungsschwelle, die Fortsetzung blockiert oder erlaubt | jede Checkliste wird Gate genannt | `KEEP`: Entscheidung, Authority und Pass/Fail-Kriterien nennen |
| `CHECKLIST` | reproduzierbare Liste zu prüfender Punkte | kann informativ oder blockierend sein | `KEEP`: Kennzeichnung `advisory` oder `gate` |
| `RETRY` | erneute Ausführung derselben Operation nach definierter Bedingung | wird mit Recovery oder Self-Correction verwechselt | `KEEP`: Limit, Backoff und Idempotenz angeben |
| `RECOVERY` | Rückkehr in bekannten sicheren Zustand oder Fortsetzung ab Checkpoint nach bekanntem Fehler | wird pauschal Self-Healing genannt | `KEEP`: A2-tauglich, wenn Pfade vorgegeben sind |
| `SELF-CORRECTION` | System bewertet eigenes Ergebnis und passt innerhalb freigegebener Grenzen Lösungsweg oder Output an | kann verborgene Regeländerung meinen | `QUALIFY`: Grenzen, Kriterien, Iterationslimit und Eskalation festlegen |
| `SELF-HEALING` | autonome Diagnose und Wiederherstellung bei Laufzeitfehlern, häufig mit Zustands- oder Konfigurationsanpassung | als Marketingwort für Retry/Recovery verwendet | `AVOID` ohne echte Diagnose, autonome Massnahme und überprüfte Wiederherstellung |
| `IDEMPOTENT` | wiederholte gleiche Operation erzeugt keinen zusätzlichen unerwünschten Effekt | fälschlich als „liefert immer identischen Output“ verstanden | `KEEP`: Seiteneffekt-Eigenschaft, nicht Determinismus |
| `DETERMINISTIC` | gleicher relevanter Zustand und Input führen nach definierter Annahme zum gleichen Output/Verlauf | LLM-Aufruf macht viele Abläufe nicht deterministisch | `KEEP`: deterministische Checks von probabilistischen Komponenten trennen |
| `HUMAN-IN-THE-LOOP` | HUMAN ist ein notwendiger Schritt innerhalb des Ablaufs | wird für jede menschliche Verantwortung benutzt | `QUALIFY` |
| `HUMAN-ON-THE-LOOP` | HUMAN überwacht und kann eingreifen, ist aber nicht jeder Schritt | jüngerer, nicht überall einheitlicher Begriff | `QUALIFY`: Eingriffsrecht und Beobachtbarkeit konkret beschreiben |

## Lokale Validationshierarchie

Der Hub verwendet bewusst ein einfaches lokales Modell:

```text
VALIDATION (= VERIFICATION)
├── REVIEW   = einzelne oder wiederholte Prüfung mit Findings
├── EVAL     = community-typische, messbare Prüfung mit Fällen und Gradern
├── AUDIT    = grösseres Validationsprojekt mit systematischer Evidenz
├── TEST     = ausführbare Prüfung mit erwartetem Ergebnis
└── CHECK    = einzelne Bedingungsprüfung
```

`VERIFICATION` bleibt auffindbares Synonym, erzeugt aber weder eine zweite
Dateifamilie noch eine zusätzliche A-Stufe. Wenn ein Ablauf mehrere Prüfpasses
benötigt, werden diese nach ihrer Funktion benannt, beispielsweise
`BLIND_REVIEW`, `CROSS_PROVIDER_REVIEW`, `DIFF_CHECK` oder `SMOKE_TEST` — nicht
allein aufgrund ihrer Reihenfolge.

Externe Normen unterscheiden Validation und Verification teilweise. Diese
abweichende Community-Bedeutung wird beim Import externer Quellen vermerkt,
ändert aber die bewusst einfachere Hub-Terminologie nicht.

# 8. Modell-, Provider- und Kontextbegriffe

| Begriff | Präzise Bedeutung | Häufige Fehlannahme | Empfehlung |
|---|---|---|---|
| `LLM` | Large Language Model als Modellklasse | LLM, Produkt, Agent und Provider seien dasselbe | `KEEP`: konkrete Ebene nennen |
| `MODEL` | konkrete Modellbezeichnung oder -version | Anbieterwechsel sei Modellwechsel und umgekehrt | `QUALIFY`: Model-ID und Version/Snapshot, wenn relevant |
| `MODEL FAMILY` | technisch/verwandtschaftlich zusammengehörige Modelle | neue Version sei unabhängig trainiert | `QUALIFY`: behauptete Unabhängigkeit belegen, nicht vermuten |
| `PROVIDER` | Organisation oder Plattform, die Modell/API/Runtime bereitstellt | Providerwechsel garantiere unabhängige Validität | `KEEP`: Providerdiversität ist Evidenzdiversität, keine Wahrheitsgarantie |
| `PROVIDER ECOSYSTEM` | lokaler Sammelbegriff für Modelle, Tools und Laufzeit desselben Providers | unscharfe technische Grenze | `DECIDE`: für A3/A4 eine prüfbare Definition und Sonderfälle festlegen |
| `CONTEXT WINDOW` | Menge an Tokens, die das Modell bei einer Inferenz berücksichtigen kann | neue Session lösche Trainingseffekte oder garantiert Unabhängigkeit | `KEEP`: Kontextisolation von Modell-/Providerdiversität trennen |
| `CONTEXT` | alle für den aktuellen Modellaufruf bereitgestellten Informationen | wird mit Memory oder Chatverlauf gleichgesetzt | `QUALIFY`: `MODEL_CONTEXT`, `RUN_CONTEXT`, `BUSINESS_CONTEXT` |
| `CONVERSATION HISTORY` | frühere Nachrichten/Ereignisse, die einem Modell erneut bereitgestellt werden können | sei automatisch vollständige Langzeit-Memory | `KEEP` |
| `STATE` | expliziter maschinenlesbarer Zustand eines Workflows oder Systems | wird mit Kontext oder Memory gleichgesetzt | `QUALIFY`: Owner, Persistenz und Schema nennen |
| `MEMORY` | Community-Sammelbegriff für persistierte Information über Runs hinweg | kann Verlauf, Notizen, Profil, DB oder Knowledge Base bedeuten | `AVOID` unqualifiziert: `SESSION_MEMORY`, `AGENT_NOTES`, `USER_MEMORY`, `KNOWLEDGE_BASE` |
| `KNOWLEDGE BASE` | kuratierter oder indexierter Wissensbestand | ist nicht automatisch RAG und nicht automatisch Memory | `KEEP` |
| `RAG` | Retrieval-Augmented Generation: externe Information wird gesucht und dem Modell zur Generierung bereitgestellt | jede Dateisuche oder DB sei RAG | `KEEP`: Retrieval, Index, Zitier-/Provenienzpfad und Evaluation benennen |
| `GRAPH RAG` | RAG-Ansatz, der graphstrukturierte Entitäten/Beziehungen und daraus gewonnene Zusammenhänge nutzt | synonym zu Workflow-Graph oder Graph Engineering | `KEEP`: nur für Knowledge-Graph-basierte Retrieval-Architektur |
| `VECTOR DATABASE` | Speicher/Index für Vektoren und Ähnlichkeitssuche | notwendiger Bestandteil jedes RAG | `QUALIFY`: technische Option, nicht Definition von RAG |
| `EMBEDDING` | Vektorrepräsentation von Inhalt für Ähnlichkeit/ML-Verarbeitung | sei bereits Wissen oder Validierung | `KEEP` |

# 9. Aktuelle Engineering-Strömungen

Diese Begriffe beschreiben zugleich eine historische Erweiterung des
AI-Engineerings und heute parallel benötigte Gestaltungsebenen. Eine neue Ebene
ersetzt die vorherige nicht; der kontrollierte Gegenstand wird grösser:

```text
PROMPT  -> ein Modellaufruf und seine Instruktionen
CONTEXT -> die für eine Inferenz ausgewählte Informationswelt
HARNESS -> die ausführende Umgebung eines Agentenlaufs
LOOP    -> wiederholte Aktion, Prüfung, Korrektur und Stop
GRAPH   -> Organisation mehrerer Schritte, Loops, Agenten und Zustände
RUNTIME / GOVERNANCE -> sicherer Betrieb, Policies, Beobachtung und Evolution
```

| Begriff | Community-Bedeutung | Reife/Mehrdeutigkeit | Empfehlung für den Hub |
|---|---|---|---|
| `PROMPT ENGINEERING` | Schreiben und Strukturieren von Modellinstruktionen für bessere Ergebnisse | etabliert, aber enger als Gesamtsystemdesign | `KEEP`: Prompts, Beispiele, Variablen und Ausgabeinstruktionen |
| `CONTEXT ENGINEERING` | Auswahl, Strukturierung und laufende Pflege aller modellrelevanten Informationen: Instruktionen, Tools, externe Daten und History | etablierender Begriff mit guter Primärdefinition | `KEEP`: umfasst Prompt Engineering, ersetzt es nicht |
| `HARNESS ENGINEERING` | Gestaltung der ausführenden Umgebung und Feedbacksysteme um Agenten: Loop, Tools, Regeln, Repo-Legibility, Tests, Observability, Recovery | 2026 stark aufkommend, noch nicht überall identisch verwendet | `KEEP` als eigener Bereich; lokale Definition festschreiben |
| `SPEC-DRIVEN DEVELOPMENT (SDD)` | Specs definieren das Was vor dem Wie; strukturierte Schritte tragen Intent bis Planung, Tasks, Implementierung und Konvergenz | mehrere Varianten: spec-first, spec-anchored, spec-as-source | `KEEP`: pro Blueprint das Persistenzmodell ausdrücklich wählen |
| `EVAL-DRIVEN DEVELOPMENT` | Entwicklung gegen wiederholbare Evals, Fälle, Grader und Metriken | verbreitet in AI-Systemen, kein Ersatz für Specs | `KEEP`: Spec sagt Soll, Eval misst beobachtete Leistung |
| `AGENT ENGINEERING` | breite Gestaltung von Agent, Tools, Harness, Evals und Betrieb | sehr weiter Oberbegriff | `QUALIFY`: nicht statt konkreter Disziplinen verwenden |
| `LOOP ENGINEERING` | Entwurf von Agentenschleifen, die selbständig planen beziehungsweise entscheiden, handeln, beobachten, prüfen, korrigieren und an einer definierten Bedingung stoppen | 2026 als eigenständige Methodik etabliert sich sichtbar; einzelne Loop-Typen bleiben zu präzisieren | `KEEP`: historische und methodische Ebene nach Harness Engineering; Stop, Budget, Validation, Recovery und Eskalation gehören zwingend dazu |
| `GRAPH ENGINEERING` | Entwurf expliziter, zustandsbehafteter Graphen aus Aufgaben, Agenten, Übergängen, Gates und Abhängigkeiten für komplexe Agentensysteme | jüngste und noch formende Ebene; kollidiert sprachlich mit Knowledge-Graph-Arbeit | `KEEP`: im AI-Entwicklungsstack meint der unqualifizierte Begriff den Agent-/Workflow-Graph; bei Wissensgraphen ausdrücklich `KNOWLEDGE GRAPH ENGINEERING` schreiben |
| `RUNTIME ENGINEERING` | sicherer und zuverlässiger Produktionsbetrieb agentischer Systeme: Identität, Berechtigungen, Isolation, Ressourcenbudgets, Persistenz, Observability, Skalierung und Recovery | Kandidat für die nächste Erweiterung; noch kein allgemein bestätigter Nachfolger | `PROPOSED`: als sechste Betriebsebene beobachten, noch nicht als historische Gewissheit festschreiben |
| `AGENTOPS` / `GOVERNANCE ENGINEERING` | Lifecycle, Policies, Evals, Monitoring, Audit, Incident Response und kontrollierte Verbesserung produktiver Agentensysteme | überlappt Runtime Engineering und bestehende MLOps/LLMOps-Praxis | `PROPOSED`: mögliche nächste Organisations- und Governance-Ebene; zunächst getrennt dokumentieren |
| `WORKFLOW GRAPH` | Workflow als Knoten, Kanten/Transitionen und gemeinsamem Zustand | frameworkspezifische Details variieren | `KEEP`: nicht mit Knowledge Graph verwechseln |
| `KNOWLEDGE GRAPH` | Entitäten und Beziehungen als Graph für Wissensrepräsentation und Abfragen | nicht automatisch Agentenworkflow | `KEEP` |
| `VIBE CODING` | Entwicklung mit starkem AI-Output und wenig expliziter Spezifikation/Detailkontrolle; Bedeutungen schwanken | kultureller, nicht normativer Begriff | `AVOID` in Standards; höchstens als Kontrastbegriff in Analysen |

# 10. Konstruktion und Control — lokale Altbegriffe

| Begriff | Fundort/Verwendung | Problem | Empfehlung |
|---|---|---|---|
| `CONSTRUCTION` | `O`, `F`: willkürlich gewählter Eigenname des thematischen Bereichs, in dem geplant, entwickelt und gebaut wird | als Eigenname zulässig; wäre als universeller Funktionstyp zu breit | `LOCAL + KEEP`: Name des vorhandenen Bereichs, keine allgemeine Architekturklasse und keine Pflichtbenennung für neue Projekte |
| `CONTROL` | `O`, `F`: Mission Control, Observer Control, Construction Control | kann Governance, UI-Steuerung, Quality Control oder Laufzeitcontroller meinen | `AVOID` allein; immer Funktionspräfix und Authority nennen |
| `MISSION_CONTROL` | `F` | Ordnungs- und Steuerungsebene für Agenten, Packages und Aufträge | klingt nach Runtime-Orchestrator, enthält aber auch Governance-Dateien | `LOCAL + DECIDE`: entweder klar als Governance-Hub definieren oder in `GOVERNANCE`/`ORCHESTRATION` trennen |
| `PACKAGE_CORE` | `O`, `F` | Bündel zentraler Agent-/Workflow-Dateien | Package ist technisch anders besetzt | `ALIAS`: im Hub in `MODULE_CORE` oder konkreten Blueprint überführen |
| `QUALITY_REVISION` | `F` | kombinierter Review-, Korrektur- und Publikationsablauf | mischt Aktivität, Rolle und Systemname | `QUALIFY`: Workflow-Name zulässig; Teilrollen separat definieren |
| `DIALOGFLOW` | `O` | lokale Bezeichnung eines Dialog-/Bauablaufs | kollidiert mit Google-Produktname und ist funktional unklar | `AVOID` für neue generische Komponenten; konkreten Workflow benennen |

# 11. Konfliktregister mit Empfehlung

| ID | Konflikt | Warum relevant | Empfehlung | HUMAN-Entscheid |
|---|---|---|---|---|
| `N-01` | `PINWALL` vs `BOARD` | überlappende Steuerungsfunktion, zwei Wahrheiten möglich | `PINWALL.md` empfohlen; `BOARD.md` Legacy-Alias; `DECISIONS.md` bleibt dauerhafte Entscheidungsquelle | Empfehlung zur Bestätigung |
| `N-02` | `MISSION` vs `README` | Zweck und Einstieg werden vermischt | beide zulassen, Funktionen strikt trennen | offen |
| `N-03` | `CONSTITUTION` vs `CONVENTIONS` | künstliche Hierarchie oder doppelte Regeln | Constitution nur für oberste unverhandelbare Prinzipien | offen |
| `N-04` | `AGENT` vs `ROLE` vs `PERSONA` | falsche Autonomie, Rechte und Dateipflichten | Agent = ausführender Akteur; Persona = Perspektive; Role = Funktion im Prompt/Ablauf | entschieden |
| `N-05` | `DEVELOPER` vs `IMPLEMENTOR` vs `BUILDER` | drei Namen für teils gleiche Rolle | Developer Oberbegriff; Implementor enge Ausführungsrolle | offen |
| `N-06` | `REVIEWER` vs `VALIDATOR` vs `VERIFIER` vs `EVALUATOR` vs `AUDITOR` | Qualitätsrollen wurden teils synonym und teils als Passreihenfolge benutzt | `VALIDATOR` Oberrolle; `VERIFIER` Alias; Reviewer, Evaluator und Auditor sind spezialisierte Prüfrollen | entschieden |
| `N-07` | `VALIDATION` vs `VERIFICATION` | externe V&V-Terminologie unterscheidet sie, lokal erhöht das die Komplexität | im Hub synonym; `VALIDATION` kanonisch, `VERIFICATION` Alias | entschieden |
| `N-08` | `WORKFLOW` vs `PIPELINE` vs `AUTOMATION` vs `SYSTEM` | technische und umgangssprachliche Verwendung überlappt | `WORKFLOW` ist technischer Standardbegriff; `PIPELINE` in Chats umgangssprachlicher Alias, ausser bei echten Daten-/Build-Pipelines | teilweise entschieden |
| `N-09` | `TOOL` als Produkt vs Agent Tool | zentral für Meta-Library und MCP | umgangssprachlicher Oberbegriff bleibt; nur in technischen Verträgen bei Bedarf qualifizieren | entschieden |
| `N-10` | `SPEC` vs `SCHEMA` vs `CONFIG` vs `DATA` | lokale Dateifamilie und semantische Dokumenttypen überlagern sich | `SPECS/` als Markdown-Steuerungsfamilie; semantischen Typ zusätzlich ausweisen; `CONFIG` nicht als neue Hauptfamilie | teilweise entschieden |
| `N-11` | `POLICY` vs `CONVENTION` vs `GUARDRAIL` | Textregel wird mit Enforcement verwechselt | Convention=Arbeitsstandard; Policy=entscheidbare Regel; Guardrail=Laufzeitmechanismus | offen |
| `N-12` | `STARTPROMPT` vs `ENTRY POINT` | Hook/API/Schedule passen nicht in Prompt-Spalte | Entry Point als Oberbegriff; Startprompt nur eine Variante | bestätigt, dokumentieren |
| `N-13` | `ONE-SHOT` vs einmalige Ausführung | Community liest One-shot oft als ein Beispiel | A1 heisst `ONE-WAY`; `ONE-SHOT` bleibt Prompttechnik oder beschreibender Bestandsbegriff | entschieden |
| `N-14` | `ONE-WAY` | lokaler, extern nicht automatisch bekannter Klassenname | Definition im A1-Skelett mitführen | entschieden |
| `N-15` | A3 `SINGLE-PROVIDER` | „single“ klingt nach einem Agenten oder Modell | `INTRA-PROVIDER AGENT SYSTEM` als Alternative prüfen | offen |
| `N-16` | A4 `MULTI-PROVIDER` | Providerwechsel ist nur Proxy für Perspektivdiversität | Eigenschaft `PROVIDER-DIVERSE VALIDATION` ergänzen; Unabhängigkeit nicht behaupten | offen |
| `N-17` | `MEMORY` | mindestens vier verschiedene technische Bedeutungen | unqualifizierten Begriff verbieten | offen |
| `N-18` | `GRAPH ENGINEERING` | Agent-/Workflow-Graph und Knowledge Graph kollidieren | als AI-Engineering-Ebene übernehmen; Wissensgraph immer qualifizieren | entschieden |
| `N-19` | `LOOP ENGINEERING` | mehrere Loop-Arten liegen innerhalb derselben Methodik | als AI-Engineering-Ebene übernehmen; konkrete Implementierung zusätzlich benennen | entschieden |
| `N-20` | `PACKAGE` vs `MODULE` | lokale Rollenbündel kollidieren mit Software-Packages | im Hub `MODULE`; alte Packages als Legacy-Alias | offen |
| `N-21` | `BAUPLAN` vs `BLUEPRINT` vs `PLAN` | drei Planungsebenen | Blueprint=Kompositionsvorlage; Plan=konkretes Vorgehen; Bauplan=Alias | offen |
| `N-22` | `CONSTRUCTION` und `CONTROL` | unspezifische Namen ausserhalb ihres lokalen Kontexts | `CONSTRUCTION` als vorhandenen Bereichsnamen behalten; `CONTROL` weiterhin qualifizieren | teilweise entschieden |
| `N-23` | `SELF-HEALING` vs `RECOVERY` | Marketingbegriff hebt A2 unnötig in A3-Nähe | A2 nutzt Recovery; Self-Healing nur bei echter autonomer Diagnose | offen |
| `N-24` | `same model`, `new session`, `different model`, `different provider` | vier verschiedene Unabhängigkeitsgrade wurden sprachlich vermischt | getrennte Metadatenfelder und keine pauschale „independent validation“ | offen |

# 12. Vorläufige Dateinamens-Empfehlung

Noch nicht vollständig normativ. Die Regeln werden gemäss dem versionierten
Änderungsmodell am Anfang dieser Datei fortlaufend ergänzt und angepasst:

1. Hub-eigene normative Dateien verwenden `UPPER_SNAKE_CASE.ext`.
2. Extern etablierte Reserved Names bleiben unverändert: `README.md`,
   `AGENTS.md`, `CLAUDE.md`.
3. Rollenverträge verwenden `AGENT_<NAME>.md` oder `ROLE_<NAME>.md` nur,
   wenn wirklich ein separater Contract existiert.
4. Singular für einen Gegenstand: `MISSION.md`, `NAMING.md`,
   `VALIDATION.md`.
5. Plural für Regelsammlungen: `CONVENTIONS.md`, `GUARDRAILS.yaml`.
6. Beispiele tragen `.example.` und dürfen nicht die produktive Source of Truth
   sein.
7. Ein Dateiname beschreibt die Funktion. Funktionsbezogene Promptnamen wie
   `MASTERPROMPT`, `STARTPROMPT`, `BRÜCKENPROMPT` und `ÜBERGABEPROMPT` sind
   zulässig, sofern ihr Scope im Promptvertrag erklärt wird. Unspezifisches
   `MAIN_*`, `FINAL_*` oder `CONTROL.*` erhält dagegen eine Präzisierung.
8. Datum oder Version ersetzt keinen Status. Archivstände gehören in Git oder
   einen ausdrücklich benannten Snapshot-/Archive-Bereich.
9. Umbenennungen erfolgen über `CANONICAL`, `ALIAS` und `DEPRECATED`; keine
   bestehende Quelle wird nur zur kosmetischen Vereinheitlichung massenhaft
   umgeschrieben.

# 13. Primärquellen zur Community-Terminologie

- OpenAI, [Design agents](https://developers.openai.com/api/docs/guides/agents/define-agents): Agent als Modell + Instruktionen + optionale Tools, Guardrails, Handoffs und strukturierte Outputs.
- OpenAI, [Evaluate your agent](https://developers.openai.com/api/docs/guides/agent-evals): Traces, Grader, Datasets und Eval Runs.
- OpenAI, [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): Workflow-, Single-Agent- und Multi-Agent-Komplexität sowie Human-, Metric- und LLM-Evals.
- OpenAI, [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents): Agent Loop aus Modellaufruf, Tool-Ausführung, Handoff und Stopbedingung.
- OpenAI, [Agents API architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture): Harness, Environment und Application Server als getrennte Systemteile.
- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Abgrenzung von vordefinierten Workflows und dynamisch entscheidenden Agents; Prompt Chaining, Routing, Parallelization, Orchestrator-Workers und Evaluator-Optimizer.
- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): Prompt Engineering versus fortlaufende Kuratierung des gesamten Modellkontexts.
- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): Eval, Transcript, Outcome, Grader und Evaluation/Agent Harness.
- GitHub Spec Kit, [What is Spec-Driven Development?](https://github.github.com/spec-kit/concepts/sdd.html): Spec vor Implementierung, Intent vor How und mehrstufige Verfeinerung.
- GitHub Spec Kit, [Spec Persistence Models](https://github.github.com/spec-kit/concepts/spec-persistence.html): `spec-first`, `spec-anchored` und `spec-as-source`.
- Model Context Protocol, [Server overview](https://modelcontextprotocol.io/specification/draft/server/index): MCP Prompts, Resources und Tools mit unterschiedlichen Kontrollmodellen.
- Microsoft Research, [GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/): GraphRAG als Kombination aus LLM-abgeleiteten Knowledge Graphs, Netzwerkanalyse, Retrieval und Generierung.
- Originale RAG-Arbeit, [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401).
- NIST, [Validation glossary](https://csrc.nist.gov/glossary/term/validation) und [Verification and Validation](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=150040): etablierte, wenn auch domänenabhängig variierende V&V-Unterscheidung.
- LangGraph, [Thinking in LangGraph](https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph): Workflow-Graph mit Nodes, Transitions, Shared State und Checkpoints.
- IBM, [What is Loop Engineering?](https://www.ibm.com/think/topics/loop-engineering): Loop Engineering als entstehende Praxis für iterative Agentenworkflows mit Act, Observe, Decide und Iterate.
- Feng et al., [Graph Engineering in the Era of LLM Agents](https://arxiv.org/abs/2608.21156): historische Folge Prompt, Context, Harness und Loop sowie Graph Engineering für Aufgaben-, Agenten- und Zustandsgraphen.

# 14. Empfohlene Reihenfolge der Besprechung

1. `PINWALL / BOARD / DECISIONS` endgültig bestätigen;
2. Reichweite der lokalen `SPECS/`-Familie festlegen;
3. A3 `SINGLE-PROVIDER` und A4 `MULTI-PROVIDER` bestätigen;
4. `PACKAGE / MODULE` und `BAUPLAN / BLUEPRINT / PLAN` entscheiden;
5. danach die Dateimatrix aktualisieren.

Diese Reihenfolge beginnt bei den Begriffen, die die meisten nachfolgenden
Spalten und Verantwortlichkeiten beeinflussen.
