# ==============================================================================
# Module: forelseBlock.py
# Topic: The 'for-else' Loop Construct & Search Target Validation
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Linear Search with Target Absent (Triggering the 'else' Block)
# • What is it for:
#   Executing fallback logic when a search loop finishes its iteration without encountering 'break'.
# • What it does:
#   - Iterates through roll numbers `rlno = [21, 12, 19, 42, 47, 53, 35]`.
#   - Searches for target `n = 44`.
#   - Since 44 does not match any element in `rlno`, the `break` statement never executes.
#   - The `else:` block triggers automatically upon natural loop completion, printing "Not found".
# • Where it is used:
#   Clean searching algorithms without needing auxiliary boolean flag variables (e.g. `found = False`).
# ------------------------------------------------------------------------------
rlno = [21, 12, 19, 42, 47, 53, 35]
n = 44

for r in rlno:
    if r == n:
        print("Roll no found")
        break
else:
    print("Not found")                 # Result: "Not found" (no element matched, break was not hit)

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Linear Search with Target Present (Short-Circuiting the 'else' Block via 'break')
# • What is it for:
#   Halting the loop immediately upon finding a match and bypassing the `else:` branch entirely.
# • What it does:
#   - Searches for target `target = 42` in `rlno`.
#   - When `r == 42`, prints "Roll no found" and invokes `break`.
#   - Because `break` is encountered, the `else:` suite is completely bypassed.
# • Where it is used:
#   Database record lookup, membership confirmation, early exit on validation pass.
# ------------------------------------------------------------------------------
target = 42
for r in rlno:
    if r == target:
        print("Roll no found")          # Result: "Roll no found" (42 matched at index 3)
        break
else:
    print("Not found")

print("-------------------------------------------------")
