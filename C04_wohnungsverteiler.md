# C4 Wohnungsverteiler

> **Stand:** Material übernommen
> **Kurz:** Jede Wohnung hat einen eigenen Stromkreisverteiler mit Hauptschalter, mindestens zwei RCD-Gruppen und 20 % Reserve. Als Installationsverteiler für Laien (DBO) muss er DIN EN 61439-3 entsprechen. Die Belegung wird im Verteiler beschriftet.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN 18015-1/-2 | Stromkreisverteiler je Wohnung |
| DIN EN 61439-3 (VDE 0660-600-3) | Installationsverteiler für Laien, Bauartnachweis |
| DIN VDE 0100-530 | Schalt- und Steuergeräte |
| DIN VDE 0100-460 | Hauptschalter → C5.5 |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Eigener Stromkreisverteiler je Wohnung | **Muss** | DIN 18015-1 |
| Verteiler mit Bauartnachweis nach DIN EN 61439-3, Herstellerangaben (Verlustleistung, Bemessungsstrom) eingehalten | **Muss** | DIN EN 61439-3 |
| Mindestens zwei RCDs 30 mA | **Soll** ⚠ prüfen | DIN 18015-1 |
| Mindestens 20 % Reserveplatz | **Soll** | DIN 18015-1 |
| Dauerhafte Beschriftung der Stromkreise | **Muss** | DIN VDE 0100-510 ⚠ prüfen |
| SPD vor den RCDs, wenn im Wohnungsverteiler | **Muss** | DIN VDE 0100-534 → C5.4 |

## 3 Auslegung

- **Verlustleistung:** Summe der Verlustleistungen der Einbaugeräte bei Betriebsstrom ≤ zulässige Verlustleistung des Verteilers (Herstellerangabe). Kritisch bei vielen RCBOs und hoher Dauerlast.
- **Gleichzeitigkeit:** Bemessungsbelastungsfaktor nach DIN EN 61439-3 beachten.
- **Teilungseinheiten (TE):** Reihen × TE pro Reihe; 20 % Reserve auf die belegten TE.

Musterbelegung → [B2](B2_stromkreisaufteilung.md).

## 4 Ausführungshinweise und Fallstricke

- Buskoppler, Logikmodule und Gateways der Gebäudesystemtechnik sind Reiheneinbaugeräte und gehören in den Stromkreisverteiler, nicht in den Kommunikationsverteiler → [C9](C09_kommunikation_gebaeudesystemtechnik.md).
- Zwischen Stromkreis- und Kommunikationsverteiler ein Rohr oder Kanal vorsehen.
- Belegungsplan auch als Dokument übergeben → [F2](F2_inbetriebsetzung_dokumentation.md).

## 5 Bestand

Bietet ein alter Verteiler keinen Platz oder keine sichere Trennung von N und PE, ist für neue Stromkreise oft eine neue Unterverteilung nötig → [E2](E2_altanlagen.md).

## 6 Querverweise

- Schutzmaßnahmen → [C5.1](C05_1_schutz_elektrischer_schlag.md) bis [C5.5](C05_5_trennen_schalten.md)
