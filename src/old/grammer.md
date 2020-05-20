<!-- 
Parser Rules
============
-->


<!-- 
Lexer Rules
===========

fragment LOWERCASE : [a-z] ;
fragment UPPERCASE : [A-Z] ;

SOURCE : 'source'
DROP : 'drop'
SELFHELP : 'help'
DESCRIBE : 'describe'
OBJLONGHELP : '--help'
OBJSHORTHELP : '-h'

PATH : 'regex_path' ;
FUNCTION_NAME : (LOWERCASE | UPPERCASE | [0-9] | '_')+ ;
ARGUMENT_KEY : (LOWERCASE | UPPERCASE | [0-9] | '_')+ ;
ARGUMENT_VALUE : [regex_value]+ ;
WHITESPACE : ' ' ;
-->