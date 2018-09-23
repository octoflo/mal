# Holds functions for reading/processing tokens
import re # for the ability to use regular expressions

class BlankError(Exception): pass # an exception with a fancy name
class Symbol(str): pass # starting as a string and changing it
class Ax_List(list):
    def __str__(self):
        slst = [str(e) for e in self]
        return "(" + " ".join(slst) + ")"

def _symbol(name):
    "creates a new symbol"
    return Symbol(name)

def _is_symbol(thing):
    "tests to see if the token is a symbol"
    return isinstance(thing, Symbol)

class Reader:
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def peek(self):
        "returns token at current position"
        if self.position >= len(self.tokens):
            return None
        else:
            return self.tokens[self.position]

    def next(self):
        "returns token at current position, imcrements position"
        results = self.peek()
        self.position += 1
        return results

def tokenize(string):
    "takes a string and returns an array with tokens"
    pattern = re.compile(r"""

    [\s,]*                # Matches any number of whitespaces or commas, it will be ignored and not tokenized.
    (
      ~@                  # Captures the special two-characters ~@ (tokenized).
     |
       [\[\]{}()'`~^@]    # Captures any special single character, one of []{}()'`~^@ (tokenized).
     |
       "(?:\\.|[^\\"])*"? # (Strings) Starts capturing at a double-quote and stops at the next double-quote (unless proceeded by \, then includes it until the next double-quote)
     |
       ;.*                # Captures any sequence of characters starting with ; (tokenized).
     |
       [^\s\[\]{}()'"`@,;]+  # Words and operators (anything that's not a special character listed)
    )
    """, re.VERBOSE)

    return [f for f in re.findall(pattern, string) if f[0] != ';']

def read_form(reader):
    "decides if the token is a list to be read or an atom"
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    elif token == ")":
        raise Exception("unexpected ')'")
    else:
        return read_atom(reader)

def read_sequence(reader, typ=list, start='(', end=')'):
    "Adds the tokens together in one list until it reaches the end"
    token = reader.next() # ignore the initial (, but still prints it
    if token != start:
        raise Exception("expected '" + start + "'")

    token = reader.peek()
    results = Ax_List()
    while token != end:
        if not token:
            raise Exception("expected '" + end + "', got EOF")
        results.append(read_form(reader))
        token = reader.peek() # ?? Why again
    reader.next() # ignore the final )
    return results

def read_list(reader):
    return read_sequence(reader, list, '(', ')')

def read_atom(reader):
    "returns token if it's a string or turns it into a symbol"
    token = reader.next()
    if token[0] == "\"":
        return token
    else:
        try:
            return int(token)
        except ValueError:
            return _symbol(token)

def read_str(string):
    "returns the string or a blankline"
    tokens = tokenize(string)
    if len(tokens) == 0:
        raise BlankError("Blank entry") # doesn't evaluate anything because there's nothing there
    reader = Reader(tokens)
    return read_form(reader) # ??
    # return read_form(Reader(tokens))
