from .recognizer import RecoRegexRule, RecoCustomRule

GRAMMAR = """
<version_cmd>   ::= "version"
<help_cmd>      ::= "help"
<drop_cmd>      ::= "drop" [ <path> { <path> } ]
<source_cmd>    ::= "source" [ <path> { <path> } ]
<describe_cmd>  ::= "describe" [ <path> { <path> } ]
<execute_cmd>   ::= [ <path> { <path> } ] <function> [ { <function> } ]
<function>      ::= <identifier> <args_flag> <args>
                 |  <identifier> <kwargs>
                 |  <identifier>
<args_flag>     ::= "--args" | "-a"
<args>          ::= <arg> { <arg> }
<kwargs>        ::= <kwarg> { <kwarg> }
<kwarg>         ::= <flag> <arg>
<arg>           ::= <boolean> | <integer> | <float> | <string>


# TERMINALS
<path>          ::= <letter> | <digit> | "/" | "." { <letter> | <digit> | "/" | "." } ".py"
<double_flag>   ::= "--" <identifier>
<flag>          ::= "-" <identifier>
<identifier>    ::= <letter> | "_" { <letter> | <digit> }
<boolean>       ::= "True" | "False"
<integer>       ::= <digit> { <digit> }
<float>         ::= [ <digit> { <digit> } ] "." <digit> { <digit> } | <digit> { <digit> } "."
<string>        ::= <letter> { <letter> }
<digit>         ::= DIGIT
<letter>        ::= LETTER
"""

RULES = [
    # ("ARGUMENT", ""),  # key=value ignored in the meantime for simplicity.
    # ("HELP_FLAG", "-h"),
    # ("HELP_DOUBLE_FLAG", "--help"),
    # ("ARGS_FLAG", "-a"),
    # ("ARGS_DOUBLE_FLAG", "--args"),
    # ("VERBOSE_FLAG", "-v"),
    # ("VERBOSE_DOUBLE_FLAG", "--verbose"),
    # ("ARG_KEY", ""),  # -key
    RecoRegexRule("PATH", r'[\w\/"\s\.]+\.py'),
    RecoRegexRule("FLAG", r"-[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule("DOUBLE_FLAG", r"--[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule(
        "NUMERIC",
        r"[+-]?(?:\d+(?:[eE][+-]?\d+)|(?:\d+\.\d*|\.\d+)(?:[eE][+-]?\d+)?)|[+-]?\d+",
    ),
    RecoRegexRule("BOOLEAN", r"True|False"),
    RecoRegexRule("IDENTIFIER", r"[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule("STRING", r"[\s\S]*"),
]
