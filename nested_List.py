# ==============================================================================
# Module: nested_List.py
# Topic: Nested Lists (2D Lists) & Multi-Attribute Record Traversals
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Multi-Attribute Record Filtering in 2D Lists
# • What is it for:
#   Filtering nested list records based on conditions applied to specific column indices.
# • What it does:
#   - Defines `employees` as a 2D list where each inner list represents `[Name, Age, Salary]`.
#   - Iterates through each record `e`.
#   - Checks if age `e[1] > 32` and salary `e[2] < 64000`.
#   - Identifies "Zlatan" (age 33, salary 25000) and prints his name.
# • Where it is used:
#   Processing matrix data, in-memory tabular datasets, CSV row parsing without external libraries.
# ------------------------------------------------------------------------------
employees = [["Amy", 23, 40000], ["Ben", 48, 78000], ["Zlatan", 33, 25000]]

for e in employees:
    if e[1] > 32 and e[2] < 64000:
        print(e[0])                     # Result: Zlatan (Age 33 > 32 and Salary 25000 < 64000)

print("------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Reverse Row Traversal Using Negative-Step 'range()'
# • What is it for:
#   Accessing nested records from last to first using indexed looping.
# • What it does:
#   - Generates indices 2, 1, 0 using `range(2, -1, -1)`.
#   - Accesses `employees[i][0]` to print names in reverse: "Zlatan", "Ben", "Amy".
# • Where it is used:
#   Stack processing, reversing tabular outputs, reverse chronological log processing.
# ------------------------------------------------------------------------------
for i in range(2, -1, -1):
    print(employees[i][0])              # Result: Prints "Zlatan", "Ben", "Amy"

print("------------------------------------------")
