#!/usr/bin/env python
# TODO:
#   - Validate token tagging by comparing the lexer output on an
#     example file against expected tokens.


try:
    from pygments import highlight, lex
    from pygments.formatters import HtmlFormatter
    from pygments.token import Error as LexerError

except ModuleNotFoundError:
    raise ImportError(
        "Missing required modules. Please install the required dependancies using `pip install -r requirements.txt`!"
    ) from None

from typing import Optional
from collections import defaultdict
from gdscript_lexer import GDScriptLexer
from gdscript_style import GDScriptStyle

def collect_lexer_errors(tokens) -> Optional[list[tuple[int, str]]]:
    line_num = 1
    errors = []
    for type, value in tokens:
        line_num += value.count('\n')
        if type is LexerError:
            errors.append((line_num, value))
    return None if len(errors) == 0 else errors 


with open("test.gd") as f:
    code = f.read()

tokens = lex(code, GDScriptLexer())
errors = collect_lexer_errors(tokens)
if errors is not None:
    print("There are", len(errors), "errors in the lexed code:")
    for line, string in errors:
       print("\tLINE",line,"AT",string)
    
    raise ValueError("Lexing errors found")

formatter = HtmlFormatter(full=True, linenos=True, style=GDScriptStyle)
with open("test.html", "w") as f:
   f.write(highlight(code, GDScriptLexer(), formatter))
