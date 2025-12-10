import re
import os

token_types = [
    ('MULTICOMMENT', r'/\*.*?\*/'),          
    ('COMMENT', r'//[^\n]*'),               
    ('STRING', r'"[^"\n]*"|\'[^\'\n]*\''), 
    ('Constant_NUMBER', r'\d+(\.\d+)?'),
    ('Identifier', r'[A-Za-z_]\w*'),
    ('Operator', r'==|!=|<=|>=|[+\-*/=<>]'),
    ('Special_Character', r'[()\[\]{};,]'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('INVALID', r'.')
]


reserved_words = {'int', 'float', 'char', 'if', 'else', 'for', 'while', 'return', 'void'}

# Compile a single regex pattern for all token types
token_regex = '|'.join(f"(?P<{name}>{pattern})" for name, pattern in token_types)
compiled_pattern = re.compile(token_regex, re.DOTALL)

def tokenize_code(code):
    """
    Tokenizes a given string of code.
    
    Args:
        code (str): The source code as a string.
        
    Returns:
        list: A list of tokens, where each token is a tuple (type, value).
    """
    tokens = []
    line_number = 1
    position = 0

    while position < len(code):
        match = compiled_pattern.match(code, position)
        if not match:
            raise SyntaxError(f"Unexpected token at line {line_number}")

        type_ = match.lastgroup
        value = match.group()

        if type_ == 'NEWLINE':
            line_number += 1
        elif type_ in ('SKIP'):
            # Skip whitespace and comments
            pass
        elif type_ == 'Identifier' and value in reserved_words:
            tokens.append(('KEYWORD', value))
        elif type_ == 'INVALID':
            raise SyntaxError(f"Invalid symbol '{value}' at line {line_number}")
        else:
            tokens.append((type_, value))

        position = match.end()

    return tokens

def extract_symbols(tokens):
    """
    Extracts identifiers and builds a simple symbol table.
    
    Args:
        tokens (list): A list of tokens from the tokenizer.
        
    Returns:
        dict: A dictionary representing the symbol table.
    """
    symbols = {}
    count = 1
    for token_type, token_value in tokens:
        if token_type == 'Identifier' and token_value not in symbols:
            symbols[token_value] = {
                'type': token_type,
                'index': count
            }
            count += 1
    return symbols

def read_file(filename):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        filename (str): The path to the file.
        
    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return None

# --- Main execution block ---
filename = "main_code.c"
# Read code from the file
source_code = read_file(filename)
if source_code:
    print(f"Successfully read code from '{filename}':\n")
    # Tokenize the code
    try:
        tokens = tokenize_code(source_code)
        print("Tokens:")
        for t in tokens:
            print(f"Token({t[0]}, {t[1]!r})")

         # Extract symbols and print the symbol table
        print("\nSymbol Table:")
        symbol_table = extract_symbols(tokens)
        for name, entry in symbol_table.items():
            print(f"{name}: {entry}")
        
    except SyntaxError as e:
        print(f"\nSyntax Error: {e}")


