---
document_id: ah-project-package-handover-takeover
title: PROJECT START PACKAGE — Handover/Takeover
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-10-01
authority: HUMAN_PILOT_REQUIRED
---

# HANDOVER / TAKEOVER CONTRACT

## Zweck

Der Vertrag verhindert, dass ein PROJECT_START_PACKAGE nur abgelegt wird,
ohne dass der naechste Agent Auftrag, Authority und Vollstaendigkeit wirklich
uebernommen hat.

## Zustaende

```text
NOT_READY
  -> READY_FOR_HANDOVER
  -> HANDOVER_OFFERED
  -> TAKEOVER_ACCEPTED
  -> IN_DEVELOPMENT

HANDOVER_OFFERED
  -> TAKEOVER_REJECTED
  -> RETURN_TO_HUB
```

## Handover-Pflichtinhalt

- Projekt- und Manifest-ID;
- Profil- und Manifestpfad;
- Library-Revision;
- bestaetigte A- und D-Stufe;
- Ziel, Scope und Nicht-Ziele;
- HUMAN-Entscheide und akzeptierte Defaults;
- offene Entscheide und akzeptierte Luecken;
- Package-Build-Report;
- Stringenz- und Diff-Status;
- naechster Agent und Startprompt;
- exakt eine naechste zulaessige Aktion.

## Takeover-Pruefung

Der PROJECT-ARCHITEKT prueft vor fachlicher Arbeit:

1. Manifest, Profil und Build-Report sind vorhanden und lesbar.
2. Alle erforderlichen Manifestdateien existieren.
3. Hash-Abweichungen und nicht deklarierte Dateien sind sichtbar.
4. Auftrag, Scope, Authority und HUMAN-Gates sind eindeutig.
5. Der naechste Schritt liegt innerhalb seiner Rolle.

## Annahme

```text
TAKEOVER_ACCEPTED
project_id: ...
manifest_id: ...
first_action: ...
```

## Ablehnung

```text
TAKEOVER_REJECTED
project_id: ...
blocking_findings:
  - ...
required_correction:
  - ...
return_target: HUB_ARCHITEKT
```

Der PROJECT-ARCHITEKT repariert ein abgelehntes Package nicht still. Der
HUB-ARCHITEKT bleibt bis zur Annahme fuer die Uebergabe verantwortlich.
