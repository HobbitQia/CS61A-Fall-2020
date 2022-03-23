"""The scheme_tokens module provides functions tokenize_line and tokenize_lines
for converting (iterators producing) strings into (iterators producing) lists
of tokens.  A token may be:

  * A number (represented as an int or float)
  * A boolean (represented as a bool)
  * A symbol (represented as a string)
  * A delimiter, including parentheses, dots, and single quotes

This file also includes some features of Scheme that have not been addressed
in the course, such as Scheme strings.
"""

from __future__ import print_function  # Python 2 compatibility

from ucb import main
import sys

_NUMERAL_STARTS = set("0123456789") | set('+-.')
_SYMBOL_CHARS = (set('!$%&*/:<=>?@^_~') | set("abcdefghijklmnopqrstuvwxyz") |
                 set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") | _NUMERAL_STARTS)
_STRING_DELIMS = set('"')
_WHITESPACE = set(' \t\n\r')
_SINGLE_CHAR_TOKENS = set("()[]'`")
_TOKEN_END = _WHITESPACE | _SINGLE_CHAR_TOKENS | _STRING_DELIMS | {',', ',@'}
DELIMITERS = _SINGLE_CHAR_TOKENS | {'.', ',', ',@'}
_MAX_TOKEN_LENGTH = 50


def chain(*iters):
    for iter in iters:
        yield from iter


def valid_symbol(s):
    """Returns whether s is a well-formed symbol."""
    if len(s) == 0:
        return False
    for c in s:
        if c not in _SYMBOL_CHARS:
            return False
    return True

def next_candidate_token(line, k):
    """A tuple (tok, k'), where tok is the next substring of line at or
    after position k that could be a token (assuming it passes a validity
    check), and k' is the position in line following that token.  Returns
    (None, len(line)) when there are no more tokens."""
    while k < len(line):
        c = line[k]
        if c == ';':
            return None, len(line)
        elif c in _WHITESPACE:
            k += 1
        elif c in _SINGLE_CHAR_TOKENS:
            if c == ']': c = ')'
            if c == '[': c = '('
            return c, k+1
        elif c == '#':  # Boolean values #t and #f
            return line[k:k+2], min(k+2, len(line))
        elif c == ',': # Unquote; check for @
            if k+1 < len(line) and line[k+1] == '@':
                return ',@', k+2
            return c, k+1
        elif c in _STRING_DELIMS:
            if k+1 < len(line) and line[k+1] == c: # No triple quotes in Scheme
                return c+c, k+2
            s = ""
            k += 1
            while k < len(line):
                c = line[k]
                if c == "\"":
                    check_token_length_warning(s, len(s) + 2)
                    return "\"" + s + "\"", k+1
                elif c == "\\":
                    if k + 1 == len(line):
                        raise SyntaxError("String ended abruptly")
                    next = line[k + 1]
                    if next == "n":
                        s += "\n"
                    else:
                        s += next
                    k += 2
                else:
                    s += c
                    k += 1
            raise SyntaxError("String ended abruptly")
        else:
            j = k
            while j < len(line) and line[j] not in _TOKEN_END:
                j += 1
            check_token_length_warning(line[k:j], min(j, len(line)) - k)
            return line[k:j], min(j, len(line))
    return None, len(line)

def tokenize_line(line):
    """The list of Scheme tokens on line.  Excludes comments and whitespace."""
    result = []
    text, i = next_candidate_token(line, 0)
    while text is not None:
        if text in DELIMITERS:
            result.append(text)
        elif text == '#t' or text.lower() == 'true':
            result.append(True)
        elif text == '#f' or text.lower() == 'false':
            result.append(False)
        elif text == 'nil':
            result.append(text)
        elif text[0] in _SYMBOL_CHARS:
            number = False
            if text[0] in _NUMERAL_STARTS:
                try:
                    result.append(int(text))
                    number = True
                except ValueError:
                    try:
                        result.append(float(text))
                        number = True
                    except ValueError:
                        pass
            if not number:
                if valid_symbol(text):
                    result.append(text.lower())
                else:
                    raise ValueError("invalid numeral or symbol: {0}".format(text))
        elif text[0] in _STRING_DELIMS:
            result.append(text)
        else:
            error_message = [
                "warning: invalid token: {0}".format(text),
                " " * 4       + line,
                " " * (i + 4) + "^"
            ]
            raise ValueError("\n".join(error_message))
        text, i = next_candidate_token(line, i)
    return result

def check_token_length_warning(token, length):
    if length > _MAX_TOKEN_LENGTH:
        import warnings
        warnings.warn("Token {} has exceeded the maximum token length {}".format(token, _MAX_TOKEN_LENGTH, length))

def tokenize_lines(inp):
    """An iterator over lists of tokens, one for each line of the iterable
    input sequence inp."""
    return (tokenize_line(line) for line in inp)

def count_tokens(inp):
    """Count the number of non-delimiter tokens in inp."""
    return len(list(chain(*tokenize_lines(inp))))

@main
def run(*args):
    import argparse
    parser = argparse.ArgumentParser(description='Count Scheme tokens.')
    parser.add_argument('file', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin,
                        help='input file to be counted')
    args = parser.parse_args()
    print('counted', count_tokens(args.file), 'tokens')