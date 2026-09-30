---
name: "<skill-name>"
description: "<Was der Skill leistet; klare Aktivierung; klare Ausschlüsse.>"
---

# [SKILL-NAME]

> TEMPLATE-METADATEN: Status `TEMPLATE`, Version `1.0.0`, erstellt am
> `2026-09-30`, Funktionsbereich `TOOLING`, bestätigter Zielname `SKILL.md`.
> Authority und Source-Check:
> `ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling`.

## Zweck

[PLATZHALTER: Welche wiederverwendbare Fähigkeit stellt dieses Paket bereit?]

## Aktivierung

Verwende diesen Skill, wenn:

- [PLATZHALTER: eindeutiger Trigger]

Verwende ihn nicht, wenn:

- [PLATZHALTER: benachbarter, aber ausgeschlossener Fall]

## Inputs

- [PLATZHALTER: erforderlicher Input und zulässige Form]

## Outputs

- [PLATZHALTER: Ergebnis, Format, Speicherort und Qualitätszustand]

## Workflow

1. [PLATZHALTER: notwendige Quellen oder Ressourcen lesen]
2. [PLATZHALTER: Arbeit in kleinsten prüfbaren Schritten ausführen]
3. [PLATZHALTER: Ergebnis validieren]
4. [PLATZHALTER: Ergebnis und Grenzen übergeben]

## Sicherheit und Authority

- [PLATZHALTER: erlaubte Wirkung]
- [PLATZHALTER: HUMAN-Gates und verbotene Wirkung]
- [PLATZHALTER: Umgang mit Credentials und untrusted Input]

## Ressourcen

- `scripts/` — [OPTIONAL: ausführbare Hilfen]
- `references/` — [OPTIONAL: nur bei Bedarf zu ladende Fachquellen]
- `assets/` — [OPTIONAL: wiederverwendbare Ausgangsartefakte]

## Validation

[PLATZHALTER: reproduzierbare Tests, visuelle Prüfung oder Eval-Kriterien]

## Fehler und Fallback

[PLATZHALTER: Wann stoppen, rückfragen oder einen sicheren Ersatzweg nutzen?]

## Provenienz

- Lokale Authority:
  `ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling`
- HUMAN-Entscheid: „TOOLING-Dateitypen prüfen“, 30. September 2026
- Source-Check: gezielt, nicht vollständig; Grenzen stehen in der lokalen
  Authority.

<!--
AUSLAGERUNGSREGEL

300 Zeilen sind nur ein Prüftrigger. Ein Skill-Paket ist auch früher sinnvoll,
wenn die Fähigkeit wiederverwendet wird, eigene Ressourcen besitzt,
unabhängig versioniert werden muss oder mehrere Agenten sie laden. Kleine,
agentenspezifische Anweisungen dürfen im AGENT-Vertrag verbleiben.
-->
