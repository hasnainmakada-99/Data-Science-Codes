#!/bin/bash
set -e
ROOT="/media/bruce-wayne/HASNAIN/VIT WORK/Data-Science-Codes"
export PYTHONPATH=/tmp

patch_cover () {
  python3 - "$1" <<'PYEOF'
import zipfile, shutil, re, sys
DOCX = sys.argv[1]
TMP = DOCX + ".tmp"
zin = zipfile.ZipFile(DOCX); zout = zipfile.ZipFile(TMP, "w", zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    d = zin.read(it.filename)
    if it.filename == "word/document.xml":
        s = d.decode("utf-8")
        s = s.replace("LAB ASSESESMENT", "LAB ASSESSMENT")
        s = re.sub(r"<w:background[^>]*/>", "", s)
        d = s.encode("utf-8")
    elif it.filename == "word/settings.xml":
        s = d.decode("utf-8")
        s = re.sub(r"<w:displayBackgroundShape[^>]*/>", "", s)
        d = s.encode("utf-8")
    elif it.filename in ("word/diagrams/data1.xml","word/diagrams/drawing1.xml"):
        s = d.decode("utf-8")
        s = s.replace("<a:t>Reg No </a:t>", "<a:t>Reg No: 26MML0031</a:t>")
        s = s.replace("<a:t>Name</a:t>", "<a:t>Name: Hasnain H. Makada</a:t>")
        d = s.encode("utf-8")
    zout.writestr(it, d)
zin.close(); zout.close(); shutil.move(TMP, DOCX)
PYEOF
}

measure () {
  python3 - "$1" "$2" <<'PYEOF'
import subprocess, re, json, sys
PDF, OUTJSON = sys.argv[1], sys.argv[2]
total = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
starts = {}
for p in range(1, total + 1):
    t = subprocess.run(["pdftotext","-layout","-f",str(p),"-l",str(p),PDF,"-"], capture_output=True, text=True).stdout
    m = re.search(r"Program S\. No\. (\d+)", t)
    foot = re.search(r"(\d+)\s*\|\s*P a g e", t)
    if m and foot and m.group(1) not in starts:
        starts[m.group(1)] = int(foot.group(1))
print("  pages:", total, "starts:", starts)
json.dump({k: str(v) for k, v in starts.items()}, open(OUTJSON, "w"))
PYEOF
}

build () {
  local dir="$1" docx="$2" map="$3" photo="$4" links="$5" builder="$6"
  echo "=== $docx ==="
  rm -f "$map"
  ( cd "$ROOT" && python3 "$builder" >/dev/null )
  patch_cover "$ROOT/$dir/$docx"
  python3 /tmp/compact_cover.py "$ROOT/$dir/$docx" >/dev/null
  ( cd "$ROOT/$dir" && rm -f "${docx%.docx}.pdf" && libreoffice --headless --convert-to pdf --outdir . "$docx" >/dev/null 2>&1 )
  measure "$ROOT/$dir/${docx%.docx}.pdf" "$map"
  ( cd "$ROOT" && python3 "$builder" >/dev/null )
  patch_cover "$ROOT/$dir/$docx"
  python3 /tmp/compact_cover.py "$ROOT/$dir/$docx" >/dev/null
  ( cd "$ROOT/$dir" && rm -f "${docx%.docx}.pdf" && libreoffice --headless --convert-to pdf --outdir . "$docx" >/dev/null 2>&1 )
  ( cd "$ROOT/$dir" && python3 "$photo" "${docx%.docx}.pdf" >/dev/null && python3 "$links" "${docx%.docx}.pdf" )
  measure "$ROOT/$dir/${docx%.docx}.pdf" "$map"
}

build "WEEK 9"  "Week9_Programs_18_21.docx" /tmp/w9_pagemap.json  /tmp/place_photo.py   /tmp/add_links.py   /tmp/w9_final.py
build "WEEK 10" "Week10_Programs_22_25.docx" /tmp/w10_pagemap.json /tmp/place_photo10.py /tmp/add_links10.py /tmp/w10_build.py
echo ALL DONE
