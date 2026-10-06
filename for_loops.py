# ==============================================================================
# Module: for_loops.py
# Topic: Iterating Over Sequences with 'for' Loops & Step Ranges
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Definite Iteration Over a List with Trailing Formatting
# • What is it for:
#   Sequentially traversing each item of a mutable list from left to right.
# • What it does:
#   - Defines a list `l = [10, 20, 30, 40, 50]`.
#   - The `for i in l:` statement extracts each element into loop variable `i`.
#   - `print(i, end=" ")` outputs all elements separated by a space without newline.
# • Where it is used:
#   Processing list elements, printing inline sequences, record streaming.
# ------------------------------------------------------------------------------
l = [10, 20, 30, 40, 50]
for i in l:
    print(i, end=" ")                   # Result: 10 20 30 40 50 
print()

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Definite Count Repetition Using 'range(start, stop, step)'
# • What is it for:
#   Repeating an operation an exact number of times without maintaining a manual counter.
# • What it does:
#   - `range(1, 6, 1)` yields sequence values 1, 2, 3, 4, 5 (length 5).
#   - The loop runs exactly 5 times, printing `"hello"` on each iteration.
# • Where it is used:
#   Fixed-count loops, generating batch tasks, repetitive actions, retry logic.
# ------------------------------------------------------------------------------
# r = range(1,6,1)

for s in range(1, 6, 1):
    print("hello")                      # Result: prints "hello" 5 times on separate lines

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Negative Stepped Indexing into a List via 'range()'
# • What is it for:
#   Accessing list elements in reverse order with custom skips using negative indices.
# • What it does:
#   - `range(-1, -8, -2)` generates indices: -1, -3, -5, -7.
#   - `l1[n]` indexes from the end:
#     - `l1[-1] -> 80`
#     - `l1[-3] -> 60`
#     - `l1[-5] -> 40`
#     - `l1[-7] -> 20`
#   - Prints values with space separation.
# • Where it is used:
#   Reverse alternate sampling, backwards list traversal, stepping through time series data.
# ------------------------------------------------------------------------------
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
for n in range(-1, -8, -2):
    print(l1[n], end=" ")               # Result: 80 60 40 20 
print()

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Iterating Over an Immutable Tuple
# • What is it for:
#   Traversing values stored in an immutable sequence data structure (`tuple`).
# • What it does:
#   - Defines tuple `t = (11, 22, 33)`.
#   - The `for item in t:` loop accesses each tuple item without altering structure.
#   - `print(item, end=" ")` outputs all elements separated by space.
# • Where it is used:
#   Reading coordinates, database row records, constant reference configs.
# ------------------------------------------------------------------------------
t = (11, 22, 33)
for item in t:
    print(item, end=" ")                # Result: 11 22 33 
print()
