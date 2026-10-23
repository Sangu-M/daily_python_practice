# ==============================================================================
# Module: function_aliasing.py
# Topic: Function Aliasing & Assigning Functions to Variables (First-Class Citizens)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Function Aliasing (Assigning Function Reference to New Identifier)
# • What is it for:
#   Treating functions as first-class objects in Python by assigning function references
#   to other variable identifiers without invoking parentheses `()`.
# • What it does:
#   - Defines function `show()` printing "function body".
#   - Assigns `display = show`, binding the identifier `display` to the same function object in memory.
#   - Invoking `show()` and `display()` executes the identical underlying code object.
#   - Further assigns `view = show`, demonstrating multiple aliases pointing to the same address.
# • Where it is used:
#   Creating concise aliases for verbose function names, dynamic function routing,
#   and strategy pattern dispatch tables.
# ------------------------------------------------------------------------------
def show():
    print("function body")

display = show                          # function aliasing (copies function address, not call)

show()                                  # Result: prints "function body"
display()                               # Result: prints "function body" (via alias)

view = show
view()                                  # Result: prints "function body" (via second alias)


print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Function Aliasing with Arguments & Return Values
# • What is it for:
#   Demonstrating that aliases retain full signature capabilities, arguments, and return values.
# • What it does:
#   - Defines `square(n)` returning `n*n`.
#   - Assigns `s = square` as a shorthand alias.
#   - Evaluates `square(3)` producing 9.
#   - Evaluates alias `s(2)` producing 4.
# • Where it is used:
#   Mathematical shorthand formulas, functional mapping arguments, and callback handlers.
# ------------------------------------------------------------------------------
def square(n):
    return n*n

s = square                              # Alias for parameterized function
print(square(3))                        # Result: 9
print(s(2))                             # Result: 4

print("---------------------------------------------------")
