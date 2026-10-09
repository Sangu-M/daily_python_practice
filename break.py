# ==============================================================================
# Module: break.py
# Topic: Terminating Loops Prematurely with 'break'
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Early Loop Termination via 'break' on Divisibility Condition
# • What is it for:
#   Immediately aborting the entire loop before it finishes all iterations of a sequence.
# • What it does:
#   - Iterates `i` over `range(4, 10)` (values 4, 5, 6, 7, 8, 9).
#   - For `i = 4, 5, 6`: `i % 7 != 0` is True, prints each value.
#   - For `i = 7`: `7 % 7 == 0`, enters `else:` branch and executes `break`.
#   - The loop halts immediately; values 7, 8, 9 are never processed.
# • Where it is used:
#   Halting execution upon finding a matching target, exiting on threshold breach, terminating infinite loops.
# ------------------------------------------------------------------------------
for i in range(4,10):
    if i%7!=0:
        print(i)                        # Result: prints 4, 5, 6
    else:
        break

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Terminating Collection Traversal Upon Encountering Negative Values
# • What is it for:
#   Stopping list iteration immediately once an invalid or sentinel element is detected.
# • What it does:
#   - Iterates through list `l = [23, 99, 74, -14, 32, 7]`.
#   - Checks `if i < 0:`.
#   - For 23, 99, 74: condition is False, prints each number.
#   - For -14: condition is True, triggers `break`, abruptly ending the loop.
#   - Subsequent items (32, 7) are skipped.
# • Where it is used:
#   Validating data streams, stopping upon detecting corrupt records or negative balances, circuit breakers.
# ------------------------------------------------------------------------------
l = [23,99,74,-14,32,7]
for i in l:
    if i<0:
        break
    print(i)                            # Result: prints 23, 99, 74
