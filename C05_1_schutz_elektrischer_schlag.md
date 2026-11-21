# C5.1 Schutz gegen elektrischen Schlag (DIN VDE 0100-410)

> **Stand:** Material übernommen
> **Kurz:** Der Fehlerschutz wird im TN-System durch automatische Abschaltung erreicht. In Endstromkreisen bis 32 A muss sie innerhalb von 0,4 s erfolgen. Zusätzlich verlangt die Norm RCDs 30 mA für Steckdosen bis 32 A und für Beleuchtungsstromkreise in Wohnungen.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-410 | 411 (automatische Abschaltung), 411.3.3 (zusätzlicher Schutz durch RCD), 411.3.4 (Leuchten in Wohnungen) ⚠ prüfen |
| DIN VDE 0100-600 | Nachweis durch Messung → F1 |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Abschaltzeit in TN-Endstromkreisen ≤ 32 A bei 230 V: 0,4 s | **Muss** | -410, Tab. 41.1 |
| RCD I_Δn ≤ 30 mA für Steckdosen ≤ 32 A (Benutzung durch Laien) | **Muss** | -410, 411.3.3 |
| RCD I_Δn ≤ 30 mA für Endstromkreise mit Leuchten in Wohnungen | **Muss** | -410, 411.3.4 |
| RCD 30 mA für Endstromkreise im Außenbereich bis 32 A | **Muss** | -410 |
| RCD-Typ passend zu den Verbrauchern (A, F, B) | **Muss** | -530 / Herstellerangabe |

## 3 Auslegung: Abschaltbedingung

Bedingung im TN-System:

Z_S · I_a ≤ U_0  →  Z_S ≤ U_0 / I_a

Für Leitungsschutzschalter gilt der Sofortauslösestrom: Typ B = 5 · I_n, Typ C = 10 · I_n.

Für den **Messwert** wird wegen Leitererwärmung im Fehlerfall und Messtoleranz die **2/3-Methode** angewandt:

Z_S,Mess ≤ 2/3 · U_0 / I_a

**Beispiel B13:**
- I_a = 5 · 13 A = 65 A
- Z_S,theoretisch ≤ 230 V / 65 A = 3,54 Ω
- Z_S,Mess ≤ 2/3 · 3,54 Ω = **2,36 Ω** (entspricht mindestens 98 A Kurzschlussstrom)

**Beispiel B16:** I_a = 80 A → Z_S,Mess ≤ **1,92 Ω** (mindestens 120 A).

**Beispiel C13:** I_a = 130 A → Z_S,Mess ≤ **1,18 Ω**.

Grenzwerttabelle für alle gängigen LS → [AH-B](AH-B_bemessungstabellen.md).

**Anteil der Leitung:** 14 m, 1,5 mm² Cu, 20 °C:
R_Leitung = 2 · 14 m / (56 · 1,5 mm²) = 0,33 Ω (bei Erwärmung im Fehlerfall rund 0,40 Ω).

Bei einer typischen Vorimpedanz am Wohnungsverteiler von 0,3–0,8 Ω liegt die Steckdose damit bei 0,6–1,2 Ω, also deutlich unter 2,36 Ω.

## 4 Ausführungshinweise und Fallstricke

- RCD ersetzt nicht die Abschaltbedingung über den LS. Beide Nachweise führen.
- In alten Netzen mit hoher Vorimpedanz oder im TT-System kann die Abschaltbedingung über LS verfehlt werden. Die Messung zeigt das sofort.
- **RCD-Typ:** Ladeeinrichtungen, Wärmepumpen und Geräte mit Frequenzumrichter erzeugen glatte Gleichfehlerströme. Herstellerangabe beachten (Typ F, Typ B oder RDC-DD in der Ladeeinrichtung) → [D1](D1_ladeeinrichtungen.md).

## 5 Bestand

Für jeden neuen oder erweiterten Stromkreis gilt die RCD-Pflicht vollständig. Eine Erweiterung an TN-C ist unzulässig → [E2](E2_altanlagen.md).

## 6 Querverweise

- Überstromschutz → [C5.3](C05_3_ueberstromschutz.md)
- Erstprüfung → [F1](F1_erstpruefung.md)
