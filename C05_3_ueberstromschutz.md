# C5.3 Schutz bei Überstrom (DIN VDE 0100-430)

> **Stand:** Material übernommen
> **Kurz:** Die Schutzeinrichtung muss die Leitung vor Überlast und Kurzschluss schützen. Grundbedingung ist I_B ≤ I_n ≤ I_z, wobei I_z die nach Verlegeart, Häufung und Temperatur *abgeminderte* Strombelastbarkeit ist.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-430 | 433 (Überlast), 434 (Kurzschluss) |
| DIN VDE 0298-4 | Strombelastbarkeit, Umrechnungsfaktoren → C6, AH-B |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| I_B ≤ I_n ≤ I_z | **Muss** | -430, 433.1 |
| I_2 ≤ 1,45 · I_z | **Muss** | -430, 433.1 |
| Kurzschlussschutz: Abschaltung, bevor die Leitung die zulässige Temperatur erreicht | **Muss** | -430, 434 |
| Schaltvermögen der Schutzeinrichtung ≥ Kurzschlussstrom am Einbauort (LS meist 6 kA) | **Muss** | -430 |

## 3 Auslegung

### 3.1 Überlastschutz

**Bedingung 1:** I_B ≤ I_n ≤ I_z

**Bedingung 2:** I_2 ≤ 1,45 · I_z

Bei Leitungsschutzschaltern (Typ B und C) liegt der große Prüfstrom normativ bei I_2 = 1,45 · I_n. Bedingung 2 folgt deshalb bei LS automatisch aus I_n ≤ I_z. Bei Schmelzsicherungen gilt das nicht ohne Weiteres.

### 3.2 Beispiel B13 an 1,5 mm², 30 °C, 2 belastete Adern, ohne Häufung

| Verlegeart | I_z | I_n ≤ I_z? |
|---|---|---|
| A2 (Rohr in wärmegedämmter Wand) | 15,5 A | 13 ≤ 15,5 erfüllt |
| B2 (Rohr auf/in Mauerwerk) | 16,5 A | 13 ≤ 16,5 erfüllt |
| C (direkt auf/unter Putz) | 19,5 A | 13 ≤ 19,5 erfüllt |

I_2 = 1,45 · 13 A = 18,85 A ≤ 1,45 · 15,5 A = 22,48 A → Bedingung 2 auch in A2 erfüllt.

### 3.3 Wann wird I_n ≤ I_z verletzt?

Mit Häufung oder Temperatur über 30 °C wird I_z abgemindert:

- **Unter Putz (C):** 3 Stromkreise nebeneinander, Faktor 0,70: 19,5 A · 0,70 = 13,65 A ≥ 13 A, gerade noch zulässig. Grenze bei einem Gesamtfaktor von 0,67.
- **Gedämmte Wand (A2):** schon 2 gebündelte Leitungen, Faktor 0,80: 15,5 A · 0,80 = 12,4 A < 13 A, **unzulässig**.

Das vollständige Beispiel mit B16 folgt in [C6](C06_kabel_leitungsanlagen.md), Abschnitt 3.4.

### 3.4 Kurzschlussschutz

Die Abschaltbedingung nach DIN VDE 0100-410 (Z_S-Grenzwert) deckt bei LS in Endstromkreisen den Kurzschlussschutz der Leitung in der Regel mit ab → [C5.1](C05_1_schutz_elektrischer_schlag.md).

## 4 Ausführungshinweise und Fallstricke

- Die Faustregel „1,5 mm² pauschal mit 16 A“ gilt als überholt.
- Häufung ist der häufigste Grund für eine unzulässige Zuordnung: gemeinsamer Mauerschlitz, Kabelkanal, Bündel über der abgehängten Decke.
- I_B realistisch ansetzen: Dauerlasten (Trockner, Heizlüfter, Ladegeräte) sind keine Spitzenlasten.

## 5 Bestand

Bei Austausch eines LS gegen einen größeren Bemessungsstrom ist die vorhandene Leitung neu zu bewerten. Das ist eine Änderung, keine Instandhaltung.

## 6 Querverweise

- Strombelastbarkeit und Umrechnungsfaktoren → [AH-B](AH-B_bemessungstabellen.md)
- Leitungsanlagen → [C6](C06_kabel_leitungsanlagen.md)
