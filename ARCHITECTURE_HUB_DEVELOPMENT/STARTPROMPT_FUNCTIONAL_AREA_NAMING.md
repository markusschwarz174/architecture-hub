---
document_id: ah-startprompt-functional-area-naming
title: Startprompt — Functional Area Naming
status: READY_FOR_USE
version: 1.0.0
created_at: 2026-09-30
scope: terminology review and file-type skeleton design
---

# STARTPROMPT — FUNKTIONSBEREICH BEARBEITEN

## Verwendung

Ersetze vor dem Start genau diesen Platzhalter:

```text
{FUNKTIONSBEREICH}
```

Zulässige Bereiche sind aktuell:

```text
MISSION
DEVELOPMENT
WORKFLOW
CONTRACT
TOOLING
QUALITY
```

## Startprompt

```text
Du arbeitest im Projekt ARCHITECTURE_HUB am vorgegebenen Funktionsbereich:

{FUNKTIONSBEREICH}

ZIEL

Wir entscheiden gemeinsam, welche Begriffe aus der GLOBAL LIBRARY als
eigenständige lokale Dateitypen für diesen Funktionsbereich tragfähig sind.
Danach entwickeln wir für jeden bestätigten Dateityp ein grobes
Begriffsskelett. Dieses Skelett benennt mögliche oder verpflichtende Inhalte
und kann später als Grundstruktur der Datei dienen.

WICHTIGE TRENNUNG

Unterscheide während der gesamten Arbeit strikt:

1. GLOBAL TERM
   Ein Begriff oder eine Systematik aus NAMING_LIBRARY.md, Community,
   professioneller Praxis oder den Sources.

2. FILE TYPE
   Ein durch HUMAN bestätigter lokaler Dateityp mit eigenständiger Funktion,
   zum Beispiel MISSION.md. Nicht jeder Begriff wird ein Dateityp.

3. TAG
   Ein Such- und Zuordnungsbegriff. Ein TAG macht Themen und verwandte
   Begriffe auffindbar. Er ist weder automatisch ein Dateityp noch automatisch
   eine Kapitelüberschrift.

4. HEADING
   Eine strukturelle Überschrift innerhalb eines Dateityps. Sie kann einen
   thematischen Begriff tragen oder generisch sein, zum Beispiel INPUT,
   OUTPUT, STATUS oder REFERENCES. Eine HEADING muss nicht aus einem TAG
   abgeleitet sein.

TAG und HEADING sind unabhängige Achsen. Derselbe Begriff kann nach
HUMAN-Entscheid beides sein. Bei MISSION sind die bestätigten TAGS zugleich
Kapitelüberschriften. Daraus folgt keine globale Regel für andere Dateitypen.

VERBINDLICHE GRUNDLAGEN

Lies zuerst:

- ARCHITECTURE_HUB_DEVELOPMENT/AH_MISSION.MD
- ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LIBRARY.md
- ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md
- die aktuellen Git-Änderungen und die letzten relevanten Entscheide

NAMING_LIBRARY.md ist die Brücke zur externen Welt. NAMING_LOCAL.md wird erst
durch HUMAN-Entscheide zur lokalen Authority. Die sechs Funktionsbereiche sind
eine bewusst subjektive lokale Ordnung und keine universelle Taxonomie.

VORGEHEN

A — BEGRIFFE IN DER GLOBAL LIBRARY SUCHEN

- Ermittle alle Begriffe und externen Systematiken, die funktional zum
  vorgegebenen Bereich passen könnten.
- Berücksichtige AI-Community, professionelle Softwareentwicklung,
  Grossunternehmen, Forschung, Standards und Herstellerterminologie.
- Nutze bei zeitabhängigen oder unsicheren Community-Begriffen aktuelle
  Primärquellen.
- Vermische noch keine externen Begriffe mit lokalen Entscheidungen.

B — GESAMTLISTE UND FILE-TYPE-VORSCHLAG ERSTELLEN

Erstelle eine prüfbare Gesamtliste mit mindestens:

- Begriff;
- Herkunft oder Verwendungskontext;
- kurze funktionale Bedeutung;
- als eigenständiger lokaler FILE TYPE geeignet: JA, NEIN oder OFFEN;
- Begründung;
- bei NEIN: wahrscheinliche Verwendung als TAG, ALIAS oder Begriff eines
  anderen Funktionsbereichs.

Schlage danach die kleinste tragfähige Menge lokaler Dateitypen vor. Vermeide
Synonymdateien, Doppelbehälter und Marmor-Strukturen.

GATE 1 — HUMAN-AI-DISKUSSION

Stoppe nach Schritt B. Stelle die vorgeschlagenen Dateitypen, Konflikte und
offenen Entscheide zur Diskussion. Schreibe noch nichts als kanonisch in
NAMING_LOCAL.md. Fahre erst nach dem HUMAN-Entscheid fort.

C — HUMAN-AI-DISKUSSION

- Kläre Funktion und Abgrenzung jedes vorgeschlagenen Dateityps.
- Entscheide, welche Begriffe FILE TYPE, ALIAS oder TAG werden.
- Halte ausdrücklich fest, welche Kandidaten verworfen oder in einen anderen
  Funktionsbereich verschoben werden.

D — BEGRIFFSSKELETT PRO BESTÄTIGTEM DATEITYP

Gib jedem bestätigten Dateityp eine noch nicht abschliessende Inhaltsstruktur:

- mögliche oder verpflichtende TAGS;
- vorgeschlagene Kapitelüberschriften;
- kurze Funktion jedes Kapitels;
- Pflicht oder optional;
- klare Abgrenzung zu anderen Dateitypen und Funktionsbereichen.

Erzeuge keine zusätzliche Datei nur deshalb, weil ein Inhalt einen eigenen
Namen besitzt.

E — SOURCE HARVEST

Suche in den freigegebenen Sources gezielt nach Perlen, die zu den bestätigten
Dateitypen und ihrem Begriffsskelett passen.

Mindestquellen, sofern vorhanden und zugänglich:

- FIELD_NOTES_DRAFT einschliesslich relevanter Archive;
- MY_AI_PROJECTS;
- AI_PROJECTS einschliesslich OPENAI und ARCHITECTURE_HUB;
- weitere vom HUMAN genannte Sources.

Für jeden Fund erfasse mindestens:

- SOURCE;
- LOCATION;
- EXTRACT oder präzise Zusammenfassung;
- Zuordnung zu FILE TYPE und TAG;
- WHY_RELEVANT.

In dieser Phase nicht deduplizieren, nicht qualitativ bewerten und nicht als
universell erklären. Sources nicht verändern oder löschen. Kopien im späteren
CONSTRUCTION-Bereich dürfen nur nach eigener HUMAN-Freigabe entfernt werden,
wenn das Original ausserhalb weiterhin vorhanden ist.

F — STAND DES SOURCE-CHECKS

Berichte transparent:

- welche Source-Wurzeln durchsucht wurden;
- welche Dateitypen und Formate einbezogen wurden;
- welche Suchmethoden und Suchbegriffe verwendet wurden;
- Anzahl und Verteilung der Treffer;
- welche zentralen Dateien zusätzlich semantisch gelesen wurden;
- bekannte Lücken, nicht zugängliche Quellen und Unsicherheiten;
- ob der Check mechanisch, stichprobenartig oder semantisch vollständig war.

Behaupte niemals „alle Perlen gefunden“, wenn dies nicht nachweisbar ist.

GATE 2 — HUMAN-AI-DISKUSSION

Stoppe nach dem Source-Check erneut. Präsentiere:

1. die bestätigten oder noch offenen Dateitypen;
2. das Begriffsskelett jedes Dateityps;
3. Widersprüche aus den Sources;
4. vorgeschlagene Ergänzungen, Verschiebungen oder Streichungen;
5. den Stand und die Grenzen des Source-Checks.

Erst der HUMAN bestätigt das vorläufige lokale Ergebnis.

ZIELZUSTAND

Am Ende besitzt der Funktionsbereich:

- einen oder mehrere klar abgegrenzte lokale Dateitypen;
- pro Dateityp ein grobes Begriffsskelett;
- bestätigte ALIASES und TAGS;
- dokumentierte Nicht-Zuordnungen und Konflikte;
- nachvollziehbare Perlen mit Provenienz;
- einen ehrlichen Stand des Source-Checks.

ARBEITSREGELN

- Funktion vor Begriff.
- Dateityp und Inhalt niemals vermischen.
- TAG und HEADING nicht voneinander ableiten; Überschneidungen ausdrücklich
  durch HUMAN entscheiden.
- Keine neue Datei ohne eigenständige Funktion.
- Keine parallelen Sources of Truth.
- Keine stillen Umdeutungen bestehender Begriffe.
- Bei Unsicherheit offen markieren statt plausibel erfinden.
- Ergebnisse auf Deutsch erklären; technische kanonische Namen bleiben in der
  vereinbarten englischen Schreibweise.

Beginne jetzt mit Schritt A für {FUNKTIONSBEREICH} und liefere anschliessend
Schritt B. Stoppe danach an GATE 1.
```
