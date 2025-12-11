# Simple C Language (Scanner & Recursive Descent Parser)

# Features
- Lexical Analysis (Scanner): Converts C source code into  tokens (Keywords, Identifiers, Operators, Numbers, etc.).

- Syntactic Analysis (Parser): Implements a Recursive Descent Parser to check the syntax of the token stream against the provided Context-Free Grammar.
- Error Detection: Detect Errors (Syntax Errors)  and provide Report for expected Token

# How It work

1-Scan and Parse 
```
Python full_scanner_and_parser.py main_code.c

```

It Scan and generate Tokens  and parse this tokens and give Result Directly  COMPILATION SUCCESSFUL!  or Error 

2-Scan and Parse AND Save Tokens

```
Python full_scanner_and_parser.py main_code.c output.txt
```

The Program work normally and Save Tokens in file.txt
___
# Grammar Rules
Program → FunctionList


FunctionList → Function FunctionList | ε


Function → Type IDENTIFIER ( ) { StatementList }


Type → int | void | float | double | char


StatementList → Statement StatementList | ε


Statement → Declaration | Assignment | IfStatement | ReturnStatement


Declaration → Type IDENTIFIER MoreVars ;


MoreVars → , IDENTIFIER MoreVars | ε


Assignment → IDENTIFIER = Expression ;


IfStatement → if ( Condition ) { StatementList } ElsePart


ElsePart → else { StatementList } | ε


ReturnStatement → return Expression ;


Condition → Expression RelOp Expression


RelOp → == | != | < | > | <= | >=


Expression → Term MoreTerms


MoreTerms → + Term MoreTerms | - Term MoreTerms | ε


Term → Factor MoreFactors


MoreFactors → * Factor MoreFactors | / Factor MoreFactors | ε


Factor → IDENTIFIER | NUMERIC_CONSTANT | ( Expression )
