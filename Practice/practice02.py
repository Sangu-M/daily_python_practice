# ==============================================================================
# Module: practice02.py
# Topic: Employee Record Manipulation with Python Dictionaries
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Dictionary CRUD Operations & Nested List Updates
# • What is it for:
#   Managing structured entity records (like an employee profile) with key-value pairs,
#   in-place updates, nested list manipulation, and key membership testing.
# • What it does:
#   - Defines dictionary `employee` with string, integer, and list fields.
#   - Reads values by key (`employee["name"]`, `employee["department"]`).
#   - Appends items to the nested skills list (`"git"`, `"docker"`).
#   - In-place increments numeric fields (`salary += 5000`).
#   - Adds new key `'exp'`, checks membership (`'Python' in ...`), tests ternary conditions,
#     and removes keys using `.pop()`.
# • Where it is used:
#   User profile management, database record mapping, configuration data modeling.
# ------------------------------------------------------------------------------
employee = {
    "name": "Rahul",
    "age": 28,
    "department": "IT",
    "skills": ["Python", "SQL"],
    "salary": 45000
}

print(employee["name"])                 # Result: Rahul
print(employee["department"])           # Result: IT

employee["skills"].append("git")
employee["skills"].append("docker")
print(employee["skills"])               # Result: ['Python', 'SQL', 'git', 'docker']

employee["salary"] += 5000
print(employee["salary"])               # Result: 50000

employee['exp'] = 3
print('Python' in employee["skills"])   # Result: True
print('Java' in employee["skills"])     # Result: False
print(len(employee["skills"]))          # Result: 4

print(employee["age"] if employee["age"] > employee["exp"] else employee["exp"])  # Result: 28

employee.pop("age")
print(employee)                         # Result: {'name': 'Rahul', 'department': 'IT', 'skills': ['Python', 'SQL', 'git', 'docker'], 'salary': 50000, 'exp': 3}
print(len(employee))                    # Result: 5