import zipfile, shutil, re, sys

DOCX = sys.argv[1]
TMP = DOCX + ".tmp"
zin = zipfile.ZipFile(DOCX)
zout = zipfile.ZipFile(TMP, "w", zipfile.ZIP_DEFLATED)

for it in zin.infolist():
    d = zin.read(it.filename)
    if it.filename == "word/document.xml":
        s = d.decode("utf-8")
        # ensure the page background is the template green
        if "<w:background" in s:
            s = re.sub(r'<w:background[^>]*/>', '<w:background w:color="E2EFD9"/>', s)
        else:
            s = s.replace("<w:body>", '<w:background w:color="E2EFD9"/><w:body>', 1)
        d = s.encode("utf-8")
    elif it.filename == "word/settings.xml":
        s = d.decode("utf-8")
        # make sure the background is actually painted
        if "displayBackgroundShape" not in s:
            s = s.replace("</w:settings>", "<w:displayBackgroundShape/></w:settings>")
        d = s.encode("utf-8")
    zout.writestr(it, d)

zin.close(); zout.close()
shutil.move(TMP, DOCX)
print("green page background restored:", DOCX.split("/")[-1])
