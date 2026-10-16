# ==============================================================================
# Module: Shallowcopy.py
# Topic: Shallow Copying via 'copy.copy()' — Isolation vs Nested Reference Sharing
# ==============================================================================

import copy

# ------------------------------------------------------------------------------
# 1. Shallow Copy Creation & Outer List Independence (The Advantage)
# • What is it for:
#   Creating a new container object while populating it with references to the child elements.
# • What it does:
#   - Defines nested list `l1 = [10, 20, [30, 40]]`.
#   - Creates a shallow copy `l2 = copy.copy(l1)` (creates a new outer list object).
#   - Appends `50` to `l1`.
#   - `l1` has 4 elements `[10, 20, [30, 40], 50]`, while `l2` remains unaffected `[10, 20, [30, 40]]`.
# • Where it is used:
#   Duplicating flat lists, creating independent collections where elements are immutable.
# ------------------------------------------------------------------------------
l1 = [10, 20, [30, 40]]
l2 = copy.copy(l1)

l1.append(50)                           # Advantage: Mutating outer list does not affect l2

print(l1)                               # Result: [10, 20, [30, 40], 50]
print(l2)                               # Result: [10, 20, [30, 40]]

print("-------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Shared Nested References in Shallow Copies (The Limitation)
# • What is it for:
#   Understanding that inner nested mutable objects are NOT recursively cloned in a shallow copy.
# • What it does:
#   - Appends `60` to the nested list via `l2[2].append(60)`.
#   - Because `l1[2]` and `l2[2]` point to the exact same inner list in memory, both reflect `[30, 40, 60]`.
# • Where it is used:
#   Recognizing why `copy.copy()` or list slicing `[:]` fails when working with nested structures.
# ------------------------------------------------------------------------------
l2[2].append(60)                        # Limitation: Inner list is shared between l1 and l2

print(l1)                               # Result: [10, 20, [30, 40, 60], 50]
print(l2)                               # Result: [10, 20, [30, 40, 60]]

print("-------------------------------------------")
