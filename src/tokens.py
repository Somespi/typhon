from enum import StrEnum, auto
from dataclasses import dataclass
from typing import Tuple
from position import Position


class TokenType(StrEnum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    FLOAT = auto()
    INTEGER = auto()
    STRING = auto()

    EQUAL = '='
    EQUAL_EQUAL = '=='
    OPEN_PAREN = '('
    CLOSE_PAREN = ')'
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    SEMI_COLON = ';'
    COLON = ':'
    COMMA = ','
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    BACKSLASH = '\\'
    MODULO = '%'
    EXPONENT = '**'

    PLUS_EQUAL = '+='
    MINUS_EQUAL = '-='
    MULTIPLY_EQUAL = '*='
    DIVIDE_EQUAL = '/='
    MODULO_EQUAL = '%='
    EXPONENT_EQUAL = '**='
    
    EOF = 'EOF'


PUNCTUATIONS = (
    TokenType.EQUAL,
    TokenType.EQUAL_EQUAL,
    TokenType.OPEN_PAREN,
    TokenType.CLOSE_PAREN,
    TokenType.OPEN_BRACE,
    TokenType.CLOSE_BRACE,
    TokenType.OPEN_BRACKET,
    TokenType.CLOSE_BRACKET,
    TokenType.SEMI_COLON,
    TokenType.COLON,
    TokenType.COMMA
)

OPERATIONS = (
    TokenType.PLUS,
    TokenType.MINUS,
    TokenType.MULTIPLY,
    TokenType.DIVIDE,
    TokenType.MODULO
)

KEYWORDS = (
    'False', 
    'None', 
    'True', 
    'and', 
    'as', 
    'assert', 
    'async', 
    'await', 
    'break', 
    'class', 
    'continue', 
    'def', 
    'del', 
    'elif', 
    'else', 
    'except', 
    'finally', 
    'for', 
    'from', 
    'if', 
    'import', 
    'in', 
    'is', 
    'lambda', 
    'not', 
    'or', 
    'pass', 
    'raise', 
    'return', 
    'try', 
    'while', 
    'with', 
    'yield'
)


@dataclass
class Token:
    position: Tuple[Position, Position]
    type: TokenType
    literal: str
