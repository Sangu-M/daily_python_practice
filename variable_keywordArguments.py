# ==============================================================================
# Module: variable_keywordArguments.py
# Topic: Variable Keyword Arguments ('**kwargs'), Unpacking, Defaults & Parameter Hierarchy
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Fixed Parameter Function Call
# • What is it for:
#   Direct 1-to-1 matching of arguments to explicit parameters.
# • What it does:
#   - Calls `recive("abhi", 23)`.
#   - Binds "abhi" to `name` and 23 to `age`.
# • Where it is used:
#   Basic functions with strict, fixed parameter requirements.
# ------------------------------------------------------------------------------
def recive(name, age):
    print(name, age)

recive("abhi", 23)                      # Result: abhi 23

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Arbitrary Keyword Arguments ('**kwargs') Dictionary Packing
# • What is it for:
#   Capturing any arbitrary number of named keyword arguments into a standard Python dictionary.
# • What it does:
#   - Defines `recive1(**kwargs)`.
#   - Calling with named arguments bundles them into a dictionary `{'name': 'abhi', 'age': 23, 'height': 4.8}`.
# • Where it is used:
#   Configurable class constructors, request query parameter processing, flexible options objects.
# ------------------------------------------------------------------------------
def recive1(**kwargs):
    print(kwargs)

recive1(name="abhi", age=23, height=4.8)    # Result: {'name': 'abhi', 'age': 23, 'height': 4.8}

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Empty '**kwargs' Invocation
# • What is it for:
#   Demonstrating that `**kwargs` safely defaults to an empty dictionary `{}` when no keyword arguments are passed.
# • What it does:
#   - Invocations of `recive2()` without arguments result in `kwargs = {}`.
# • Where it is used:
#   Optional configuration handlers where users supply zero or more parameters.
# ------------------------------------------------------------------------------
def recive2(**kwargs):
    print(kwargs)

recive2()                               # Result: {} (Empty dictionary)

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Combining Explicit Parameter with '**kwargs'
# • What is it for:
#   Separating mandatory named fields from arbitrary metadata.
# • What it does:
#   - `recive3(name, **kwargs)` extracts `name="abhi"`.
#   - The remaining keyword arguments are packed into `kwargs`.
# • Where it is used:
#   User profile updates where `user_id` is required and remaining fields are variable.
# ------------------------------------------------------------------------------
def recive3(name, **kwargs):
    print(name, kwargs)

recive3(name="abhi", age=23, height=4.8)    # Result: abhi {'age': 23, 'height': 4.8}

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 5. Dictionary Unpacking ('**dict') into '**kwargs'
# • What is it for:
#   Unpacking an existing dictionary's key-value pairs directly as keyword arguments.
# • What it does:
#   - `dic` contains student records.
#   - `bothunP(**dic)` unpacks dictionary keys as arguments, and `**a` repacks them inside the function.
# • Where it is used:
#   Passing deserialized JSON payloads into processing functions.
# ------------------------------------------------------------------------------
def bothunP(**a):
    print(a)

dic = {
    "name": "raj",
    "city": "bangalore",
    "age": 23,
    "course": "Mca",
    "marks": 95.4
}

bothunP(**dic)                          # Result: {'name': 'raj', 'city': 'bangalore', 'age': 23, 'course': 'Mca', 'marks': 95.4}

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 6. Dictionary Unpacking into Exact Named Positional Parameters
# • What is it for:
#   Routing dictionary keys directly to identically named function parameters.
# • What it does:
#   - `bothunP1(name, age, city, course, marks)` expects specific parameter names.
#   - `bothunP1(**dic1)` routes matching dictionary keys to parameter variables.
# • Where it is used:
#   Mapping database query result dictionaries into function parameters.
# ------------------------------------------------------------------------------
def bothunP1(name, age, city, course, marks):
    print(name, age, city, course, marks)

dic1 = {
    "name": "raj",
    "city": "bangalore",
    "age": 23,
    "course": "Mca",
    "marks": 95.4
}

bothunP1(**dic1)                        # Result: raj 23 bangalore Mca 95.4

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 7. Unpacking with Selective Parameter Extraction & Trailing '**k' Repacking
# • What is it for:
#   Pulling out specific expected fields while bundling all extraneous dictionary keys into `**k`.
# • What it does:
#   - Redefined `bothunP1(name, age, **k)` explicitly binds `name` and `age`.
#   - Trailing keys (`city`, `course`, `marks`) are repacked into dictionary `k`.
# • Where it is used:
#   API controllers extracting primary IDs while keeping payload metadata in `extra`.
# ------------------------------------------------------------------------------
def bothunP1(name, age, **k):
    print(name, age, k)

bothunP1(**dic1)                        # Result: raj 23 {'city': 'bangalore', 'course': 'Mca', 'marks': 95.4}

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 8. Default Parameter Values & Flexible Argument Overrides
# • What is it for:
#   Supplying default values for parameters that callers can optionally override.
# • What it does:
#   - Defines `order_food(beverage="water", sprinkler="salt")`.
#   - Invocations use defaults, override first parameter, override both positionally, or override using keywords.
# • Where it is used:
#   Configurable settings (e.g. `timeout=30`, `debug=False`).
# ------------------------------------------------------------------------------
def order_food(beverage="water", sprinkler="salt"):
    print(beverage, sprinkler)

order_food()                            # Result: water salt (Both defaults used)
order_food("sprite")                    # Result: sprite salt (beverage overridden)
order_food("coke", "pepper")            # Result: coke pepper (Both overridden positionally)
order_food(sprinkler="organo", beverage="fizz") # Result: fizz organo (Overridden by keywords)

print("----------------------------------------------------")

# ------------------------------------------------------------------------------
# 9. Complete Parameter Precedence Hierarchy
# • What is it for:
#   Synthesizing positional parameters, arbitrary *args, keyword defaults, and arbitrary **kwargs.
# • What it does:
#   - Precedence order:
#     1. Positional parameters (`name`, `age`)
#     2. Variable positional arguments (`*friends`)
#     3. Keyword arguments with defaults (`love="mother"`)
#     4. Variable keyword arguments (`**details`)
# • Where it is used:
#   Advanced Python frameworks, decorator factories, complex API client methods.
# ------------------------------------------------------------------------------
def about_person(name, age, *friends, love="mother", **details):
    print(name, age, friends, love, details)

about_person(
    "raj", 25, "ram", "sham", "bheem",
    love="father",
    hobby="editing", genaral="NCRT", sport="kabaddi", philosophy="peaceful"
)
# Result: raj 25 ('ram', 'sham', 'bheem') father {'hobby': 'editing', 'genaral': 'NCRT', 'sport': 'kabaddi', 'philosophy': 'peaceful'}
