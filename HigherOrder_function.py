# ==============================================================================
# Module: HigherOrder_function.py
# Topic: Higher-Order Functions & Callback Function Invocations
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Higher-Order Function with Function Reference as Argument
# • What is it for:
#   Passing functions as arguments into other functions (callbacks), establishing
#   the foundation of functional programming and dynamic code execution.
# • What it does:
#   - Defines `conduct_mock(subject)` as a Higher-Order Function accepting a function reference `subject`.
#   - Prints the function object representation `subject` (shows function name and memory address).
#   - Calls `subject()` to invoke the passed callback function body.
#   - Defines candidate callbacks `python_exam()` and `java_exam()`.
#   - Invokes `conduct_mock(python_exam)` which executes `python_exam` inside `conduct_mock`.
# • Where it is used:
#   Event handlers, task schedulers, asynchronous callbacks, and middleware layers.
# ------------------------------------------------------------------------------
def conduct_mock(subject):              # Higher-order function (accepts function as parameter)
    print(subject)                      # Result: <function python_exam at 0x...>
    subject()                           # Invokes callback function


def python_exam():                      # Callback function
    print("python exam for 60 min")

def java_exam():                        # Candidate callback function
    print("java exam for 90 min")

# p = python_exam
# j = java_exam

conduct_mock(python_exam)               # Result: prints memory address and "python exam for 60 min"

print("-------------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Polymorphic Workflow Execution via Reusable Callback Runner
# • What is it for:
#   Creating generic execution runners that decouple high-level workflow orchestration
#   from specific task implementations.
# • What it does:
#   - Defines `full_bodyCheckup(test)` taking any diagnostic test function as argument.
#   - Invokes `test()` callback internally.
#   - Calls `full_bodyCheckup(blood_test)` to run the blood analysis routine.
#   - Calls `full_bodyCheckup(bp_test)` to run the blood pressure check routine.
# • Where it is used:
#   Automated testing frameworks (pytest/unittest), plugin architectures, and pipeline runners.
# ------------------------------------------------------------------------------
def full_bodyCheckup(test):             # Generic workflow runner
    test()


def blood_test():                       # Specific task routine 1
    print("your blood group is A")

def bp_test():                          # Specific task routine 2
    print("BP is normal")

full_bodyCheckup(blood_test)            # Result: "your blood group is A"
full_bodyCheckup(bp_test)               # Result: "BP is normal"
