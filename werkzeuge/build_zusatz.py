"""Baut die Zusatzdokumente im Ordner zusatz/ zu je einer PDF.

Aufruf:  python werkzeuge/build_zusatz.py   (aus dem Ordner werk/)
"""
from pathlib import Path

import fitz
from markdown_it import MarkdownIt

from build_pdf import CSS, WERK, chrome_pdf, md_zu_html

ZUSATZ = WERK / "zusatz"

PROTOKOLL_CSS = """
@page { margin: 12mm 12mm 16mm 12mm; }
body { font-size: 8.6pt; }
h1 { font-size: 13.5pt; margin-bottom: 4px; }
h2 { font-size: 10.5pt; margin: 10px 0 3px 0; }
p { margin: 3px 0; }
table { font-size: 8.2pt; margin: 3px 0 6px 0; }
th, td { padding: 2px 4px; height: 6.3mm; vertical-align: middle; }
th { height: auto; }
tr:nth-child(even) td { background: #fff; }
thead:not(:has(th:not(:empty))) { display: none; }
table { break-inside: avoid; }
"""

DOKUMENTE = [
    # (Markdown, Fußzeile, zusätzliches CSS)
    ("DGUV-V3_Pruefung_Wohnung.md",
     "Wiederkehrende Prüfung ortsfester Anlagen in Wohnungen - RwTec", ""),
    ("DGUV-V3_Pruefprotokoll_Wohnung.md",
     "Prüfprotokoll Wohnung - DGUV V3 / DIN VDE 0105-100 - Protokoll-Nr. ________", PROTOKOLL_CSS),
]


def baue(md_datei, fusszeile, extra_css):
    quelle = ZUSATZ / md_datei
    md = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")
    inhalt = md_zu_html(md, quelle.read_text(encoding="utf-8"), basis=ZUSATZ)
    seite = (f'<!doctype html><html lang="de"><head><meta charset="utf-8">'
             f'<title>{quelle.stem}</title><style>{CSS}{extra_css}</style></head>'
             f'<body>{inhalt}</body></html>')
    ziel = quelle.with_suffix(".pdf")
    roh = quelle.with_suffix(".roh.pdf")
    chrome_pdf(seite, roh)
    doc = fitz.open(roh)
    n = doc.page_count
    for i, s in enumerate(doc):
        y = s.rect.height - 8 * 2.835
        s.insert_text((12 * 2.835, y), fusszeile, fontsize=7, fontname="helv", color=(0.4, 0.4, 0.4))
        txt = f"Seite {i + 1} von {n}"
        b = fitz.get_text_length(txt, fontname="helv", fontsize=7)
        s.insert_text((s.rect.width - 12 * 2.835 - b, y), txt, fontsize=7, fontname="helv",
                      color=(0.4, 0.4, 0.4))
    doc.set_metadata({"title": quelle.stem.replace("_", " "), "author": "RwTec"})
    doc.save(ziel, garbage=3, deflate=True)
    doc.close()
    roh.unlink()
    print(f"Fertig: {ziel.name} ({n} Seiten)")


if __name__ == "__main__":
    for d in DOKUMENTE:
        baue(*d)
