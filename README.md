# 💻 Simple C-Like Language Compiler Frontend (Scanner & Parser)

This repository contains the **lexical analyzer (Scanner)** and **syntactic analyzer (Parser)** for a small, C-like programming language. This project is a foundational exercise in compiler construction, demonstrating the conversion of raw source code into a stream of tokens and then validating that stream against a formal grammar using a **Recursive Descent Parser**.

---

## 🚀 Features

* **Lexical Analysis (Scanner):** Converts C-like source code into meaningful tokens (Keywords, Identifiers, Operators, Numbers, etc.).
* **Syntactic Analysis (Parser):** Implements a **Recursive Descent Parser** to check the syntax of the token stream against the provided Context-Free Grammar.
* **Error Detection:** Provides clear error reporting for both unexpected characters (**Lexical Errors**) and violations of the grammar rules (**Syntax Errors**).
* **Comment Handling:** Properly skips and tokenizes both single-line (`//`) and multi-line (`/* ... */`) comments during both scanning and parsing.

---

## ⚙️ Project Structure

The core functionality is contained within a single Python file for simplicity:

| File | Description |
| :--- | :--- |
| `full_scanner_and_parser.py` | Contains the integrated Scanner and Recursive Descent Parser logic. |
| `main_code.c` | A sample input file used for demonstrating the compiler's functionality. |

---

## ▶️ Running the Code

The main Python script (`full_scanner_and_parser.py`) includes the core logic for both the scanner and parser. You will need to modify the main execution block of this file to handle command-line arguments (`sys.argv`) for reading external files and determining the output mode.

### Recommended Setup (Using `full_scanner_and_parser.py`)

1.  **Save the Code:** Ensure the combined code is saved as `full_scanner_and_parser.py`.
2.  **Input File:** Create an input file (e.g., `test.c`) containing the C-like source code you wish to analyze.

### Execution Commands

These commands demonstrate the required two modes of operation:

#### Mode 1: Scan and Parse (Full Frontend Analysis)

This command reads the input file, tokenizes it, and attempts to parse the resulting token stream against the grammar.

```bash
python full_scanner_and_parser.py test.c

---
## 📖 Grammar Rules

The parser uses the following **Context-Free Grammar (CFG)** rules, which define the legal structure of programs in this language. Non-terminals are enclosed in angle brackets (`<>`).

```bnf
<Program> ::= <FunctionList>

<FunctionList> ::= <Function> <FunctionList> | ε

<Function> ::= <Type> IDENTIFIER '(' ')' '{' <StatementList> '}'

<Type> ::= KEYWORD('int') | KEYWORD('void') | KEYWORD('float') | KEYWORD('double') | KEYWORD('char')

<StatementList> ::= <Statement> <StatementList> | ε

<Statement> ::= <Declaration>
            | <Assignment>
            | <IfStatement>
            | <ReturnStatement>

<Declaration> ::= <Type> IDENTIFIER <MoreVars> SPECIAL_CHAR(';')

<MoreVars> ::= SPECIAL_CHAR(',') IDENTIFIER <MoreVars> | ε

<Assignment> ::= IDENTIFIER OPERATOR('=') <Expression> SPECIAL_CHAR(';')

<IfStatement> ::= KEYWORD('if') SPECIAL_CHAR('(') <Condition> SPECIAL_CHAR(')') <Block> <ElsePart>

<Block> ::= SPECIAL_CHAR('{') <StatementList> SPECIAL_CHAR('}')

<ElsePart> ::= KEYWORD('else') <Block> | ε

<ReturnStatement> ::= KEYWORD('return') <Expression> SPECIAL_CHAR(';')

<Condition> ::= <Expression> <RelOp> <Expression>

<RelOp> ::= OPERATOR('==') | OPERATOR('!=') | OPERATOR('<') | OPERATOR('>') | OPERATOR('<=') | OPERATOR('>=')

<Expression> ::= <Term> <MoreTerms>

<MoreTerms> ::= OPERATOR('+') <Term> <MoreTerms>
            | OPERATOR('-') <Term> <MoreTerms>
            | ε

<Term> ::= <Factor> <MoreFactors>

<MoreFactors> ::= OPERATOR('*') <Factor> <MoreFactors>

              | OPERATOR('/') <Factor> <MoreFactors>
              | ε

<Factor> ::= IDENTIFIER
         | CONSTANT_NUMBER
         | SPECIAL_CHAR('(') <Expression> SPECIAL_CHAR(')')

