---
document_id: ah-mission
title: Architecture Hub Mission
status: DRAFT
version: 1.0.0-draft
created_at: 2026-09-29T22:58:59+02:00
updated_at: 2026-09-30T21:43:00+02:00
authority: HUMAN_APPROVAL_REQUIRED
architecture_skeleton: 1.0.0-draft
---

# AH MISSION

## ZWECK

Der `ARCHITECTURE_HUB` verhindert, dass bei jedem Projekt wieder bei null
begonnen wird. Er sammelt die besten wiederverwendbaren Perlen aus Dokumenten,
Chats, Workspaces und realen Entwicklungen und konzentriert sie in einer
universellen Architektur-Library.

Die Library enthält nicht nur einzelne Regeln, sondern auch Anleitungen,
Entscheidungshilfen, Standards, Module, Checklisten, Blueprints, Templates,
Beispiele und bewusst markierte Platzhalter. Sie kann Projekt- und Tooltypen
unterscheiden und für einen konkreten Auftrag die passenden Bausteine als
begründeten Startpunkt bereitstellen.

Beispiel: Für den Auftrag «Baue ein Tool, das die Dateien in Ordner X
normalisiert» liefert der Hub nicht ein starres Master-Tool. Er wählt aus der
Library die geeigneten Standards, Scripts, Specs, Schemas, Security-Gates und
Prüfungen für genau diesen Auftrag aus.

Der Hub unterstützt damit die Sichtung, Präsentation und Interpretation von
Quellen, die Protokollierung von Entscheiden, die Auswahl übertragbarer
Bausteine und den Bau von SPECS, Tools und Automationen. Er ist selbst kein
Master-Tool für eine einzelne Arbeit, sondern die wiederverwendbare
Architekturquelle für viele unterschiedliche Arbeiten.

## Warum der Hub existiert

Wertvolle Muster, Specs, Templates, Scripts, Checklisten, Beispiele und
Entscheidungshilfen sind heute über Projekte, Dokumente, Chats und Workspaces
verteilt. Der Hub macht diese Perlen auffindbar, vergleichbar, testbar und
wiederverwendbar. Bewährte Erkenntnisse aus neuen Projekten fliessen
kontrolliert zurück.

## Die Library als kuratierte All-Star-Auswahl

Die `ARCHITECTURE_HUB_LIBRARY` ist eine orchestrierte Best-of-Auswahl von
Bausteinen, mit denen neue Systeme gebaut werden. Einige Bausteine sind
universell einsetzbar, andere gelten nur für bestimmte Fachgebiete,
Projektarten oder Architekturstufen. Die Auswahl soll HUMAN und KI dabei
helfen, für eine Aufgabe den passenden Dateityp, das passende Werkzeug und
die passende Ausführungsart zu wählen.

Erkenntnisse aus Projekten werden nicht direkt in die Library geschrieben.
Feedback von aussen gelangt zuerst in einen Entwicklungs-Briefkasten. Dort
wird es mit Quelle und Kontext geprüft, mit dem Bestand verglichen und erst
nach einem positiven Entscheid als Library-Kandidat weitergeführt.
Bestehende Bausteine werden zudem regelmässig sowie durch konkrete Ereignisse
ausgelöst überprüft, kuratiert, verbessert, abgelöst oder begründet belassen.

## CYCLE OF LIFE

Die Library ist zugleich Startpunkt und Rückkehrpunkt jeder Entwicklung:

```text
ARCHITECTURE_HUB_LIBRARY
  -> passende Architekturstufe bestimmen
  -> Grunddateien und notwendige Zusatzbausteine auswählen
  -> Tool, Automation oder System entwickeln
  -> real einsetzen und prüfen
  -> Lessons Learned getrennt erfassen
  -> universellen Kern kuratieren und reviewen
  -> freigegebene Verbesserung versioniert in die Library zurückführen
  -> nächste Entwicklung startet mit der verbesserten Library
```

Dabei gilt:

1. **Start aus der Library.** Eine Entwicklung verwendet zuerst vorhandene
   Standards, Module, Checklisten und Blueprints, bevor Neues gebaut wird.
2. **Projektspezifisch entwickeln.** Die konkrete Entwicklung darf die
   Library nicht nebenbei verändern. Sie arbeitet in ihrem eigenen Scope.
3. **Erfahrung sichern.** Am Ende werden Erfolge, Fehler, fehlende Bausteine,
   Umwege und neue Muster als Lessons Learned festgehalten.
4. **Nicht alles zurückspielen.** Projektspezifische Details bleiben im
   Projekt. Nur der nachweislich übertragbare Kern wird Library-Kandidat.
5. **Prüfen und entscheiden.** KURATOR und REVIEWER prüfen Provenienz,
   Universalität, Grenzen, Dubletten und Evidenz; wirksame Promotion benötigt
   den zuständigen HUMAN-Entscheid.
6. **Versioniert zurückführen.** Neue oder verbesserte Bausteine gelangen mit
   Genealogie, Version und Rückweg in die Library.

So wird jede Entwicklung zum möglichen Lernlauf für den Hub, ohne dass die
Library zum ungeprüften Ablageordner wird.

## Der Hub ist

- eine kuratierte Bibliothek mit Provenienz und Versionen;
- eine Entwicklungswerkbank für neue oder verbesserte Bausteine;
- ein Entscheidungsraum mit kurzen Architecture Decision Records;
- eine Quelle für reproduzierbare Projekt- und Tool-Architekturen;
- ein Lernkreislauf zwischen universeller Library und realer Anwendung.

## Der Hub ist nicht

- kein Master-Tool, das jedem Projekt dieselbe Struktur aufzwingt;
- kein ungeprüfter Ablageordner für interessante Dateien;
- kein Ersatz für projektspezifische Fachentscheide;
- kein einzelner Agent und kein einzelner Chat;
- keine Authority allein aufgrund von Plausibilität oder KI-Urteil.

## Leitprinzipien

1. **Artefakte tragen das Gedächtnis.** Chats und Agents sind
   Arbeitsoberflächen; versionierte Dateien halten den dauerhaften Stand.
2. **Provenienz vor Übernahme.** Jeder Baustein bleibt bis zur Quelle und zum
   HUMAN-Entscheid nachvollziehbar.
3. **Universell bedeutet begrenzt übertragbar.** Jeder Baustein nennt
   Anwendungsbedingungen, Grenzen und Gegenanzeigen.
4. **Prüfung vor Promotion.** Kein Kandidat gelangt ohne definierte Kriterien
   und nachvollziehbares Review in die Library.
5. **Komposition statt Monolith.** Neue Systeme werden aus passenden,
   kompatiblen Bausteinen zusammengestellt.
6. **Realer Einsatz liefert Evidenz.** Rückfluss verändert die Library nur
   nach erneuter Kuratierung und Prüfung.
7. **So wenig Tooling wie nötig.** Automatisierung folgt wiederholbarer
   Mechanik; sie wird nicht vorsorglich gebaut.

# ARCHITEKTUR-SKELETT 1.0 — DRAFT

## Zweck des Skeletts

Das Skelett ordnet Systeme nicht nach Laufzeit, Lebensdauer, Öffentlichkeit,
Wiederverwendbarkeit oder Anzahl technischer Schritte. Es ordnet sie nach der
Verantwortung des Systems sowie nach der Grenze seiner Validation.

Die A-Stufe wird immer für einen **konkreten Workflow oder eine konkrete
Systemgrenze** bestimmt. Ein Repository darf mehrere Stufen enthalten. Ein
A1-Tool kann Teil einer A2-Automation sein; ein Projekt kann eine
A2-Laufzeitautomation und zugleich einen A4-Entwicklungsprozess enthalten.

## Die vier Architekturstufen

| Stufe | Name | Verantwortet | Validation | Harte Grenze |
|---|---|---|---|---|
| **A1** | **ONE_WAY-TOOL** | ein Ergebnis | HUMAN prüft und korrigiert Prompt oder Script | kein autonomer Validations- oder Korrekturloop |
| **A2** | **AUTOMATION** | einen vorgegebenen Ablauf bis zu einem definierten Endzustand | einfache maschinelle Validation | System steuert und validiert den festgelegten Ablauf |
| **A3** | **SINGLE-PROVIDER AGENT SYSTEM** | ein begrenztes Ziel | Validation in neuer, isolierter Session innerhalb desselben Provider-Ökosystems | Sessiongrenze wird überschritten, Providergrenze nicht |
| **A4** | **MULTI-PROVIDER SYSTEM** | ein providerübergreifendes Ziel- und Validationssystem | Produktion, Validation oder Verifikation durch unterschiedliche Provider beziehungsweise unabhängige Modellfamilien | mindestens eine Provider- oder Modellfamiliengrenze wird überschritten |

## A1 — ONE_WAY-TOOL

Ein A1 ONE_WAY-TOOL erbringt ein Ergebnis. Es kann intern viele technische
Schritte enthalten und kurz oder jahrelang verwendet werden. Der HUMAN prüft
das Ergebnis. Passt es nicht, korrigiert der HUMAN den Prompt oder das Script
und startet erneut.

**Benötigt:**

- `PROMPT*.md` und/oder ausführbares `SCRIPT.*`.

**Optional:**

- `SCHEMA.*`;
- `AGENTS.md`;
- `CLAUDE.md`.

**Spezialregel:**

- `[REPEAT]` macht `MISSION.md` erforderlich.

**Typische Anwendungen:**

- Dateien normalisieren;
- Text klassifizieren;
- Metadaten extrahieren;
- Dateinamen vereinheitlichen;
- einen ONE-SHOT-PROMPT ausführen.

## A2 — AUTOMATION

Eine A2 AUTOMATION übernimmt nach einem dokumentierten Entry Point einen
vorgegebenen Ablauf und führt ihn kontrolliert bis zu einem definierten
Endzustand. Der Entry Point kann ein `STARTPROMPT`, ein Hook, ein Zeitplan, ein
API-Aufruf, ein manueller Befehl oder ein Ereignis eines anderen Systems sein.
Er wird in `AUTOMATION.md` dokumentiert; deshalb existiert keine allgemeine
Pflichtdatei `HOOK.md`.

Eine A2-Automation:

- besitzt einen ausdrücklich definierten Startpunkt und Endzustand;
- verantwortet Reihenfolge, Übergaben und bekannte Verzweigungen;
- validiert ihren Endzustand maschinell;
- macht Erfolg, Abbruch und Fehler unterscheidbar;
- verfügt über eine `PINWALL.md` als aktuelle Entwicklungssteuerung; ein
  bestehendes `BOARD.md` kann dieselbe Funktion erfüllen, aber beide werden
  nicht parallel als aktuelle Wahrheit geführt;
- dokumentiert das Verhalten bei wiederholtem Start;
- ist möglichst idempotent oder schützt vor unbeabsichtigter
  Doppelverarbeitung;
- verwendet begrenztes, zustandsbewusstes Self-Healing und RECOVERY innerhalb
  des freigegebenen Ablaufs.

Jeder abgeschlossene Abschnitt endet mit einem bestätigten Output, der
zugleich als Checkpoint oder Milestone dient; beide Begriffe werden hier
synonym verwendet. Wird die Operation zwischen
ENTRY und diesem Output unterbrochen, setzt sie beim letzten bestätigten
Output fort, statt den gesamten Ablauf am Anfang neu zu starten. RECOVERY darf
begrenzte Wiederholungen, Quarantäne eines fehlerhaften Elements, Rückkehr in
einen sicheren Zustand und Eskalation an den HUMAN umfassen. Self-Healing
erkennt bekannte Zustände, bewahrt gültiges Vorhandenes und ergänzt oder
repariert nur innerhalb des definierten Vertrags. Unbekannte Fehler stoppen
oder eskalieren; sie erlauben keine freie Veränderung des Lösungswegs.

**Benötigt:**

- `MISSION.md`;
- `AUTOMATION.md`;
- ausführbares `SCRIPT.*`;
- `NAMING_LOCAL.md`;
- `VALIDATION.md`;
- `CONVENTIONS.md`;
- `PINWALL.md`.

**Optional:**

- `STARTPROMPT.md`;
- `SCHEMA.*`;
- `AGENTS.md`;
- `CLAUDE.md`;
- `SPRACHREGELN.md`;
- `GUARDRAILS.yaml`;
- `DATA.example.json` oder `DATA.example.jsonl`;
- `DATABASE_SCHEMA.sql`.

## A3 — SINGLE-PROVIDER AGENT SYSTEM

Ein A3-System besteht aus einem oder mehreren Agenten beziehungsweise Rollen,
die innerhalb desselben Provider-Ökosystems arbeiten. Es verantwortet ein
begrenztes Ziel und darf innerhalb seiner freigegebenen Grenzen den Lösungsweg
wählen oder anpassen.

Produktion und Validation erfolgen in getrennten Sessions. Der Validator
erhält vorzugsweise nur das zu prüfende Artefakt, die Spezifikation, die
Validationskriterien und notwendige Quellen. Eine neue Session reduziert
Kontextverankerung, beseitigt aber keine provider- oder trainingsbedingten
blinden Flecken.

A3 erlaubt begrenzte Self-Correction: Ergebnis prüfen, Ursache einer
Abweichung untersuchen, einen zulässigen alternativen Weg wählen, begrenzt
erneut versuchen und danach an den HUMAN eskalieren. Eigener Code,
`GUARDRAILS` oder Authorities dürfen nicht autonom verändert werden.

Ein **AGENT** ist ein eigenständiger Akteur mit Mission, Input, Output,
Rechten, Grenzen, Übergabe und Stop-Bedingung. Eine **ROLE** ist eine begrenzte
Funktion oder Perspektive innerhalb eines Agenten oder Workflows. Separate
Dateien `AGENT_<NAME>.md` und `ROLE_<NAME>.md` sind optional; ihre Verträge
können in der Systemspezifikation stehen.

## A4 — MULTI-PROVIDER SYSTEM

Ein A4-System verteilt Produktion, Validation oder Verifikation auf Modelle
verschiedener Provider beziehungsweise unabhängiger Modellfamilien. Beispiele
sind «OpenAI baut, Anthropic validiert» oder «GPT übersetzt, Claude validiert,
GPT verifiziert».

Der Providerwechsel erhöht die Diversität der Prüfung, garantiert aber keine
Wahrheit. Deterministische Checks und HUMAN-Authority bleiben bestehen. Die
Konflikt- und Entscheidungsregeln werden nicht durch die A-Stufe festgelegt;
sie leben versioniert in `CONVENTIONS.md` und den anwendbaren Agentenverträgen.

Bei lokal betriebenen Modellen zählt die unabhängige Modellfamilie und nicht
der technische Hosting-Ort.

## Trennfragen

1. **A1 oder A2:** Prüft erst der HUMAN das Ergebnis, oder kontrolliert und
   validiert das System den Ablauf bis zu seinem Endzustand?
2. **A2 oder A3:** Ist der Lösungsweg vorgegeben, oder darf das System ihn
   innerhalb definierter Grenzen selbst wählen oder verändern?
3. **A3 oder A4:** Bleiben Produktion und Validation innerhalb desselben
   Provider-Ökosystems, oder wird eine Provider- beziehungsweise unabhängige
   Modellfamiliengrenze überschritten?

Nicht entscheidend sind Laufzeit, Wiederholbarkeit, Lebensdauer,
Öffentlichkeit, Anzahl technischer Schritte oder Anzahl benannter Rollen.

## Datei-Matrix 1.0

Die Matrix führt **Dateifamilien**, nicht nur starre Dateinamen. Eine konkrete
Datei darf projektspezifisch benannt sein, muss aber einer Funktion eindeutig
zugeordnet werden können. `●` bedeutet Pflicht, `○` optional, `—` nicht Teil
der Grundausstattung und `[REPEAT]` Pflicht bei beabsichtigter Wiederverwendung.

### Kern und Steuerung

| Dateifamilie | A1 | A2 | A3 | A4 | Funktion |
|---|:---:|:---:|:---:|:---:|---|
| `MISSION.md` | `[REPEAT]` | ● | ● | ● | Zweck, Grenzen und Erfolg |
| `PROMPT*.md` | `●¹` | ○ | ● | ● | ausführbarer oder steuernder KI-Auftrag |
| `SCRIPT.*` / Source Code | `●¹` | ● | ○ | ○ | deterministische Ausführung oder Orchestration |
| `AUTOMATION.md` | — | ● | ○ | ○ | Entry Point, Ablauf, Zustände und Endzustand |
| `AGENT_SYSTEM.md` | — | — | ● | ● | Ziel, Agenten-/Rollenstruktur, Sessions und Loops |
| `MULTI_PROVIDER.md` | — | — | — | ● | Providergrenzen und Übergaben |
| `PINWALL.md` / funktionales `BOARD.md` | ○ | ● | ● | ● | aktueller Stand und Entwicklungssteuerung |
| `NAMING_LOCAL.md` | ○ | ● | ● | ● | lokale Namen, IDs und Pfadregeln |
| `CONVENTIONS.md` / `CONVENTION.md` | ○ | ● | ● | ● | verbindliche Arbeits- und Authority-Regeln |
| `VALIDATION.md` | — | ● | ● | ● | Prüfkriterien, Status und Endzustände |
| `GUARDRAILS.yaml` | ○ | ○ | ● | ● | maschinenlesbare Grenzen |
| `SECURITY.md` | ○ | ○ | ● | ● | Risiken, Rechte, Daten und Schutzmassnahmen |

`¹` A1 benötigt mindestens einen ausführbaren Kern: `PROMPT` und/oder
`SCRIPT`; beide zusammen sind erlaubt, aber nicht zwingend.

### Verträge, Agenten und Daten

| Dateifamilie | A1 | A2 | A3 | A4 | Funktion |
|---|:---:|:---:|:---:|:---:|---|
| `SPECS/*.md` / `SPEC_*.md` | ○ | ○ | ○ | ○ | zusätzliche fachliche oder technische Verträge |
| `SCHEMA.*` | ○ | ○ | ○ | ○ | Strukturvertrag für Ein-, Aus- oder Übergaben |
| `STARTPROMPT.md` | ○ | ○ | ○ | ○ | promptbasierter Entry Point |
| `AGENTS.md` / `CLAUDE.md` | ○ | ○ | ○ | ○ | werkzeug- oder providerbezogene Projektinstruktionen |
| `AGENT_<NAME>.md` | ○ | ○ | ○ | ○ | separater Agentenvertrag |
| `ROLE_<NAME>.md` | ○ | ○ | ○ | ○ | separate Rollenbeschreibung |
| `SPRACHREGELN.md` | ○ | ○ | ○ | ○ | Sprache, Ton und Terminologie |
| `CONFIG.*` | ○ | ○ | ○ | ○ | Laufzeitkonfiguration ohne Geheimnisse |
| `DATA.example.json` / `.jsonl` | ○ | ○ | ○ | ○ | ungefährliche Beispieldaten oder Austauschmuster |
| `DATABASE_SCHEMA.sql` | ○ | ○ | ○ | ○ | initiale Datenbankstruktur ohne Echtdaten |
| `migrations/*.sql` | ○ | ○ | ○ | ○ | versionierte Datenbankänderungen |
| `INDEX.*` / `MANIFEST.*` | ○ | ○ | ○ | ○ | Inventar, Identität und Zusammensetzung |

`SPECS` sind ausdrücklich nicht abgeschafft. `AUTOMATION.md`,
`AGENT_SYSTEM.md` und `MULTI_PROVIDER.md` sind bereits primäre Specs ihrer
Stufe. Zusätzliche Specs werden verwendet, wenn weitere Verträge nicht sauber
in diese Kerndateien passen.

### Prüfung, Kontinuität und Governance

| Dateifamilie | A1 | A2 | A3 | A4 | Funktion |
|---|:---:|:---:|:---:|:---:|---|
| `tests/*` / `TEST_*.md` | ○ | ○ | ○ | ○ | ausführbare oder dokumentierte Tests |
| `EVALS.md` / Eval-Dateien | ○ | ○ | ● | ● | systematische Bewertung nichtdeterministischer Qualität |
| `HANDOFF.md` | ○ | ○ | ● | ● | verbindlicher Fortsetzungskontext zwischen Sessions |
| `LOG.jsonl` / `JOURNAL.md` | ○ | ○ | ● | ● | append-only Evidenz und Verlauf |
| `REPORT*.md` / Validation Reports | ○ | ○ | ○ | ○ | Ergebnis einer Prüfung oder eines Laufs |
| `ADR_*.md` / `DECISIONS_LOG.md` | ○ | ○ | ○ | ○ | Architektur- und HUMAN-Entscheide |
| `WORK_TICKET.md` / `BAUPLAN.md` / `PLAN.md` | ○ | ○ | ○ | ○ | begrenzter Entwicklungsauftrag und Bauplan |
| `README.md` / `INSTALL.md` | ○ | ○ | ○ | ○ | Einstieg, Verwendung und Installation |
| `LICENSE.md` / `CONTRIBUTING.md` | ○ | ○ | ○ | ○ | rechtliche und kollaborative Regeln |
| `LESSONS_LEARNED.md` | ○ | ○ | ○ | ○ | Rückflusskandidaten für die Library |
| `SOURCES.md` / Provenienzdateien | ○ | ○ | ○ | ○ | Quellen, Herkunft und Nutzungsgrenzen |

### Betrieb, Auslieferung und Fachartefakte

| Dateifamilie | A1 | A2 | A3 | A4 | Funktion |
|---|:---:|:---:|:---:|:---:|---|
| Hook-, Scheduler- oder Plugin-Dateien | ○ | ○ | ○ | ○ | konkrete technische Entry Points |
| Deployment- und Dependency-Dateien | ○ | ○ | ○ | ○ | Build, Installation und Auslieferung |
| `INPUT`, `SOURCE`, `FIXTURE` | ○ | ○ | ○ | ○ | fachliche Eingaben und Testmaterial |
| `OUTPUT`, `ARTIFACT`, `REPORT` | ○ | ○ | ○ | ○ | erzeugte Ergebnisse und Evidenz |
| `ASSETS` und Medien | ○ | ○ | ○ | ○ | Bilder, Audio, Video und Darstellungsdateien |
| Runtime-State, Checkpoints und Locks | ○ | ○ | ○ | ○ | flüchtiger oder wiederaufnehmbarer Betriebszustand |
| Archiv, Snapshot und Backup | ○ | ○ | ○ | ○ | historische oder wiederherstellbare Stände |

Runtime-Daten, Caches, virtuelle Umgebungen, vendorte Abhängigkeiten und
generierte Binaries sind keine Architekturpflichten. Sie werden einer
Betriebs- oder Artefaktfamilie zugeordnet und grundsätzlich nicht nur deshalb
in die Matrix aufgenommen, weil sie in einem alten Projekt vorhanden sind.

## Regeln gegen Redundanz

1. `MISSION.md` erklärt das **Warum**; `README.md` erklärt Einstieg und Nutzung.
2. `VALIDATION.md` definiert den Prüfvertrag; Tests und Evals führen ihn aus;
   Reports speichern Evidenz.
3. `SCHEMA` definiert Struktur; `CONFIG` setzt Verhalten; `GUARDRAILS` setzen
   Grenzen; `DATA` enthält Payloads oder Beispiele.
4. `AUTOMATION.md`, `AGENT_SYSTEM.md` und `MULTI_PROVIDER.md` sind primäre
   stufenspezifische Specs. Zusätzliche Specs dürfen sie nicht duplizieren.
5. `PINWALL.md` ist die aktuelle Sicht. Ein bestehendes `BOARD.md` darf als
   funktionales Äquivalent dienen. Beide werden nicht parallel als aktuelle
   Wahrheit geführt. Logs und Journale sind Verlauf, nicht zweite Pinwall.
6. `AGENTS.md` und `CLAUDE.md` steuern Werkzeuge im Projekt. `AGENT_<NAME>.md`
   beschreibt einen Akteur; `ROLE_<NAME>.md` beschreibt eine Funktion.
7. Zentral versionierte `NAMING_LOCAL.md` und `CONVENTIONS.md` werden verlinkt, wo
   dies zuverlässig möglich ist. Lokale Dateien sind versionierte Snapshots,
   Ergänzungen oder bewusst dokumentierte Abweichungen.
8. Echtdaten, Secrets und persönliche Inhalte werden nicht als
   `DATA.example.*` ausgegeben und nicht in öffentliche Repositories
   übernommen.

## Erfolg

Der Hub ist erfolgreich, wenn ein neuer Auftrag schneller zu einer
begründeten, testbaren Architektur führt und zugleich sichtbar bleibt:

- welche Architekturstufe für welchen Workflow gilt;
- welche Bausteine verwendet wurden;
- weshalb sie passen;
- welche Alternativen verworfen wurden;
- welche projektspezifischen Lücken offen sind;
- welche Erfahrungen später in die Library zurückfliessen dürfen.
