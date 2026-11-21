# C6 Kabel- und Leitungsanlagen

> **Stand:** Material übernommen (mit ausgearbeitetem Rechenbeispiel)
> **Kurz:** Querschnitt und Absicherung ergeben sich aus Verlegeart, Häufung, Umgebungstemperatur und Spannungsfall, nicht aus Faustregeln. Leitungen liegen nur in den Installationszonen nach DIN 18015-3, damit spätere Bohrungen sie nicht treffen.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-520 | Kabel- und Leitungsanlagen, Verlegearten |
| DIN VDE 0298-4 | Strombelastbarkeit, Umrechnungsfaktoren, Anhang A (25 °C in Wohnräumen) |
| DIN VDE 0100-430 | Zuordnung Schutzeinrichtung → C5.3 |
| DIN 18015-1 | Spannungsfall |
| DIN 18015-3 | Installationszonen |
| DIN VDE 0100-559 | Leuchten |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| I_z nach Verlegeart, mit Umrechnungsfaktoren für Häufung und Temperatur | **Muss** | DIN VDE 0298-4 |
| Spannungsfall Messeinrichtung → Verbrauchsmittel ≤ 3 % | **Muss** ⚠ prüfen | DIN 18015-1 |
| Unsichtbar verlegte Leitungen nur in Installationszonen | **Muss** | DIN 18015-3 |
| Leitungen waagerecht oder senkrecht, nicht schräg | **Muss** | DIN 18015-3 |
| Telekommunikations- und Rundfunkleitungen austauschbar in Rohren | **Muss** | DIN 18015-3 |
| Herdanschluss mindestens 2,5 mm² | **Muss** | DIN 18015-1 |

## 3 Auslegung

### 3.1 Strombelastbarkeit

I_z = I_r · f_Häufung · f_Temperatur

I_r = Tabellenwert für die Verlegeart (30 °C). Tabellen → [AH-B](AH-B_bemessungstabellen.md).

### 3.2 Spannungsfall Wechselstrom

ΔU % = (2 · L · I · cos φ) / (κ · A · U_0) · 100   (κ_Cu = 56 m/(Ω·mm²) bei 20 °C, U_0 = 230 V)

### 3.3 Installationszonen (DIN 18015-3)

| Zone | Lage | Vorzugsmaß |
|---|---|---|
| ZW-o (waagerecht oben) | 15–45 cm unter fertiger Decke | 30 cm |
| ZW-u (waagerecht unten) | 15–45 cm über fertigem Fußboden | 30 cm |
| ZW-m (waagerecht mittig) | 90–120 cm über FFB, in Räumen mit Arbeitsflächen | 100 cm |
| ZS-t, ZS-f (senkrecht an Türen, Fenstern) | 10–30 cm neben Rohbaukante | 15 cm |
| ZS-e (senkrecht an Ecken) | 10–30 cm neben Rohbauecke | 15 cm |

⚠ prüfen: Zonen in Decken und Fußböden (Ausgabe 2016) ergänzen.

### 3.4 Ausgearbeitetes Beispiel: 1,5 mm² an B13 oder B16?

Ausgangslage: neuer Steckdosenstromkreis, 1,5 mm² Cu, 14 m, 2 belastete Adern.

**Fall B16 – wann noch zulässig:**

| Verlegeart | I_z (30 °C) | Ergebnis |
|---|---|---|
| C, einzeln unter/auf Putz | 19,5 A | 16 ≤ 19,5 zulässig, solange die Leitung allein liegt und keine Wärmequelle in der Nähe ist |
| B2, einzeln im Rohr auf/in Massivwand | 16,5 A | 16 ≤ 16,5 rechnerisch zulässig, praktisch ohne Reserve |

**Fall B16 – wann unzulässig:**

1. **Wärmegedämmte Wand (A1/A2):** I_z = 15,5 A < 16 A. Anhang A der DIN VDE 0298-4 erlaubt für Wohnräume bei dauerhaft höchstens 25 °C 16,5 A. In gedämmten Dachgeschossen, an Außenwänden im Sommer oder neben warmen Rohren ist das nicht sicher; Fachbetriebe planen deshalb mit 30 °C.
2. **Häufung**, schon ab 2 Leitungen (Faktor 0,80):
   - B2: 16,5 A · 0,80 = 13,2 A < 16 A
   - C: 19,5 A · 0,80 = 15,6 A < 16 A
   - Selbst mit 25 °C ist ab 3 Leitungen Schluss: 21 A · 0,70 = 14,7 A < 16 A
3. **Umgebungstemperatur über 30 °C** (Technikraum, abgehängte Decke mit Trafos, Heizungsrohre): Der Temperaturfaktor drückt I_z unter 16 A.
4. **Spannungsfall:** 14 m bei 16 A: 2 · 14 · 16 / (56 · 1,5 · 230) = **2,32 %** (20 °C) bis 2,78 % (warmer Leiter). Mit 0,5–0,8 % auf der Zuleitung liegt man an der 3-%-Grenze. Ab etwa 15–18 m ab Verteiler ist 1,5 mm²/16 A wegen des Spannungsfalls unzulässig.
5. **Schleifenimpedanz:** B16 braucht 80 A Sofortauslösestrom statt 65 A bei B13; Z_S,Mess sinkt von 2,36 Ω auf 1,92 Ω. In alten Gebäuden mit langer, dünner Zuleitung kann das knapp werden.
6. **Drehstrom 5 × 1,5 mm² in gedämmten Wänden und Herdanschluss:** grundsätzlich unzulässig (Herd mindestens 2,5 mm²).

**Fazit:** B16 an 1,5 mm² hält die Norm nur ein, wenn die Leitung allein liegt, nicht in Dämmung verlegt ist und der Spannungsfall auf der Zuleitung klein ist. **B13 an 1,5 mm²** umgeht diese Fallstricke und entspricht der heutigen Praxis. Wer volle 16 A mit Reserve für Häufung, Dämmung und längere Wege braucht, verlegt **3 × 2,5 mm²**.

## 4 Ausführungshinweise und Fallstricke

- Mehrere Leitungen gebündelt in einer Dämmschicht vertragen deutlich weniger Strom als die Tabellenwerte für freie Verlegung. Das wird in der Praxis oft übergangen.
- Wer außerhalb der Installationszonen verlegt, schafft eine dauerhafte Gefahrenstelle. Abweichungen im Bestandsplan dokumentieren.
- Zwischenbesichtigung vor dem Verputzen: der letzte Zeitpunkt, zu dem die Leitungsführung ohne Aufwand prüfbar ist → [AH-C](AH-C_checklisten.md).

## 5 Bestand

Alte Leitungen ohne Schutzleiter → [E2](E2_altanlagen.md). Bei Erhöhung des LS-Bemessungsstroms die Leitung neu bewerten.

## 6 Querverweise

- Überstromschutz → [C5.3](C05_3_ueberstromschutz.md)
- Tabellen → [AH-B](AH-B_bemessungstabellen.md)
