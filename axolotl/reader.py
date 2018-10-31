# Holds functions for reading and processing tokens

import re # import the ability to use regular expressions (defined later)
import ax_types as types # import functions, lists, etc. previous definined

class BlankError(Exception): pass # display an exception error if given a blank line

class Reader:
    def __init__(self, tokens, position=0):
        """Every reader instance will be given the tokens and postition that will later be parsed."""
        self.tokens = tokens
        self.position = position

    def peek(self):
        """This returns token at current position"""
        if self.position >= len(self.tokens):
            return None
        else:
            return self.tokens[self.position]

    def next(self):
        """This returns token at current position, imcrements position"""
        results = self.peek()
        self.position += 1
        return results

def tokenize(string):
    """This takes a string and returns an array in token form."""
    # Regular Expressions can be pretty confusing to read, so comments are provided for each line.

    pattern = re.compile(r"""

    [\s,]*                   # Any number of whitespaces or commas will be ignored, so you can use them to organize however you'd like
    (
      ~@                     # Captures the special two-characters ~@ as tokens.
     |
       [\[\]{}()'`~^@]       # Captures any special single character, one of []{}()'`~^@ as tokens.
     |
       "(?:\\.|[^\\"])*"?    # Captures strings. Starts capturing at a double-quote and stops at the next double-quote,
                             # unless proceeded by \, meaning a quote is included in the string.
     |
       |.*                   # A comment is made by a straight line. Captures the series of characters starting with | as tokens.
     |
       [^\s\[\]{}()'"`@,|]+  # Captures any other words and operators (anything that's not a special character listed) as tokens.
    )
    """, re.VERBOSE)

    return [f for f in re.findall(pattern, string) if f[0] != ':']
    # As long as the tokens aren't a comment, return them.

def get_tokens(expression):
    """This will put the given expression through the regular expression and tokenize them."""
    reader = Reader(tokenize(expression))
    return read_form(reader)

def unescape(s):
    """When displaying it to the reader we don't want the backslash in front of quotes,
    so this function takes them out."""
    return s.replace('\\\\', '\u029e').replace('\\"', '"').replace('\\n', '\n').replace('\u029e', '\\')

def read_form(reader):
    """This assesses what the types of token (list or atom) and decides how it should print it."""
    token = reader.peek() # Looks at the current token

    # List:
    if token == "(":
        return read_list(reader)
    elif token == ")":
        raise Exception("unexpected ')'") # Raise an error if the expression is incomplete

    # Vector:
    if token == "[":
        return read_vector(reader)
    elif token == "]":
        raise Exception("unexpected ']'")

    # Dictionary:
    if token == "{":
        return read_dic(reader)
    elif token == "}":
        raise Exception("unexpected '}'")
    else:
        return read_atom(reader)

def read_sequence(reader, typ=list, start='(', end=')'):
    """Adds the evaluated tokens together into one new expression."""
    token = reader.next() # Does not print the intial expression, but still prints it to the reader
    if token != start: # Make sure the expected type (starting with a '(' or '[' ) matches what is actually given
        raise Exception("expected '" + start + "'")

    token = reader.peek() # Looks at current token
    results = typ() # Assesses the types of that token (list, array, function, etc.)

    while token != end: # As long as we haven't gotten to the end of the expression (a closing parenthesis as default)
        if not token: # If no ending token was given, produce an error
            raise Exception("expected '" + end + "', got EOF")
        results.append(read_form(reader)) # Add the evaluated tokens to the new list
        token = reader.peek() # Look at the next token
    reader.next() # ignore the final )
    return results

# The following functions evaluate the expressions by putting the tokens through read sequence,
# but look for different symbols at the start and end depending on their types.
# For example read_list takes a list, so it's start and end are ()

def read_list(reader):
    return read_sequence(reader, types.Ax_List, '(', ')')

def read_vector(reader):
    return read_sequence(reader, types.Ax_Vector, '[', ']')

def read_dic(reader):
    return read_sequence(reader, types.Ax_Dict, '{', '}')

def read_atom(reader):
    """Returns evaluted tokens if it's not a list, vector, or dictionary already defined in a function"""

    token = reader.next() # Looks at the current token
    if token == None: # If the token is a comment
        return None

    elif token[0] == '"': # If the token is a quote, use the unescape function to add the proper backslashes
        if token[-1] == '"':
            return unescape(token[1:-1])
        else:
            raise Exception("expected '\"', got EOF")

    elif token[0] == "\"": # If it starts with a quote it must be a string
        return read_str(token)

    elif token[0] == ":": # For Keywords, the keys in a dictionary that point to a value
        return types.new_keyword(token)

    # Return the respective boolean value if given one as a token
    elif token == "none":
        return None
    elif token == "true":
        return True
    elif token == "false":
        return False
    else:
        try:
            return int(token) # If it weren't any of those types it must be a number
        except ValueError:
            return types.new_symbol(token) # If it isn't a number, it must be a symbol

def read_str(string):
    """If the token is a string it should return the same string or a blankline"""
    return string[1:-1]
