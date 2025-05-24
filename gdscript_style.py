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
    godot_theme = {
        "symbol_color": "#abc9ff",  # --md-code-hl-operator-color, --md-code-hl-punctuation-color
        "keyword_color": "#ff7085",  # --md-code-hl-keyword-color, --md-code-hl-special-color
        "control_flow_keyword_color": "#ff8ccc",  #
        "base_type_color": "#42ffc2",  # .nb.nb-Type
        "engine_type_color": "#8fffdb",  # --md-code-hl-engine-type-color
        "user_type_color": "#c7ffed",  # --md-code-hl-user-type-color
        # "comment_color": "#cdcfd2",  # --md-code-hl-comment-color
        "comment_color": "#76787E",  # comment without transparency, on this background_color
        "doc_comment_color": "#99b3cc",  #
        "string_color": "#ffeda1",  # --md-code-hl-string-color
        "background_color": "#1d2229",  # --md-code-bg-color
        "completion_background_color": "#363d4a",  #
        "completion_selected_color": "#ffffff",  #
        "completion_existing_color": "#ffffff",  #
        "completion_font_color": "#cdcfd2",  #
        "text_color": "#cdcfd2",  # --md-code-hl-generic-color, --md-code-hl-name-color, --md-code-fg-color
        "line_number_color": "#cdcfd2",  #
        "safe_line_number_color": "#cdf8d2",  #
        "caret_color": "#ffffff",  #
        "selection_color": "#70bafa",  #
        "brace_mismatch_color": "#ff786b",  #
        "current_line_color": "#ffffff",  #
        "line_length_guideline_color": "#363d4a",  #
        "word_highlighted_color": "#ffffff",  # --md-code-hl-color
        "number_color": "#a1ffe0",  # --md-code-hl-number-color
        "function_color": "#57b3ff",  # --md-code-hl-function-color
        "member_variable_color": "#bce0ff",  # --md-code-hl-variable-color, --md-code-hl-constant-color
        "mark_color": "#ff786b",  #
        "breakpoint_color": "#ff786b",  #
        "code_folding_color": "#ffffff",  #
        "search_result_color": "#ffffff",  #

        "gdscript/function_definition_color": "#66e6ff",  #
        "gdscript/global_function_color": "#a3a3f5",  #
        "gdscript/node_path_color": "#b8c47d",  #
        "gdscript/node_reference_color": "#63c259",  #
        "gdscript/annotation_color": "#ffb373",  #
        "gdscript/string_name_color": "#ffc2a6",  #
    }

    background_color = godot_theme["background_color"]
    styles = {
        Whitespace:               "#bbbbbb",  # for whitespace
        Text:                     godot_theme["text_color"],  # text
        Comment:                  godot_theme["comment_color"],  # any kind of comments
        Punctuation:              godot_theme["symbol_color"],  # punctuation (e.g. [!.,])

        Keyword:                  godot_theme["keyword_color"],  # any kind of keyword; especially if it doesn’t match any of the subtypes
        Keyword.ControlFlow:      godot_theme["control_flow_keyword_color"],  # (e.g. if, else, return, break)

        Literal:                  godot_theme["keyword_color"],  # any literals (e.g. true, false, PI, NAN)

        Operator:                 godot_theme["symbol_color"],  # for any punctuation operator (e.g. +, -)
        Operator.Word:            godot_theme["keyword_color"],  # for any operator that is a word (e.g. not, in)

        Name.Builtin:             godot_theme["engine_type_color"],  # names that are available in the global namespace, used for builtin classes
        Name.Builtin.Type:        godot_theme["base_type_color"],  # types that are available in the global namespace
        Name.Builtin.Function:    godot_theme["gdscript/global_function_color"],  # functions that are available in the global namespace
        Name.Function:            godot_theme["function_color"],  # function names
        Name.Class:               godot_theme["user_type_color"],  # user made class names / declarations
        Name.Variable:            godot_theme["member_variable_color"],  # variable names
        Name.Variable.Instance:   godot_theme["member_variable_color"],  # member variable names
        Name.Constant:            godot_theme["member_variable_color"],  # constant names
        Name.Decorator:           godot_theme["gdscript/annotation_color"],  # decorators / annotations
        Name.Builtin.Pseudo:      godot_theme["keyword_color"],  # Builtin names that are implicit (e.g. self in Ruby, this in Java).

        String:                   godot_theme["string_color"],  # string literals
        String.Doc:               godot_theme["string_color"],  # doc string literal
        String.Interpol:          godot_theme["string_color"],  # interpolated parts (e.g. %s)
        String.Escape:            godot_theme["symbol_color"],  # escape sequences
        String.Other:             godot_theme["gdscript/node_reference_color"],  # node references

        Number:                   godot_theme["number_color"],  # number literal

        Error:                    "border:#ff0000"  # represents lexer errors (very useful for debugging)
    }
