#!/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index_root():
    return '''<body>
<big><big><big>
<ol>
  <li>Add the Infusion of Wormwood.<br><img src="/static/InfusionofWormwood.webp" width="250" height="136"></li>
  <li>Add the Powdered Root of Asphodel.<br><img src="/static/Powdered_Asphodel.webp" width="250" height="136"></li>
  <li>Stir twice clockwise.</li>
  <li>Add the sloth brain.<br><img src="/static/A_Sloth_brain.webp" width="250" height="136"></li>
  <li>Add the Sopophorous Bean's juice.<br><img src="/static/Sopophorous_Bean_HM.webp" width="250" height="136"></li>
  <li>Stir seven times anti-clockwise.</li>
</ol>
</big></big></big>
</body>'''


if __name__ == "__main__":
    app.run()

