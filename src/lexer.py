from position import Position
import tokens

class Lexer: 
    def __init__(self, source: str):
        self.source = source
        self.position = Position(-1, 1, source)
        self.current_char = lambda: self.position.current
        self.tokens = []
    
    def lex(self) -> list[tokens.Token]:
        self.position.peek()
        while self.current_char() is not None:
            if self.current_char().isspace(): 
                self.position.peek()
            elif self.current_char().isdigit():
                self.tokens.append(self._number())
            elif self.current_char().isalpha():
                self.tokens.append(self._identifier())
            elif self.current_char() in tokens.PUNCTUATIONS:
                self.tokens.append(self._punctuation())
            elif self.current_char() in tokens.OPERATIONS:
                self.tokens.append(self._operations())
            elif self.current_char() in {'"', "'"}:
                self.tokens.append(self._string())
            else:
                ... # TODO: Error handling
        return self.tokens
    
    def _number(self) -> tokens.Token: 
        start_position = self.position.copy()
        number = self.current_char()
        is_float = False
        self.position.peek()
        while self.current_char() is not None and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.' and not is_float:
                is_float = True
            elif self.current_char() == '.' and is_float:
                ... # TODO: Error handling
            number += self.current_char()
            self.position.peek()
        return tokens.Token((start_position, self.position.copy()), tokens.TokenType.INTEGER if not is_float else tokens.TokenType.FLOAT, number)

    def _punctuation(self, start_position: Position=None, punctuation: str=None) -> tokens.Token: 
        start_position = start_position if start_position is not None else self.position
        punctuation = punctuation if punctuation is not None else self.current_char()
        self.position.peek()
        return tokens.Token((start_position, self.position.copy()), tokens.TokenType(punctuation), punctuation)
    
    
    def _operations(self) -> tokens.Token:
        start_position = self.position.copy()
        operation = self.current_char()
        self.position.peek()
        if operation == '*' and self.current_char() == '*':
            operation += self.current_char()
            self.position.peek()
        
        if self.current_char() == '=':
            operation += self.current_char()
            self.position.peek()
        return self._punctuation(start_position, operation)
    
    def _identifier(self) -> tokens.Token:
        start_position = self.position.copy()
        identifier = self.current_char()
        self.position.peek()
        while self.current_char() is not None and (self.current_char().isalnum() or self.current_char() == '_'):
            identifier += self.current_char()
            self.position.peek()
        if identifier in tokens.KEYWORDS:
            return tokens.Token((start_position, self.position.copy()), tokens.TokenType.KEYWORD, identifier)
        else:
            return tokens.Token((start_position, self.position.copy()), tokens.TokenType.IDENTIFIER, identifier)
    
    def _string(self) -> tokens.Token:
        start_position = self.position.copy()
        starting = self.current_char()
        self.position.peek()
        string = ""
        while self.current_char() is not None and self.current_char() != starting:
            string += self.current_char()
            self.position.peek()
        self.position.peek()
        return tokens.Token((start_position, self.position.copy()), tokens.TokenType.STRING, string)