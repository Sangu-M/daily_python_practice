# ==============================================================================
# Module: practice07.py
# Topic: Nested Student Profile Management & Dictionary Utility Methods
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Multi-Level Dictionary Manipulation & Dictionary Methods
# • What is it for:
#   Working with deeply nested hierarchical entities (combining dictionaries, lists,
#   and primitives) and utilizing safe lookup (`get()`) and removal (`pop()`, `popitem()`).
# • What it does:
#   - Defines a `student` record with nested marks list and nested address dictionary.
#   - Updates nested fields: `student["address"]["city"] = "mysore"`.
#   - Appends to inner list: `student["skills"].append("git")`.
#   - Tests safe attribute retrieval using `.get("phone")` (returns `None` without crashing).
#   - Uses conditional insertion to set default key `"department"`.
#   - Demonstrates dictionary views: `.keys()`, `.values()`, `.items()`.
#   - Demonstrates removal via `.pop("experience")` and `.popitem()` (removes last inserted key-value pair).
#   - Empties entire dictionary using `.clear()`.
# • Where it is used:
#   Student Information Systems (SIS), document stores (MongoDB records), API payload mutation.
# ------------------------------------------------------------------------------
student = {
    "name": "Rahul",
    "age": 22,
    "marks": [78, 85, 92],
    "skills": ["Python", "SQL"],
    "address": {
        "city": "Bangalore",
        "state": "Karnataka"
    }
}

print(student["name"])                  # Result: Rahul
print(student["age"])                   # Result: 22

student["skills"].append("git")
student["age"] = 23
student["address"]['city'] = "mysore"
student["experience"] = 0
student["email"] = "rahul@gmail.com"

print(student.get("phone"))             # Result: None (safe lookup without KeyError)

if "department" not in student.keys():
    student["department"] = "computer science"

print(student.keys())
print(student.values())
print(student.items())
print(student["marks"][1])              # Result: 85

student.pop("experience")
student.popitem()                       # Removes last inserted item ('department')
print(student)

student.clear()
print(student)                          # Result: {}