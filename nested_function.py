# ==============================================================================
# Module: nested_function.py
# Topic: Nested Functions & Encapsulated Function Declarations
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Inner (Nested) Function Declaration & Local Scope Containment
# • What is it for:
#   Encapsulating private helper functions inside a parent function scope to hide
#   implementation details from the global namespace.
# • What it does:
#   - Defines outer function `outer()`.
#   - Defines inner child function `inner()` within `outer()`'s local namespace.
#   - The identifier `inner` exists strictly within `outer()`'s local scope.
#   - `outer()` executes its own statements, then calls `inner()`.
#   - Direct calls to `inner()` from outside `outer()` would trigger `NameError`.
# • Where it is used:
#   Building function factories, closure generators, decorators, and helper routines.
# ------------------------------------------------------------------------------
def outer():
    print("function outer body")        # Outer function logic

    def inner():                        # Nested inner function (local to outer)
        print("function inner body")    # Inner function logic

    inner()                             # Calling inner function locally inside outer

outer()                                 # Result: executes outer, then triggers inner
