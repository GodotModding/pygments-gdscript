from pygments.style import Style
from pygments.token import (
    Text,
    Keyword,
    Literal,
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
        Text:                     "#cdcfd2",  # text
        Whitespace:               "#bbbbbb",  # for whitespace
        # Comment:                  "#cdcfd2",  # any kind of comments
        Comment:                  "#76787E",  # comment without transparency, on this background_color
        Punctuation:              "#abc9ff",  # punctuation (e.g. [!.,])

        Keyword:                  "#ff7085",  # any kind of keyword; especially if it doesn’t match any of the subtypes
        Keyword.ControlFlow:      "#ff8ccc",  # (e.g. if, else, return, break)

        Literal:                  "#ff7085",  # any literals (e.g. true, false, PI, NAN)

        Operator:                 "#abc9ff",  # for any punctuation operator (e.g. +, -)
        Operator.Word:            "#ff7085",  # for any operator that is a word (e.g. not, in)

        Name.Builtin:             "#8fffdb",  # names that are available in the global namespace, used for builtin classes
        Name.Builtin.Type:        "#42ffc2",  # types that are available in the global namespace
        Name.Builtin.Function:    "#a3a3f5",  # functions that are available in the global namespace
        Name.Function:            "#57b3ff",  # function names
        Name.Class:               "#c7ffed",  # user made class names / declarations
        Name.Variable:            "#bce0ff",  # variable names
        Name.Constant:            "#bce0ff",  # constant names
        Name.Decorator:           "#ffb373",  # decorators / annotations
        Name.Builtin.Pseudo:      "#ff7085",  # Builtin names that are implicit (e.g. self in Ruby, this in Java).

        String:                   "#ffeda1",  # string literals
        String.Doc:               "#ffeda1",  # doc string literal
        String.Interpol:          "#ffeda1",  # interpolated parts (e.g. %s)
        String.Escape:            "#abc9ff",  # escape sequences
        String.Other:             "#63c259",  # node references

        Number:                   "#a1ffe0",  # number literal

        Error:                    "border:#ff0000"  # represents lexer errors (very useful for debugging)
    }

    reference_colors = {
        "#abc9ffff",  # symbol_color --md-code-hl-operator-color
        "#abc9ffff",  # symbol_color --md-code-hl-punctuation-color
        "#ff7085ff",  # keyword_color --md-code-hl-keyword-color
        "#ff7085ff",  # keyword_color --md-code-hl-special-color
        "#ff8cccff",  # control_flow_keyword_color
        "#42ffc2ff",  # base_type_color .nb.nb-Type
        "#8fffdbff",  # engine_type_color --md-code-hl-engine-type-color
        "#c7ffedff",  # user_type_color --md-code-hl-user-type-color
        "#cdcfd280",  # comment_color --md-code-hl-comment-color
        "#99b3cccc",  # doc_comment_color
        "#ffeda1ff",  # string_color --md-code-hl-string-color
        "#1d2229ff",  # background_color --md-code-bg-color
        "#363d4aff",  # completion_background_color
        "#ffffff12",  # completion_selected_color
        "#ffffff24",  # completion_existing_color
        "#cdcfd2ff",  # completion_font_color
        "#cdcfd2ff",  # text_color --md-code-hl-generic-color --md-code-hl-name-color --md-code-fg-color
        "#cdcfd280",  # line_number_color
        "#cdf8d2bf",  # safe_line_number_color
        "#ffffffff",  # caret_color
        "#70bafa66",  # selection_color
        "#ff786bff",  # brace_mismatch_color
        "#ffffff12",  # current_line_color
        "#363d4aff",  # line_length_guideline_color
        "#ffffff12",  # word_highlighted_color --md-code-hl-color
        "#a1ffe0ff",  # number_color --md-code-hl-number-color
        "#57b3ffff",  # function_color --md-code-hl-function-color
        "#bce0ffff",  # member_variable_color --md-code-hl-variable-color
        "#bce0ffff",  # member_variable_color --md-code-hl-constant-color
        "#ff786b4d",  # mark_color
        "#ff786bff",  # breakpoint_color
        "#ffffff45",  # code_folding_color
        "#ffffff12",  # search_result_color

        "#66e6ffff",  # gdscript/function_definition_color
        "#a3a3f5ff",  # gdscript/global_function_color
        "#b8c47dff",  # gdscript/node_path_color
        "#63c259ff",  # gdscript/node_reference_color
        "#ffb373ff",  # gdscript/annotation_color
        "#ffc2a6ff",  # gdscript/string_name_color
    }


