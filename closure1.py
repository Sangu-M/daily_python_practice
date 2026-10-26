# ==============================================================================
# Module: closure1.py
# Topic: Function Closures, Lexical Scoping & Persistent State Encapsulation
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. The Three Structural Criteria of a Python Closure (Read-Only Enclosing State)
# • What is it for:
#   Preserving outer scope variables (free variables) inside an inner function even
#   after the outer function has finished executing and exited its frame.
# • What it does:
#   - Rule 1: Create an outer enclosing function with an outer local variable (`count = 100`).
#   - Rule 2: Create a nested inner function that accesses that enclosing variable.
#   - Rule 3: Return the inner function object reference (without parentheses).
#   - When `increment = counter()` is evaluated, a closure is formed.
#   - Calling `increment()` accesses `count` from closure cell memory, printing 100.
# • Where it is used:
#   Data encapsulation, function factory patterns, and currying parameters.
# ------------------------------------------------------------------------------
def counter():                          # 1) Outer function with enclosing variable
    count = 100                         # 2) Free variable in enclosing frame
    def increment():
        print(count)                    # Accesses free variable
    return increment                    # 3) Return inner function address


increment = counter()
increment()                             # Result: 100


print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Stateful Incrementing Closure with 'nonlocal' Mutation
# • What is it for:
#   Maintaining mutable private state across repeated function calls without relying
#   on global variables or OOP class boilerplate.
# • What it does:
#   - Initializes `count = 0` in enclosing function.
#   - Inner function `increment()` declares `nonlocal count` and increments `count += 1`.
#   - Returns `increment`.
#   - Calling `increment()` repeatedly increments state: 1, 2, 3, 4.
# • Where it is used:
#   Sequential ID generators, analytics event counters, and rate limiter buckets.
# ------------------------------------------------------------------------------
def counter():                          # 1) Outer function
    count = 0                           # Enclosing state
    def increment():
        nonlocal count                  # Binds to outer variable for in-place mutation
        count += 1
        print(count)
    return increment                    # Returns closure


increment = counter()
increment()                             # Result: 1
increment()                             # Result: 2
increment()                             # Result: 3
increment()                             # Result: 4


print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Stateful Decrementing Countdown Closure
# • What is it for:
#   Illustrating countdown / decremental tracking where private state decreases with each invocation.
# • What it does:
#   - Outer function initializes `count = 5`.
#   - Inner function `dec()` uses `nonlocal count` and decrements `count -= 1`.
#   - Four consecutive calls produce: 4, 3, 2, 1.
# • Where it is used:
#   Retry budget counters, consumable token quotas, and game lives tracking.
# ------------------------------------------------------------------------------
def counter():                          # 1) Outer function
    count = 5                           # Starting threshold
    def dec():
        nonlocal count                  # Binds to outer variable
        count -= 1
        print(count)
    return dec                          # Returns countdown closure


dec = counter()
dec()                                   # Result: 4
dec()                                   # Result: 3
dec()                                   # Result: 2
dec()                                   # Result: 1
