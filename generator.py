# ==============================================================================
# Module: generator.py
# Topic: Python Generator Functions, The 'yield' Keyword & Lazy State Evaluation
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Standard Function 'return' vs Unreachable Multiple Returns
# • What is it for:
#   Contrasting standard functions that terminate upon reaching the first `return`
#   statement against generator functions that can produce multiple values over time.
# • What it does:
#   - Defines `display()` with three consecutive `return` statements.
#   - First `return 10` terminates execution immediately and destroys the stack frame.
#   - `return 20` and `return 30` are unreachable dead code.
#   - Calling `display()` always returns 10.
# • Where it is used:
#   Highlighting the fundamental limitation of standard returns for sequence streaming.
# ------------------------------------------------------------------------------
def display():
    print("function body")
    return 10                           # Exits function immediately; remaining lines unreachable
    return 20
    return 30

val = display()
print(val)                              # Result: 10
val1 = display()
print(val1)                             # Result: 10

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Generator Function Lifecycle & Execution Resumption with 'yield'
# • What is it for:
#   Yielding values lazily where execution pauses at each `yield` and resumes on `next()`.
# • What it does:
#   - Defines `display1()` containing multiple `yield` expressions.
#   - Calling `var = display1()` returns a generator iterator object without executing body.
#   - First `next(var)`: executes until first `yield 10`, then pauses.
#   - Second `next(var)`: resumes, prints "hello", yields 20, pauses.
#   - Third `next(var)`: resumes, yields 30, pauses.
# • Where it is used:
#   Lazy evaluation, reading massive log files line-by-line, and memory-efficient streaming.
# ------------------------------------------------------------------------------
def display1():
    print("second function")
    print("generator func")
    yield 10                            # Yields 10 and pauses execution state
    print("hello")                      # Resumes execution upon next()
    yield 20                            # Yields 20 and pauses
    yield 30                            # Yields 30 and pauses

var = display1()

print(var)                              # Result: <generator object display1 at 0x...>

print(next(var))                        # Result: prints "second function", "generator func", returns 10
print(next(var))                        # Result: prints "hello", returns 20
print(next(var))                        # Result: returns 30

print(display1())                       # Result: creates a brand-new generator object instance

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Stateful Computation Pipelines & Materializing Generators to Collections
# • What is it for:
#   Tracking evolving internal state across sequential yields and casting the generator
#   into a concrete list.
# • What it does:
#   - `dis()` initializes `value = 5`.
#   - Yields `value**2` (25).
#   - Mutates `value = value + 3` (8), yields `value**3` (512).
#   - Mutates `value = value - 3` (5), yields `value**2` (25).
#   - Mutates `value = value + 5` (10), yields `value` (10).
#   - Calling `list(var1)` drains all yields into `[25, 512, 25, 10]`.
# • Where it is used:
#   Step-by-step mathematical computations, coordinate transforms, and sequence generation.
# ------------------------------------------------------------------------------
def dis():
    print("we sre printing values")
    value = 5
    yield value**2                      # Yield 1: 5**2 = 25
    value = value + 3                   # value = 8
    yield value**3                      # Yield 2: 8**3 = 512
    value = value - 3                   # value = 5
    yield value**2                      # Yield 3: 5**2 = 25
    value = value + 5                   # value = 10
    yield value                         # Yield 4: 10

var1 = dis()

"""
# Manual next() and for-loop traversal options:
print(var1)
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))

# for loop approach:
for i in var1:
    print(i)
"""

# Explicit typecasting consumes the full generator into an in-memory list
print(list(var1))                       # Result: [25, 512, 25, 10]
