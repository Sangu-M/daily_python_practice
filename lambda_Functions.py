# ==============================================================================
# Module: lambda_Functions.py
# Topic: Lambda Functions (Anonymous Inline Expressions) & Callback Transformations
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Standard 'def' Function vs Lambda Anonymous Expression
# • What is it for:
#   Creating compact, unnamed functions for simple single-expression operations
#   without the ceremony of a full `def` block.
# • What it does:
#   - Defines `square(n)` returning `n**2` via standard `def` block; `square(3)` evaluates to 9.
#   - Defines equivalent anonymous function: `var1 = lambda n: n**2`.
#   - The expression after `:` is implicitly returned.
#   - `var1(5)` evaluates to 25.
# • Where it is used:
#   Inline math calculations, simple key selectors for sorting, and quick utility transformations.
# ------------------------------------------------------------------------------
def square(n):
    return n**2

var = square(3)
print(var)                              # Result: 9
print("--------------------------------------------------")

var1 = lambda n: n**2
print(var1(5))                          # Result: 25

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Immediately Invoked Function Expression (IIFE) with Lambda
# • What is it for:
#   Evaluating a lambda expression on the spot without binding it to an intermediate variable.
# • What it does:
#   - Wraps lambda expression in parentheses: `(lambda n: n**2)`.
#   - Appends invocation arguments immediately: `(10)`.
#   - Directly evaluates `10**2`, outputting 100.
# • Where it is used:
#   Dynamic inline configuration values, temporary math scaling, and self-contained routines.
# ------------------------------------------------------------------------------
print((lambda n: n**2)(10))             # Result: 100 (second approach: immediate invocation)

# print((lambda n: n**2)(int(input()))) # Interactive dynamic user input variant

print("--------------------------------------------------")

'''
# Background Evolution: From Manual Loops & Named Functions to Lambdas
def sqList(*l):
    l1 = [] 
    for i in l:
        l1.append(i**2)
    print(l1)

l = [10, 20, 30, 40]
sqList(*l)
# print(var2)   

def sq(n):
    return n**2
def cu(n):
    return n**3

def convert(fun, *col):
    n = []
    for i in col:
        result = fun(i)
        n.append(result)
    return n

l = [10, 20, 30, 40]
var3 = convert(sq, *l)
var4 = convert(cu, *l)

print(var3)
print(var4)
'''

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Passing Anonymous Lambdas into Higher-Order Transformation Functions
# • What is it for:
#   Supplying concise ad-hoc transformation rules directly at the function call site
#   without having to declare separate named helper functions.
# • What it does:
#   - `convert(fun, *col)` receives transformation function `fun` and unpacks elements.
#   - Evaluates `convert(lambda n: n**2, *l)` to compute squares: `[100, 400, 900, 1600]`.
#   - Evaluates `convert(lambda n: n**3, *l)` to compute cubes: `[1000, 8000, 27000, 64000]`.
# • Where it is used:
#   Passing custom map transformations, filter predicates, and event-driven handlers.
# ------------------------------------------------------------------------------
def convert(fun, *col):
    n = []
    for i in col:
        result = fun(i)
        n.append(result)
    return n

l = [10, 20, 30, 40]
var3 = convert(lambda n: n**2, *l)      # Squares transformation callback
var4 = convert(lambda n: n**3, *l)      # Cubes transformation callback

print(var3)                             # Result: [100, 400, 900, 1600]
print(var4)                             # Result: [1000, 8000, 27000, 64000]
