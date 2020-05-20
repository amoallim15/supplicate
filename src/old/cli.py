import sys
import argparse

_usage = """

Supplicate a python function execution.

Commands:
  source        Source a specific file/s in current folder pyproject.toml
  drop          Drops a specific file/s in current folder pyproject.toml
  version       Print the tool version information

Usage:
  supp <command> [<args>]
  supp [<filepaths>] [<functions (--args/-a) [values]>]
  supp [<filepaths>] [<functions [--key value]>]
  supp [<filepaths>] [<functions [key=value]>]

Use "supp <command> --help" for more information about a given command.
"""

class CLI():
	
	def __init__(self):
		parser = argparse.ArgumentParser(usage=_usage)
		parser.add_argument('test', help="nothing")
		args = parser.parse_args()
		pass


# def main():
# 	print(sys.argv, end='\n\n')
	"""
	manages top-level CLI supplication, typically via ``setup.py`` entrypoints.

	Designed for distributing supplication
	"""

def main():
	CLI()