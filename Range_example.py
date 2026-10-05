# ==============================================================================
# Module: Range_example.py
# Topic: The 'range()' Sequence Generator & Type Conversions
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Initializing 'range()' with (start, stop, step) & Type Inspection
# • What is it for:
#   Generating immutable, memory-efficient arithmetic progressions without storing
#   all sequence numbers in RAM at once.
# • What it does:
#   - `range(start, stop, step)` generates integers from `start` up to but excluding `stop`.
#   - `print(range_obj)` outputs the compact generator representation `range(1, 10)`.
#   - `type(range_obj)` confirms that range is a distinct built-in sequence type: `<class 'range'>`.
# • Where it is used:
#   Definite loop counts, memory-efficient indexing, sequence generation, batch pagination.
# ------------------------------------------------------------------------------
range_obj = range(1, 10, 1)
print(range_obj)                        # Result: range(1, 10) (lazy evaluation representation)
print(type(range_obj))                  # Result: <class 'range'>

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Single-Argument 'range(stop)' & Direct 'for' Loop Iteration
# • What is it for:
#   Running a block of code a fixed number of times using the default start (0) and step (1).
# • What it does:
#   - Calling `range(5)` sets `start=0`, `stop=5`, and `step=1`.
#   - In the `for i in range(5):` loop, `i` successively receives 0, 1, 2, 3, 4.
# • Where it is used:
#   Standard repeat counters, zero-based array indexing, iteration cycles.
# ------------------------------------------------------------------------------
nums = range(5)                         # Represents: 0, 1, 2, 3, 4
for i in range(5):
    print(i)                            # Result: prints 0, 1, 2, 3, 4 on separate lines

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Converting 'range' to Collection Data Types ('list', 'tuple', 'set', 'str')
# • What is it for:
#   Materializing lazy range values into accessible, in-memory data structures.
# • What it does:
#   - `list(range_obj)` evaluates and packs values into a mutable list.
#   - `tuple(range_obj)` packs values into an immutable tuple.
#   - `set(range_obj)` loads values into a deduplicated, unordered set.
#   - `str(range_obj)` returns string representation `'range(1, 10)'` (not expanded numbers).
# • Where it is used:
#   Creating predefined numeric datasets, generating test inputs, fast membership lookups.
# ------------------------------------------------------------------------------
l1 = list(range_obj)
print(l1)                               # Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("----------------------------------------------")

T1 = tuple(range_obj)
print(T1)                               # Result: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("----------------------------------------------")

s1 = set(range_obj)
print(s1)                               # Result: {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("----------------------------------------------")

S1 = str(range_obj)
print(S1)                               # Result: 'range(1, 10)' (string literal of range object)

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Edge Cases and Negative Bounds in 'range()'
# • What is it for:
#   Handling negative sequence bounds and non-unit step increments safely.
# • What it does:
#   - `range(-20)`: start defaults to 0 and step to +1. Because 0 > -20, it terminates
#     immediately, yielding an empty sequence `[]`.
#   - `range(-4, 5, 2)`: starts at -4 and steps by +2 up to 5, generating -4, -2, 0, 2, 4.
# • Where it is used:
#   Interval calculations spanning negative numbers, coordinate grids, reverse sequences.
# ------------------------------------------------------------------------------
r1 = range(-20)
l2 = list(r1)
print(l2)                               # Result: [] (empty list because start 0 > stop -20 with step +1)

print("----------------------------------------------")

print(list(range(-4, 5, 2)))            # Result: [-4, -2, 0, 2, 4]
