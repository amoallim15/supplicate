import sys
import re


class RecognizerException(Exception):
    def __init__(self, message, value, index):
        super().__init__(message)
        self.value = value
        self.index = index


class Recognizer:
    def __init__(self, rules):
        self.group_type = {}
        self.buffer = []
        self.index = 0
        idx = 1
        regex_parts = []
        for _type, _regex in rules:
            groupname = "GROUP_{}".format(idx)
            regex_parts.append("(?P<{}>{})".format(groupname, _regex))
            self.group_type[groupname] = _type
            idx += 1
        self.regex = re.compile("|".join(regex_parts))

    def feed(self, ls):
        self.buffer += ls
        self.index = 0

    def __token(self):
        if self.index >= len(self.buffer):
            return None
        match = self.regex.match(self.buffer[self.index])
        if not match:
            raise RecognizerException(
                message='Recognizer failed at "{}" of index {}'.format(
                    self.buffer[self.index], self.index
                ),
                index=self.index,
                value=self.buffer[self.index],
            )
        print(match.groupdict())
        if match and match.span()[1] == len(self.buffer[self.index]):
            groupname = match.lastgroup
            token_type = self.group_type[groupname]
            token_value = match.group(groupname)
            token_index = self.index
            self.index += 1
            return token_type, token_value, token_index

    def __iter__(self):
        return self

    def __next__(self):
        token = self.__token()
        if token is None:
            raise StopIteration
        return token


rules = [
    ("PATH", """[\w\/"\s\.]+\.py"""),  # python file path
    ("FLAG", """-[a-zA-Z_]+[a-zA-Z0-9]*"""),  # -e -h -a -v -*
    (
        "DOUBLE_FLAG",
        """--[a-zA-Z_]+[a-zA-Z0-9]*""",
    ),  # --env --help --args --verbose --*
    (
        "NUMERIC",
        "[+-]?(?:\d+(?:[eE][+-]?\d+)|(?:\d+\.\d*|\.\d+)(?:[eE][+-]?\d+)?)|[+-]?\d+",
    ),  # integer
    ("BOOLEAN", """True|False"""),  # True / False
    ("IDENTIFIER", """[a-zA-Z_]+[a-zA-Z0-9]*"""),  # function/arguments keys or values
    ("STRING", """[\s\S]*"""),  # string
]

a = Recognizer(rules)

a.feed(["hellop.py", "test", "-a", "2", "True", "1hellow"])
for cc in a:
    print(cc)
