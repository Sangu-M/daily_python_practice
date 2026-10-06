# ==============================================================================
# Module: practice 04.py
# Topic: Set Operations, Set Relations & Mathematical Set Methods
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Set Mutation, Relational Tests & Mathematical Set Operations
# • What is it for:
#   Performing unique collection operations, relational checks (subset, superset, disjoint),
#   and mathematical set combinations (union, intersection, difference, symmetric difference).
# • What it does:
#   - Adds elements with `.add()`, removes with `.remove()`, and pops an arbitrary element with `.pop()`.
#   - Tests relations with `.isdisjoint()`, `.issubset()`, and `.issuperset()`.
#   - Computes set operations:
#     - `intersection()`: common elements.
#     - `difference()`: elements in left set but not in right set.
#     - `symmetric_difference()`: elements in either set, but not in both.
#     - `union()`: all unique elements combined across both sets.
#   - Clears set with `.clear()`.
# • Where it is used:
#   Filtering duplicates, relational queries, permission comparisons, category intersections.
# ------------------------------------------------------------------------------
numbers = {10, 20, 30}
other_numbers = {20, 30, 40, 50}

numbers.add(60)
numbers.add(70)
numbers.add(80)
numbers.remove(10)
numbers.pop()                           # Removes an arbitrary element (e.g. 70)

print(numbers.isdisjoint(other_numbers))   # Result: False (shares elements {20, 30})
print(numbers.issubset(other_numbers))     # Result: False
print(numbers.issuperset(other_numbers))   # Result: False

s1 = numbers.intersection(other_numbers)
s2 = numbers.difference(other_numbers)
s3 = numbers.symmetric_difference(other_numbers)
s4 = numbers.union(other_numbers)
s5 = {20, 30}.issubset(numbers)
s6 = numbers.issuperset({20, 30})

print(s1)                               # Result: {20, 30}
print(s2)                               # Result: {80, 60}
print(s3)                               # Result: {40, 80, 50, 60}
print(s4)                               # Result: {40, 80, 50, 20, 60, 30}
print(s5)                               # Result: True
print(s6)                               # Result: True

numbers.clear()
print(numbers)                          # Result: set()

a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))                  # Result: True (no common elements)
