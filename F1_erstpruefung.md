# F1 Erstprüfung (DIN VDE 0100-600)

> **Stand:** Material übernommen
> **Kurz:** Vor der Inbetriebnahme wird jede Anlage besichtigt, erprobt und gemessen. Erst nach bestandener Prüfung darf sie in Betrieb gehen. Das Prüfprotokoll ist der einzige Nachweis, dass die Schutzmaßnahmen tatsächlich wirken.

---

## 1 Normgrundlage

| Regelwerk | Abschnitt |
|---|---|
| DIN VDE 0100-600 | Erstprüfung |
| DIN VDE 0100-410 | Abschaltbedingungen → C5.1 |
| DIN EN 61557 | Messgeräte ⚠ prüfen |

## 2 Prüfschritte

| Schritt | Inhalt |
|---|---|
| **Besichtigen** | Auswahl und Errichtung der Betriebsmittel, Kennzeichnung, Leitungsführung, Badbereiche, Schutzpotentialausgleich, SPD-Anschluss (0,5 m), Dokumentation vorhanden |
| **Erproben** | RCD-Prüftaste, Funktion von Schaltern, Verriegelungen, Rauchwarnmeldern |
| **Messen** | siehe Abschnitt 3 |

## 3 Messungen und Grenzwerte

| Messung | Grenzwert | Hinweis |
|---|---|---|
| Durchgängigkeit Schutzleiter und Schutzpotentialausgleich | niederohmig, plausibel zur Leitungslänge | Messstrom ≥ 200 mA |
| Isolationswiderstand (Anlagen bis 500 V) | ≥ 1 MΩ bei 500 V DC | SPD und empfindliche Geräte vorher abklemmen |
| Schleifenimpedanz Z_S | ≤ 2/3 · U_0 / I_a (z. B. B13 ≤ 2,36 Ω, B16 ≤ 1,92 Ω) | Tabelle → [AH-B](AH-B_bemessungstabellen.md) |
| RCD: Auslösezeit | ≤ 300 ms bei I_Δn (unverzögerter RCD) | |
| RCD: Berührungsspannung | ≤ 50 V | |
| Drehfeld | rechtsdrehend an Drehstromsteckdosen/Herd | |
| Spannungsfall | ≤ Budget nach DIN 18015-1 | nur bei Bedarf rechnerisch oder messtechnisch |

⚠ prüfen: Grenzwerte am Normtext bestätigen.

## 4 Ausführungshinweise und Fallstricke

- Ohne Messprotokoll gibt es keinen Nachweis der Schutzwirkung; das wird im Schadensfall zum Problem.
- Messwerte je Stromkreis in die Stromkreisliste übertragen → [AH-E](AH-E_muster.md).
- Bei Erweiterungen: neuen Teil vollständig prüfen, betroffenen Altteil mitmessen.

## 5 Querverweise

- Inbetriebsetzung und Dokumentation → [F2](F2_inbetriebsetzung_dokumentation.md)
- Wiederholungsprüfung → [F3](F3_betrieb_wiederholungspruefung.md)
