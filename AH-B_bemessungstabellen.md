# AH-B Bemessungstabellen

> **Stand:** ausgearbeitet, Werte gegen DIN VDE 0298-4 prüfen ⚠
> **Kurz:** Arbeitstabellen für Strombelastbarkeit, Umrechnungsfaktoren und Schleifenimpedanz-Grenzwerte. Maßgeblich bleibt der Normtext.

---

## B.1 Strombelastbarkeit I_r in A – Cu, PVC-isoliert (70 °C), Umgebung 30 °C

**Zwei belastete Adern (Wechselstrom)**

| Querschnitt mm² | A1 | A2 | B1 | B2 | C |
|---|---|---|---|---|---|
| 1,5 | 15,5 | 15,5 | 17,5 | 16,5 | 19,5 |
| 2,5 | 19,5 | 18,5 | 24 | 23 | 27 |
| 4 | 26 | 25 | 32 | 30 | 36 |
| 6 | 34 | 32 | 41 | 38 | 46 |
| 10 | 46 | 43 | 57 | 52 | 63 |
| 16 | 61 | 57 | 76 | 69 | 85 |

**Drei belastete Adern (Drehstrom)**

| Querschnitt mm² | A1 | A2 | B1 | B2 | C |
|---|---|---|---|---|---|
| 1,5 | 13,5 | 13 | 15,5 | 15 | 17,5 |
| 2,5 | 18 | 17,5 | 21 | 20 | 24 |
| 4 | 24 | 23 | 28 | 27 | 32 |
| 6 | 31 | 29 | 36 | 34 | 41 |
| 10 | 42 | 39 | 50 | 46 | 57 |
| 16 | 56 | 52 | 68 | 62 | 76 |

**Verlegearten (Kurzform):** A1 Aderleitungen im Rohr in wärmegedämmter Wand · A2 mehradrige Leitung im Rohr in wärmegedämmter Wand · B1 Aderleitungen im Rohr auf/in Wand · B2 mehradrige Leitung im Rohr auf/in Wand · C direkt auf/in Wand (unter Putz)

## B.2 Umrechnungsfaktoren Häufung (gebündelt, direkt auf/in Wand oder im Rohr)

| Anzahl Stromkreise | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Faktor | 1,00 | 0,80 | 0,70 | 0,65 | 0,60 | 0,57 | 0,54 | 0,52 | 0,50 |

## B.3 Umrechnungsfaktoren Umgebungstemperatur (PVC, 70 °C)

| Umgebung °C | 25 | 30 | 35 | 40 | 45 | 50 |
|---|---|---|---|---|---|---|
| Faktor | 1,06 | 1,00 | 0,94 | 0,87 | 0,79 | 0,71 |

Hinweis: DIN VDE 0298-4 Anhang A erlaubt für Wohnräume bei dauerhaft höchstens 25 °C erhöhte Werte (z. B. 1,5 mm² A2: 16,5 A). Siehe [C6](C06_kabel_leitungsanlagen.md), Abschnitt 3.4.

## B.4 Grenzwerte Schleifenimpedanz (TN, U_0 = 230 V, Abschaltung ≤ 0,4 s)

Z_S,max = U_0 / I_a · Messwert nach 2/3-Methode: Z_S,Mess = 2/3 · Z_S,max

| LS | I_a | Z_S,max Ω | Z_S,Mess Ω |
|---|---|---|---|
| B6 | 30 A | 7,67 | 5,11 |
| B10 | 50 A | 4,60 | 3,07 |
| B13 | 65 A | 3,54 | 2,36 |
| B16 | 80 A | 2,88 | 1,92 |
| B20 | 100 A | 2,30 | 1,53 |
| B25 | 125 A | 1,84 | 1,23 |
| B32 | 160 A | 1,44 | 0,96 |
| C10 | 100 A | 2,30 | 1,53 |
| C13 | 130 A | 1,77 | 1,18 |
| C16 | 160 A | 1,44 | 0,96 |
| C20 | 200 A | 1,15 | 0,77 |
| C32 | 320 A | 0,72 | 0,48 |

## B.5 Zuordnung Querschnitt – LS für typische Endstromkreise (Empfehlung)

| Leitung | Bedingungen | LS |
|---|---|---|
| 3 × 1,5 mm² | Licht | B10 |
| 3 × 1,5 mm² | Steckdosen, bis ca. 15 m, Häufung ≤ 3 unter Putz | B13 |
| 3 × 2,5 mm² | Steckdosen, Küche, Großgeräte, längere Wege | B16 |
| 5 × 2,5 mm² | Herd bis 11 kW | B16, 3-polig |

Begründung → [C6](C06_kabel_leitungsanlagen.md), [C5.3](C05_3_ueberstromschutz.md).
