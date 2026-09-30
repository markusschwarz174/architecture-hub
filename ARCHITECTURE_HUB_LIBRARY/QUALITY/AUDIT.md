# AUDIT — STUB

> Dateityp für eine allgemeine AI-Prüfung mit Übergabe an HUMAN. Instanzen werden als `AUDIT_<ID>.md` geführt.

## Auftrag

- Audit-ID: `<AUDIT-ID>`
- Prüfscope: `<System / Zeitraum / Version>`
- Auftraggeber: `<HUMAN / Stelle>`
- Prüf-SOLL und Quellen: `<Referenzen>`
- Untersuchte Evidenz: `<Referenzen und Hashes>`

## Eingesetzte Prüfpositionen

- [ ] `EXPERT_REVIEW`
- [ ] `SIMULATION_TEST`
- [ ] `DIFF_CHECK`
- [ ] `FINAL_TEST`

Auslassungen und Begründung: `<Text>`

## Feststellungen

| ID | Beobachtung | Evidenz | Auswirkung | Status |
|---|---|---|---|---|
| `<FINDING-ID>` | `<beobachtbar>` | `<Referenz>` | `<Wirkung>` | `<PASS/FAIL/HOLD/BORDERLINE/INCONCLUSIVE>` |

## Gesamturteil

`<PASS / FAIL / HOLD / BORDERLINE / INCONCLUSIVE>`

Begründung: `<kurz und evidenzgebunden>`

## Übergabe an HUMAN

- Zu entscheidende Frage: `<nur wenn nötig>`
- Empfohlener nächster Schritt: `<keine verdeckte Reparatur>`
- Zugehörige Report-, Event- oder Incident-IDs: `<IDs>`
