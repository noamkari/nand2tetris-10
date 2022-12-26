import sys

from JackTokenizer import JackTokenizer


def cur_token(toke):
    if toke.token_type() == "KEYWORD":
        return toke.keyword()
    if toke.token_type() == "SYMBOL":
        return toke.symbol()
    if toke.token_type() == "IDENTIFIER":
        return toke.identifier()
    if toke.token_type() == "INT_CONST":
        return toke.int_val()
    if toke.token_type() == "STRING_CONST":
        return toke.string_val()


if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as f:
        toke = JackTokenizer(f)
        while toke.has_more_tokens():
            print(f"{toke.token_type()}: {cur_token(toke)}")
            toke.advance()
