# ==============================================================================
# Module: condition_expression.py
# Topic: Conditional Expressions (Ternary Operator in Python)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Inline Conditional Expression (Ternary Operator)
# • What is it for:
#   Providing a concise, one-line syntax for evaluating a condition and selecting
#   one of two values without requiring a full multi-line `if-else` statement.
# • What it does:
#   - Syntax formula: `value_if_true if condition else value_if_false`
#   - Reads an integer `n` from user input.
#   - Evaluates whether `n` is even (`n % 2 == 0`).
#   - If even, computes and returns `n ** 2` (square of n).
#   - If odd, computes and returns `n ** 3` (cube of n).
#   - Stores the evaluated outcome into variable `result` and prints it.
# • Where it is used:
#   Concise variable assignments, inline data transformations, list/dictionary
#   comprehensions, and return statements.
# ------------------------------------------------------------------------------
n = int(input())
result = n**2 if n%2==0 else n**3    # Result: n**2 if even, else n**3 (e.g., 4 -> 16, 3 -> 27)
print(result)                        # Outputs: 16 (for n=4) or 27 (for n=3)

print("-----------------------------------------------------")
