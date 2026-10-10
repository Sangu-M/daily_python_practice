# ==============================================================================
# Module: nestedForLoop.py
# Topic: Nested 'for' Loops & Multi-Level Iteration
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Cartesian Product Combinations with Nested 'for' Loops
# • What is it for:
#   Generating all possible pairings (Cartesian product) between two independent sequences.
# • What it does:
#   - Outer loop iterates through each food item `i` in `l = ["Dosa", "Idli", "Puri"]`.
#   - For each food item, the inner loop iterates through all condiments `n` in `l1 = ["Chattni", "Sambar", "Saagu"]`.
#   - Prints every combination pair (3 x 3 = 9 combinations).
# • Where it is used:
#   Generating menu pairings, grid coordinate spaces, test case matrix generation, permutation pairs.
# ------------------------------------------------------------------------------
l = ["Dosa", "Idli", "Puri"]
l1 = ["Chattni", "Sambar", "Saagu"]
for i in l:
    for n in l1:
        print(i, n)                     # Result: Prints 9 combinations (Dosa Chattni ... Puri Saagu)

print("------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Generating Mathematical Multiplication Tables via Nested 'range()'
# • What is it for:
#   Iterating over multi-tier numerical sequences with outer and inner index ranges.
# • What it does:
#   - Outer loop iterates `i` through multipliers 6 to 8 using `range(6, 9)`.
#   - Inner loop iterates `j` through multiplicands 1 to 10 using `range(1, 11)`.
#   - Computes and prints the formatted equation `f"{i} X {j} = {i*j}"`.
# • Where it is used:
#   Displaying multiplication tables, 2D matrix coordinate computations, batch process iteration.
# ------------------------------------------------------------------------------
for i in range(6, 9):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")     # Result: Prints multiplication tables for 6, 7, and 8

print("------------------------------------------")

# ------------------------------------------------------------------------------
# 3. String Word Capitalization via Tokenization and Iteration
# • What is it for:
#   Splitting a multi-word sentence and transforming each word individually.
# • What it does:
#   - Splits string `s = "hello world"` into word tokens `['hello', 'world']`.
#   - Iterates through each word, applies `.capitalize()` to uppercase the first letter, and prints with a trailing space.
# • Where it is used:
#   Display name normalization, formatting book/article titles, custom text sanitization.
# ------------------------------------------------------------------------------
s = "hello world"
l = s.split()
print(l)                                # Result: ['hello', 'world']
for i in l:
    print(str(i.capitalize()), end=" ") # Result: Hello World 
print()

print("------------------------------------------")
