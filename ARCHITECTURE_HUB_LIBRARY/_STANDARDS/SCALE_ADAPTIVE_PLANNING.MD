---
document_id: ah-standard-scale-adaptive-planning
title: Scale-Adaptive Planning
status: DRAFT
version: 0.1.0
created_at: 2026-09-29T23:20:23+02:00
authority: HUMAN_APPROVAL_REQUIRED
type: STANDARD
---

# Scale-Adaptive Planning

## Zweck

Planung und Grundausstattung werden an die reale Grösse und das reale Risiko
einer Entwicklung angepasst. Zwei Achsen wirken zusammen:

1. **Umfangstyp A1 bis A4:** legt die Grundausstattung fest.
2. **Trigger:** ergänzt unabhängig vom Typ genau die Bausteine, die durch
   Daten, Risiken, Betrieb oder Zusammenarbeit erforderlich werden.

Es wird mit dem kleinsten tragfähigen Typ begonnen. Ein Trigger ergänzt eine
Pflicht; er bläht nicht automatisch den gesamten Projekttyp auf.

## Umfangstypen

- **A1 – Einmal-Tool:** eng begrenzter einmaliger Lauf, zum Beispiel ein
  Dokument-Normalisierer.
- **A2 – Wiederkehrende Automation:** wiederholter oder geplanter Lauf mit
  dauerhaft erwartbarem Verhalten.
- **A3 – KI-Assistent mit Wissensbasis:** dialogische oder agentische Funktion
  mit Quellen-, Wissens- oder Zustandsbezug.
- **A4 – Multi-Agent-System oder Produkt:** mehrere Rollen, Nutzer oder
  Komponenten mit langfristigem Betrieb und eigener Produktarchitektur.

## Grundausstattung nach Umfang

| Typ | Script | Schema | Begleit-Agent | README | MISSION.md | NAMING.md | FORMAT.md | ADRs | Evals | RAG | DB | SECURITY.md |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A1 Einmal-Tool, z. B. Dokument-Normalisierer | ● | ● | ● | ○ | – | – | – | – | – | – | – | Trigger |
| A2 Wiederkehrende Automation | ● | ● | ● | ● | ○ | ○ | ● | – | ○ | – | ○ | Trigger |
| A3 KI-Assistent mit Wissensbasis | ● | ● | ● | ● | ● | ● | ● | ○ | ● | ● | ○ | ● |
| A4 Multi-Agent-System oder Produkt | ● | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● | ● |

**Legende:** ● Pflicht · ○ optional · – weglassen · **Trigger** nur bei
zutreffender Trigger-Regel Pflicht.

## Trigger-Regeln

- **Security:** Externe oder schützenswerte Daten, Credentials, Netzwerk,
  autonome Mutationen, Löschung oder andere erhebliche Nebenwirkungen machen
  `SECURITY.md` und die anwendbaren Security-Checklisten zur Pflicht.
- **RAG:** Ein wachsender oder häufig wechselnder Quellenbestand, der nicht
  zuverlässig in den Arbeitskontext passt, macht eine begründete
  Retrieval-Entscheidung erforderlich. Ein kleiner stabiler Bestand ist kein
  RAG-Trigger.
- **DB:** Dauerhafter Zustand über Läufe, Beziehungen, Abfragen,
  Mehrfachzugriff oder konkurrierende Writes machen eine DB-Entscheidung
  erforderlich.
- **Evals:** Wiederholte Nutzung, hohe Fehlerkosten, nichtdeterministisches
  Verhalten oder kritische Negativfälle machen Evals zur Pflicht.
- **ADRs:** Mehrere tragfähige Optionen oder eine schwer rückgängig zu
  machende Architekturentscheidung verlangen ein ADR.
- **FORMAT/NAMING:** Mehrere Producer, maschinenübergreifende Übergaben oder
  wiederverwendbare Artefakte verlangen explizite Format- und Naming-Regeln.
- **README/MISSION:** Übergabe an andere Personen, längerfristiger Betrieb oder
  Wiederverwendung verlangen verständlichen Zweck, Startweg und Grenzen.
- **Agentenvertrag:** Autonome Entscheidungen, Rollenübergaben oder mehrere
  Actors verlangen einen expliziten Agentenvertrag mit Inputs, Outputs,
  Authority und Stop-Bedingungen.

## Auswahlregel

Der Plan nennt immer:

1. gewählten Umfangstyp mit Begründung;
2. ausgelöste Trigger;
3. daraus resultierende Pflichtbausteine;
4. bewusst weggelassene optionale Bausteine;
5. offene HUMAN-Entscheide.

Eine Abweichung von der Grundausstattung ist zulässig, wenn sie begründet und
bei wirksamer Tragweite als ADR festgehalten wird.
