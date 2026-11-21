# B2 Leistungsbedarf und Stromkreisaufteilung

> **Stand:** Material übernommen (Musterverteiler bereinigt)
> **Kurz:** Großgeräte bekommen eigene Stromkreise. Licht und Steckdosen der Hauptwohnräume werden getrennt und auf mindestens zwei RCD-Gruppen verteilt, damit ein einzelner Fehler nicht die ganze Wohnung abschaltet. Im Verteiler werden mindestens 20 % Platz als Reserve vorgehalten.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN 18015-1 | Stromkreise, Stromkreisverteiler, Bemessung |
| DIN 18015-2 | Anzahl der Stromkreise |
| DIN VDE 0100-410 | RCD 30 mA |
| DIN VDE 0100-430, DIN VDE 0298-4 | Zuordnung Querschnitt/Schutzeinrichtung → C5.3, C6 |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Eigener Stromkreis für Herd/Kochfeld (Drehstrom) | **Muss** | DIN 18015-1/-2 |
| Eigene Stromkreise für Geschirrspüler, Waschmaschine, Trockner | **Soll** | DIN 18015-2 |
| Endstromkreise auf mindestens zwei RCDs (30 mA) aufteilen | **Soll** ⚠ prüfen | DIN 18015-1 |
| Mindestens 20 % Reserveplatz im Stromkreisverteiler | **Soll** | DIN 18015-1 |
| Gleichmäßige Aufteilung auf die Außenleiter | **Soll** | DIN 18015-1 |
| Zuleitung Wohnungsverteiler auf 63 A ausgelegt | **Soll** ⚠ prüfen | DIN 18015-1 → C3 |
| Licht und Steckdosen in Haupträumen getrennt | **Empfehlung** | Praxis |

## 3 Schutzkonzept im Wohnungsverteiler

- **Hauptschalter:** 3-polig, 63 A, zur Freischaltung der gesamten Wohnung
- **RCD-Gruppe 1 und 2:** je 4-polig, 40 A / 30 mA, Typ A
- **RCBO (FI/LS):** 2-polig, 30 mA, für Stromkreise, die unabhängig von den Gruppen-RCDs laufen sollen (Kühlgeräte, Bad)
- **SPD Typ 2** vor den RCDs, falls nicht im Zählerschrank → [C5.4](C05_4_ueberspannungsschutz.md)

## 4 Musterverteiler 3-Zimmer-Wohnung (ca. 75–90 m²)

4-reihiger Verteiler, mehr als 20 % Reserve. Die Querschnitte sind gegenüber dem Quellmaterial **bereinigt**: B16 nur noch auf 2,5 mm², Kreise mit 1,5 mm² an B13 bzw. B10 (Begründung → [C6](C06_kabel_leitungsanlagen.md), Abschnitt 3.4).

| Kreis | Schutzorgan | LS | Leitung (NYM-J) | Außenleiter | Versorgungsbereich |
|---|---|---|---|---|---|
| F1 | RCD 1 | B16, 3-polig | 5 × 2,5 mm² | L1-L2-L3 | Herd/Kochfeld, Backofen |
| F2 | RCD 1 | B16 | 3 × 2,5 mm² | L1 | Geschirrspüler |
| F3 | RCD 1 | B16 | 3 × 2,5 mm² | L2 | Arbeitssteckdosen Küche |
| F4 | RCD 1 | B16 | 3 × 2,5 mm² | L3 | Wohnzimmer: Steckdosen, Medienwand |
| F5 | RCD 1 | B13 | 3 × 1,5 mm² | L1 | Schlafzimmer: Steckdosen |
| F6 | RCD 1 | B10 | 3 × 1,5 mm² | L2 | Beleuchtung Wohnzimmer, Küche, Flur, Balkon |
| F7 | RCD 2 | B16 | 3 × 2,5 mm² | L1 | Waschmaschine |
| F8 | RCD 2 | B16 | 3 × 2,5 mm² | L2 | Wäschetrockner |
| F9 | RCD 2 | B16 | 3 × 2,5 mm² | L3 | Mikrowelle/Dampfgarer |
| F10 | RCD 2 | B13 | 3 × 1,5 mm² | L1 | Kinder-/Arbeitszimmer: Steckdosen |
| F11 | RCD 2 | B10 | 3 × 1,5 mm² | L2 | Beleuchtung Schlaf-, Kinderzimmer |
| F12 | RCD 2 | B13 | 3 × 1,5 mm² | L3 | Flur, Abstellraum: Steckdosen |
| F13 | RCD 2 | B13 | 3 × 1,5 mm² | L3 | Balkon/Loggia: Außensteckdose, Außenleuchte |
| F14 | RCBO 30 mA | B13 | 3 × 1,5 mm² | L1 | Bad: Beleuchtung, Waschtischsteckdosen (→ C8) |
| F15 | RCBO 30 mA | B13 | 3 × 1,5 mm² | L2 | Kühl-/Gefrierkombination |
| F16 | RCD 1 | B13 | 3 × 1,5 mm² | L3 | Kommunikationsverteiler: Router, ONT, Türsprechanlage |
| – | – | – | – | – | Reserve: mindestens 20 % der Teilungseinheiten |

**Änderungen gegenüber dem Quellmaterial (Übersichtsbericht):**
- Steckdosenkreise mit 3 × 1,5 mm² an B16 auf B13 umgestellt, Wohnzimmer auf 3 × 2,5 mm²/B16
- Licht und Steckdosen im Schlafzimmer getrennt (F5/F11)
- Multimedia-Kreis nicht mehr „direkt“, sondern über RCD: Er versorgt Steckdosen, also gilt die RCD-Pflicht nach DIN VDE 0100-410
- Mikrowelle, Trockner, Waschmaschine einheitlich 2,5 mm² wegen Dauerlast

## 5 Ausführungshinweise und Fallstricke

- **Verfügbarkeit bei einem Fehler:** Durch die Trennung von Licht und Steckdosen und die RCBOs für Bad und Kühlgerät bleibt die Wohnung bei einem Isolationsfehler nutzbar und beleuchtet.
- **Herdanschluss:** Kochfelder über 11 kW brauchen größere Querschnitte. Herstellerangabe prüfen.
- **Phasenlage der RCDs:** Pro RCD-Gruppe die Außenleiter gleichmäßig belegen, sonst lösen hohe Ableitströme einer Phase eher aus.
- **Kommunikationsverteiler:** braucht einen eigenen Kreis mit mehreren Steckdosen → [C9](C09_kommunikation_gebaeudesystemtechnik.md).

## 6 Bestand

Bei Erweiterung um neue Stromkreise gelten für diese Kreise die aktuellen Normen vollständig, einschließlich RCD und Erstprüfung → [E1](E1_eingriffsarten.md).

## 7 Querverweise

- Wohnungsverteiler → [C4](C04_wohnungsverteiler.md)
- Querschnitt und Absicherung → [C5.3](C05_3_ueberstromschutz.md), [C6](C06_kabel_leitungsanlagen.md)
- Muster Stromkreisliste → [AH-E](AH-E_muster.md)
