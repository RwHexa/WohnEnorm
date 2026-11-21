# C1 Netzanschluss, Hausanschlussraum, Hauptleitung

> **Stand:** Material übernommen
> **Kurz:** Der Hausanschlusskasten ist die Eigentumsgrenze. Im Mehrfamilienhaus ist ein Hausanschlussraum Pflicht. Die Hauptleitung zum Zählerplatz wird für mindestens 63 A ausgelegt; ihr Spannungsfall ist auf 0,5 % begrenzt.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| NAV | Netzanschluss und Anschlussnutzung |
| VDE-AR-N 4100 | Hausanschluss, Hauptstromversorgungssystem |
| DIN 18012 | Hausanschlussraum, -nische, -wand |
| DIN 18015-1 | Hauptleitungen, Spannungsfall |

## 2 Anforderungen

| Anforderung | Verbindlichkeit | Fundstelle |
|---|---|---|
| Hausanschlussraum in Mehrfamilienhäusern | **Muss** | DIN 18012 |
| Mindestmaße Hausanschlussraum: Breite 1,80 m, Höhe 2,00 m | **Muss** ⚠ prüfen | DIN 18012 |
| Unterbringung von HAK, Zählerschrank, Haupterdungsschiene, Telekommunikation | **Soll** | DIN 18012 |
| Hauptleitung mit mindestens 63 A Belastbarkeit | **Soll** | DIN 18015-1 |
| Spannungsfall HAK → Messeinrichtung höchstens 0,5 % | **Muss** ⚠ prüfen | DIN 18015-1, VDE-AR-N 4100 |

## 3 Auslegung

**Spannungsfall Drehstrom:**

ΔU % = (√3 · L · I · cos φ) / (κ · A · U_n) · 100

mit κ_Cu = 56 m/(Ω·mm²) bei 20 °C, U_n = 400 V.

**Spannungsfall-Budget der Kundenanlage** ⚠ prüfen:

| Abschnitt | Grenze |
|---|---|
| Hauptleitung HAK → Zähler | 0,5 % |
| Messeinrichtung → Anschlusspunkt Verbrauchsmittel | 3 % |
| davon typisch: Zähler → Wohnungsverteiler | 0,5–1,0 % |
| davon: Endstromkreis | der Rest bis 3 % |

> **Widerspruch im Quellmaterial:** Der Übersichtsbericht rechnet die 0,5 % der Hauptleitung *in* die 3 % ein; die Absicherungs-Ausarbeitung zählt die 3 % *ab Zähler*. DIN 18015-1 zählt ab der Messeinrichtung. Vor Veröffentlichung am Normtext bestätigen.

**Typische Werte Hauptleitung:**

| Abschnitt | Absicherung | Mindestquerschnitt Cu | Max. ΔU |
|---|---|---|---|
| Hauptleitung HAK → Zähler | 63 A (NH im HAK) | 16 mm² | 0,5 % |

## 4 Ausführungshinweise und Fallstricke

- TAB des Netzbetreibers vor der Planung abrufen. Sie können vom Standard abweichende Festlegungen enthalten.
- Bei mehreren Wohnungen entscheidet die Gleichzeitigkeit über den Querschnitt der Hauptleitung. Spätere Wallboxen und Wärmepumpen einrechnen → [D4](D4_auswirkungen_anlage.md).

## 5 Bestand

Bestehende Hauptleitungen sind häufig zu klein für neue Großverbraucher. Vor dem Anschluss einer Ladeeinrichtung oder Wärmepumpe die Hauptleitung prüfen.

## 6 Querverweise

- Zählerplatz → [C2](C02_zaehlerplatz.md)
- Erdung, Haupterdungsschiene → [C7](C07_erdung_potentialausgleich.md)
