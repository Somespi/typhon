from enum import StrEnum, auto
from dataclasses import dataclass
from typing import Tuple
from position import Position

class TokenType(StrEnum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    FLOAT = auto()
    INTEGER = auto()

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
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    MODULO = '%'
    EXPONENT = '**'
    
    PLUS_EQUAL = '+='
    MINUS_EQUAL = '-='
    MULTIPLY_EQUAL = '*='
    DIVIDE_EQUAL = '/='
    MODULO_EQUAL = '%='
    EXPONENT_EQUAL = '**='


PUNCTUATIONS =  (
    TokenType.EQUAL, 
    TokenType.EQUAL_EQUAL, 
    TokenType.OPEN_PAREN, 
    TokenType.CLOSE_PAREN,
    TokenType.OPEN_BRACE,
    TokenType.CLOSE_BRACE,
    TokenType.OPEN_BRACKET,
    TokenType.CLOSE_BRACKET,
    TokenType.SEMI_COLON,
    TokenType.COLON
)

@dataclass 
class Token:
    position: Tuple[Position, Position]
    type: TokenType 
    literal: str


