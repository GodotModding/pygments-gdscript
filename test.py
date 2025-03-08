from pygments import highlight
from pygments.formatters import HtmlFormatter
from gdscript import GDScriptLexer, GDScriptStyle

with open("test.gd") as f:
    code = f.read()

formatter = HtmlFormatter(full=True, linenos=True, style=GDScriptStyle)
with open("test.html", "w") as f:
    highlight(code, GDScriptLexer(), formatter, outfile=f)
