import subprocess, os, re, html

BASE = "/media/bruce-wayne/HASNAIN/VIT WORK/Data-Science-Codes/WEEK 10"
PROG = os.path.join(BASE, "programs")
OUT = os.path.join(BASE, "assets")
os.makedirs(OUT, exist_ok=True)
CP = ":".join(os.path.join(BASE, "lib", f)
              for f in sorted(os.listdir(os.path.join(BASE, "lib"))) if f.endswith(".jar"))

PROGS = {22: "Program22", 23: "Program23", 24: "Program24", 25: "Program25"}

def run_capture(cls):
    tp = "/tmp/cap10_%s.txt" % cls
    if os.path.exists(tp):
        os.remove(tp)
    cmd = "scala -cp '%s:%s' %s" % (CP, os.path.join(BASE, "out"), cls)
    subprocess.run(["script", "-q", "-c", cmd, tp], cwd=PROG,
                   capture_output=True, text=True, timeout=400)
    raw = open(tp, "rb").read().decode("utf-8", "replace")
    lines = []
    for ln in raw.split("\n"):
        if ln.startswith("Script started") or ln.startswith("Script done"):
            continue
        ln = ln.replace("\r", "").rstrip()
        ln = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", ln)
        lines.append(ln)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines

def terminal_html(lines, title, cmdtext):
    body = []
    body.append('<span class="p">hasnain@vit:~/WEEK 10/programs$</span>')
    body.append('<span class="cmd">%s</span>' % html.escape(cmdtext))
    for ln in lines:
        esc = html.escape(ln)
        if ln.strip().startswith("=") or ln.startswith("PROGRAM"):
            body.append('<span class="hl">%s</span>' % esc)
        elif re.match(r"^\s*\d+\.", ln):
            body.append('<span class="num">%s</span>' % esc)
        else:
            body.append('<span class="out">%s</span>' % (esc if esc else " "))
    text = "\n".join(body)
    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#2b2b2b; }
.win { width:1000px; background:#300a24; border-radius:8px 8px 0 0; overflow:hidden;
       font-family:'DejaVu Sans Mono',monospace; }
.bar { height:34px; background:#3c3c3c; display:flex; align-items:center; padding:0 12px; }
.dot { width:13px; height:13px; border-radius:50%%; margin-right:8px; }
.r{background:#ff5f56}.y{background:#ffbd2e}.g{background:#27c93f}
.ttl { color:#d8d8d8; font-size:12.5px; margin-left:10px; font-family:'DejaVu Sans',sans-serif; }
.term { padding:14px 16px 18px 16px; font-size:13px; line-height:1.40; white-space:pre-wrap;
        word-break:break-all; }
.p { color:#8ae234; font-weight:bold; }
.cmd { color:#ffffff; }
.hl { color:#34e2e2; }
.num { color:#fce94f; }
.out { color:#eeeeec; }
</style></head><body><div class="win">
<div class="bar"><div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
<div class="ttl">%s</div></div>
<div class="term">%s</div></div></body></html>""" % (html.escape(title), text)

def shoot(h, png, height):
    hp = "/tmp/_t10.html"
    open(hp, "w").write(h)
    if os.path.exists(png):
        os.remove(png)
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--screenshot=" + png, "--window-size=1000,%d" % height, hp],
                   capture_output=True, timeout=200)

SPLIT = {22: "4. Formatted descriptions", 23: "4. Average apple price",
         24: "4. Aggregate statistics", 25: "3. Exact statistics"}

for num, cls in PROGS.items():
    lines = run_capture(cls)
    open(os.path.join(OUT, "Program%d_output.txt" % num), "w").write("\n".join(lines))
    marker = SPLIT[num]
    split = len(lines) // 2
    for i, ln in enumerate(lines):
        if marker in ln:
            split = i
            break
    parts = [lines[:split], lines[split:]]
    for idx, part in enumerate(parts, start=1):
        cmdtext = "scala -cp 'lib/*:out' %s" % cls
        h = terminal_html(part, "%s.scala" % cls, cmdtext)
        png = os.path.join(OUT, "Program%d_part%d.png" % (num, idx))
        shoot(h, png, max(260, 70 + len(part) * 20))
    print("Program%d: %d lines split at %d" % (num, len(lines), split))
print("done")
