import os

from pygments import highlight
from pygments.formatters import HtmlFormatter
from gdscript_lexer import GDScriptLexer
from gdscript_style import GDScriptStyle

EXAMPLE_FILES = "tests/examplefiles/"

for file_name in os.listdir("%s" % EXAMPLE_FILES):
    if not file_name.endswith(".gd"):
        continue
    with open(EXAMPLE_FILES + file_name) as f:
        code = f.read()

    formatter = HtmlFormatter(full=True, linenos=True, style=GDScriptStyle)
    with open(EXAMPLE_FILES + file_name.rstrip(".gd") + ".html", "w") as f:
        highlight(code, GDScriptLexer(), formatter, outfile=f)
