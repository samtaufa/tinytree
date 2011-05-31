import countershape.layout
import countershape.template
import countershape.widgets
import countershape.grok
from countershape.doc import *

this.layout = countershape.layout.Layout("_layout.html")
this.markdown = markup.RST()

ns.docTitle = "Tinytree Manual"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "aldo@nullcube.com"
ns.foot = "Copyright Nullcube 2008"
ns.head = countershape.template.File(None, "_header.html")
ns.sidebar = countershape.widgets.SiblingPageIndex(
            '/index.html', exclude=['countershape']
          )
this.titlePrefix = "TinyTree Manual - "

ns.ctgrok = countershape.grok.parse("../tinytree.py")
ns.example = readFrom("_example.py")

pages = [
    Page("index.mdtext", "Introduction"),
    Page("api.mdtext", "API"),
    Page("admin.mdtext", "Administrivia")
]
