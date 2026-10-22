# Week 10 — Programs 22–25 (Scala)

| # | Week | Date | Topic | Library |
|---|------|------|-------|---------|
| 22 | 13 | 15-10-2026 | Case Classes | stdlib |
| 23 | 13 | 15-10-2026 | Fruit prices | Saddle + Vegas |
| 24 | 14 | 22-10-2026 | Fruit revenue | Breeze + Plotly |
| 25 | 14 | 22-10-2026 | Exact statistics | Spire + Saddle |

## Build

    bash lib/fetch_libs.sh                 # download the 13 jars (36 MB, gitignored)
    CP=$(ls lib/*.jar | tr '\n' ':')
    mkdir -p out
    scalac -cp "$CP" -d out programs/*.scala
    scala -cp "$CP:out" Program22          # ... Program23, 24, 25

## Record

    Week10_Programs_22_25.docx   editable record
    Week10_Programs_22_25.pdf    submitted record (17 pages)

Post-processing, in order:

    python3 tools/place_cover_photo.py Week10_Programs_22_25.pdf
    python3 tools/add_pdf_links.py    Week10_Programs_22_25.pdf

LibreOffice drops hyperlink annotations on PDF export, so the clickable links
are added to the PDF afterwards as /Link annotations with /URI actions.
