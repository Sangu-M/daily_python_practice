# ==============================================================================
# Module: local_variable.py
# Topic: Local Variables, Function Scope Isolation & Variable Shadowing
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Local Variable Declaration & Lifecycle
# • What is it for:
#   Confining variables strictly within a function's local execution scope.
# • What it does:
#   - Defines `showcase()` where `a = 100` is initialized inside the function.
#   - Mutates `a = a + 20` to 120.
#   - When the function finishes executing, the local namespace is destroyed.
#   - Attempting to access `a` outside the function raises `NameError: name 'a' is not defined`.
# • Where it is used:
#   Preventing variable name collisions, encapsulating temporary computation state.
# ------------------------------------------------------------------------------
def showcase():
    a = 100                             # Local variable
    print("accssing inside the  function body", a)
    a = a + 20
    print("after modifing the LV inside the function ", a)

showcase()                              # Result: Accesses 100, modifies to 120

# Note: Accessing 'a' outside the function raises NameError:
# print("accsing outside the function ", a)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Function Parameters as Local Variables
# • What is it for:
#   Demonstrating that parameters passed to a function reside in its local namespace.
# • What it does:
#   - Defines `showcase1(a, b)` receiving arguments 10 and 20.
#   - Mutates local `a = a + 20` (30) and `b = b - 2` (18).
#   - Modifications exist purely within the local function frame.
# • Where it is used:
#   Passing parameters safely without risking modification of caller's outer variables.
# ------------------------------------------------------------------------------
def showcase1(a, b):
    print("accssing inside the  function body", a, b)
    a = a + 20
    b = b - 2
    print("after modifing the LV inside the function ", a, b)

showcase1(10, 20)                       # Result: Accesses 10 20, modifies to 30 18

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Variable Shadowing: Local Scope Precedence (LEGB Rule)
# • What is it for:
#   Understanding how a local variable shadows (masks) an identically named global variable.
# • What it does:
#   - Defines global variable `game = "cricket"`.
#   - Inside `play()`, declares local `game = "chess"`.
#   - Inside the function, the local identifier is looked up first (LEGB: Local before Global).
#   - Outside the function, the global variable `game` remains untouched as `"cricket"`.
# • Where it is used:
#   Allowing functions to use generic variable names (e.g., `id`, `count`, `name`) without corrupting module-level state.
# ------------------------------------------------------------------------------
game = "cricket"                        # Global variable

def play():
    game = "chess"                      # Local variable (Shadows global variable)
    print(game, "inside the fuction the LV is first priority")

play()                                  # Result: "chess inside the fuction the LV is first priority"

print(game, "inside the fuction the GV is first priority")  # Result: "cricket inside the fuction the GV is first priority"
