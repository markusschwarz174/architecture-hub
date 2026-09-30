# Architecture Hub

> **Status:** Aktiver Aufbau. Teile der Bibliothek und mehrere Rollen- und
> Prozessbeschreibungen befinden sich noch im Entwurfs- oder Prüfstatus.

Über die Monate hinweg sind bei mir viele Projekte entstanden und später
wieder in Vergessenheit geraten. In jedem Projekt entstehen tolle Ideen, und
mit der Zeit entwickeln sich die Projekte weiter. Doch eines ist bei jedem
Projekt gleich: Ich beginne immer wieder bei null.

## Wozu dient dieses Repository?

Mit dem Architecture Hub will ich eine kuratierte Sammlung wiederverwendbarer
Architekturbausteine aufbauen, die ich für AI-gestützte Arbeitsabläufe und
Projekte nutzen kann.

Mit den Bausteinen in der Bibliothek kann ich Pakete zusammenstellen, die auf
meine Projekte zugeschnitten sind und Erfahrungen aus früheren Projekten in
sich tragen. Bewährte Bausteine kommen erneut zum Einsatz. Gleichzeitig
entstehen in den Projekten neue oder verbesserte Bausteine, die zurück in die
Bibliothek fliessen.

So entsteht ein Kreislauf. Ich beginne nicht mehr bei null.

## S*AI*DSTEP Learning

Während der Arbeit an meinen Projekten begegne ich immer wieder Fragen: Was
bedeutet dieser Begriff? Wie funktioniert jenes Tool? Was erzählt mir ChatGPT
da gerade?

Dann stehe ich vor dem Dilemma, ob ich die Frage ignorieren oder vertiefen
soll. Praktisch immer gehe ich ihr auf den Grund – und zwar im gleichen Chat.
Das führt irgendwann dazu, dass das Kontextfenster überladen ist.

Ich möchte diese Lerngelegenheiten während der Arbeit besser nutzen, indem ich
solche Themenwechsel – ChatGPT nennt sie „Sidesteps“ – strukturiert in den
Arbeitsprozess integriere. Dazu will ich meine Werkzeuge aus meinem Unterricht
nutzen und einen automatisierten, AI-geführten Lernpfad bauen.
Dabei entscheide ich über Dauer, Schwierigkeitsgrad, Entwicklungshorizont
und anschliessende Umsetzung im Projekt.

## Aufbau

| Bereich | Zweck |
| --- | --- |
| `ARCHITECTURE_HUB_LIBRARY/` | Kuratierter Nutzbestand mit Architekturbausteinen, Vorlagen und Standards |
| `ARCHITECTURE_HUB_DEVELOPMENT/` | Entwicklungswerkstatt für Quellen, Kandidaten, Entwürfe, Audits und Promotion |
| `ARCHITECTURE_HUB_ASSETS/` | Grafiken und weitere unterstützende Medien |
| `PROJECT_INFO.yaml` | Identität, Status und Grunddaten des Projekts |
| `PROJECT_BOARD.md` | Aktueller Stand, Entscheidungen, offene Fragen und nächste Schritte |
| `PROJECT_LOG.jsonl` | Vorgesehene fortlaufende Projektaufzeichnung |

## Bibliotheksbereiche

Der aktuelle Bibliotheksbestand ist nach funktionalen Verantwortungen
gegliedert:

- `MISSION` — Zweck, Zielbild, Grenzen und Erfolgskriterien
- `CONTRACT` — Regeln, Berechtigungen, Konventionen und Lebenszyklen
- `DEVELOPMENT` — Discovery, Konzeption, Architektur, Bau und Dokumentation
- `WORKFLOW` — Abläufe, Spezifikationen und Automatisierung
- `QUALITY` — Reviews, Validierung, Inspektion und Vorfallbehandlung
- `TOOLING` — Vorlagen für Agenten, Prompts, Skills und Skripte
- `_STANDARDS` — bereichsübergreifende Standards

Nicht jede Datei ist bereits ein freigegebener Standard. Der jeweilige Status
in der Datei und die Angaben im Projektboard sind massgebend.

## Einstieg

1. Lies zuerst [`PROJECT_INFO.yaml`](PROJECT_INFO.yaml) und
   [`PROJECT_BOARD.md`](PROJECT_BOARD.md).
2. Prüfe Zweck, Status und Geltungsbereich des gewünschten Bausteins.
3. Übernimm nur die für dein Projekt benötigten Bestandteile.
4. Dokumentiere Anpassungen, Herkunft und bewusste Abweichungen.
5. Führe vor einem produktiven Einsatz eine zum Risiko passende Prüfung durch.

## Reifegrad und Grenzen

Der Architecture Hub ist derzeit weder ein fertiges Framework noch eine
installierbare Software. Er wird eine wachsende Arbeits- und Wissensbasis
bleiben. Einige Inhalte sind bewusst als `DRAFT` gekennzeichnet. Solche
Inhalte muss ich noch prüfen und freigeben.

## Herkunft und Transparenz

Die Bausteine gehen auf frühere Projekte zurück und wurden teilweise für eine
allgemeinere Wiederverwendung überarbeitet.

Die Infografik unter `ARCHITECTURE_HUB_ASSETS/INFOGRAPHICS/` wurde mit
Unterstützung von ChatGPT erzeugt und ist ein erster Entwurf. Die
Verantwortung für Auswahl, Einordnung und Veröffentlichung liegt beim
Projektinhaber, also bei mir.

## Mitwirken

Das Projekt befindet sich im Aufbau. Hinweise auf Widersprüche, fehlende
Grenzen, unklare Begriffe und nicht belegte Annahmen sind besonders willkommen.
Vor einer grösseren Änderung sollte zuerst beschrieben werden, welches Problem
gelöst wird und woran eine Verbesserung erkennbar ist.

## Lizenz

Sofern nicht anders angegeben, stehen die veröffentlichten Inhalte unter der
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License](LICENSE.md). Material Dritter und ausdrücklich anders lizenzierte
Dateien sind davon nur im jeweils angegebenen Umfang erfasst.
