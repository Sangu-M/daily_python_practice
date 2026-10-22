# ==============================================================================
# Module: globel_variable.py
# Topic: Global Variables & Mutating Module Scope via the 'global' Keyword
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Modifying Global Variables Inside Functions via 'global'
# • What is it for:
#   Explicitly granting a function permission to rebind or mutate a module-level global variable.
# • What it does:
#   - Defines global `a = 100`.
#   - Inside `display()`, declares `global a`.
#   - Increments `a = a + 50` (150).
#   - Because of `global a`, the mutation directly updates the module's global state.
# • Where it is used:
#   Global counters, application runtime configuration changes, state flags.
# ------------------------------------------------------------------------------
a = 100                                 # Global variable
b = 200

def display():
    global a
    a = a + 50                          # Modifies global 'a' inside function
    print("inside  function ", a)

display()                               # Result: "inside  function  150"

# ------------------------------------------------------------------------------
# 2. Mutating Global Variables in the Outer Module Scope
# • What is it for:
#   Demonstrating that global variables remain accessible and modifiable anywhere in module scope.
# • What it does:
#   - Modifies `a = a + 20` (150 + 20 = 170).
#   - Prints the updated global value.
# • Where it is used:
#   Standard sequential module-level execution.
# ------------------------------------------------------------------------------
a = a + 20                              # Modifying variable outside function
print("outside the function", a)        # Result: "outside the function 170"

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Multi-Variable 'global' Declarations in a Single Statement
# • What is it for:
#   Declaring multiple global targets concisely using comma separation (`global a, b`).
# • What it does:
#   - In `display1()`, specifies `global a, b`.
#   - Mutates `a = a + 50` (170 + 50 = 220) and `b = b - 20` (200 - 20 = 180).
#   - Both global variables are updated persistently.
# • Where it is used:
#   Batch state synchronization routines, multi-variable reset handlers.
# ------------------------------------------------------------------------------
def display1():
    global a, b                         # Single statement declaring multiple global variables
    a = a + 50                          # Modifies global 'a' inside function
    b = b - 20                          # Modifies global 'b' inside function
    print("inside  function ", a)
    print("inside  function ", b)

display1()                              # Result: Prints "inside  function  220" and "inside  function  180"

print("------------------------------------------------")
