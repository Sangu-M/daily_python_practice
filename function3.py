# ==============================================================================
# Module: function3.py
# Topic: Positional Arguments, Missing Argument Errors & Function Redefinition
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Required Positional Arguments & Missing Argument TypeError
# • What is it for:
#   Enforcing that functions receive exactly the required number of positional inputs.
# • What it does:
#   - Defines `book_ticket(movie_name, price)` expecting two positional arguments.
#   - Calling `book_ticket("jailer", 500)` binds `"jailer"` to `movie_name` and `500` to `price`.
#   - Omitting an argument (e.g. `book_ticket(500)`) raises:
#     `TypeError: book_ticket() missing 1 required positional argument: 'price'`.
# • Where it is used:
#   Mandating essential parameters (e.g., recipient and payload in messaging functions).
# ------------------------------------------------------------------------------
def book_ticket(movie_name, price):
    print("Booking Ticket")
    print(f"{movie_name} movie ticket cost,{price}")

book_ticket("jailer", 500)              # Result: Prints "Booking Ticket" and "jailer movie ticket cost,500"

# Note on Missing Positional Arguments:
# Calling book_ticket(500) raises:
# TypeError: book_ticket() missing 1 required positional argument: 'price'

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Multi-Parameter Functions & Sequential Argument Binding
# • What is it for:
#   Mapping inputs sequentially to distinct parameter variables based on their call positions.
# • What it does:
#   - Defines initial version of `celebrate_birthday(name, cake)`.
#   - Invocations match `"Yasash"` to `name` and `"Honey Cake"` to `cake`.
# • Where it is used:
#   Event handling, status message formatting, logging event details.
# ------------------------------------------------------------------------------
def celebrate_birthday(name, cake):
    print(f"{name} celebrated Birthday  by cutting {cake}")

celebrate_birthday("Yasash", "Honey Cake")  # Result: "Yasash celebrated Birthday  by cutting Honey Cake"

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Function Redefinition (Python Does Not Support Method Overloading by Signature)
# • What is it for:
#   Understanding that defining a function with the same name replaces the prior definition in module scope.
# • What it does:
#   - Redefines `celebrate_birthday(name, cake, place)` with three parameters.
#   - The 2-argument version is overwritten; calling with 3 arguments now succeeds.
# • Where it is used:
#   Avoiding accidental function masking, understanding Python dynamic binding principles.
# ------------------------------------------------------------------------------
def celebrate_birthday(name, cake, place):
    print(f"{name} celebrated Birthday  by cutting {cake} in {place}")

celebrate_birthday("Yasash", "Honey Cake", "pune")  # Result: "Yasash celebrated Birthday  by cutting Honey Cake in pune"
