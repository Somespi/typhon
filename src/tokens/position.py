


class Position:
    def __init__(self, col: int, line: int, source: str):
        self.col = col 
        self.line = line
        self.current = None
        self.pos = -1 
        self.source = source

    def copy(self):
        return self

    def peek(self):
        if self.pos + 1 < len(self.source):
            self.pos += 1
            self.current = self.source[self.pos]
            if self.current == '\n':
                self.line += 1
                self.col   = 0
            else:
                self.col  += 1 
        else:
            self.current =  None

    @property
    def current(self):
        return self.current
