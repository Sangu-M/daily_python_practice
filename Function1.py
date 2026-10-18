# ==============================================================================
# Module: Function1.py
# Topic: Function Definition, Invocation, Return Values & Execution Flow
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Function Declaration, 'pass' Placeholder & Function Object vs Call
# • What is it for:
#   Defining reusable blocks of code using the `def` keyword and understanding the difference between function objects and invocations.
# • What it does:
#   - Defines `display()` with `pass` as an empty syntactic placeholder.
#   - Defines `display1()` that prints a message.
#   - `print(display1)` prints the function's memory representation (`<function display1 at 0x...>`).
#   - `display1()` executes the body and prints "This is display function".
# • Where it is used:
#   Structuring modular code, passing functions as first-class citizens/callbacks.
# ------------------------------------------------------------------------------
def display():
    pass

def display1():
    print("This is display function")

print(display1)                        # Result: <function display1 at 0x...> (Function memory object)
display1()                              # Result: "This is display function" (Function execution)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Reusability: Invoking Functions Multiple Times
# • What is it for:
#   Eliminating code duplication by packaging repetitive logic into callable functions.
# • What it does:
#   - Defines `wish()` which prints "Happy Birthday!!".
#   - Calls `wish()` twice sequentially.
# • Where it is used:
#   Notification senders, status alerts, repetitive UI updates.
# ------------------------------------------------------------------------------
def wish():
    print("Happy Birthday!!")

wish()                                  # Result: Happy Birthday!!
wish()                                  # Result: Happy Birthday!!

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Returning Values from Functions with 'return'
# • What is it for:
#   Passing computed data back to the caller for assignment or further processing.
# • What it does:
#   - Defines `get_number()` which prints a status message and returns the integer `333`.
#   - `var = get_number()` captures the returned value `333`.
#   - `print(get_number())` prints both the side-effect output and the evaluated return value.
#   - `get_number()` calls the function without storing the return value.
# • Where it is used:
#   Data retrieval functions, calculation formulas, database queries.
# ------------------------------------------------------------------------------
def get_number():
    print("function Execution")
    return 333

var = get_number()                      # Calls function, assigns 333 to var
print(var)                              # Result: 333

print(get_number())                     # Prints "function Execution", then prints 333
get_number()                            # Prints "function Execution" (return value discarded)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Premature Exit via 'return' & Unreachable (Dead) Code
# • What is it for:
#   Understanding that `return` immediately terminates function execution and hands control back.
# • What it does:
#   - Defines `get()` with `return 333` followed by `print("Hello world")` and `return 3.14`.
#   - Once `return 333` executes, the function exits immediately; subsequent statements are dead code and never run.
# • Where it is used:
#   Guard clauses, early exits on validation failures.
# ------------------------------------------------------------------------------
def get():
    print("function Execution")
    return 333
    print("Hello world")                # Unreachable dead code (never executed)
    return 3.14                         # Unreachable dead code (never executed)

print(get())                            # Result: Prints "function Execution", then prints 333

print("------------------------------------------------")
