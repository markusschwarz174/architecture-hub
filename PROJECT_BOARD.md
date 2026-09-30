# PROJECT BOARD – Architecture Hub

## Aktueller Stand

ARCHITEKT V1 und DEVELOPER V1 sind durch HUMAN-Direktive auf ACTIVE gesetzt.
REVIEWER und KURATOR bleiben DRAFT. Das Architektur-Skelett A1 bis A4 liegt
als Version `1.0.0-draft` in `AH_MISSION.MD` vor. Der Abgleich mit bestehenden
Projekten und Dateifamilien ist in `AH_SKELETON_V1_AUDIT.MD` dokumentiert.

## Nächster Schritt

Die A3-Dateien und danach die A4-Dateien fachlich einzeln prüfen. Anschliessend
das Skelett gegen einen realen Workflow anwenden und erst nach diesem
Praxistest als Library-Standard freigeben.

## Entscheidungen

- Das Projekt heisst `ARCHITECTURE_HUB` und wird als eigenständiges Projekt
  direkt unter `/AI_PROJECTS/` geführt.
- `ARCHITECTURE_HUB_LIBRARY` ist der kuratierte Nutzbestand.
- `ARCHITECTURE_HUB_DEVELOPMENT` ist die Werkbank für Quellen, Kandidaten,
  Entscheidungen, Tests und Promotion.
- `/SYSTEM` bleibt der lokale Betriebsbestand und übernimmt nur freigegebene
  Werkzeuge oder Verträge.
- Ein Chat ist Arbeitsraum, nie Langzeitgedächtnis oder Authority.
- Vier getrennte Rollenverträge definieren ARCHITEKT, DEVELOPER, REVIEWER
  und KURATOR. Der ASSEMBLER bleibt bis zu einer späteren Produktphase
  vertagt.
- ARCHITEKT V1 ist aus AGENT_ARCHY abgeleitet; nur universelle Prinzipien
  wurden übernommen.
- DEVELOPER V1 enthält die für den Hub angepassten K1 bis K11 sowie den
  Methodenstand zu SDD, Prompt-, Context-, Loop-, Graph-, Harness-, Eval-,
  Trace-, Tool- und Security-Engineering vom 29. September 2026.
- K11 lautet für den Hub: Entwicklung dient einem real einsetzbaren Tool
  oder einer belegten Verbesserung der Library, nie dem Prozess als
  Selbstzweck.
- A1 bis A4 bilden Verantwortung und Validationsgrenzen ab, nicht Laufzeit,
  Lebensdauer, Öffentlichkeit oder Wiederverwendbarkeit.
- Klassifiziert wird der konkrete Workflow oder die Systemgrenze, nicht
  pauschal das gesamte Repository.
- `SPECS` bleiben als optionale Dateifamilie erhalten. Die stufenspezifischen
  Kerndateien sind bereits primäre Specs.
- Die Mission ist während der Entwicklung die Single Source of Truth für das
  Skelett 1.0; der Library-Standard verweist darauf, statt die Matrix zu
  duplizieren.

## Adressierte Funktionsübergaben — provisorisch

- `DEVELOPMENT`: Wahl von Dateityp und Werkzeug sowie `SCRIPT`, `AI_PASS` oder
  `HYBRID` ist im DEVELOPER-Vertrag angekommen.
- `QUALITY`: Nachweise, `FILESYS`, Systemüberwachung und die präventive
  INSPECTOR-Prüfung sind im Inspection-Konzept angekommen.
- `CONTRACT`: Zentraler Paketvertrag und spezialisierte Rollen sind als
  offene Übergabe vorgemerkt. Da noch kein CONTRACT-Funktionsbereich besteht,
  wird dafür noch kein kanonisches Artefakt erfunden.

## Offene Fragen

- Bestehen `GUARDRAILS.yaml`, `SECURITY.md`, `EVALS` und `HANDOFF.md` den
  Praxistest als Pflichtdateien für kleine A3- und A4-Systeme?
- Welche bereits bestätigten Perlen werden als erster Seed-Bestand promoted?
- Soll der erste Kompositionstest ein `NORMALIZE_TOOL` für einen realen
  Zielordner oder ein kontrolliertes Beispiel sein?

## Parkplatz

- Spätere UI oder Suchoberfläche.
- Automatische semantische Suche erst nach tragfähigem Katalog und echten
  Retrieval-Tests.
