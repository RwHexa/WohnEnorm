"""Baut alle Kapitel des Werkes zu einer Gesamt-PDF zusammen.

Ablauf: Markdown -> eine HTML-Datei (markdown-it) -> PDF (Chrome headless)
-> Seitenzahlen, Lesezeichen und Inhaltsverzeichnis-Seiten (PyMuPDF).

Aufruf:  python werkzeuge/build_pdf.py   (aus dem Ordner werk/)
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF
from markdown_it import MarkdownIt

WERK = Path(__file__).resolve().parent.parent
AUSGABE = WERK / "Elektrische_Anlagen_Wohnungsbau_Gesamt.pdf"
CHROME_KANDIDATEN = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]
TITEL = "Elektrische Anlagen im Wohnungsbau"

CSS = """
@page { size: A4; margin: 18mm 17mm 20mm 17mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", Calibri, Arial, sans-serif; font-size: 10pt;
       line-height: 1.45; color: #1d232a; }
h1 { font-size: 19pt; color: #0b3d63; border-bottom: 2px solid #0b3d63;
     padding-bottom: 4px; margin: 0 0 10px 0; }
h2 { font-size: 13pt; color: #0b3d63; margin: 18px 0 6px 0; break-after: avoid; }
h3 { font-size: 11pt; color: #23527a; margin: 14px 0 4px 0; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
section.kapitel { break-before: page; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px 0;
        font-size: 8.8pt; break-inside: auto; }
tr { break-inside: avoid; }
th { background: #e3ecf4; color: #0b3d63; text-align: left; }
th, td { border: 1px solid #b9c6d2; padding: 3px 5px; vertical-align: top; }
tr:nth-child(even) td { background: #f6f9fb; }
blockquote { margin: 6px 0 12px 0; padding: 6px 10px; background: #eef4f9;
             border-left: 4px solid #0b3d63; }
blockquote p { margin: 2px 0; }
code { font-family: Consolas, monospace; font-size: 9pt; background: #f1f3f5;
       padding: 0 2px; }
pre { background: #f1f3f5; padding: 6px 8px; font-size: 8.5pt; white-space: pre-wrap; }
hr { border: 0; border-top: 1px solid #c9d3dc; margin: 10px 0; }
a { color: #0b5c99; text-decoration: none; }
.pruefen { background: #fff1b8; color: #7a4b00; font-weight: 600;
           padding: 0 2px; border-radius: 2px; }
.titelseite { height: 250mm; display: flex; flex-direction: column;
              justify-content: center; }
.titelseite .logo { width: 24mm; height: 24mm; margin-bottom: 14px; }
.titelseite h1 { font-size: 30pt; border: 0; margin-bottom: 4px; }
.titelseite .unter { font-size: 16pt; color: #23527a; margin-bottom: 40px; }
.titelseite .meta { font-size: 11pt; color: #444; line-height: 1.8; }
.titelseite .hinweis { margin-top: 50px; padding: 10px 12px; background: #fff7d6;
                       border-left: 4px solid #d9a400; font-size: 9.5pt; }
.inhalt { break-before: page; }
.inhalt h1 { margin-bottom: 14px; }
.toc { width: 100%; border: 0; font-size: 10pt; }
.toc td { border: 0; padding: 2px 4px; background: none !important; }
.toc tr.teil td { font-weight: 700; color: #0b3d63; padding-top: 9px; }
.toc td.nr { width: 14mm; color: #555; }
.toc td.seite { width: 14mm; text-align: right; }
"""


def kapitel_reihenfolge():
    """Reihenfolge aus dem Inhaltsverzeichnis in INHALT.md (Teilzeilen inklusive)."""
    eintraege = []
    for zeile in (WERK / "INHALT.md").read_text(encoding="utf-8").splitlines():
        if zeile.startswith("## "):
            break
        teil = re.match(r"\|\s*\|\s*\*\*(.+?)\*\*", zeile)
        if teil:
            eintraege.append(("teil", teil.group(1), None))
            continue
        kap = re.match(r"\|\s*([^|]+?)\s*\|\s*\[([^\]]+)\]\(([^)/]+\.md)\)", zeile)
        if kap:
            eintraege.append(("kapitel", kap.group(1), (kap.group(2), kap.group(3))))
    return eintraege


def anker(dateiname):
    return "k-" + Path(dateiname).stem


def md_zu_html(md, text, basis=WERK):
    # Bilder nur einbinden, wenn vorhanden (Pfad relativ zur Markdown-Datei)
    def bild(m):
        pfad = (basis / m.group(1)).resolve()
        return m.group(0).replace(m.group(1), pfad.as_uri()) if pfad.exists() else ""
    text = re.sub(r'<img src="([^"]+)"[^>]*>', bild, text)
    # "Stand" und "Kurz" im Kopfkasten als eigene Absätze
    text = text.replace("\n> **Kurz:**", "\n>\n> **Kurz:**")
    # Checklisten-Kästchen
    text = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", text, flags=re.M)
    text = re.sub(r"^(\s*)- \[x\] ", r"\1- ☑ ", text, flags=re.M)
    h = md.render(text)
    # Querverweise auf Kapiteldateien -> interne Anker
    h = re.sub(r'href="([^"#/]+)\.md(#[^"]*)?"', lambda m: f'href="#k-{m.group(1)}"', h)
    h = h.replace("⚠ prüfen", '<span class="pruefen">⚠ prüfen</span>')
    h = h.replace("⚠", '<span class="pruefen">⚠</span>').replace(
        '<span class="pruefen"><span class="pruefen">⚠</span> prüfen</span>',
        '<span class="pruefen">⚠ prüfen</span>')
    return h


def baue_html(eintraege, seiten=None):
    md = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")
    seiten = seiten or {}
    toc = []
    teile = []
    for art, nr, daten in eintraege:
        if art == "teil":
            toc.append(f'<tr class="teil"><td colspan="3">{html.escape(nr)}</td></tr>')
            continue
        titel, datei = daten
        s = seiten.get(datei, "")
        toc.append(f'<tr><td class="nr">{html.escape(nr)}</td>'
                   f'<td><a href="#{anker(datei)}">{html.escape(titel)}</a></td>'
                   f'<td class="seite">{s}</td></tr>')
        text = (WERK / datei).read_text(encoding="utf-8")
        if datei == "00_vorwort.md":
            # Buchtitel steht auf der Titelseite; nur das Kapitel ab "# 00" übernehmen
            text = text[text.index("# 00"):]
        teile.append(f'<section class="kapitel" id="{anker(datei)}">{md_zu_html(md, text)}</section>')

    # Bearbeitungsstand aus INHALT.md (ohne Inhaltsverzeichnis) anhängen
    readme = (WERK / "INHALT.md").read_text(encoding="utf-8")
    rest = readme[readme.index("## Bereinigte"):]
    s = seiten.get("README.md", "")
    toc.append('<tr class="teil"><td colspan="3">Arbeitsstand</td></tr>')
    toc.append(f'<tr><td class="nr"></td><td><a href="#k-README">Bearbeitungsstand und offene Punkte</a></td>'
               f'<td class="seite">{s}</td></tr>')
    teile.append('<section class="kapitel" id="k-README">'
                 + md_zu_html(md, "# Bearbeitungsstand und offene Punkte\n\n" + rest) + "</section>")

    logo = WERK / "bilder" / "logo-rwtec.png"
    logo_html = f'<img class="logo" src="{logo.as_uri()}" alt="RwTec">' if logo.exists() else ""
    titelseite = f"""
<div class="titelseite">
  {logo_html}
  <h1>{TITEL}</h1>
  <div class="unter">Normen, Vorschriften, Ausführung</div>
  <div class="meta">
    Für Elektrofachkräfte und Planer<br>
    Wohnung im Mehrfamilienhaus · Bestand und Sanierung · Neue Verbraucher<br>
    RwTec · Stand November 2026
  </div>
  <div class="hinweis"><b>Arbeitsfassung zur Durchsicht.</b> Gelb markierte Stellen
  (<span class="pruefen">⚠ prüfen</span>) sind vor der Veröffentlichung gegen den Normtext abzugleichen.
  Ausgabestände: siehe Anhang AH-A.</div>
</div>"""
    inhalt = (f'<div class="inhalt"><h1>Inhalt</h1><table class="toc">{"".join(toc)}</table></div>')
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8">'
            f'<title>{TITEL}</title><style>{CSS}</style></head><body>'
            f'{titelseite}{inhalt}{"".join(teile)}</body></html>')


def chrome_pdf(html_text, ziel):
    chrome = next((c for c in CHROME_KANDIDATEN if c.exists()), None)
    if not chrome:
        sys.exit("Weder Chrome noch Edge gefunden.")
    with tempfile.TemporaryDirectory() as tmp:
        quelle = Path(tmp) / "werk.html"
        quelle.write_text(html_text, encoding="utf-8")
        subprocess.run([str(chrome), "--headless=new", "--disable-gpu",
                        "--no-pdf-header-footer", f"--user-data-dir={tmp}\\profil",
                        f"--print-to-pdf={ziel}", quelle.as_uri()],
                       check=True, capture_output=True, timeout=180)


def kapitelseiten(pdf_pfad, eintraege):
    """Findet die Startseite jedes Kapitels über den Text der Abschnittsüberschrift."""
    doc = fitz.open(pdf_pfad)
    seiten = {}
    start = 2  # nach Titelseite und Inhalt suchen
    ziele = [(d[1], d[1]) for a, _, d in eintraege if a == "kapitel"] + [("README.md", "README.md")]
    for datei, _ in ziele:
        if datei == "README.md":
            kopf = "Bearbeitungsstand und offene Punkte"
        else:
            erste = next(z for z in (WERK / datei).read_text(encoding="utf-8").splitlines()
                         if z.startswith("# ") and (datei != "00_vorwort.md" or z.startswith("# 00")))
            kopf = erste[2:].strip()
        such = kopf[:40]
        for i in range(start, doc.page_count):
            if doc[i].search_for(such):
                seiten[datei] = i + 1
                start = i
                break
    doc.close()
    return seiten


def nachbearbeiten(pdf_pfad, eintraege, seiten):
    doc = fitz.open(pdf_pfad)
    n = doc.page_count
    for i, seite in enumerate(doc):
        if i == 0:
            continue
        r = seite.rect
        y = r.height - 10 * 2.835
        seite.insert_text((17 * 2.835, y), f"{TITEL} - Arbeitsfassung November 2026",
                          fontsize=7.5, fontname="helv", color=(0.4, 0.4, 0.4))
        txt = f"Seite {i + 1} von {n}"
        breite = fitz.get_text_length(txt, fontname="helv", fontsize=7.5)
        seite.insert_text((r.width - 17 * 2.835 - breite, y), txt,
                          fontsize=7.5, fontname="helv", color=(0.4, 0.4, 0.4))
    # Lesezeichen
    toc = [[1, "Titel", 1], [1, "Inhalt", 2]]
    teil = None
    for art, nr, daten in eintraege:
        if art == "teil":
            teil = nr
            erste = next((seiten.get(d[1]) for a, _, d in eintraege[eintraege.index((art, nr, daten)) + 1:]
                          if a == "kapitel" and seiten.get(d[1])), None)
            if erste:
                toc.append([1, nr, erste])
            continue
        if daten[1] in seiten:
            toc.append([2 if teil else 1, f"{nr} {daten[0]}", seiten[daten[1]]])
    if "README.md" in seiten:
        toc.append([1, "Bearbeitungsstand und offene Punkte", seiten["README.md"]])
    doc.set_toc(toc)
    doc.set_metadata({"title": TITEL, "subject": "Normen, Vorschriften, Ausführung",
                      "author": "RwTec", "keywords": "DIN VDE 0100, DIN 18015, VDE-AR-N 4100"})
    tmp = pdf_pfad.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf_pfad)


def main():
    eintraege = kapitel_reihenfolge()
    roh = WERK / "_build_roh.pdf"
    # Durchlauf 1: Seiten ermitteln, Durchlauf 2: mit Seitenzahlen im Inhaltsverzeichnis
    chrome_pdf(baue_html(eintraege), roh)
    seiten = kapitelseiten(roh, eintraege)
    chrome_pdf(baue_html(eintraege, seiten), roh)
    seiten2 = kapitelseiten(roh, eintraege)
    if seiten2 != seiten:
        print("Hinweis: Seitenzahlen haben sich im 2. Durchlauf verschoben.")
    nachbearbeiten(roh, eintraege, seiten2)
    roh.replace(AUSGABE)
    fehlend = [d[1] for a, _, d in eintraege if a == "kapitel" and d[1] not in seiten2]
    print(f"Fertig: {AUSGABE} ({fitz.open(AUSGABE).page_count} Seiten)")
    if fehlend:
        print("Kapitelanfang nicht gefunden:", fehlend)


if __name__ == "__main__":
    main()
