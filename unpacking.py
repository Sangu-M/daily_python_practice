# ==============================================================================
# Module: unpacking.py
# Topic: Sequence Unpacking & Extended Iterable Unpacking with Asterisk '*'
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Exact 1-to-1 Sequence Unpacking
# • What is it for:
#   Distributing elements of an iterable directly into distinct individual variables.
# • What it does:
#   - Unpacks `[10, 20, 30]` into variables `a, b, c`.
#   - Each variable receives its corresponding positional element.
# • Where it is used:
#   Tuple assignment, multiple return value extraction, coordinate unpacking (`x, y = get_pos()`).
# ------------------------------------------------------------------------------
a, b, c = [10, 20, 30]
print(a)                                # Result: 10
print(b)                                # Result: 20
print(c)                                # Result: 30

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 2. Extended Unpacking with Asterisk '*' at the Beginning
# • What is it for:
#   Capturing leading variable-length items into a list while assigning trailing items to specific variables.
# • What it does:
#   - Unpacks `[10, 20, 30, 40, 50, 60, 70, 80]` into `*a, b, c, d`.
#   - `d` gets 80, `c` gets 70, `b` gets 60.
#   - `*a` collects the remaining leading elements into list `[10, 20, 30, 40, 50]`.
# • Where it is used:
#   Splitting sequences to extract fixed suffixes, parsing fixed-format tail records.
# ------------------------------------------------------------------------------
*a, b, c, d = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)                                # Result: [10, 20, 30, 40, 50]
print(b)                                # Result: 60
print(c)                                # Result: 70
print(d)                                # Result: 80

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. Extended Unpacking with Asterisk '*' in the Middle
# • What is it for:
#   Extracting fixed head and tail elements while gathering all intermediate values into a list.
# • What it does:
#   - Unpacks into `a, *b, c, d`.
#   - `a` gets 10, `c` gets 70, `d` gets 80.
#   - `*b` collects all intermediate elements into list `[20, 30, 40, 50, 60]`.
# • Where it is used:
#   Trimming headers and footers from data rows, parsing packets with fixed start/end flags.
# ------------------------------------------------------------------------------
a, *b, c, d = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)                                # Result: 10
print(b)                                # Result: [20, 30, 40, 50, 60]
print(c)                                # Result: 70
print(d)                                # Result: 80

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. Extended Unpacking with Asterisk '*' for Trailing/Internal Segments
# • What is it for:
#   Capturing specific front items and a single final item, grouping the remainder.
# • What it does:
#   - Unpacks into `a, b, *c, d`.
#   - `a` gets 10, `b` gets 20, `d` gets 80.
#   - `*c` collects the middle-to-end items into list `[30, 40, 50, 60, 70]`.
# • Where it is used:
#   Extracting identifiers and metadata from the front, payload in the middle, checksum at the end.
# ------------------------------------------------------------------------------
a, b, *c, d = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)                                # Result: 10
print(b)                                # Result: 20
print(c)                                # Result: [30, 40, 50, 60, 70]
print(d)                                # Result: 80

print("----------------------------------------")
