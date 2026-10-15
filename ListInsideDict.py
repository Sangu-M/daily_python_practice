# ==============================================================================
# Module: ListInsideDict.py
# Topic: Row-Oriented Records (List of Dictionaries) & Directional Iteration
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Row-Oriented Record Collection (List of Dictionaries)
# • What is it for:
#   Organizing records where each row is an independent dictionary containing attribute fields.
# • What it does:
#   - Defines `company` as a list containing 3 employee dictionary objects.
#   - Iterates through `company` and prints each employee record.
# • Where it is used:
#   Standard format for REST API payloads, SQL query result sets, NoSQL document collections.
# ------------------------------------------------------------------------------
company = [
    {
        "name": "amy",
        "age": 23,
        "salary": 75000,
        "dept": "HR"
    },
    {
        "name": "ben",
        "age": 48,
        "salary": 42000,
        "dept": "sales"
    },
    {
        "name": "chad",
        "age": 33,
        "salary": 33000,
        "dept": "devolopment"
    }
]

print("------------------------------------------------")

for i in company:
    print(i)                            # Result: Prints each employee's dictionary record

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Extracting Specific Attributes from Each Record
# • What is it for:
#   Projecting a single key across all dictionary objects in the sequence.
# • What it does:
#   - Iterates through `company` and accesses `i["name"]`.
# • Where it is used:
#   Building dropdown selectors, name tags, customer ID listings.
# ------------------------------------------------------------------------------
for i in company:
    print(i["name"])                    # Result: Prints "amy", "ben", "chad"

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Reverse Record Traversal via Negative-Step 'range()'
# • What is it for:
#   Accessing list elements in reverse order without modifying the original collection.
# • What it does:
#   - Iterates backwards from index 2 down to 0 via `range(2, -1, -1)`.
#   - Prints names in reverse: "chad", "ben", "amy".
# • Where it is used:
#   Processing recent transactions first, reverse timeline feeds, undo history.
# ------------------------------------------------------------------------------
for i in range(2, -1, -1):
    print(company[i]["name"])           # Result: Prints "chad", "ben", "amy"

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Reverse Sequence Slicing '[::-1]'
# • What is it for:
#   Creating a newly reversed shallow copy of the record list using step slicing.
# • What it does:
#   - Evaluates `company[::-1]`, creating a reversed list containing `[chad_dict, ben_dict, amy_dict]`.
# • Where it is used:
#   Non-destructive list inversion, reverse order display.
# ------------------------------------------------------------------------------
print(company[::-1])                    # Result: Prints reversed list of employee dictionaries

print("------------------------------------------------")
