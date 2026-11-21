# C2 Zählerplatz

> **Stand:** Material übernommen
> **Kurz:** Der Zählerschrank nach VDE-AR-N 4100:2026-04 gliedert sich senkrecht in den netzseitigen Anschlussraum (NAR), das Zählerfeld mit Raum für Zusatzanwendungen (RfZ/APZ) und den anlagenseitigen Anschlussraum (AAR). Das RfZ gehört dem Netz- und Messstellenbetreiber, nicht dem Kunden.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| VDE-AR-N 4100 | Zählerplatz, Ausgabe 2026-04 → [AH-A](AH-A_normenverzeichnis.md) |
| DIN VDE 0603-1 | Zählerplätze |
| TAB des Netzbetreibers | ergänzende Festlegungen |
| EnWG § 14a | Steuereinrichtung → D3 |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Zählerplatz nach VDE-AR-N 4100:2026-04 bei Neubau, Umbau und Nutzungsänderung (bindend seit 12.03.2026) | **Muss** | VDE-AR-N 4100 |
| SLS-Schalter im NAR, 35 A Standard, 50 A bei Dauerstrom (Wärmepumpe, Ladeeinrichtung) | **Muss** | VDE-AR-N 4100 |
| Zählerfeld 450 mm hoch: 300 mm Zähler + 150 mm RfZ (APZ-Feld) | **Muss** | VDE-AR-N 4100 |
| Im RfZ ausschließlich Betriebsmittel von Netz- und Messstellenbetreiber | **Muss** | VDE-AR-N 4100 |
| Überspannungsschutz (Typ 1 bzw. Kombiableiter Typ 1+2) im NAR auf der 40-mm-Sammelschiene | **Muss**, je nach Fall | VDE-AR-N 4100 → C5.4 |
| Im AAR höchstens drei Wechselstromkreise direkt abgesichert | **Muss** ⚠ prüfen | VDE-AR-N 4100 |
| Zählerschrank mit Reserve für spätere Erweiterungen auslegen | **Empfehlung** | dieses Werk |

## 3 Aufbau

| Bereich | Inhalt | Eigentum/Zugang |
|---|---|---|
| NAR (netzseitiger Anschlussraum) | Sammelschiene, SLS, SPD Typ 1/1+2 | plombiert, nur eingetragener Betrieb |
| Zählerfeld | elektronischer Zähler (300 mm) | Messstellenbetreiber |
| RfZ / APZ-Feld (150 mm) | Smart-Meter-Gateway, Steuereinrichtung § 14a EnWG, RJ45-Dose, Tarifschaltgeräte, Sicherungen dafür | Netz-/Messstellenbetreiber |
| AAR (anlagenseitiger Anschlussraum) | Abgang zur Wohnung, wenige Wechselstromkreise | Kunde |

**Typische Bemessung:**

| Abschnitt | Absicherung | Querschnitt Cu |
|---|---|---|
| Zählerplatz-Verdrahtung | SLS 35 A / 50 A | 10 mm² / 16 mm² |

## 4 Ausführungshinweise und Fallstricke

- **Kein Router im RfZ.** Kundeneigene Schaltgeräte und Verteiler sind dort unzulässig. Der Router gehört in den Kommunikationsverteiler → [C9](C09_kommunikation_gebaeudesystemtechnik.md).
- **Großzügig auslegen.** Ladeeinrichtung, Wärmepumpe und Speicher kommen häufig später. Ein zu knapper Zählerschrank bedeutet dann Austausch, nicht Erweiterung.
- **SLS-Größe** früh mit dem Bauherrn klären: Dauerstromanwendungen erzwingen 50 A.

## 5 Bestand

Bestand ohne Eingriff behält seinen Zustand. Bei Umbau, Nutzungsänderung oder Anschluss neuer Großverbraucher gilt VDE-AR-N 4100:2026-04, meist mit Austausch des Zählerschranks → [E3](E3_nachruestpflichten.md), [D4](D4_auswirkungen_anlage.md).

## 6 Querverweise

- Überspannungsschutz → [C5.4](C05_4_ueberspannungsschutz.md)
- Steuerbare Verbrauchseinrichtungen → [D3](D3_waermepumpe_14a.md)
