#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
shlex example: see http://pymotw.com/2/shlex/
simple lexer (e.g. for command-line utilities)
"""
from shlex import split, shlex


def test_shlex():
    text = """ stuff much # comment"""
    print("ORIGINAL:", repr(text))
    print()
    print("TOKENS:")
    print(split(text))


def test_shlex2():
    text = """a,b source more.txt # comment"""
    lexer = shlex(text)  # consider posix=True
    lexer.wordchars += "."  # '.' is not a delimiter. In some situations, add ._-\
    lexer.source = (
        "source"
    )  # Since the source property of the lexer is set to “source”, when the keyword is encountered the filename appearing in the next title is automatically included.
    # control the whitespace characters used to split words.
    lexer.whitespace += ","
    print("TOKENS:")
    try:
        for token in lexer:
            print(repr(token))
    except ValueError as err:
        first_line_of_error = lexer.token.splitlines()[0]
        print(
            "ERROR:",
            lexer.error_leader(),
            str(err),
            'following "' + first_line_of_error + '"',
        )


def main():
    test_shlex()
    print()
    test_shlex2()


if __name__ == "__main__":
    main()