# ==============================================================================
# Module: practice03.py
# Topic: In-Place List Mutation Methods ('append', 'insert', 'pop', 'reverse', 'sort')
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Mutating Lists: In-Place Modifications vs Returning New Objects
# • What is it for:
#   Building, modifying, reordering, and querying elements in a dynamic list structure.
# • What it does:
#   - Initializes `numbers = [10, 20, 30]`.
#   - `.append(val)` appends elements to the end in-place.
#   - `.insert(index, val)` inserts elements at specific positions in-place.
#   - `.pop()` removes and returns the last element.
#   - `.index(val)` and `.count(val)` query position and frequency.
#   - `.reverse()` and `.sort()` reorder elements in-place (they return `None`).
# • Where it is used:
#   Data preparation, sorting algorithms, queue/stack operations, list restructuring.
# ------------------------------------------------------------------------------
numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)

numbers.insert(0, 5)
numbers.insert(2, 15)
numbers.pop()                           # Removes 50

print(numbers.index(20))                # Result: 3
print(numbers.count(10))                # Result: 1

numbers.reverse()
print(numbers)                          # Result: [40, 30, 20, 15, 10, 5]

numbers.sort()
print(numbers)                          # Result: [5, 10, 15, 20, 30, 40]

# ------------------------------------------------------------------------------
# Educational Concept Note: In-Place Methods vs Built-in Functions
# • Creating vs Modifying:
#   - In-place methods (e.g. `list.sort()`, `list.reverse()`) mutate the existing list
#     directly in memory and intentionally return `None`. If you write `x = numbers.sort()`,
#     `x` will be `None`!
#   - Functions that produce new collections (e.g. `sorted()`, `list()`) leave the original
#     untouched and return a brand new list.
# • `sort()` vs `sorted()`:
#   - `list.sort()` is a list method that sorts any list in-place (numbers, strings, etc.).
#   - `sorted(iterable)` is a built-in function that works on any iterable (strings, tuples, sets, dicts)
#     and returns a new sorted list.
# ------------------------------------------------------------------------------
