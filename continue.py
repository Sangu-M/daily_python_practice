# ==============================================================================
# Module: continue.py
# Topic: Skipping Iterations with 'continue'
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Skipping Iterations Based on Divisibility ('or' Logical Condition)
# • What is it for:
#   Bypassing the remaining statements of the current loop cycle and immediately
#   advancing to the next iteration without terminating the entire loop.
# • What it does:
#   - Iterates `i` from 11 through 49 using `range(11, 50, 1)`.
#   - Checks `if i % 5 == 0 or i % 7 == 0:`.
#   - If True, executes `continue`, skipping `print(i)` and jumping to the next number.
#   - Multiples of 5 (15, 20, 25, 30, 35, 40, 45) and 7 (14, 21, 28, 35, 42, 49) are skipped.
# • Where it is used:
#   Filtering out unwanted numeric values, skipping invalid records, leap-frog processing.
# ------------------------------------------------------------------------------
print("----------------------------------------------------")

print("start")
for i in range(11,50,1):
    if i%5==0 or i%7==0:
        continue
    print(i)                            # Result: prints numbers between 11-49 not divisible by 5 or 7
print("stop")

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Filtering Negative Numbers from a List Traversal
# • What is it for:
#   Skipping negative or invalid items in a list while continuing to process positive items.
# • What it does:
#   - Iterates through `l = [23, 99, 74, -14, 32, 7, -3, -100]`.
#   - Evaluates `if i < 0:`.
#   - If negative (-14, -3, -100), `continue` skips the print statement.
#   - Only non-negative numbers (23, 99, 74, 32, 7) are printed.
# • Where it is used:
#   Data cleaning, filtering out negative values (e.g., negative prices, corrupted sensor data).
# ------------------------------------------------------------------------------
l = [23,99,74,-14,32,7,-3,-100]
for i in l:
    if i<0:
        continue
    print(i)                            # Result: prints 23, 99, 74, 32, 7
print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Filtering Strings with Prefix Matching ('str.startswith()')
# • What is it for:
#   Skipping string elements that start with a specific substring or title.
# • What it does:
#   - Iterates through `names` list.
#   - Evaluates `if name.startswith("Mrs"):`.
#   - If True ("MrsRao", "MrsAdithi", "MrsAmy"), skips printing via `continue`.
#   - Prints only non-matching names ("MrSmith", "MrJohn", "KrGanesh").
# • Where it is used:
#   Categorization filtering, ignoring specific file extensions, excluding user prefixes or tags.
# ------------------------------------------------------------------------------
names = ["MrSmith","MrsRao","MrJohn","MrsAdithi","MrsAmy","KrGanesh"]
for name in names:
    if name.startswith("Mrs"):
        continue
    print(name)                         # Result: prints "MrSmith", "MrJohn", "KrGanesh"
print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Filtering Strings Containing Substrings via Membership Operator ('in')
# • What is it for:
#   Skipping strings that contain specific characters or letters (case-insensitive check).
# • What it does:
#   - Iterates through `names` list.
#   - Evaluates `if "a" in name or "A" in name:`.
#   - Skips names containing lowercase 'a' or uppercase 'A' ("MrsRao", "MrsAdithi", "MrsAmy", "KrGanesh").
#   - Prints only names without 'a' or 'A': "MrSmith", "MrJohn".
# • Where it is used:
#   Search filters, keyword blacklists, sanitizing inputs, character screening.
# ------------------------------------------------------------------------------
names = ["MrSmith","MrsRao","MrJohn","MrsAdithi","MrsAmy","KrGanesh"]
for name in names:
    if "a" in name or "A" in name:
        continue
    print(name)                         # Result: prints "MrSmith", "MrJohn"

print("----------------------------------------------------")
