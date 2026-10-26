# ==============================================================================
# Module: enclosing_vriable.py
# Topic: Enclosing Scope, Nonlocal Variables & State Retention in Nested Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Mutating Enclosing Scope Variables Using the 'nonlocal' Keyword
# • What is it for:
#   Enabling an inner nested function to modify and rebind variables defined in its
#   enclosing (outer non-global) scope.
# • What it does:
#   - Outer function defines enclosing variables `a = 100` and `b = 200`.
#   - Inner function declares `nonlocal a, b` to avoid creating separate local variables.
#   - Modifies `a = a + 20` (120) and prints `a + 30` (evaluates to 150).
#   - Modifies `b = b - 20` (180) and prints `b` (180).
#   - Mutations directly alter the outer function's variable state.
# • Where it is used:
#   Stateful callback counters, nested state machines, and lightweight closures.
# ------------------------------------------------------------------------------
def outer():
    a = 100
    b = 200                             # Enclosing variable in outer frame
    def inner():
        nonlocal a, b                   # Rebinds to enclosing outer variables
        print("inner function body")
        a = a + 20                      # Updates enclosing a to 120
        print(a + 30)                   # Result: 150
        b = b - 20                      # Updates enclosing b to 180
        print(b)                        # Result: 180
    inner()

outer()

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Combining 'global' and 'nonlocal' in Multi-Tier Scope Resolution
# • What is it for:
#   Demonstrating the distinction between global namespace modification (`global`)
#   and enclosing scope modification (`nonlocal`) under Python's LEGB rule.
# • What it does:
#   - Initializes global variable `a = 100`.
#   - In `outer()`, `global a` allows modifying global `a` to `a + 70` (170).
#   - Defines enclosing variable `b = 200` inside `outer()`.
#   - In `inner()`, `nonlocal b` allows modifying enclosing `b` to `b * 3` (600).
# • Where it is used:
#   Architectures requiring global config updates alongside localized closure state.
# ------------------------------------------------------------------------------
a = 100
def outer():
    global a                            # Modifies module-level global variable
    a = a + 70
    print("a = ", a)                    # Result: a = 170
    b = 200                             # Enclosing variable
    def inner():
        nonlocal b                      # Modifies outer function's enclosing variable
        b = b * 3
        print("b = ", b)                # Result: b = 600
    inner()

outer()

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Persistent Local Frame State Across Multiple Inner Calls
# • What is it for:
#   Observing how an enclosing variable retains its updated state across consecutive
#   inner function invocations within the same parent frame execution.
# • What it does:
#   - Initializes enclosing `count = 0` inside `counter()`.
#   - `increment()` increments `count` by 1 and prints it.
#   - Calling `increment()` twice in succession prints 1 and then 2.
# • Where it is used:
#   Internal sequence generation, accumulator tallying, and multi-step workflows.
# ------------------------------------------------------------------------------
def counter():
    count = 0                           # Enclosing counter variable
    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()                         # First call Result: 1
    increment()                         # Second call Result: 2

counter()

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Returning Inner Function Reference: The Anatomy of a Closure Factory
# • What is it for:
#   Returning the inner function object so its enclosing environment is packaged
#   and persists in memory even after the outer function has completed execution.
# • What it does:
#   - `counter()` defines enclosing `count = 0` and returns `increment` function reference.
#   - Assigns `increment = counter()`, creating a closure holding `count`.
#   - Invoking `increment()` executes the preserved closure state, printing 1.
# • Where it is used:
#   Closure generators, state encapsulation without classes, event listeners.
# ------------------------------------------------------------------------------
def counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        print(count)

    return increment                    # Returns inner function address (Closure creation)

# print(counter())                      # Would print function object representation

increment = counter()                   # Creates closure instance
increment()                             # Result: 1
