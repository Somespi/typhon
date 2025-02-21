from pprint import pprint
from lexer import Lexer

TEST_INDEX_COUNT = 0

def test_lexer(source: str):
    global TEST_INDEX_COUNT
    print(f"Test {(TEST_INDEX_COUNT := TEST_INDEX_COUNT + 1)}".center(26, '='))
    lexer = Lexer(source)
    pprint(lexer.lex())
    print("=" * 26, '\n')


test_lexer("1 + 1 = 2;")
test_lexer("13 + 13 == 26.5;")
test_lexer("34.65 *= 45.5;\n 456.23;")
test_lexer("test_function(53 and 56);")