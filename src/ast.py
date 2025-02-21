from dataclasses import dataclass


@dataclass
class Node: 
    ... 
    
@dataclass
class Expression(Node):
    ... 

@dataclass
class Statement(Expression):
    ... 

@dataclass
class IntegerNode(Expression):
    value: int 

@dataclass
class FloatNode(Expression):
    value: float 

@dataclass
class LiteralNode(Expression):
    value: str 

@dataclass
class BoolNode(Expression):
    value: bool
    

@dataclass
class NoneNode(Expression):
    ... 

@dataclass
class Lambda(Expression):
    arguments: list[Node]
    body: Expression


@dataclass
class Program(Node):
    body: list[Statement]