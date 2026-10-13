# ==============================================================================
# Module: Nested_Dictionary.py
# Topic: Nested Dictionaries & Hierarchical Key-Value Data Processing
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Nested Dictionary Structure & Key Traversal via '.keys()'
# • What is it for:
#   Organizing records hierarchically where each key maps to an inner sub-dictionary.
# • What it does:
#   - Defines `company` containing employee IDs (`emp1`, `emp2`, `emp3`) as primary keys.
#   - Iterates through `company.keys()` to display individual record identifiers.
# • Where it is used:
#   JSON API responses, hierarchical entity stores, database primary-key object caches.
# ------------------------------------------------------------------------------
company = {
    "emp1": {
        "name": "amy",
        "age": 23,
        "salary": 75000,
        "dept": "HR"
    },
    "emp2": {
        "name": "ben",
        "age": 48,
        "salary": 42000,
        "dept": "sales"
    },
    "emp3": {
        "name": "chad",
        "age": 33,
        "salary": 33000,
        "dept": "devolopment"
    }
}

print(company)                          # Result: Prints full nested dictionary structure

for e in company.keys():
    print(e)                            # Result: Prints "emp1", "emp2", "emp3"

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 2. Extracting Nested Dictionaries via '.values()'
# • What is it for:
#   Directly retrieving nested dictionary objects and indexing inner attributes.
# • What it does:
#   - Iterates over each inner dictionary `e` returned by `company.values()`.
#   - Prints the full inner dictionary, then accesses `e["name"]`.
# • Where it is used:
#   Deserializing nested payloads, processing document database collections.
# ------------------------------------------------------------------------------
for e in company.values():
    print(e)                            # Result: Prints each employee's full attribute dictionary
    print(e["name"])                    # Result: Prints "amy", "ben", "chad"

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 3. Accessing Inner Records via Dictionary Key Indexing
# • What is it for:
#   Iterating over outer keys and accessing inner dictionaries using standard bracket syntax.
# • What it does:
#   - Traverses default dictionary iterator (keys `e`).
#   - Accesses `company[e]` to fetch each nested sub-dictionary.
# • Where it is used:
#   Key-based dynamic lookup, updating nested records in place.
# ------------------------------------------------------------------------------
for e in company:
    print(company[e])                   # Result: Prints inner dictionary for each employee

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 4. Attribute Extraction & Specific Field Projections
# • What is it for:
#   Extracting single attributes (such as names or salaries) from nested structures.
# • What it does:
#   - Iterates through `company` and accesses `company[e]["name"]`.
#   - Iterates again and accesses `company[e]["salary"]`.
# • Where it is used:
#   Column projection, report generation, calculating payroll or roster listings.
# ------------------------------------------------------------------------------
for e in company:
    print(company[e]["name"])           # Result: Prints "amy", "ben", "chad"

print("---------------------------------------")

for e in company:
    print(company[e]["salary"])         # Result: Prints 75000, 42000, 33000

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 5. Multi-Condition Filtering on Nested Dictionary Attributes
# • What is it for:
#   Selecting specific entities matching multiple criteria across nested attributes.
# • What it does:
#   - Evaluates `company[e]["salary"] > 30000 and company[e]["dept"] == "sales"`.
#   - Finds `emp2` ("ben", salary 42000, dept "sales") and prints his name.
# • Where it is used:
#   Querying datasets, permission checks, HR filtering by department and compensation.
# ------------------------------------------------------------------------------
for e in company:
    if company[e]["salary"] > 30000 and company[e]["dept"] == "sales":
        print(company[e]["name"])       # Result: ben (Salary 42000 > 30000 and Dept is sales)

print("---------------------------------------")
