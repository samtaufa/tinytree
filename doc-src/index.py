import countershape.layout
import countershape.template
import countershape.widgets
import countershape.grok
from countershape.doc import *

this.layout = countershape.layout.Layout("_layout.html")
this.markdown = "rst"

ns.docTitle = "Tinytree Manual"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "aldo@nullcube.com"
ns.foot = "Copyright Nullcube 2008"
ns.head = readFrom("_header.html")
ns.sidebar = countershape.widgets.SiblingPageIndex(
            '/index.html', exclude=['countershape']
          )
this.titlePrefix = "TinyTree Manual - "

ns.ctgrok = countershape.grok.grok("../tinytree.py")
ns.example = readFrom("_example.py")

pages = [
    Page("index.html", "Introduction"),
    Page("api.html", "API"),
    Page("admin.html", "Administrivia")
]
