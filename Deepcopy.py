# ==============================================================================
# Module: Deepcopy.py
# Topic: Full Recursive Object Cloning via 'copy.deepcopy()'
# ==============================================================================

import copy

# ------------------------------------------------------------------------------
# 1. Deep Copy Creation via 'copy.deepcopy()'
# • What is it for:
#   Creating a completely independent, recursively cloned duplicate of an object and all its nested sub-objects.
# • What it does:
#   - Defines nested list `l1 = [10, 20, [30, 40]]`.
#   - Generates a deep clone `l2 = copy.deepcopy(l1)`.
#   - `l2` and all child elements are entirely distinct objects in memory (`l1[2] is not l2[2]`).
# • Where it is used:
#   Config state duplication, game state snapshots, undo/redo buffers for complex graphs.
# ------------------------------------------------------------------------------
l1 = [10, 20, [30, 40]]
l2 = copy.deepcopy(l1)                  # Deep copy: Fully recursive duplication
print(l2)                               # Result: [10, 20, [30, 40]]

# ------------------------------------------------------------------------------
# 2. Outer List Independence Under Mutation
# • What is it for:
#   Confirming that changes to outer elements in `l1` have no effect on `l2`.
# • What it does:
#   - Appends `50` to `l1`.
#   - `l1` becomes `[10, 20, [30, 40], 50]`, while `l2` remains `[10, 20, [30, 40]]`.
# • Where it is used:
#   Ensuring base template collections are untouched by worker threads.
# ------------------------------------------------------------------------------
l1.append(50)

print(l1)                               # Result: [10, 20, [30, 40], 50]
print(l2)                               # Result: [10, 20, [30, 40]]

print("-------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Nested Sub-List Independence (Mutating 'l2[2]')
# • What is it for:
#   Demonstrating that inner sub-lists are completely decoupled between copies.
# • What it does:
#   - Appends `60` to the nested list in `l2` via `l2[2].append(60)`.
#   - `l2[2]` becomes `[30, 40, 60]`, while `l1[2]` remains untouched as `[30, 40]`.
# • Where it is used:
#   Branching scenarios, modifying child elements safely without side effects.
# ------------------------------------------------------------------------------
l2[2].append(60)
print(l1)                               # Result: [10, 20, [30, 40], 50]
print(l2)                               # Result: [10, 20, [30, 40, 60]]

print("-------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Reverse Nested Independence (Mutating 'l1[2]')
# • What is it for:
#   Confirming bidirectional isolation between original and cloned nested structures.
# • What it does:
#   - Appends `1000` to `l1[2]`.
#   - `l1[2]` reflects `[30, 40, 1000]`, while `l2[2]` retains `[30, 40, 60]`.
# • Where it is used:
#   Guaranteeing 100% data integrity in multi-tenant or concurrent operations.
# ------------------------------------------------------------------------------
l1[2].append(1000)
print(l1)                               # Result: [10, 20, [30, 40, 1000], 50]
print(l2)                               # Result: [10, 20, [30, 40, 60]]
