# C9 Kommunikation und Gebäudesystemtechnik (DIN 18015-4)

> **Stand:** Material übernommen
> **Kurz:** Jede Wohnung braucht neben dem Stromkreisverteiler einen Kommunikationsverteiler als Sternpunkt des Heimnetzes. DIN 18015-4 gilt für Gebäude, die mit Gebäudesystemtechnik ausgestattet *oder dafür vorbereitet* werden. Die Vorbereitung ist der häufigere Fall und der wertvollste Teil der Norm.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN 18015-4 | Ausgabe 2022-08 (ersetzt 2014-05, Umfang von 28 auf 41 Seiten erweitert) |
| DIN 18015-2/-3 | Kommunikationsverteiler, Rohrnetze, Installationszonen |
| DIN EN 50173-4 | Kommunikationskabelanlagen in Wohnungen |
| VDE-AR-N 4100 | RfZ im Zählerplatz → C2 |

**Quellenlage:** Der Normtext ist kostenpflichtig. Die Angaben stammen aus veröffentlichten Kurzreferaten und Inhaltsangaben. Die Gliederung ist für die Ausgabe 2014 belegt und dürfte im Kern fortbestehen.

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Kommunikationsverteiler je Wohnung zusätzlich zum Stromkreisverteiler | **Soll** | DIN 18015 |
| Rohr oder Kanal zwischen Stromkreis- und Kommunikationsverteiler | **Muss** | DIN 18015-4 |
| Eigenes Rohrnetz jeweils für IuK und RuK | **Muss** | DIN 18015-4 |
| Kommunikationsleitungen austauschbar in Rohren | **Muss** | DIN 18015-3 |
| Buskoppler, Logikmodule, Gateways im Stromkreisverteiler | **Soll** | DIN 18015-4 |
| Sternförmige Datenverkabelung, mindestens Kat. 6A | **Empfehlung** | DIN EN 50173-4, Praxis |
| Abstimmung mit dem Bauherrn: Funktionen, Bedienorte, Erweiterbarkeit | **Soll** | DIN 18015-4 |

## 3 Inhalt der DIN 18015-4

| Abschnitt | Inhalt |
|---|---|
| 4 | Errichtungsgrundsätze: Leitungsführung, Dimensionierung der Verteilung, Installationsdosen, Anordnung der Komponenten |
| 5–7 | Bedienfunktionen, Anzeige- und Bedieneinrichtungen, Schnittstellen, einschließlich Beleuchtungsplanung |
| Anhang A | Beispiel einer Konfiguration mit Adressierungsschema |

Abschnitt 4 ist der praktisch wichtigste Teil. Dort stehen die baulichen Festlegungen, die sich später nicht mehr ändern lassen.

**Übertragungswege:**

| Weg | Auflage |
|---|---|
| Busleitung | Regelfall, Leitungsführung nach Abschnitt 4 |
| Powerline | Signale dürfen die Wohnung nicht verlassen und Nachbarn nicht stören (ohne Filter im Zählerschrank kaum einzuhalten) |
| Funk | Störfestigkeit beachten. Stahlbeton und metallbedampfte Scheiben verringern die Reichweite. |

## 4 Kommunikationsverteiler

- **Inhalt:** TAE-Dose, Router oder Modem, Switch, Verstärker, Netzteile, Glasfaser-Abschlusspunkt (APL/ONT)
- **Größe:** nicht festgelegt. Sie ergibt sich aus den Komponenten und der Zahl der abgehenden Rohre.
- **Nicht verwechseln:** Das RfZ im Zählerschrank gehört dem Netzbetreiber; der eigene Router gehört in den Kommunikationsverteiler.
- **WLAN:** Ein geschlossener Metallschrank ist ein Faradayscher Käfig. Lösung: verkabelte Access Points in der oberen Installationszone oder an der Decke. Der Router im Verteiler bleibt dann reiner Router.
- **Steckdosen großzügig:** Router, ONT, Switch, NAS bringen jeweils ein Netzteil mit. Wärmeabfuhr im geschlossenen Schrank beachten.
- **Reserve:** Die 20 % aus DIN 18015 beziehen sich auf den Stromkreisverteiler. Den Kommunikationsverteiler trotzdem großzügig auslegen; dort kommt erfahrungsgemäß mehr hinzu.

## 5 RAL-RG 678 „plus“

Anlagen mit Gebäudesystemtechnik erhalten den Zusatz „plus“ (z. B. Ausstattungswert 1 plus). Das ist keine eigene Stufe, sondern eine Ergänzung zu jeder der drei Stufen → [B1](B1_bedarfsermittlung_ausstattung.md).

## 6 Vorbereitung ohne Systementscheidung

Eine Busleitung im Rohbau mitzuziehen kostet fast nichts; sie nachträglich einzubringen bedeutet Stemmarbeiten in jedem Raum. Wer sich beim System noch nicht festlegen will, hält mit dieser Vorbereitung KNX, Funk und IP-Lösungen offen:

- sternförmige Leitungsführung
- tiefe Installationsdosen
- Leerrohre zu den Fenstern für Antriebe
- Reserveplatz im Verteiler

## 7 Bestand

Nachträglich ist eine sternförmige Verkabelung in einer bewohnten Wohnung kaum wirtschaftlich. Hier lohnt vorausschauende Planung mehr als an fast jeder anderen Stelle.

## 8 Querverweise

- Zählerplatz, RfZ → [C2](C02_zaehlerplatz.md)
- Wohnungsverteiler → [C4](C04_wohnungsverteiler.md)

**Quellen:** DIN 18015-4:2022-08 und 2014-05 (DIN Media, Kurzreferat); Hager Tipp 21 (DIN 18015, Mindestausstattung); IET Berlin und Hager Tipp 44 zu VDE-AR-N 4100:2026-04.
