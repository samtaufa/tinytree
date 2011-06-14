import countershape.layout
import countershape.template
import countershape.widgets
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

rootPath = os.path.abspath(".")

def showsrc(path):        
    return readFrom(os.path.join(rootPath, path))

ns.showsrc = showsrc

pages = [
    Page("index.md", "Introduction"),
    PythonPage("../tinytree.py", 
        title="Source"),
    Page("admin.md", "Administrivia")
]
