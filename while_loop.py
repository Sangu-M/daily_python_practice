# ==============================================================================
# Module: while_loop.py
# Topic: Condition-Controlled Iteration with 'while' Loops
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic 'while' Loop with Increment Counter
# • What is it for:
#   Executing a code block repeatedly as long as a boolean test condition remains True.
# • What it does:
#   - Initializes counter `i = 1`.
#   - Evaluates condition `i < 6` before each iteration cycle.
#   - Prints `i` and increments `i += 1` on each pass.
#   - Terminates when `i` reaches 6 (condition becomes False).
# • Where it is used:
#   Counting loops, polling conditions, repeating tasks until a state threshold is reached.
# ------------------------------------------------------------------------------
i = 1
while i < 6:
    print(i)                            # Result: prints 1, 2, 3, 4, 5 on separate lines
    i += 1

print("---------------------------------")

# ------------------------------------------------------------------------------
# 2. 'while' Loop with Non-Unit Step Increments
# • What is it for:
#   Advancing loop counter by custom step sizes (e.g., +3) across an arithmetic sequence.
# • What it does:
#   - Initializes `e = 2`.
#   - In each cycle, prints `e` and increments `e += 3`.
#   - Yields values: 2, 5, 8, 11, 14.
#   - Terminates when `e` increments to 17 (since 17 < 15 is False).
# • Where it is used:
#   Sampling data at regular intervals, pagination offsets, stepped numeric calculations.
# ------------------------------------------------------------------------------
e = 2
while e < 15:
    print(e)                            # Result: prints 2, 5, 8, 11, 14 on separate lines
    e += 3

print("---------------------------------")

# ------------------------------------------------------------------------------
# 3. 'while' Loop with Negative Starting Bound & Positive Stepping
# • What is it for:
#   Iterating upward from a negative integer bound toward a negative upper threshold.
# • What it does:
#   - Initializes `a = -14`.
#   - Checks condition `a < -1` before each cycle.
#   - Prints `a` and increments `a += 3`.
#   - Yields values: -14, -11, -8, -5, -2.
#   - Terminates when `a` becomes 1 (since 1 < -1 is False).
# • Where it is used:
#   Negative temperature ramps, coordinate progressions approaching origin, countdown offsets.
# ------------------------------------------------------------------------------
a = -14
while a < -1:
    print(a)                            # Result: prints -14, -11, -8, -5, -2 on separate lines
    a += 3

print("---------------------------------")
