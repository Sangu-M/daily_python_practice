# ==============================================================================
# Module: filterFunction.py
# Topic: Built-in 'filter()' Function & Boolean Predicate Filtering
# ==============================================================================

print("--------------------------------------------------")

'''
# Background comparison with manual filtering loop:
def convert(fun, *col):
    n = []
    for i in col:
        if i % 2 == 0:
            result = fun(i)
            n.append(result)
    return n
'''

# ------------------------------------------------------------------------------
# 1. Numeric Filtering with Modulo Boolean Predicates
# • What is it for:
#   Selecting elements from a collection that satisfy a boolean condition (predicate),
#   discarding all items where the predicate returns False.
# • What it does:
#   - Defines list `l = [1, 2, 3, 4]`.
#   - Predicate lambda `lambda n: n % 2 == 0` tests for even numbers.
#   - Built-in `filter()` lazily yields only matching items.
#   - Casts to `list` producing `[2, 4]`.
# • Where it is used:
#   Data pruning, extracting valid records, removing invalid IDs or null values.
# ------------------------------------------------------------------------------
l = [1, 2, 3, 4]

print(list(filter(lambda n: n % 2 == 0, l)))  # Result: [2, 4]

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. String Filtering by Length & Substring Membership (Case Sensitivity)
# • What is it for:
#   Filtering text collections based on character length thresholds and substring queries.
# • What it does:
#   - Defines string list `l1 = ["Alex", "Carrison", "Richard", "Zaraki", "Gengistu"]`.
#   - `lambda i: len(i) > 6` filters strings with length > 6: `('Carrison', 'Richard', 'Gengistu')`.
#   - `lambda i: "A" in i or "a" in i` checks for 'A' or 'a' using boolean `or`.
#   - `lambda i: "a" in i.lower()` accomplishes the same check idiomatically via `.lower()`.
#   - Both yield: `('Alex', 'Carrison', 'Richard', 'Zaraki')`.
# • Where it is used:
#   Search query auto-complete, keyword matching, and password complexity criteria.
# ------------------------------------------------------------------------------
l1 = ["Alex", "Carrison", "Richard", "Zaraki", "Gengistu"]

print(tuple(filter(lambda i: len(i) > 6, l1)))
# Result: ('Carrison', 'Richard', 'Gengistu')

print(tuple(filter(lambda i: "A" in i or "a" in i, l1)))
# Result: ('Alex', 'Carrison', 'Richard', 'Zaraki')

print(tuple(filter(lambda i: "a" in i.lower(), l1)))
# Result: ('Alex', 'Carrison', 'Richard', 'Zaraki') (idiomatic case-insensitive match)

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Quick Review: Dictionary Item Removal ('popitem()' vs 'pop()')
# Syntax: dict.popitem() | dict.pop(key)
# • What is it for:
#   Removing key-value pairs from dictionaries: removing the last inserted item
#   via LIFO order with `popitem()` or targeting a specific key via `pop(key)`.
# • What it does:
#   - Defines dictionary `d = {10: 1, 20: 2, 30: 3}`.
#   - `d.popitem()` removes and returns the last (key, value) tuple: `(30, 3)`.
#   - `d.pop(10)` removes key 10 and returns its mapped value: `1`.
#   - Remaining dictionary is `{20: 2}`.
# • Where it is used:
#   Undo operations, cache eviction, and processing work queues stored in dictionaries.
# • Key Takeaway:
#   `popitem()` removes the last item and returns a `(key, value)` tuple; `pop(k)` returns only the value.
# ------------------------------------------------------------------------------
d = {
    10: 1,
    20: 2,
    30: 3
}
print(d.popitem())  # Result: (30, 3) (removes last inserted key-value pair as a tuple)
print(d.pop(10))    # Result: 1 (removes key 10 and returns its associated value)
print(d)            # Result: {20: 2} (remaining dictionary)

