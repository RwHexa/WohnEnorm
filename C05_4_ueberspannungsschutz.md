# C5.4 Überspannungsschutz (DIN VDE 0100-443/-534, DIN EN 50550)

> **Stand:** Material übernommen (Tabellen aus dem ÜSS-PDF neu aufgebaut)
> **Kurz:** Seit der Ausgabe 2016-10 der DIN VDE 0100-443 ist der Schutz gegen transiente Überspannungen auch in Wohngebäuden gefordert; die Übergangsfrist endete am 14.12.2018. Üblich ist ein Typ 2 oder ein Kombiableiter Typ 1+2. Gegen dauerhafte Überspannung bei N-Leiterbruch hilft das nicht. Dafür gibt es POP-Einrichtungen nach DIN EN 50550.

---

## 1 Normgrundlage

| Regelwerk | Regelungsbereich | Praktische Bedeutung |
|---|---|---|
| DIN VDE 0100-443 | *Ob*: wann ein SPD erforderlich ist | Bei Neuanlagen in Wohngebäuden praktisch immer |
| DIN VDE 0100-534 | *Wie*: Auswahl und Errichtung der SPD | Typ, Einbauort, 0,5-m-Regel, Erdungsquerschnitt |
| VDE-AR-N 4100 | Einbau im Zählerplatz | SPD auf der 40-mm-Sammelschiene im NAR. Typ 1 bei äußerem Blitzschutz oder Freileitungseinspeisung |
| DIN EN 62305 (VDE 0185-305) | Blitzschutz | Bei äußerem Blitzschutz: Typ 1 bzw. 1+2 am Gebäudeeintritt im Blitzschutz-Potentialausgleich |
| DIN EN 50550 | POP | Schutz gegen netzfrequente Überspannung (TOV), insbesondere bei N-Leiterbruch |
| DIN VDE 0100-712/-722 | PV, E-Mobilität | SPD auf der DC-Seite der PV, Schutz der Ladeeinrichtung |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| SPD bei Neuanlagen in Wohngebäuden | **Muss** | -443 (Ausgabe 2016-10, Übergangsfrist bis 14.12.2018) |
| Typ 1 bzw. Typ 1+2 bei äußerem Blitzschutz oder Freileitungseinspeisung | **Muss** | -534, VDE-AR-N 4100 |
| Gesamte Anschlussleitungslänge (Abgriff → SPD → Erdungsschiene) ≤ 0,5 m | **Muss** | -534 |
| Erdungsleiter ≥ 16 mm² Cu bei Typ 1 bzw. 1+2, ≥ 6 mm² Cu bei Typ 2 | **Muss** | -534 |
| SPD in Energieflussrichtung vor den RCDs | **Muss** | -534 |
| Zusätzlicher Typ 2 in Unterverteilungen, die mehr als 10 m Leitungslänge vom vorgeschalteten SPD entfernt sind | **Soll** | -534 |
| POP nach DIN EN 50550 | **Empfehlung** (nicht pauschal vorgeschrieben) | DIN EN 50550 |

## 3 Auswahl

| Typ | Funktion | Einbauort |
|---|---|---|
| Typ 1 | Blitzstromableiter (Grobschutz) | Gebäudeeintritt, NAR |
| Typ 2 | Überspannungsableiter (Mittelschutz) | Zählerschrank/Wohnungsverteiler |
| Typ 1+2 | Kombiableiter | NAR, ersetzt Typ 1 + Typ 2 |
| Typ 3 | Geräteschutz (Feinschutz) | am Endgerät, max. 10 m hinter Typ 2 ⚠ prüfen |

**POP (DIN EN 50550):** Gewöhnliche SPD wirken nur gegen Spannungsspitzen im Mikrosekundenbereich. Bei einem unterbrochenen Neutralleiter (Sternpunktverschiebung) können dauerhaft bis zu 400 V an den Verbrauchern anliegen. Eine POP-Einrichtung überwacht die Spannung L–N und trennt ab etwa 275 V AC über den gekoppelten LS oder RCD allpolig. Verbaute SPD sollten eine hohe TOV-Festigkeit haben (z. B. U_C = 440 V).

Sinnvoll ist POP bei empfindlichen Verbrauchern, Freileitungsnetzen und alten Steigleitungen.

## 4 Ausführungshinweise und Fallstricke

- **0,5-m-Regel** ist die häufigste Fehlerquelle. Längere Anschlussleitungen erzeugen einen induktiven Spannungsfall, der die Schutzwirkung aufhebt. V-Verdrahtung bevorzugen.
- Arbeiten im plombierten NAR nur durch den eingetragenen Betrieb (§ 13 NAV).
- Datenleitungen (Antenne, Telefon, Netzwerk) in den Überspannungsschutz einbeziehen.

## 5 Bestand

| Anlagenstatus | Pflicht | Einordnung |
|---|---|---|
| Neuanlage, Neubau, komplette Kernsanierung | **Muss** | Ohne SPD keine Inbetriebnahme. -443/-534 und VDE-AR-N 4100 gelten vollständig. |
| Unveränderte Bestandsanlage | keine Nachrüstpflicht | Wenn bei Errichtung normgerecht. Nachrüstung aus Sicherheits- und Versicherungsgründen empfohlen. |
| Wesentliche Erweiterung, Umbau | **Muss** für den erweiterten Teil | Auslöser: PV, Ladeeinrichtung, Wärmepumpe, neuer Stromkreis, Zählerschrankumbau |
| Versicherung | vertragliche Obliegenheit | Viele Versicherer verlangen SPD in aktuellen Tarifen |

→ [E3](E3_nachruestpflichten.md)

## 6 Querverweise

- Zählerplatz → [C2](C02_zaehlerplatz.md)
- Erdung → [C7](C07_erdung_potentialausgleich.md)
- PV, Ladeeinrichtung → [D1](D1_ladeeinrichtungen.md), [D2](D2_photovoltaik_speicher.md)
