GRAMMAR = '''
	cmd = 
		| version_cmd
		| help_cmd
		| drop_cmd
		| source_cmd
		| describe_cmd
		| execute_cmd
		;
	version_cmd = "version" ;
	help_cmd = "help" ;
	drop_cmd = "drop" { path }* ;
	source_cmd = "source" { path }* ;
	describe_cmd = "describe" { path }* ;
	execute_cmd =  { path }* { function }* ;
	function = 
		| identifier args_flag args
		| identifier kwargs
		| identifier
		;
	args_flag = "--args" | "-a" ;
	args = { arg }* ;
	kwargs = { kwarg }* ;
	kwarg = flag arg ;
	arg = boolean | numeric | string ;
	
	identifier = /[a-zA-Z_]+[a-zA-Z0-9]*/ ;
	flag = /-[a-zA-Z_]+[a-zA-Z0-9]*/ ;
	boolean = "True" | "False" ;
	numeric = /\d+/ ;
	string = /[a-zA-Z]+/ ;
	path = /[a-zA-Z]+\.py/ ;

'''


def main():
    import pprint
    import json
    from grako import parse
    from grako.util import asjson

    ast = parse(GRAMMAR, 'file.py a.py testing.py test2 -hello True False test3 test4 --args 1 2')
    json_ast = asjson(ast)
    print(ast)


if __name__ == '__main__':
    main()