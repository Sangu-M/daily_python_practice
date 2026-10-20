# ==============================================================================
# Module: function4..py
# Topic: Arithmetic Calculation Functions & Value Returns
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Addition Function with Computation and Explicit Return
# • What is it for:
#   Performing arithmetic addition on two numeric inputs and returning the calculated sum.
# • What it does:
#   - Defines `add(num1, num2)` which adds `num1 + num2` into `result`.
#   - Returns `result` to the caller.
#   - `print(add(1, 2))` prints the debug message "adding numbers" and then prints returned `3`.
# • Where it is used:
#   Mathematical utilities, tallying shopping cart subtotals, accumulators.
# ------------------------------------------------------------------------------
print("-------------------------------------------------")
def add(num1, num2):
    print("adding numbers")
    result = num1 + num2
    return result

print(add(1, 2))                        # Result: Prints "adding numbers", then prints 3

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Subtraction Function with Negative Difference Handling
# • What is it for:
#   Computing the difference between two numerical operands and returning the evaluated value.
# • What it does:
#   - Defines `sub(num1, num2)` which calculates `num1 - num2`.
#   - `sub(1, 2)` computes `1 - 2 = -1` and returns it.
# • Where it is used:
#   Discount computations, calculating relative deltas or coordinates.
# ------------------------------------------------------------------------------
def sub(num1, num2):
    print("sub numbers")
    result = num1 - num2
    return result

print(sub(1, 2))                        # Result: Prints "sub numbers", then prints -1

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Compound Calculation Function Performing Multiple Operations
# • What is it for:
#   Executing multiple distinct mathematical calculations within a single cohesive function call.
# • What it does:
#   - Defines `cal(n1, n2)` calculating addition (`n1 + n2`), subtraction (`n1 - n2`), and multiplication (`n1 * n2`).
#   - Calling `cal(5, 3)` outputs 8, 2, and 15 respectively.
# • Where it is used:
#   Financial reporting suites, physics trajectory solvers, multi-metric telemetry summaries.
# ------------------------------------------------------------------------------
def cal(n1, n2):
    add_val = n1 + n2
    sub_val = n1 - n2
    mul_val = n1 * n2
    print(add_val)
    print(sub_val)
    print(mul_val)

cal(5, 3)                               # Result: Prints 8, 2, 15

print("-------------------------------------------------")
