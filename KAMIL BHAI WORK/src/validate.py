#!/usr/bin/env python3
"""OOXML child-order validator for the element types this build touches.
PowerPoint enforces CT sequence order; LibreOffice does not. This catches the difference."""
import sys, zipfile, re
from lxml import etree

C = '{http://schemas.openxmlformats.org/drawingml/2006/chart}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'

ORDERS = {
 'chartSpace': ['date1904','lang','roundedCorners','style','clrMapOvr','pivotSource','protection',
                'chart','spPr','txPr','externalData','printSettings','userShapes','extLst'],
 'chart': ['title','autoTitleDeleted','pivotFmts','view3D','floor','sideWall','backWall','plotArea',
           'legend','plotVisOnly','dispBlanksAs','showDLblsOverMax','extLst'],
 'plotArea': ['layout','areaChart','area3DChart','lineChart','line3DChart','stockChart','radarChart',
              'scatterChart','pieChart','pie3DChart','doughnutChart','barChart','bar3DChart','ofPieChart',
              'surfaceChart','surface3DChart','bubbleChart','dTable','spPr','extLst'],
 'scaling': ['logBase','orientation','max','min','extLst'],
 'catAx': ['axId','scaling','delete','axPos','majorGridlines','minorGridlines','title','numFmt',
           'majorTickMark','minorTickMark','tickLblPos','spPr','txPr','crossAx','crosses','crossesAt',
           'auto','lblAlgn','lblOffset','tickLblSkip','tickMarkSkip','noMultiLvlLbl','extLst'],
 'valAx': ['axId','scaling','delete','axPos','majorGridlines','minorGridlines','title','numFmt',
           'majorTickMark','minorTickMark','tickLblPos','spPr','txPr','crossAx','crosses','crossesAt',
           'crossBetween','majorUnit','minorUnit','dispUnits','extLst'],
 'barChart': ['barDir','grouping','varyColors','ser','dLbls','gapWidth','overlap','serLines','axId','extLst'],
 'doughnutChart': ['varyColors','ser','dLbls','firstSliceAng','holeSize','extLst'],
 'dLbls': ['numFmt','spPr','txPr','dLblPos','showLegendKey','showVal','showCatName','showSerName',
           'showPercent','showBubbleSize','separator','showLeaderLines','leaderLines','extLst'],
 'manualLayout': ['layoutTarget','xMode','yMode','wMode','hMode','x','y','w','h','extLst'],
 'txPr': ['bodyPr','lstStyle','p'],
 'spPr': ['xfrm','custGeom','prstGeom','noFill','solidFill','gradFill','blipFill','pattFill','grpFill',
          'ln','effectLst','effectDag','scene3d','sp3d','extLst'],
}

def check(root, part, errs):
    for el in root.iter():
        q = etree.QName(el)
        name = q.localname
        if q.namespace not in (C[1:-1], A[1:-1]):
            continue
        order = ORDERS.get(name)
        if not order:
            continue
        seen, last = [], -1
        for ch in el:
            cq = etree.QName(ch)
            cn = cq.localname
            if cn not in order:
                continue
            i = order.index(cn)
            if i < last:
                errs.append(f"{part}: <{name}> has <{cn}> out of order (after <{seen[-1]}>)")
            last = i
            seen.append(cn)
        dup = [x for x in set(seen) if seen.count(x) > 1
               and x not in ('ser','p','axId','valAx','catAx','dateAx','serAx')]
        for d in dup:
            errs.append(f"{part}: <{name}> has duplicate <{d}> ×{seen.count(d)}")

def main(path):
    z = zipfile.ZipFile(path)
    errs = []
    n = 0
    for name in z.namelist():
        if not name.endswith('.xml'):
            continue
        if not (name.startswith('ppt/charts/') or name.startswith('ppt/slides/')
                or name.startswith('ppt/slideLayouts/') or name.startswith('ppt/slideMasters/')):
            continue
        try:
            root = etree.fromstring(z.read(name))
        except Exception as e:
            errs.append(f"{name}: XML PARSE FAILURE {e}")
            continue
        n += 1
        check(root, name, errs)
    # relationship sanity
    for name in z.namelist():
        if name.endswith('.rels'):
            root = etree.fromstring(z.read(name))
            ids = [r.get('Id') for r in root]
            if len(ids) != len(set(ids)):
                errs.append(f"{name}: duplicate r:id")
    print(f"parts scanned: {n}")
    if errs:
        print(f"FAIL — {len(errs)} violation(s)")
        for e in errs[:40]:
            print("  ", e)
        sys.exit(1)
    print("PASS — all child sequences valid")

if __name__ == '__main__':
    main(sys.argv[1])
