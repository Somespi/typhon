from pprint import pprint
from lexer import Lexer
from parser import Parser

TEST_INDEX_COUNT = 0

def test_parser(source: str):
    global TEST_INDEX_COUNT
    print(f"Test {(TEST_INDEX_COUNT := TEST_INDEX_COUNT + 1)}".center(26, '='))
    lexer = Lexer(source)
    parser = Parser(lexer.lex())
    pprint(parser.parse())
    print("=" * 26, '\n')


test_parser("345;")
test_parser("'Hello, World!';")
test_parser("lambda x,y,z: 456;")