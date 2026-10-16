# ==============================================================================
# Module: Generalcopy.py
# Topic: Variable Aliasing & Reference Assignment (General Copy)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Reference Assignment / Variable Aliasing ('l2 = l1')
# • What is it for:
#   Binding multiple variable names to the exact same object in memory.
# • What it does:
#   - Defines list `l1 = [10, 20, [30, 40]]`.
#   - Assigns `l2 = l1`. No new list object is created; `l2` and `l1` point to the identical memory address (`id(l1) == id(l2)`).
#   - Prints `l2`, showing the initial contents.
# • Where it is used:
#   Passing object references to functions, sharing live mutable state across components.
# ------------------------------------------------------------------------------
l1 = [10, 20, [30, 40]]
l2 = l1                                 # General copy (Reference aliasing)
print(l2)                               # Result: [10, 20, [30, 40]]

# ------------------------------------------------------------------------------
# 2. Outer List Mutation Mutates Both Variables
# • What is it for:
#   Demonstrating that modifying the object through one reference affects all references.
# • What it does:
#   - Appends `50` to `l1`.
#   - Because `l1` and `l2` point to the same list in memory, both `l1` and `l2` reflect the addition of `50`.
# • Where it is used:
#   Understanding reference side effects and unexpected data mutation bugs.
# ------------------------------------------------------------------------------
l1.append(50)

print(l1)                               # Result: [10, 20, [30, 40], 50]
print(l2)                               # Result: [10, 20, [30, 40], 50]

print("-------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Nested List Mutation via Aliased Reference
# • What is it for:
#   Demonstrating that mutating nested mutable elements via either alias modifies both.
# • What it does:
#   - Appends `60` to the nested list at index 2 using `l2[2].append(60)`.
#   - Both `l1` and `l2` display the updated nested list `[30, 40, 60]`.
# • Where it is used:
#   Shared data models, cache instances, event buses.
# ------------------------------------------------------------------------------
l2[2].append(60)
print(l1)                               # Result: [10, 20, [30, 40, 60], 50]
print(l2)                               # Result: [10, 20, [30, 40, 60], 50]

print("-------------------------------------------")
