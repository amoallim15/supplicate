from pyparsing import (
	quotedString,
	Word,
	Literal,
	pyparsing_common,
	Group,
	Optional,
	ZeroOrMore,
	OneOrMore,
	alphanums,
	WordEnd,
	Combine
)

IDENTIFIER = pyparsing_common.identifier
VALUE = quotedString ^ pyparsing_common.number ^ Literal('None')
PATH = Combine(OneOrMore(Word(alphanums + '/\\~ "')) + Literal('.py') + WordEnd())
#
ARGS_FLAG = Literal('--args') ^ Literal('-a')
HELP_FLAG = Literal('--help') ^ Literal('-h')
# 
EQUAL_SIGN = Literal('=')
DOUBLE_DASH_SIGN = Literal('--')
# 
args = ARGS_FLAG.suppress() + OneOrMore(Group(VALUE))
fwargs = OneOrMore(Group(DOUBLE_DASH_SIGN.suppress() + IDENTIFIER + VALUE))
kwargs = OneOrMore(Group(IDENTIFIER + EQUAL_SIGN.suppress() + VALUE))
# 
args_func = Group(IDENTIFIER + Group(Optional(args)) + Optional(HELP_FLAG)) 
kwargs_func = Group(IDENTIFIER + Group(Optional(kwargs)) + Optional(HELP_FLAG))
fwargs_func = Group(IDENTIFIER + Group(Optional(fwargs)) + Optional(HELP_FLAG))
#
paths = Group(ZeroOrMore(PATH))
args_funcs = Group(ZeroOrMore(args_func))
kwargs_funcs = Group(ZeroOrMore(kwargs_func))
fwargs_funcs = Group(ZeroOrMore(fwargs_func))
# 
command_1 = paths + args_funcs
command_2 = paths + kwargs_funcs
command_3 = paths + fwargs_funcs

Command = command_1 ^ command_2 ^ command_3



