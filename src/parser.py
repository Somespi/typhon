import tokens
import nodes


class Parser:
    def __init__(self, tokens: list[tokens.Token]):
        self.tokens = tokens
        self.pos = 0  
        self.current = lambda: self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self):
        self.pos += 1
    
    def expect(self, tok_literal: str):
        if not self.current() or self.current().type != tokens.TokenType(tok_literal):
            raise SyntaxError(f"Expected '{tok_literal}', got '{self.current().literal if self.current() else 'EOF'}' at {self.tokens[self.pos - 1].position[1]}")
        self.advance()

    def parse(self):
        program = nodes.Program([])
        while self.current() and self.current().type != tokens.TokenType.EOF:
            program.body.append(self._statement())
        return program

    def _statement(self):
        token = self.current()
        self.advance()
        
        if token.literal == 'lambda':
            return self._lambda()
        else: 
            expr = self._expression(token)
            self.expect(';')
            return expr
    
    
    def _lambda(self):
        arguments_list = []
        while self.current().type == tokens.TokenType.IDENTIFIER:
            arguments_list.append(self.current().literal)
            self.advance()
            if self.current().type == tokens.TokenType.COMMA:
                self.advance()
            else:
                break 
        self.expect(':')
        lambda_node = nodes.Lambda(arguments_list, self._expression(self.current()))
        self.advance()
        self.expect(';')
        return lambda_node
    
    def _expression(self, token):

        if token.type == tokens.TokenType.INTEGER:
            return nodes.IntegerNode(int(token.literal))
        elif token.type == tokens.TokenType.FLOAT:
            return nodes.FloatNode(float(token.literal))
        elif token.type == tokens.TokenType.STRING:
            return nodes.LiteralNode(token.literal)
        elif token.literal in {'True', 'False'}:
            return nodes.BoolNode(token.literal == 'True')

        raise SyntaxError(f"Unexpected token: {token.literal} at {self.pos}")