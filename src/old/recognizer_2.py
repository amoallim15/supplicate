import re


class RecoToken:
    def __init__(self):
        self.index = -1
        self.type = None
        self.value = None

    def __repr__(self):
        return f"RecoToken({self.type}, {self.value}, {self.index})"


class RecoMatch:
    def __init__(self, index, type, value):
        self.index = index
        self.type = type
        self.value = value

    def __len__(self):
        return len(self.value)


class RecoRule:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def match(self, data, index):
        return self.func(data, index)

    def __repr__(self, name):
        return f"{type(self).__name__}({self.name}, {self.func})"


class RecoRegexRule(RecoRule):
    def __init__(self, name, regex_str):
        self.name = name
        self.regex_str = regex_str
        self.func = re.compile(regex_str)

    def match(self, data, index):
        m = self.func.match(data[index])
        if m:
            return RecoMatch(index, self.name, m.group())


class Reco:
    def __init__(self, rules):
        self.lex_data = None
        self.lex_index = 0
        self.lex_len = 0
        self.rules = rules
        self.nomatch_token_type = "NOMATCH"

    def input(self, ls):
        self.lex_data = ls
        self.lex_index = 0
        self.lex_len = len(ls)

    def token(self):
        if self.lex_index >= self.lex_len:
            return None
        for rule in self.rules:
            _match = rule.match(self.lex_data, self.lex_index)
            if not _match:
                continue
            if len(_match) < len(self.lex_data[self.lex_index]):
                continue
            token = RecoToken()
            token.index = _match.index
            token.type = _match.type
            token.value = _match.value
            self.lex_index += 1
            return token
        else:
            token = RecoToken()
            token.type = self.nomatch_token_type
            token.index = self.lex_index
            token.value = self.lex_data[self.lex_index]
            self.lex_index += 1
            return token

    def __iter__(self):
        return self

    def __next__(self):
        token = self.token()
        if token is None:
            raise StopIteration
        return token
