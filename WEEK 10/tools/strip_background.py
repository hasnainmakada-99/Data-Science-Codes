import zipfile, shutil, re, sys

for DOCX in sys.argv[1:]:
    TMP = DOCX + ".tmp"
    zin = zipfile.ZipFile(DOCX)
    zout = zipfile.ZipFile(TMP, "w", zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        d = zin.read(it.filename)
        if it.filename == "word/document.xml":
            s = d.decode("utf-8")
            s = re.sub(r"<w:background[^>]*/>", "", s)
            d = s.encode("utf-8")
        elif it.filename == "word/settings.xml":
            s = d.decode("utf-8")
            s = re.sub(r"<w:displayBackgroundShape[^>]*/>", "", s)
            d = s.encode("utf-8")
        zout.writestr(it, d)
    zin.close(); zout.close()
    shutil.move(TMP, DOCX)
    print("page background removed:", DOCX.split("/")[-1])
