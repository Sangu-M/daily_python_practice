# ==============================================================================
# Module: practice05.py
# Topic: Nested Dictionaries & Entity Record Analytics
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Nested Dictionary Structure, Updates & Aggregations
# • What is it for:
#   Structuring real-world hierarchical datasets (such as company departments and employees)
#   using nested dictionaries, lists, and aggregating metrics (max, min, total).
# • What it does:
#   - Defines a nested dictionary of employees containing age, salary, and skills list.
#   - Traverses nested layers (`employees["Rahul"]["salary"]`, `employees["Priya"]["skills"][1]`).
#   - Updates inner nested values and dynamically inserts new employee entries (`"Sneha"`).
#   - Aggregates salaries into a list and determines highest and lowest earners via `max()`, `min()`,
#     and conditional matching.
#   - Calculates total payroll and uses dictionary view methods (`keys()`, `values()`, `pop()`).
# • Where it is used:
#   JSON payload processing, backend database schemas, employee/payroll management systems.
# ------------------------------------------------------------------------------
employees = {
    "Rahul": {
        "age": 25,
        "salary": 40000,
        "skills": ["Python", "SQL"]
    },
    "Priya": {
        "age": 27,
        "salary": 45000,
        "skills": ["Java", "SQL"]
    },
    "Arun": {
        "age": 24,
        "salary": 38000,
        "skills": ["Python", "HTML"]
    }
}

print(employees["Rahul"]["salary"])     # Result: 40000
print(employees["Priya"]["skills"][1])  # Result: SQL

employees["Arun"]["salary"] += 4000
print(employees["Arun"]["salary"])      # Result: 42000

employees["Sneha"] = {"age": 26, "salary": 50000, "skills": ["Python", "React"]}
print(employees)
employees["Rahul"]["salary"] += 5000

salaries = [
    employees["Arun"]["salary"],
    employees["Rahul"]["salary"],
    employees["Priya"]["salary"],
    employees["Sneha"]["salary"]
]
print(salaries)                         # Result: [42000, 45000, 45000, 50000]

highest = max(salaries)
lowest = min(salaries)

if employees["Rahul"]["salary"] == highest:
    print("Rahul")
elif employees["Priya"]["salary"] == highest:
    print("Priya")
elif employees["Arun"]["salary"] == highest:
    print("Arun")
elif employees["Sneha"]["salary"] == highest:
    print("Sneha")                      # Result: Sneha (highest salary: 50000)

if employees["Rahul"]["salary"] == lowest:
    print("Rahul")
elif employees["Priya"]["salary"] == lowest:
    print("Priya")
elif employees["Arun"]["salary"] == lowest:
    print("Arun")                       # Result: Arun (lowest salary: 42000)
elif employees["Sneha"]["salary"] == lowest:
    print("Sneha")    

total_salary = (
    employees["Rahul"]["salary"]
    + employees["Priya"]["salary"]
    + employees["Arun"]["salary"]
    + employees["Sneha"]["salary"]
)
print(total_salary)                     # Result: 182000

print("Priya" in employees)             # Result: True
print("Java" in employees["Priya"]["skills"])  # Result: True

print(employees.keys())                 # Result: dict_keys(['Rahul', 'Priya', 'Arun', 'Sneha'])
print(employees.values())
employees.pop("Arun")
print(employees)
