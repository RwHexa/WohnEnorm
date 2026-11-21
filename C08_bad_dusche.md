# C8 Räume mit Badewanne oder Dusche (DIN VDE 0100-701)

> **Stand:** Material übernommen (Maße ergänzt, prüfen)
> **Kurz:** Das Bad wird in die Bereiche 0, 1 und 2 eingeteilt, in denen jeweils nur bestimmte Betriebsmittel zulässig sind. Alle Stromkreise im Bad brauchen einen RCD 30 mA, und es gilt die Pflicht zum zusätzlichen Schutzpotentialausgleich. Eine falsch gesetzte Steckdose lässt sich nur mit Stemmarbeiten beheben.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-701 | Räume mit Badewanne oder Dusche |
| DIN VDE 0100-702 | Becken von Schwimmbädern (kurz) |
| DIN VDE 0100-703 | Räume mit Saunaheizungen (kurz) |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| RCD I_Δn ≤ 30 mA für alle Stromkreise im Raum | **Muss** | -701 |
| Zusätzlicher Schutzpotentialausgleich der fremden leitfähigen Teile | **Muss** | -701 ⚠ prüfen (Ausnahmen) |
| Steckdosen nicht in Bereich 0, 1 und 2 (Ausnahme: SELV, Rasiersteckdosen-Einheiten mit Trenntransformator in Bereich 2) | **Muss** | -701 |
| Schutzart Bereich 0: IPX7, Bereiche 1 und 2: mindestens IPX4 (IPX5 bei Strahlwasser) | **Muss** | -701 |
| Schalter und Steckdosen außerhalb der Bereiche 0–2 | **Muss** | -701 |

## 3 Bereiche

| Bereich | Ausdehnung | Zulässig |
|---|---|---|
| 0 | Innenraum der Wanne bzw. Duschtasse | nur SELV ≤ 12 V AC, fest angeschlossen, IPX7 |
| 1 | senkrecht über Wanne/Dusche bis 2,25 m über Fußboden; bei bodengleicher Dusche Radius 1,20 m um den Wasseraustritt | fest angeschlossene Verbrauchsmittel, die der Hersteller dafür vorsieht (Durchlauferhitzer, Whirlpool, Lüfter), SELV |
| 2 | 0,60 m waagerecht um Bereich 1, bis 2,25 m Höhe | zusätzlich Leuchten, Rasiersteckdosen-Einheiten, SELV-Steckdosen |
| außerhalb | – | Steckdosen, Schalter |

⚠ prüfen: Maße und Zulässigkeiten am Normtext bestätigen und eine Skizze (Grundriss und Schnitt) in `bilder/` ergänzen.

## 4 Ausführungshinweise und Fallstricke

- Die Bereiche werden vom fertigen Bauzustand aus gemessen (Wanne, Duschtasse, Duschabtrennung). Planänderungen im Sanitärbereich ziehen die Elektroplanung mit.
- Waschtischsteckdosen bei schmalen Bädern: Abstand zur Duschzone prüfen.
- Eigener Stromkreis mit RCBO bewährt sich → [B2](B2_stromkreisaufteilung.md).

## 5 Bestand

Bei Badsanierung gilt -701 für den gesamten neu gestalteten Raum.

## 6 Querverweise

- Potentialausgleich → [C7](C07_erdung_potentialausgleich.md)
- Typische Mängel → [AH-D](AH-D_typische_maengel.md)
