from pyparsing import *
from pyparsing import (
    quotedString,
    Word,
    Literal,
    pyparsing_common,
    Group,
    Optional,
    delimitedList,
    ZeroOrMore,
    OneOrMore,
    Regex,
)

"""
building blocks:

- literal = quoated string or number
- path = special regex
# 
- paths = path Group
- func = ^ identifier + literal('=') + literal
         ^ 
- identifier
- operator
- flag
- string
"""
#
##### Terminals..
#
# values
QUOTED_STRING = quotedString
NUMBER = pyparsing_common.number
NONE = Literal("None")
# identifiers
IDENTIFIER = Regex("[a-zA-Z_]+[a-zA-Z0-9]*")  # Unicode standard annex UAX-31
PATH_IDENTIFIER = quotedString  # [posix path pattern] [non-posix path pattern]
# keywords
SUPP_KEYWORD = Literal("supp")
VERSION_KEYWORD = Literal("version")
SOURCE_KEYWORD = Literal("source")
DROP_KEYWORD = Literal("drop")
DESCRIBE_KEYWORD = Literal("describe")
# flag keywords
ARGS_FLAG = Literal("--args") ^ Literal("-a")
HELP_FLAG = Literal("--help") ^ Literal("-h")
ENV_FLAG = Literal("--env") ^ Literal("-e")
VERBOSE_FLAG = Literal("--verbose")
# sign keywords
EQUAL_SIGN = Literal("=")
DOUBLE_DASH_SIGN = Literal("--")
#
##### Non Terminals..
#
action = oneOf(VERSION_KEYWORD ^ SOURCE_KEYWORD ^ DROP_KEYWORD ^ DESCRIBE_KEYWORD)
#
path = PATH_IDENTIFIER
paths = Group(ZeroOrMore(path))
#
value = QUOTED_STRING ^ NUMBER ^ NONE
arg = Group(value)
fwarg = Group(DOUBLE_DASH_SIGN + IDENTIFIER + value)
kwarg = Group(IDENTIFIER + EQUAL_SIGN + value)
#
args = ARGS_FLAG + OneOrMore(arg)
fwargs = OneOrMore(fwarg)
kwargs = OneOrMore(kwarg)
#
function_style_1 = Group(IDENTIFIER + Group(Optional(args)) + Optional(HELP_FLAG))
function_style_2 = Group(IDENTIFIER + Group(Optional(kwargs)) + Optional(HELP_FLAG))
function_style_3 = Group(IDENTIFIER + Group(Optional(fwargs)) + Optional(HELP_FLAG))
#
functions_style_1 = Group(ZeroOrMore(function_style_1))
functions_style_2 = Group(ZeroOrMore(function_style_2))
functions_style_3 = Group(ZeroOrMore(function_style_3))
#
command_style_1 = IDENTIFIER + paths + functions_style_1
command_style_2 = IDENTIFIER + paths + functions_style_2
command_style_3 = IDENTIFIER + paths + functions_style_3

print(
    command_style_1.parseString(
        'supp "./" "./file.py" "./test.py" hello_bye a=None b=None fsa --help'
    )
)


identifier = Word(alphas)
literal = quotedString ^ pyparsing_common.number
assignment = identifier + Literal("=") + quotedString
