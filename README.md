<img src="bilder/logo-rwtec.png" width="72" alt="RwTec">

# WohnEnorm

**Elektrische Anlagen im Wohnungsbau – Normen, Vorschriften, Ausführung**

Ein Fach- und Nachschlagewerk für **Elektrofachkräfte und Planer**. Es stellt die Normen und Vorschriften zusammen, die beim Errichten, Erweitern und Prüfen elektrischer Anlagen in Wohnungen gelten. Zu jeder Anforderung nennt es die Fundstelle, die Verbindlichkeit (Muss/Soll/Empfehlung) und den Rechenweg.

📄 **Gesamtfassung als PDF:** [Elektrische_Anlagen_Wohnungsbau_Gesamt.pdf](Elektrische_Anlagen_Wohnungsbau_Gesamt.pdf)
📑 **Inhaltsverzeichnis mit Bearbeitungsstand:** [INHALT.md](INHALT.md)

---

## Geltungsbereich

- Wohnungen im **Mehrfamilienhaus**, Neubau: vom Hausanschluss bis zur Steckdose
- **Bestand und Sanierung**: Instandhaltung, Erweiterung, neuer Stromkreis
- **Neue Verbraucher und Erzeuger**: Ladeeinrichtung, Photovoltaik, Speicher, Wärmepumpe, § 14a EnWG

## Aufbau

Das Werk folgt dem **Energiefluss**: Netz → Zählerplatz → Wohnungsverteiler → Leitungsanlage → Betriebsmittel. Davor steht die Planung, danach kommen Prüfung und Betrieb.

| Teil | Inhalt |
|---|---|
| [A](A1_rechtsrahmen.md) | Grundlagen: Rechtsrahmen, Normensystematik, Begriffe und Netzsysteme |
| [B](B1_bedarfsermittlung_ausstattung.md) | Planung: Ausstattung nach DIN 18015-2 / RAL-RG 678, Stromkreisaufteilung |
| [C](C01_netzanschluss.md) | Anlagenaufbau: Netzanschluss, Zählerplatz, Wohnungsverteiler, Schutzmaßnahmen, Leitungsanlagen, Erdung, Bad, Kommunikation, Brandschutz |
| [D](D1_ladeeinrichtungen.md) | Neue Verbraucher und Erzeuger |
| [E](E1_eingriffsarten.md) | Bestand und Sanierung |
| [F](F1_erstpruefung.md) | Prüfung, Inbetriebnahme, Dokumentation, Betrieb |
| [AH](AH-A_normenverzeichnis.md) | Normenverzeichnis, Bemessungstabellen, Checklisten, typische Mängel, Muster, Glossar |

Alle Kapitel sind gleich gegliedert: **Normgrundlage → Anforderungen → Auslegung und Berechnung → Ausführungshinweise → Bestand → Querverweise.** Ausgabestände der Normen stehen nur an einer Stelle, im [Normenverzeichnis AH-A](AH-A_normenverzeichnis.md).

## Stand

**Arbeitsfassung, November 2026.** Stellen mit **⚠ prüfen** sind noch gegen den jeweiligen Normtext abzugleichen. Welche Kapitel ausgearbeitet und welche noch Gerüst sind, steht in [INHALT.md](INHALT.md).

## PDF selbst bauen

Voraussetzungen: Python 3 mit `markdown-it-py` und `PyMuPDF`, dazu Google Chrome oder Microsoft Edge.

```bash
pip install markdown-it-py pymupdf
python werkzeuge/build_pdf.py
```

Das Skript liest die Kapitelreihenfolge aus `INHALT.md`, setzt alles zu einer HTML-Seite zusammen, druckt sie über Chrome/Edge headless als PDF und ergänzt Seitenzahlen, Inhaltsverzeichnis und Lesezeichen.

## Mitarbeit

Hinweise auf Fehler, neuere Ausgabestände oder fehlende Themen gern als Issue. Neue Kapitel bitte nach der [Kapitelvorlage](_vorlage_kapitel.md) anlegen und in `INHALT.md` eintragen.

## Hinweis

Dieses Werk gibt einen Überblick über das geltende Regelwerk. Es ist **keine Planungsunterlage** und ersetzt weder den Normtext noch die Fachplanung. Normen werden laufend überarbeitet; Ausgabestände sind vor jeder Verwendung zu prüfen. Normtexte selbst sind urheberrechtlich geschützt und nicht Bestandteil dieses Repositorys. Ausführung und Anmeldung beim Netzbetreiber bleiben dem eingetragenen Installationsbetrieb vorbehalten (§ 13 NAV).

## Lizenz

[MIT](LICENSE) · © 2026 RwTec
