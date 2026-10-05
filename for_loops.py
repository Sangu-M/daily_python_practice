# ==============================================================================
# Module: for_loops.py
# Topic: Iterating Over Sequences with 'for' Loops & Print Formatting
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Definite Iteration Over a List with Custom Separators & End Characters
# • What is it for:
#   Traversing sequence items one by one in order using Python's `for-in` loop,
#   paired with granular formatting controls via `sep` and `end`.
# • What it does:
#   - Defines a list of integers `l = [10, 20, 30, 40]`.
#   - The `for i in l:` statement iterates over each integer in the list sequentially.
#   - In each loop cycle, `print("Hello", i, end=" ", sep="/")` outputs:
#     - `"Hello"` and `i` joined by separator `"/"` (e.g., `"Hello/10"`).
#     - Ends the line with a trailing space `" "` rather than standard newline `\n`.
# • Where it is used:
#   Displaying batch records, processing collection elements, data serialization,
#   formatted terminal logs, and streaming console output without line breaks.
# ------------------------------------------------------------------------------
l = [10, 20, 30, 40]
for i in l:
    print("Hello", i, end=" ", sep="/")    # Result: Hello/10 Hello/20 Hello/30 Hello/40 
