# ==============================================================================
# Module: Dictionary_list.py
# Topic: Columnar Data Layout (Dictionary Containing Lists) & Cross-Field Filtering
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Columnar Data Structure & Key Traversal
# • What is it for:
#   Representing structured tabular datasets where each dictionary key is a column name and the value is a list of column values.
# • What it does:
#   - Defines `employess` containing columnar fields: "names", "ages", "salaries", "dept".
#   - Iterates through the keys of the dictionary and prints each column header.
# • Where it is used:
#   Data science dataframe representations (e.g. Pandas `DataFrame` dictionary constructor), CSV parsers.
# ------------------------------------------------------------------------------
employess = {
    "names": ["Amy", "Ben", "Chad"],
    "ages": [23, 78, 41],
    "salaries": [70000, 42000, 24000],
    "dept": ["Sales", "HR", "Market"]
}

for i in employess:
    print(i)                            # Result: Prints "names", "ages", "salaries", "dept"

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 2. Extracting Complete Column Value Lists
# • What is it for:
#   Accessing entire series of column data for statistical calculations or serialization.
# • What it does:
#   - Iterates through `employess` keys and prints each column's list.
# • Where it is used:
#   Aggregating statistics (mean, median, sum) on specific columns.
# ------------------------------------------------------------------------------
for i in employess:
    print(employess[i])                 # Result: Prints ['Amy', 'Ben', 'Chad'], [23, 78, 41], etc.

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 3. Accessing the First Element Across All Columns
# • What is it for:
#   Inspecting top-of-file sample records (equivalent to `.head(1)` in data analysis).
# • What it does:
#   - Accesses index `0` of each column list (`employess[i][0]`).
# • Where it is used:
#   Previewing the first row across all tabular columns.
# ------------------------------------------------------------------------------
for i in employess:
    print(employess[i][0])              # Result: Prints "Amy", 23, 70000, "Sales"

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 4. Cross-Column Index-Based Querying & Dynamic Length Bounds
# • What is it for:
#   Correlating values across parallel lists at identical row indices.
# • What it does:
#   - First uses `range(3)` to check `if employess["ages"][i] > 40: print(employess["names"][i])`.
#   - Next uses dynamic bounds `range(len(employess["ages"]))` for robust scaling with any dataset size.
#   - Filters employees older than 40: "Ben" (78) and "Chad" (41).
# • Where it is used:
#   Relational record querying, column matching, generating notification lists.
# ------------------------------------------------------------------------------
for i in range(3):
    if employess["ages"][i] > 40:
        print(employess["names"][i])     # Result: Ben, Chad (Hardcoded range(3))

for i in range(len(employess["ages"])):
    if employess["ages"][i] > 40:
        print(employess["names"][i])     # Result: Ben, Chad (Dynamic range based on list length)

print("--------------------------------------")
