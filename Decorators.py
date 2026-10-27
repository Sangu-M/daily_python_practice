# ==============================================================================
# Module: Decorators.py
# Topic: Python Decorators, Function Wrappers & '@decorator' Syntax with '*args' and '**kwargs'
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Fundamental Decorator Mechanism (Manual Function Wrapping)
# • What is it for:
#   Extending or modifying the behavior of a function dynamically without altering
#   its underlying source code.
# • What it does:
#   - Step 1: Defines higher-order decorator function `decorator(fun)`.
#   - Step 2: Defines inner `wrapper()` function containing pre-execution and post-execution logic.
#   - Step 3: Invokes original `fun()` inside wrapper.
#   - Step 4: Returns the wrapper function address.
#   - Manually wraps: `gift = decorator(gift)`.
#   - Invoking `gift()` triggers wrapper logic around original function.
# • Where it is used:
#   Logging execution timestamps, pre-flight authentication checks, and resource cleanup.
# ------------------------------------------------------------------------------
def decorator(fun):                     # Step 1: Decorator function
    def wrapper():                      # Step 2: Wrapper function wraps original function
        print("choose the gift papper") # Pre-execution logic
        fun()                           # Calling original function
        print("add a label")            # Post-execution logic
    return wrapper                      # Step 4: Return the inner wrapper function

def gift():                             # Original function to be extended
    print("gift is choose as WATCH")

gift = decorator(gift)                  # Manual decorator binding
gift()                                  # Result: prints prep, function output, and label

print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Decorating Functions with Explicit Positional Parameters
# • What is it for:
#   Ensuring the wrapper function receives and correctly forwards arguments to the
#   wrapped target function.
# • What it does:
#   - Defines decorator `packing(fun)`.
#   - Inner `packed(name, person)` receives arguments and forwards them: `fun(name, person)`.
#   - Adds personalized celebratory output and packaging completion messages.
#   - Calls `pack_completed("chocolate", "raj")`.
# • Where it is used:
#   Input validation decorators, sanitizing function arguments, user-bound auditing.
# ------------------------------------------------------------------------------
def packing(fun):
    def packed(name, person):
        print("choose  gift box")
        fun(name, person)               # Forwarding positional arguments
        print(f"happy Birthday!! {person}")
        print("add a label")
        print("packing is completed")
    return packed

def cake(name, person):
    print(f"{name} cake selected")

pack_completed = packing(cake)
pack_completed("chocolate", "raj")      # Result: wraps cake selection with gift box & bday message

print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Decorators with Variable-Length Positional Arguments ('*args' / '*invited')
# • What is it for:
#   Enabling decorator wrappers to handle functions accepting arbitrary numbers of
#   positional parameters.
# • What it does:
#   - `packed(name, person, *invited)` packs extra arguments into a tuple.
#   - Unpacks and passes them into `fun(name, person, *invited)`.
#   - Prints the tuple of invited guests: `('tom', 'sam', 'ram', 'kamal')`.
# • Where it is used:
#   Variadic mathematical helpers, flexible CLI command handlers, multi-recipient alerts.
# ------------------------------------------------------------------------------
def packing(fun):
    def packed(name, person, *invited):
        print("choose  gift box")
        fun(name, person, *invited)     # Unpacks variadic arguments into target
        print(f"happy Birthday!! {person}")
        print("add a label")
        print("packing is completed")
        print(f"friends are comming to party{invited}")
    return packed

def cake(name, person, *invited):
    print(f"{name} cake selected")

pack_completed = packing(cake)
pack_completed("chocolate", "raj", "tom", "sam", "ram", "kamal")

print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Standard '@' Syntactic Sugar with Both '*args' and '**kwargs'
# • What is it for:
#   Using Python's canonical `@decorator` syntax along with universal `*args` and `**kwargs`
#   to decorate any function signature with keyword arguments.
# • What it does:
#   - `@packing` syntax above `cake(...)` replaces manual assignment (`cake = packing(cake)`).
#   - Wrapper accepts and forwards both `*invited` (positional) and `**details` (keyword).
#   - Unpacks both into `cake` and outputs party details dictionary.
# • Where it is used:
#   Flask/FastAPI route decorators, pytest fixtures, Django authentication (`@login_required`).
# ------------------------------------------------------------------------------
def packing(fun):
    def packed(name, person, *invited, **details):
        print("choose  gift box")
        fun(name, person, *invited, **details)
        print(f"happy Birthday!! {person}")
        print("add a label")
        print("packing is completed")
        print(f"friends are comming to party{invited}")
        print(f"Party Details {details}")
    return packed

@packing                                # Canonical Python decorator syntax
def cake(name, person, *invited, **details):
    print(f"{name} cake selected")

# pack_completed = packing(cake)        # Manual decoration alternative
cake("chocolate", "raj", "tom", "sam", "ram", "kamal", party="BDYparty", location="BTM bangalore", ROOM_no=200, Time="10:30PM")

print("---------------------------------------------------")
