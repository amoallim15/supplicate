"""
# 
supp help >> app arguments help
supp version >> app version
# 
supp source >> source a file/dir as active
	./ 
	/blah.py <
	/foo.py
supp drop >> drop current active file/dir if sourced
# 
supp describe >> describes a file current or (path must be provided)
supp describe file.py
# 
supp --help|-h >> describe a file current if no file is sourced fail
supp file.py --help|-h >> describes a file
#
supp file.py func func func >> func:, func:, func:,
supp file.py func --args|-a blah blah blah  >> func: [blah, blah, blah]
supp file.py func -a blah -b blah -c blah >> func: { a: blah, b: blah, c: blah }
#
supp func func func >> func:, func:, func:,
supp func --args|-a blah blah blah  >> func: [blah, blah, blah]
supp func -a blah -b blah -c blah >> func: { a: blah, b: blah, c: blah }
#
done.

1: if argv[1] == help >> ignore rest >> execute help command
2: if argv[1] == version >> ignore rest >> execute version command
3: if argv[1] == source >> ignore rest >> execute source command
4: if argv[1] == drop >> ignore rest >> execute drop command
5: if argv[1] == describe
	5.1 >> search for a file argument
	5.2 >> if exist >> ignore rest >> execute describe command
	5.3 >> if not exist >> ignore rest >> execute desribe command
6: if argv[1] == [--help|-h] 
	6.1 >> search for a file argument
	6.2 >> if exist >> ignore rest >> execute describe command
	6.3 >> if not exist >> ignore rest >> execute describe command
7: if argv[1] == file_path
	7.1 >> if argv[2] == file_path >> go to 7:
	7.2 >> if argv[3] == [--help|-h] >> go to 6:
	7.2 >> if not >> got to 8
8: if argv[1] == UNKNOWN >> 
||	8.1 >> if argv[2] == [--args|-a] >> parse func/args pattern 
		>> if match >> execute all
		>> if not match >> go to 8.2
||	8.2 >> parse func arguments pattern 
		>> if match >> execute a;;
		>> if not raise error

"""


use_cases = [
	# simple
	'supp source', #0 source command
	'supp source ./', #1 source command
	'supp source file.py', #2 source command
	'supp source file.py -f sds', #3 source command with error
	# 
	'supp drop', #4 drop command
	'supp drop blah.py -a fds', #5 drop command with error
	'supp drop hi.py', #6 drop command with error if hi.py is not sourced
	# 
	'supp', #7 help command
	'supp help', #8 help command
	'supp help -a bar.py', #9 help command with error
	'supp version', #10 version command
	'supp version test', #11 version command with error
	# 
	'supp ./ ./file.py ./test.py hello_world bye', #12 execute command [$3 file_paths] [$2 funcs]
	'supp blah blah', #13 execute command [$2 funcs]
	'supp blah -a bye', #14 execute command [$1 func](bye)
	'supp blah -hi bye', #15 execute command [$1 func](hi=bye)
	'supp blah -hi bye come', #16 execute command [$1 func](hi=bye) with error
	'supp blah -a bye -d lets', #17 execute command [$1 func](a=bye, d=lets)
	'supp blah --args bye', #18 execute command [$1 func](bye)
	'supp blah --a bye hi now', #19 execute command [$1 func](bye, hi, now)
]
