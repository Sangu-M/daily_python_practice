# ==============================================================================
# Module: ReduceFunction.py
# Topic: 'functools.reduce()' Aggregation & Chained Functional Pipelines ('filter' + 'map')
# ==============================================================================

from functools import reduce

# ------------------------------------------------------------------------------
# 1. Cumulative Sequence Reduction with 'functools.reduce()'
# • What is it for:
#   Applying a function of two arguments cumulatively to the items of an iterable
#   from left to right, collapsing the entire sequence into a single scalar value.
# • What it does:
#   - Imports `reduce` from the standard `functools` module.
#   - Defines list `l = [2, 4, 6, 8, 10]`.
#   - Cumulative sum: `(((2 + 4) + 6) + 8) + 10 = 30`.
#   - Cumulative product: `(((2 * 4) * 6) * 8) * 10 = 3840`.
#   - Cumulative string concatenation across `l1`: `"todayisfriday"`.
# • Where it is used:
#   Computing factorials, running totals, GCD across lists, and custom folding algorithms.
# ------------------------------------------------------------------------------
l = [2, 4, 6, 8, 10]
print(int(reduce(lambda a, b: a + b, l)))     # Result: 30 (Cumulative addition)

print(int(reduce(lambda a, b: a * b, l)))     # Result: 3840 (Cumulative multiplication)

l1 = ["today", "is", "friday"]
print(str(reduce(lambda a, b: a + b, l1)))    # Result: todayisfriday (String reduction)

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Comparative Approaches: Imperative Loop vs Multi-Step vs Chained Pipeline
# • What is it for:
#   Comparing traditional imperative loops against functional pipeline decomposition
#   and inline nested functional compositions (`map(..., filter(...))`).
# • What it does:
#   - Approach A (Imperative Loop): Iterates over `l2 = [2, 3, 4, 5, 6, 7, 8]`, checks `i % 2 == 0`,
#     squares it, and appends to `l3`: `[4, 16, 36, 64]`.
#   - Approach B (Two-Stage Functional): First filters even numbers into `l4`, then maps squares.
#   - Approach C (Chained One-Liner): Feeds `filter(...)` directly into `map(...)` without intermediate lists.
# • Where it is used:
#   Refactoring bulky conditional loops into declarative functional data streams.
# ------------------------------------------------------------------------------
l2 = [2, 3, 4, 5, 6, 7, 8]

# Approach A: Traditional imperative for loop with condition
l3 = []
for i in l2:
    if i % 2 == 0:
        s = i**2
        l3.append(s)
print(l3)                               # Result: [4, 16, 36, 64]

print("--------------------------------------------------")

# Approach B: Explicit two-step filter then map
l4 = list(filter(lambda i: i % 2 == 0, l2))
print(list(map(lambda n: n**2, l4)))     # Result: [4, 16, 36, 64]

print("--------------------------------------------------")

# Approach C: Streamlined nested functional pipeline
print(list(map(lambda n: n**2, filter(lambda i: i % 2 == 0, l2))))
# Result: [4, 16, 36, 64]
