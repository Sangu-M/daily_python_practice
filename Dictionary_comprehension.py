# ==============================================================================
# Module: Dictionary_comprehension.py
# Topic: Python Dictionary Comprehensions: Mapping, Slicing, Filtering & Ternary Logic
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Transformation Dictionary Comprehension
# Syntax: {key_expr: value_expr for var in iterable}
# • What is it for:
#   Creating brand-new dictionaries from any iterable in a single, fast, and
#   readable line without needing manual for-loops or empty dictionary initialization.
# • What it does:
#   - Iterates through numeric list `l = [10, 20, 30, 40]`.
#   - Maps each number `i` to its squared value `i**2`.
#   - Iterates through string list `l2` and maps each name to its string length `len(i)`.
# • Where it is used:
#   Building lookup tables, mapping IDs to computed values, frequency tables,
#   and fast key-value data indexing.
# • Key Takeaway:
#   Both key and value expressions are evaluated for every element in the source iterable.
# ------------------------------------------------------------------------------
# For transforming only
l = [10, 20, 30, 40]
d1 = {i: i**2 for i in l}  # Syntax for general {key_exp:value_exp for var in collection}
print(d1)                  # Result: {10: 100, 20: 400, 30: 900, 40: 1600}

print("-----------------------------------------------")

l2 = ["chatura", "hasaranga", "sangakara", "tharanga", "malinga"]
d2 = {i: len(i) for i in l2}
print(d2)                  # Result: {'chatura': 7, 'hasaranga': 9, 'sangakara': 9, 'tharanga': 8, 'malinga': 7}
# print(dict(i : len(i) for i in l2))

print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 2. String Slicing in Value Expressions (Length Offset vs Negative Step)
# Syntax: {var: var[len(var)-k:] for var in iterable} vs {var: var[-k::] for var in iterable}
# • What is it for:
#   Extracting substrings or suffix patterns directly into dictionary values during creation.
# • What it does:
#   - `d3` uses explicit length arithmetic `len(i)-3` as the start index to grab the last 3 chars.
#   - `d4` uses Python's idiomatic negative indexing `[-3::]` to grab the exact same suffix.
#   - Both yield identical dictionaries mapping names to their last 3 characters.
# • Where it is used:
#   Extracting file extensions (`filename: ext`), area codes, domain suffixes,
#   or trailing currency codes.
# • Key Takeaway:
#   Negative slicing `[-3:]` is more concise, readable, and avoids manual `len()` calculations.
# ------------------------------------------------------------------------------
d3 = {i: i[len(i)-3:] for i in l2}
print(d3)                  # Result: {'chatura': 'ura', 'hasaranga': 'nga', 'sangakara': 'ara', 'tharanga': 'nga', 'malinga': 'nga'}

print("-----------------------------------------------")

d4 = {i: i[-3::] for i in l2}
print(d4)                  # Result: {'chatura': 'ura', 'hasaranga': 'nga', 'sangakara': 'ara', 'tharanga': 'nga', 'malinga': 'nga'}

print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Filtering Dictionary Comprehensions with Trailing 'if' Clause
# Syntax: {key_expr: value_expr for var in iterable if boolean_condition}
# • What is it for:
#   Selecting and keeping only items that satisfy a specific condition, dropping
#   unwanted elements during dictionary construction.
# • What it does:
#   - `d5` filters numbers divisible by 4 (`i % 4 == 0`), squaring only 20 and 40.
#   - `d6 (1st)` filters strings ending with `"nga"` using `str.endswith("nga")`.
#   - `d6 (2nd)` filters strings containing substring `"ara"` using membership operator `in`.
# • Where it is used:
#   Filtering database rows, picking passing students, sanitizing configuration dictionaries.
# • Key Takeaway:
#   The trailing `if` acts as a gatekeeper; only elements evaluating to `True` become entries.
# ------------------------------------------------------------------------------
d5 = {i: i**2 for i in l if i % 4 == 0}
print(d5)                  # Result: {20: 400, 40: 1600}

print("-----------------------------------------------")

# 2nd syntax for filtering only
d6 = {i: len(i) for i in l2 if i.endswith("nga")}
print(d6)                  # Result: {'hasaranga': 9, 'tharanga': 8, 'malinga': 7}

print("-----------------------------------------------")

d6 = {i: len(i) for i in l2 if "ara" in i}
print(d6)                  # Result: {'hasaranga': 9, 'sangakara': 9, 'tharanga': 8}

print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Conditional Value Assignment with Ternary 'if - else' & Dict '.items()' Iteration
# Syntax: {key: (val_true if cond else val_false) for key, val in iterable_or_dict.items()}
# • What is it for:
#   Transforming values dynamically using inline decision logic (`Pass` vs `Fail`),
#   and processing existing dictionaries by inspecting both key and value simultaneously.
# • What it does:
#   - Evaluates marks list: numbers > 35 receive `'Pass'`, otherwise `'fail'`.
#   - Traverses `students.items()`: checks student score `val > 35` and assigns `'pass'` or `'fail'`.
# • Where it is used:
#   Grading systems, threshold tagging (e.g. `High` / `Low` risk), status mapping,
#   and ETL data reclassification pipelines.
# • Key Takeaway:
#   When using `if - else` (ternary), it MUST precede the `for` loop because it defines the value expression.
# ------------------------------------------------------------------------------
marks = [34, 89, 91, 46, 57, 9, 87]
result = {i: ("Pass" if i > 35 else "fail") for i in marks}
print(result)              # Result: {34: 'fail', 89: 'Pass', 91: 'Pass', 46: 'Pass', 57: 'Pass', 9: 'fail', 87: 'Pass'}

print("-----------------------------------------------")

students = {
    "jo": 72,
    "yo": 89,
    "lo": 25,
    "bo": 45
}

result1 = {key: ("pass" if val > 35 else "fail") for key, val in students.items()}
print(result1)             # Result: {'jo': 'pass', 'yo': 'pass', 'lo': 'fail', 'bo': 'pass'}

print("-----------------------------------------------")
