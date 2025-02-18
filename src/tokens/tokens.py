from enum import Enum, auto
from dataclasses import dataclass
from typing import Tuple
from position import Position

class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    FLOAT = auto()
    INTEGER = auto()

    EQUAL = auto()
    EQUAL_EQUAL = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    OPEN_BRACE = auto()
    CLOSE_BRACE = auto()
    OPEN_BRACKET = auto()
    CLOSE_BRACKET = auto()


@dataclass 
class Token:
    position: Tuple[Position, Position]
    type: TokenType 
    literal: str
    
