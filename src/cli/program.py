import argparse
import sys
import os


class SuppCLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Supplicate")
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            self.main()
        else:
            getattr(self, args.command)()

    def main(self):
        print("main", sys.argv)
        print(os.environ)
        pass

    def version(self):
        print("version", sys.argv)
        pass

    def help(self):
        print("help", sys.argv)
        pass

    def source(self):
        print("source", sys.argv)
        pass

    def drop(self):
        print("drop", sys.argv)
        pass

    def describe(self):
        print("describe", sys.argv)
        pass
