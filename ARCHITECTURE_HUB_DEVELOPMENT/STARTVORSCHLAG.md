---
document_id: architecture-hub-startvorschlag
title: Startvorschlag fuer Architecture Hub V0
status: DRAFT
version: 0.1.0
created_at: 2026-09-29T22:32:46+02:00
authority: HUMAN_APPROVAL_REQUIRED
---

# Startvorschlag fuer Architecture Hub V0

## 1. Zielbild

`ARCHITECTURE_HUB` ist eine Meta-Bibliothek fuer bewaehrte,
wiederverwendbare Architekturbausteine. Sie ist kein Master-Tool und erzeugt
nicht fuer jedes Projekt dieselbe Architektur. Sie stellt aus einem konkreten
Projektauftrag ein begruendetes, pruefbares Set passender Bausteine zusammen.

Der Kreislauf lautet:

```text
Quelle
  -> Kandidat mit Provenienz
  -> HUMAN-Auswahl
  -> normalisierter Bibliotheksbaustein
  -> validierte Promotion
  -> projektspezifische Komposition
  -> realer Einsatz und Evidenz
  -> Verbesserung oder neuer Kandidat
```

## 2. Kein Vorab-Grossbau

Vor der Meta-Library wird kein zweites grosses Tool gebaut. Fuer V0 genuegt
eine kleine, dateibasierte Werkbank mit klaren Vertraegen. Automatisierung
folgt erst dort, wo ein wiederholter mechanischer Schritt nachweisbar ist.

Auch ein einzelner Agent ist nicht die Architektur. Vier eigenständige
Rollenverträge trennen die Funktionen mit dauerhaftem Dateizustand:

- `AH_AGENT_ARCHITEKT.MD`;
- `AH_AGENT_DEVELOPER.MD`;
- `AH_AGENT_REVIEWER.MD`;
- `AH_AGENT_KURATOR.MD`.

Diese Rollen koennen je nach Risiko nacheinander von einem Agenten oder von
mehreren Actors ausgefuehrt werden. Getrennte Agents sind dort notwendig, wo
unabhaengiges Review oder echte Parallelisierung einen Vorteil hat. Ein
ASSEMBLER wird erst spaeter als Produkt der Library entwickelt.

## 3. Zwei getrennte Bereiche

### `ARCHITECTURE_HUB_LIBRARY`

Nur freigegebener, wiederverwendbarer Nutzbestand:

- Bibliothekskatalog;
- typisierte Architekturbausteine;
- Projektprofile und Kompositionsregeln;
- Vorlagen;
- Referenzbeispiele und Tests;
- Release-Manifest.

### `ARCHITECTURE_HUB_DEVELOPMENT`

Die Werkbank und nachvollziehbare Entstehung:

- Quellenregister und Sichtungsprotokolle;
- Kandidaten und HUMAN-Entscheide;
- Deduplikation und Konfliktanalyse;
- Entwuerfe, Promotion-Reports und Validation;
- Kompositionsexperimente;
- Rueckfluss aus Projekten.

## 4. Kleinste sinnvolle Bibliothekseinheit

Eine "Perle" wird nicht nur als guter Satz gespeichert. Ein nutzbarer
Baustein braucht mindestens:

- stabile ID und Typ;
- Problem und beabsichtigten Nutzen;
- Regel oder Muster;
- Anwendungsbedingungen;
- Grenzen und Gegenanzeigen;
- Provenienz bis zur Quelle;
- Reifegrad und Entscheidstatus;
- benoetigte Schnittstellen zu anderen Bausteinen;
- beobachtbare Abnahme oder Testevidenz.

Nur so kann ein spaeterer Composer begruenden, warum ein Baustein fuer ein
`NORMALIZE_TOOL` passt oder nicht passt.

## 5. Komposition statt Kopieren

Ein Projektauftrag wird zuerst in ein `PROJECT_PROFILE` uebersetzt. Fuer das
Beispiel "Dateien in Ordner X normalisieren" enthaelt es unter anderem:

- Ziel und Nicht-Ziele;
- Quelltypen und Schutzklassen;
- erlaubte Mutationen;
- Idempotenz- und Rollbackbedarf;
- Fehlerlokalitaet;
- Nachweis- und HUMAN-Gates;
- erwartete Outputs.

Der Composer liefert danach kein loses Prompt-Konvolut, sondern ein
`ASSEMBLY_MANIFEST`: ausgewaehlte Bausteine, Auswahlgruende, verworfene
Alternativen, Abhaengigkeiten, offene Luecken und die daraus gebauten SPECS.

## 6. Bruecke zum lokalen `/SYSTEM`

`ARCHITECTURE_HUB` entwickelt und kuratiert. `/SYSTEM` betreibt. Deshalb:

1. Rohquellen und Kandidaten bleiben im Development-Bereich.
2. Freigegebene universelle Bausteine werden in den Content-Bereich promoted.
3. Ein konkretes Systemwerkzeug wird ueber CONSTRUCTION gebaut und validiert.
4. `/SYSTEM` erhaelt nur den fuer den Betrieb notwendigen freigegebenen
   Vertrag, Skill, Hook, Schema, Script oder die Vorlage.
5. Projekterfahrung fliesst als Evidenz zurueck, nicht als ungepruefte Regel.

## 7. 90-Minuten-Ziel fuer V0

### Minute 0-15: Vertrag und Taxonomie

- Ziel, Grenzen und Authority festziehen.
- Bausteintypen und Reifegrade definieren.
- Minimales Quellen- und Provenienzschema festlegen.

### Minute 15-35: Seed-Katalog

- Bereits bestaetigte Perlen aus dem vorhandenen Perlenkatalog deduplizieren.
- Kleine repräsentative Auswahl als echte Bibliothekseintraege normalisieren.
- Offene Kandidaten klar ausserhalb des Nutzbestands halten.

### Minute 35-55: Composer-Vertrag

- `PROJECT_PROFILE` und `ASSEMBLY_MANIFEST` spezifizieren.
- Auswahl-, Ausschluss- und Konfliktregeln definieren.
- Ausgabeform fuer ein SPEC-Paket festlegen.

### Minute 55-70: Chats bibliothekarisieren

- Ein Intake-Verfahren fuer Chat-Exporte definieren.
- Original, Interpretation, Kandidat und HUMAN-Entscheid trennen.
- Wiederholbare Ernte in `/SYSTEM` als kleine Betriebsfunktion vorbereiten.

### Minute 70-85: End-to-End-Probe

- Ein `NORMALIZE_TOOL` aus dem Seed-Katalog komponieren.
- Manifest, SPECS und Lueckenbericht erzeugen.
- Auswahl gegen Auftrag und Quellen pruefen.

### Minute 85-90: Abschluss

- HUMAN zeigt die V0-Artefakte und den einen naechsten Schritt.
- Offene Fragen und bewusst nicht gebaute Automatisierung festhalten.
- Nur belegte neue Perlen in die Rueckfluss-Warteschlange geben.

## 8. Abnahme fuer V0

V0 ist gut genug, wenn:

1. Content und Development nicht vermischt sind.
2. Jeder freigegebene Baustein Quelle, Grenzen und Status besitzt.
3. Ein Auftrag nachvollziehbar zu einem Assembly-Manifest fuehrt.
4. Das Beispielpaket keine stillen oder unbelegten Regeln enthaelt.
5. Ein Chat in Kandidaten ueberfuehrt werden kann, ohne ihn zur Authority zu
   machen.
6. Der Rueckfluss aus Projekten als eigener Promotion-Prozess beschrieben ist.
7. `/SYSTEM` nicht durch unfertige Library-Entwuerfe veraendert wurde.

## 9. Erster HUMAN-Entscheid

Freigabe oder Revision dieses Startvorschlags. Danach beginnt der 90-Minuten-
Lauf mit dem Bibliotheksvertrag und einer kleinen Seed-Auswahl; nicht mit einer
vollstaendigen Migration aller Quellen.
