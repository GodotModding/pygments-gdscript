from pygments.style import Style
from pygments.token import (
    Text,
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Whitespace,
    Punctuation,
)


class GDScriptStyle(Style):
    background_color = "#1d2229"

    styles = {
        Text:                     "#ffffff", # text
        Whitespace:               "#bbbbbb", # for whitespace
        Comment:                  "#cdcfd2", # any kind of comments
        Punctuation:              "#abc9ff", # punctuation (e.g. [!.,])

        Keyword:                  "#ff7085", # Any kind of keyword; especially if it doesn’t match any of the subtypes

        Operator:                 "#abc9ff", # For any punctuation operator (e.g. +, -)
        Operator.Word:            "#ff7085", # For any operator that is a word (e.g. not, in)

        Name.Builtin:             "#42ffc2", # names that are available in the global namespace (NOT USED)
        Name.Builtin.Type:        "#42ffc2", # types that are available in the global namespace
        Name.Builtin.Function:    "#a3a3f5", # functions that are available in the global namespace
        Name.Function:            "#57b3ff", # function names
        Name.Class:               "#42ffc2", # class names / declarations
        Name.Variable:            "#bce0ff", # variable names
        Name.Constant:            "#bce0ff", # constant names
        Name.Decorator:           "#ffb373", # decorators / annotations (TODO)

        String:                   "#ffeda1", # string literals
        String.Doc:               "#ffeda1", # doc string literal
        String.Interpol:          "#ffeda1", # interpolated parts (e.g. %s)
        String.Escape:            "#ffeda1", # escape sequences

        Number:                   "#a1ffe0", # number literal

        Error:                    "border:#FF0000" # represents lexer errors (very useful for debugging)
    }
