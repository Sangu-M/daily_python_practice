# ==============================================================================
# Module: packin.py
# Topic: Sequence Packing — Explicit vs Implicit Tuple Packing
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Explicit / Manual Collection Packing
# • What is it for:
#   Bundling multiple literal values explicitly into a container using collection delimiters (e.g. `[]`).
# • What it does:
#   - Bundles `1, 2, 3` into list `a = [1, 2, 3]`.
#   - Prints the collection `[1, 2, 3]` and inspects its type `<class 'list'>`.
# • Where it is used:
#   Initializing dynamic lists, creating mutable collections from scratch.
# ------------------------------------------------------------------------------
# Explicit / Manual Packing
a = [1, 2, 3]
print(a)                                # Result: [1, 2, 3]
print(type(a))                          # Result: <class 'list'>

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Implicit / Automatic Tuple Packing
# • What is it for:
#   Automatically bundling comma-separated expressions into a single immutable tuple without parentheses.
# • What it does:
#   - Assigns `a = 1, 2, 3, 4`.
#   - Python implicitly creates a `tuple` containing `(1, 2, 3, 4)`.
#   - Prints `(1, 2, 3, 4)` and verifies type `<class 'tuple'>`.
# • Where it is used:
#   Returning multiple values from a function (`return x, y`), defining quick constant coordinate pairs.
# ------------------------------------------------------------------------------
# Implicit / Automatic Packing
a = 1, 2, 3, 4
print(a)                                # Result: (1, 2, 3, 4)
print(type(a))                          # Result: <class 'tuple'>
