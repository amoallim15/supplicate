import re
import copy

class LexerException():
    """
    Exception raised if an invalid shell block is encountered.
    """
    def __init__(self, message, value, index):
        super().__init__(message)
        self.message = message
        self.value = value
        self.index = index

class Token():
    """
    Representation of a single token.
    """
    __slots__ = ('type', 'value', 'index')
    def __repr__(self):
        return f'Token(type={self.type}, value={self.value}, index={self.index})'

class LexerMeta(type):
    """
    Meta class for initiating the lexer class.
    """
    @staticmethod
    def __new__(cls, clsname, bases, attrs):
        funcs = { key: val for key, val in attrs.items() if callable(val) }
        cls = super().__new__(cls, clsname, bases, attrs)
        cls.funcs = funcs
        return cls

class Lexer(metaclass=LexerMeta):
    tokens = set()
    literals = set()
    # funcs = {}


    def a(self): return True


b = Lexer()

print(dir(b))