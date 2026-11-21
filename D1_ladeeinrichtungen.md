# D1 Ladeeinrichtungen für Elektrofahrzeuge (DIN VDE 0100-722)

> **Stand:** Gerüst
> **Kurz:** Jede Ladeeinrichtung bekommt einen eigenen Stromkreis mit eigenem RCD und Schutz gegen Gleichfehlerströme. Sie ist beim Netzbetreiber zu melden, ab 12 kW genehmigungspflichtig. Im Neubau verlangt das GEIG Leitungsinfrastruktur (Leerrohre).

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-722 | Stromversorgung von Elektrofahrzeugen |
| VDE-AR-N 4100 | Anmeldung, Genehmigung |
| GEIG | Leitungsinfrastruktur in Wohngebäuden |
| EnWG § 14a | steuerbare Verbrauchseinrichtung → D3 |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Eigener Endstromkreis je Ladepunkt | **Muss** | -722 |
| RCD ≤ 30 mA je Ladepunkt, Schutz gegen DC-Fehlerströme (RCD Typ B oder Typ A/F + RDC-DD 6 mA) | **Muss** | -722 |
| Meldung beim Netzbetreiber; Genehmigung bei > 12 kVA Summenleistung | **Muss** | VDE-AR-N 4100 |
| Leerrohre für Ladeinfrastruktur im Neubau (Stellplätze) | **Muss** ⚠ prüfen (Schwellenwerte) | GEIG |
| Überspannungsschutz | **Muss** | -443/-534 → C5.4 |

## 3 Auslegung

offen: Querschnitt und Spannungsfall für 11 kW (16 A, 3-phasig), Lastmanagement bei mehreren Ladepunkten im MFH.

## 4 Ausführungshinweise und Fallstricke

- RCD-Typ nach Herstellerangabe. Ein RCD Typ A vor einer Ladeeinrichtung ohne RDC-DD wird durch Gleichfehlerströme blind.
- Im MFH: Wohnungseigentumsrecht (Anspruch auf Gestattung) und Zuordnung zum Zähler der Wohnung klären.

## 5 Bestand

Der Anschluss einer Ladeeinrichtung löst häufig Zählerschrank-Umbau und SPD-Nachrüstung aus → [D4](D4_auswirkungen_anlage.md).

## 6 Querverweise

- RCD → [C5.1](C05_1_schutz_elektrischer_schlag.md)
- § 14a EnWG → [D3](D3_waermepumpe_14a.md)
