# 🐍 Daily Python Basics & Fundamentals Practice

Welcome to my daily Python learning and practice journey! This repository documents core Python concepts, fundamental syntax, data structures, built-in methods, and real-world use cases practiced day by day.

---

## 📊 Learning Roadmap Overview

| Day | Date | Topic | Key Files |
| :---: | :---: | :--- | :--- |
| **Day 01** | 11/09/2026 | First Python Program & Output | `demo.py` |
| **Day 02** | 12/09/2026 | Variables, Reassignment & Memory `id()` | `sample.py`, `sample1.py` |
| **Day 03** | 13/09/2026 | List Data Type & List Methods | `list_datatype.py`, `list_methods.py` |
| **Day 04** | 14/09/2026 | Tuple Data Structure & Immutability | `tuple_datatype.py` |
| **Day 05** | 15/09/2026 | Set Data Structure & Set Operations | `set_datatype.py`, `set_methods.py` |
| **Day 06** | 16/09/2026 – 18/09/2026 | Dictionary Mapping & Dict Methods | `dictionaary.py`, `dictionary_method.py`, `dictionary.py` |
| **Day 07** | 19/09/2026 | String Data Type, Methods & Concatenation | `string_datatype.py`, `String_methods.py`, `concatination.py` |
| **Day 08** | 20/09/2026 | Comprehensive All-Datatypes Review | `ALLdatatypesPractice.py` |
| **Day 09** | 21/09/2026 | Sequence Slicing `[start:stop:step]` | `sliceing.py` |
| **Day 10** | 22/09/2026 | Explicit & Implicit Type Casting | `explicit_typecasting.py`, `implicit_typecasting.py` |
| **Day 11** | 23/09/2026 | Inter-Collection Conversions & Truthiness | `typecasting3.py`, `typecasting4.py` |
| **Day 12** | 24/09/2026 | Dynamic Expression Evaluation `eval()` | `eval_function.py` |
| **Day 13** | 25/09/2026 | Interactive User Input `input()` | `input_function.py` |
| **Day 14** | 26/09/2026 | Character & Unicode Mapping (`ord` & `chr`) | `charactertoUnicode.py` |
| **Day 15** | 27/09/2026 | Advanced `print()` Parameters (`sep`, `end`) | `print_function.py` |
| **Day 16** | 28/09/2026 | Python Operators (Arithmetic, Relational, Logic, Assignment) | `arithmetic_operators.py`, `Comparison_operator.py`, `Logical_operators.py`, `Assignment_operator.py` |
| **Day 17** | 29/09/2026 | Advanced Operators (Bitwise, Identity, Membership, Short-Circuit Logic) | `Bitwise_operator.py`, `Bitwise_operator2.py`, `Identity_operator.py`, `Membership_operator.py`, `Logical_operators2.py` |
| **Day 18** | 30/09/2026 | Conditional Statements & Flow Control (`if`, `if-else`) | `Conditional_statement.py`, `if_else_condition.py` |
| **Day 19** | 01/10/2026 | Multi-Way Decision, Nested Conditions & Pattern Matching (`match-case`) | `if_elif_else.py`, `nested_if.py`, `Match_case.py` |
| **Day 20** | 05/10/2026 | Conditional Expressions, `range()` Sequences & `for` Loops | `condition_expression.py`, `Range_example.py`, `for_loops.py` |



---

## 📅 Daily Practiced Concepts & File Mappings

### Day 01: Python Basics & Console Output (11/09/2026)
* > First Python Program & Console Printing (`demo.py`)

---

### Day 02: Variables, Reassignment & Memory Management (12/09/2026)
* > Basic String Output and Execution Flow (`sample.py`)
* > Variable Assignment & Value Reassignment (`sample1.py`)
* > Integer Interning (Caching) & Memory Address Inspection via `id()` (`sample1.py`)

---

### Day 03: List Data Structure & Core Methods (13/09/2026)
* > List Creation (`[]`, `list()`), Negative Indexing & Mutability (`list_datatype.py`)
* > Adding Elements with `append()` and `insert()` (`list_methods.py`)
* > Merging Lists with `extend()` vs List Concatenation `+` (`list_methods.py`)
* > Removing Elements with `pop()` and `remove()` (`list_methods.py`)
* > Sequence Reversal with `reverse()` and Sorting with `sort()` (`list_methods.py`)
* > Frequency & Lookup with `count()` and `index()` (`list_methods.py`)
* > Practical Challenge: Sum of Smallest and Largest Number (`list_methods.py`)
* > String Tokenization `split()` vs Character List `list()` (`list_methods.py`)

---

### Day 04: Tuple Data Structure & Immutability (14/09/2026)
* > Empty Tuple Initialization & Length with `len()` (`tuple_datatype.py`)
* > Single-Element Tuple Trailing Comma Syntax `(50,)` (`tuple_datatype.py`)
* > Heterogeneous Tuples & Negative Indexing (`tuple_datatype.py`)
* > Immutability Constraints (`TypeError` on item assignment) (`tuple_datatype.py`)

---

### Day 05: Set Data Structure & Mathematical Venn Operations (15/09/2026)
* > Empty Set Creation with `set()`, Unordered Nature & Automatic Deduplication (`set_datatype.py`)
* > Adding & Updating Items with `add()` and `update()` (`set_methods.py`)
* > Arbitrary Removal with `pop()` (`set_methods.py`)
* > Safe vs Strict Element Deletion: `discard()` vs `remove()` (`set_methods.py`)
* > Clearing Set with `clear()` (`set_methods.py`)
* > Set Subsets & Supersets: `issubset()` and `issuperset()` (`set_methods.py`)
* > Disjoint Sets Verification with `isdisjoint()` (`set_methods.py`)
* > Venn Operations: `union()`, `intersection()`, `difference()`, and `symmetric_difference()` (`set_methods.py`)

---

### Day 06: Dictionary Mapping & Key-Value Methods (16/09/2026 – 18/09/2026)
* > Dictionary Creation, Key-Value Pairs, Lookup, Updating & Adding Pairs (`dictionaary.py`)
* > Safe Key Insertion with `setdefault()` (`dictionary_method.py`)
* > Merging Dictionaries with `update()` (`dictionary_method.py`)
* > Safe Key Access with `get()` (Avoiding `KeyError`) (`dictionary_method.py`)
* > Removing Items with `pop()` and Last-In-First-Out `popitem()` (`dictionary_method.py`)
* > Dictionary Views: `keys()`, `values()`, and `items()` (`dictionary_method.py`)
* > IDLE Interactive Shell Session Log & Debugging History (`dictionary.py`)

---

### Day 07: String Data Type, Built-in Methods & Formatting (19/09/2026)
* > String Literals, Special Characters & Zero-Based Indexing (`string_datatype.py`)
* > Letter Case Methods: `capitalize()`, `title()`, `upper()`, `lower()`, `swapcase()` (`String_methods.py`)
* > Case State Checks: `isupper()` and `islower()` (`String_methods.py`)
* > Substring Matching: `startswith()` and `count()` (`String_methods.py`)
* > Substring Replacement with `replace()` and Location with `index()` (`String_methods.py`)
* > Character Type Validation: `isalpha()`, `isdigit()`, `isalnum()` (`String_methods.py`)
* > String Tokenizing with `split()` (Whitespace, Comma, Slash) (`String_methods.py`)
* > Iterable Joining with `join()` (Space, Delimiters) (`String_methods.py`)
* > String Concatenation (`+`), `str.format()`, and Formatted String Literals (f-strings) (`concatination.py`)

---

### Day 08: Comprehensive Multi-Datatype Review (20/09/2026)
* > Master Practice of Lists, Sets, Dictionaries, and Strings (`ALLdatatypesPractice.py`)
* > List Operations (`append`, `extend`, `insert`, `pop`, `remove`, `count`, `index`, `reverse`, `clear`) (`ALLdatatypesPractice.py`)
* > Set Operations (`add`, `update`, `pop`, `remove`, `discard`, `issubset`, `issuperset`, `isdisjoint`, `union`, `intersection`, `difference`, `symmetric_difference`) (`ALLdatatypesPractice.py`)
* > Dictionary Operations (`setdefault`, `update`, `get`, `popitem`, `pop`, `keys`, `values`, `items`, `clear`) (`ALLdatatypesPractice.py`)
* > String Operations & Whitespace Trimming (`lstrip`, `rstrip`, `strip`) (`ALLdatatypesPractice.py`)

---

### Day 09: Sequence Slicing Concepts (21/09/2026)
* > Slicing Syntax Formula `[start : stop : step]` on Lists (`sliceing.py`)
* > Step Strides and Sub-sampling (`sliceing.py`)
* > Head (`[:N]`) and Tail (`[N:]`) Extraction (`sliceing.py`)
* > Backward Slicing with Negative Steps (`sliceing.py`)
* > Complete Sequence Reversal with `[::-1]` (`sliceing.py`)
* > Substring Slicing on Strings (`sliceing.py`)

---

### Day 10: Type Casting Fundamentals (22/09/2026)
* > Explicit Type Conversion: `int()`, `float()`, `complex()`, `bool()` (`explicit_typecasting.py`)
* > Scalar Conversions & Float Truncation (`explicit_typecasting.py`)
* > Complex Conversion Restrictions (`TypeError` on complex to scalar) (`explicit_typecasting.py`)
* > Implicit Type Casting (Automatic Promotion: `bool` -> `int` -> `float` -> `complex`) (`implicit_typecasting.py`)

---

### Day 11: Advanced Inter-Collection Conversions (23/09/2026)
* > List Conversions to `tuple()`, `set()`, `str()` (`typecasting3.py`)
* > Tuple Conversions to `set()`, `list()`, `str()` (`typecasting3.py`)
* > Set Conversions to `list()`, `tuple()`, `str()` (`typecasting3.py`)
* > String Character Explosion to `list()`, `tuple()`, `set()` (`typecasting3.py`)
* > Dictionary Key and Value Conversions (`typecasting3.py`)
* > Truthiness of Non-Empty vs Empty Collections with `bool()` (`typecasting4.py`)
* > Parsing Numeric Strings into `int`, `float`, and `complex` (`typecasting4.py`)

---

### Day 12: Dynamic Expression Evaluation (24/09/2026)
* > Real-World Dynamic Arithmetic and Function Evaluation with `eval()` (`eval_function.py`)
* > Parsing Complex Python Literals & Data Structures (`eval_function.py`)
* > Parsing Boolean and Primitive String Literals (`eval_function.py`)

---

### Day 13: Interactive Console Input & Parsing (25/09/2026)
* > Reading Console Keystrokes with `input()` as String (`input_function.py`)
* > Parsing String Input to Integer for Numeric Addition (`input_function.py`)
* > Parsing Floating-Point Input for Measurement Calculations (`input_function.py`)
* > Parsing Complex Number Input (`input_function.py`)
* > Boolean Input Gotcha (`bool("False") == True`) and Safe Handling (`input_function.py`)

---

### Day 14: Characters & Unicode Code Points (26/09/2026)
* > Character to Unicode / ASCII Code Point Conversion with `ord()` (`charactertoUnicode.py`)
* > ASCII Code Point to Character Conversion with `chr()` (`charactertoUnicode.py`)
* > Character Range Mapping (Uppercase A-Z, Lowercase a-z, Digits 0-9, Symbols) (`charactertoUnicode.py`)

---

### Day 15: Advanced Print Function Parameters (27/09/2026)
* > Item Separation Formatting with `sep` parameter (`print_function.py`)
* > Output Line Ending Customization with `end` parameter (`print_function.py`)
* > Combining `sep` and `end` for Inline Reports & Custom Layouts (`print_function.py`)
* > Stream Output Redirection with `file` and Buffer Control with `flush` (`print_function.py`)

---

### Day 16: Python Operators (28/09/2026)
* > Arithmetic Operators: `+`, `-`, `*`, `/`, `%`, `//`, `**` (`arithmetic_operators.py`)
* > Comparison / Relational Operators: `==`, `!=`, `>`, `<`, `>=`, `<=` (`Comparison_operator.py`)
* > Logical Operators: `and`, `or` with Truth Tables & Short-Circuiting (`Logical_operators.py`)
* > Assignment / In-Place Compound Operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=` (`Assignment_operator.py`)

---

### Day 17: Advanced Operators & Logic Deep Dive (29/09/2026)
* > Bitwise Binary Operations: AND (`&`), OR (`|`), XOR (`^`) with Bitmasking (`Bitwise_operator.py`)
* > Bitwise NOT Operator: One's Complement (`~n = -(n+1)`) & Two's Complement System (`Bitwise_operator2.py`)
* > Bitwise Binary Shifts: Left Shift (`<<`) & Right Shift (`>>`) with Exponent Formulas (`Bitwise_operator2.py`)
* > Object Identity Operators: `is` and `is not` (`Identity_operator.py`)
* > Identity vs Equality: Memory Reference Address (`id()`) vs Value Equivalence (`==`) (`Identity_operator.py`)
* > Membership Operators: `in` across Lists, Tuples, Sets, Strings, and Dictionaries (`Membership_operator.py`)
* > Dictionary Membership Gotcha: Checking Keys vs `.values()` vs `.items()` (`Membership_operator.py`)
* > Non-Boolean Short-Circuit Evaluation: Truthy & Falsy Operands with `and` & `or` (`Logical_operators2.py`)
* > Default Fallback Idiom: Selecting First Truthy Value or Default (`Logical_operators2.py`)

---

### Day 18: Conditional Statements & Control Flow (30/09/2026)
* > One-Way Decision Making: Simple `if` Statement & Indented Execution Blocks (`Conditional_statement.py`)
* > Integrating Method Results into Conditions: `str.startswith()` (`Conditional_statement.py`)
* > Two-Way Mutually Exclusive Branching: `if ... else` Structure (`if_else_condition.py`)
* > Input & Data Validation with String Length Checks `len() > 2` (`if_else_condition.py`)

---

### Day 19: Multi-Way Branching, Nested Conditions & Pattern Matching (01/10/2026)
* > Multi-Way Decision Making: `if - elif - else` Ladder for Tiered Grade Evaluation (`if_elif_else.py`)
* > Boundary Conditions: Comparing `range()` Half-Open Membership vs Relational Operators (`if_elif_else.py`)
* > Nested Conditional Statements: Hierarchical Outer & Inner `if` Decision Trees (`nested_if.py`)
* > Multi-Stage Eligibility Validation: Voter Verification Flow (Citizenship & Age) (`nested_if.py`)
* > Structural Pattern Matching: Modern Python 3.10+ `match - case` Syntax (`Match_case.py`)
* > Default / Fallback Matching with the Wildcard `case _` Pattern (`Match_case.py`)

---

### Day 20: Conditional Expressions, 'range()' Sequences & 'for' Loops (05/10/2026)
* > Inline Conditional Expression / Ternary Operator (`n**2 if n%2==0 else n**3`) (`condition_expression.py`)
* > Sequence Generator `range(start, stop, step)` and Object Representation (`Range_example.py`)
* > Single-Argument `range(stop)` and Counter Iteration (`Range_example.py`)
* > Materializing `range` into Collections: `list()`, `tuple()`, `set()`, and String Literal `str()` (`Range_example.py`)
* > Boundary Handling with Negative Arguments & Non-Unit Steps (`Range_example.py`)
* > Definite Sequence Iteration with `for-in` Loop (`for_loops.py`)
* > Output Formatting with Custom Separator `sep="/"` and Trailing Space `end=" "` (`for_loops.py`)


---

## 📋 Progress Tracking & Practice Roadmap

For the complete daily tracker, upcoming curriculum milestones, and practicing checklist, see [TODO.md](file:///f:/CodePlayground/Python%20Workspace/TODO.md).

---

## 🛠️ How to Run Any Practice Script

Run any module directly using Python in your terminal:

```bash
# Example 1: Run Bitwise Operators practice
python Bitwise_operator.py

# Example 2: Run Identity & Membership Operators practice
python Identity_operator.py
python Membership_operator.py

# Example 3: Run Conditional Statements practice
python Conditional_statement.py
python if_else_condition.py

# Example 4: Run Decision Branching & Pattern Matching practice
python if_elif_else.py
python nested_if.py
python Match_case.py

# Example 5: Run String Methods practice
python String_methods.py

# Example 6: Run All Data Types Practice
python ALLdatatypesPractice.py

# Example 7: Run Conditional Expressions & Loops practice
python condition_expression.py
python Range_example.py
python for_loops.py
```