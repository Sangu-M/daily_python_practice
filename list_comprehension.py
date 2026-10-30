# ==============================================================================
# Module: list_comprehension.py
# Topic: Python List Comprehensions: Transformations, Filtering & Ternary Conditions
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Transformation List Comprehension ('[expr for item in iterable]')
# • What is it for:
#   Constructing new lists from existing iterables using concise, pythonic syntax
#   that executes significantly faster than manual `.append()` loops.
# • What it does:
#   - Defines source list `l = [10, 15, 20, 25]`.
#   - Evaluates `nl = [n**2 for n in l]`, squaring each element in-place.
#   - Produces transformed list: `[100, 225, 400, 625]`.
# • Where it is used:
#   Mathematical mapping, scaling arrays, type casting sequences in bulk.
# ------------------------------------------------------------------------------
l = [10, 15, 20, 25]

nl = [n**2 for n in l]                  # Unconditional expression evaluation
print(nl)                               # Result: [100, 225, 400, 625]

# ------------------------------------------------------------------------------
# 2. Filtering Comprehension with Trailing 'if' Clause
# • What is it for:
#   Filtering elements during list construction without needing an explicit `filter()` call.
# • What it does:
#   - Evaluates `nl1 = [n for n in l if n % 3 == 0]`: retains only items divisible by 3 -> `[15]`.
#   - Evaluates `nl2 = [n**2 for n in l if n % 10 == 0]`: filters items divisible by 10 (10, 20)
#     and squares them -> `[100, 400]`.
# • Where it is used:
#   Combining filter and map operations in a single readable, high-performance expression.
# ------------------------------------------------------------------------------
nl1 = [n for n in l if n % 3 == 0]       # Trailing if predicate
print(nl1)                              # Result: [15]

nl2 = [n**2 for n in l if n % 10 == 0]   # Filtering + transformation combined
print(nl2)                              # Result: [100, 400]

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Conditional Transformation with Ternary 'if - else' Expression
# • What is it for:
#   Applying branching transformation rules where every element is transformed based
#   on an inline condition (using `expr1 if cond else expr2`).
# • What it does:
#   - Defines list `l2 = [5, 10, 15, 20]`.
#   - If element is divisible by 10: compute square (`n**2`).
#   - Else: compute cube (`n**3`).
#   - For 5: cube = 125.
#   - For 10: square = 100.
#   - For 15: cube = 3375.
#   - For 20: square = 400.
# • Where it is used:
#   Conditional data cleaning, piecewise normalization, and value replacement flags.
# ------------------------------------------------------------------------------
l2 = [5, 10, 15, 20]

print([n**2 if n % 10 == 0 else n**3 for n in l2])
# Result: [125, 100, 3375, 400]
