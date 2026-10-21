# ==============================================================================
# Module: positionalArgument.py
# Topic: Positional Arguments, Keyword Arguments & Variable Positional '*args'
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Positional Argument Binding & Order Dependency
# • What is it for:
#   Passing arguments whose meaning is determined purely by the order of parameters.
# • What it does:
#   - Defines `play(name, score)`.
#   - Calling `play(56, "raj")` assigns `56` to `name` and `"raj"` to `score`.
#   - Prints "56 scored raj in an innings", illustrating the danger of mismatched order.
# • Where it is used:
#   Understanding function calling bugs when positions are swapped accidentally.
# ------------------------------------------------------------------------------
def play(name, score):
    print(f"{name} scored {score} in an innings")

play(56, "raj")                         # Result: "56 scored raj in an innings" (Order mismatch issue)

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Keyword Arguments (Named Arguments)
# • What is it for:
#   Binding caller values directly by parameter name, freeing the caller from strict ordering.
# • What it does:
#   - Calls `play(score=56, name="raj")`.
#   - Explicitly directs `56` to `score` and `"raj"` to `name` regardless of order.
# • Where it is used:
#   Improving code readability, configuring options with clear explicit parameter names.
# ------------------------------------------------------------------------------
play(score=56, name="raj")              # Result: "raj scored 56 in an innings" (Correct mapping)

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Keyword Arguments in Authentication Workflows
# • What is it for:
#   Providing explicit parameter binding for multi-argument security/validation functions.
# • What it does:
#   - Calls `login(username="abhi", password=123, otp=1234)`.
#   - Explicit argument keys ensure parameters are routed to proper fields.
# • Where it is used:
#   API authentication, form submission handlers.
# ------------------------------------------------------------------------------
def login(username, password, otp):
    print(f"{username} successfully loged in")

login(username="abhi", password=123, otp=1234)  # Result: "abhi successfully loged in"

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Variable-Length Positional Arguments via '*args'
# • What is it for:
#   Allowing a function to accept any arbitrary number of positional arguments bundled into a tuple.
# • What it does:
#   - Defines `collect(*a)`.
#   - Calling `collect(20, 30, 40, 50)` bundles arguments into tuple `(20, 30, 40, 50)`.
#   - Calling `collect()` with no arguments receives an empty tuple `()`.
# • Where it is used:
#   Variadic utilities like `print()`, math summations `sum_all(*nums)`.
# ------------------------------------------------------------------------------
def collect(*a):
    print(a)

collect(20, 30, 40, 50)                 # Result: (20, 30, 40, 50)
collect()                               # Result: ()

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 5. Argument Unpacking with Asterisk '*' at Call Site
# • What is it for:
#   Unpacking elements of a sequence into separate individual positional parameters.
# • What it does:
#   - Defines `uncoll1(a, b, c, d)` expecting 4 separate values.
#   - `uncoll1(*l1)` unpacks list `[10, 20, 30, 40]` into `a=10, b=20, c=30, d=40`.
# • Where it is used:
#   Forwarding collected items from an array/list directly into fixed parameter functions.
# ------------------------------------------------------------------------------
def uncoll1(a, b, c, d):
    print(a, b, c, d)

l1 = [10, 20, 30, 40]
uncoll1(*l1)                            # Result: 10 20 30 40

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 6. Combining Call-Site Unpacking with Parameter-Site Packing
# • What is it for:
#   Unpacking an existing list and repacking it inside the receiving function via `*a`.
# • What it does:
#   - `uncoll2(*l2)` unpacks elements `10, 20, 30, 40` into call args.
#   - Function parameter `*a` repacks them into tuple `(10, 20, 30, 40)`.
# • Where it is used:
#   Decorator wrappers, argument forwarding in middleware.
# ------------------------------------------------------------------------------
def uncoll2(*a):
    print(a)

l2 = [10, 20, 30, 40]
uncoll2(*l2)                            # Result: (10, 20, 30, 40)

print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 7. Mixing Fixed Positional Parameters with Trailing '*args'
# • What is it for:
#   Extracting specific leading and middle positional arguments, capturing the rest into a tuple.
# • What it does:
#   - `uncoll3(a, b, d, *c)` with `*l3` containing 9 elements.
#   - `a` receives 10, `b` receives 20, `d` receives 30.
#   - `*c` collects remaining elements `(40, 50, 60, 70, 80, 90)`.
# • Where it is used:
#   Command handlers: `handle_cmd(command, user, priority, *options)`.
# ------------------------------------------------------------------------------
def uncoll3(a, b, d, *c):
    print(a)
    print(b)
    print(c)
    print(d)

l3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
uncoll3(*l3)                            # Result: Prints 10, 20, (40, 50, 60, 70, 80, 90), 30

print("----------------------------------------------")
