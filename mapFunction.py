# ==============================================================================
# Module: mapFunction.py
# Topic: Built-in 'map()' Function, Lambda Transformations & Collection Casting
# ==============================================================================

print("--------------------------------------------------")

'''
# Comparison with manual loop implementation:
def convert(fun, *col):
    n = []
    for i in col:
        result = fun(i)
        n.append(result)
    return n

l = [10, 20, 30, 40]
var3 = convert(lambda n: n**2, *l)
var4 = convert(lambda n: n**3, *l)

print(var3)
print(var4)
'''

# ------------------------------------------------------------------------------
# 1. Built-in 'map()' Object Lifecycle & Materialization to List
# • What is it for:
#   Applying a transformation rule to every item of an iterable without writing explicit
#   loops, producing a lazy, memory-efficient map iterator.
# • What it does:
#   - Calls `map(lambda n: n**2, [10, 20, 30, 40])`, returning a `<map>` iterator object.
#   - Evaluates `list(mo)` to drain the iterator into `[100, 400, 900, 1600]`.
# • Where it is used:
#   Bulk data type conversions (e.g. `map(int, input().split())`), mathematical scaling.
# ------------------------------------------------------------------------------
mo = map(lambda n: n**2, [10, 20, 30, 40])
l = list(mo)
print(l)                                # Result: [100, 400, 900, 1600]

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Compact Inline Transformations & Identity Mapping
# • What is it for:
#   Constructing single-line mapping pipelines and observing identity functions (`lambda n: n`).
# • What it does:
#   - Squares each element directly inside `list(map(lambda n: n**2, ...))`.
#   - Identity mapping `lambda n: n` returns each element unaltered: `[10, 20, 30, 40]`.
# • Where it is used:
#   Concise ETL expressions and passing default identity transformations.
# ------------------------------------------------------------------------------
print(list(map(lambda n: n**2, [10, 20, 30, 40])))  # Result: [100, 400, 900, 1600]
print(list(map(lambda n: n, [10, 20, 30, 40])))     # Result: [10, 20, 30, 40] (Identity)

print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. String Transformations across Output Types ('tuple', 'list', 'set')
# • What is it for:
#   Applying string methods across string sequences and casting the output iterator
#   into diverse target data structures.
# • What it does:
#   - Evaluates `map(lambda i: i.upper(), ...)` into immutable `tuple`: `('DRONA', 'BHEEMA', 'ANGANDA', 'VANI')`.
#   - Evaluates into mutable `list`: `['DRONA', 'BHEEMA', 'ANGANDA', 'VANI']`.
#   - Evaluates `map(lambda i: i.capitalize(), ...)` into unordered, deduplicated `set`.
# • Where it is used:
#   Standardizing names, normalizing search queries, and sanitizing textual dataset columns.
# ------------------------------------------------------------------------------
print(tuple(map(lambda i: i.upper(), ["drona", "bheema", "anganda", "vani"])))
# Result: ('DRONA', 'BHEEMA', 'ANGANDA', 'VANI')

print(list(map(lambda i: i.upper(), ["drona", "bheema", "anganda", "vani"])))
# Result: ['DRONA', 'BHEEMA', 'ANGANDA', 'VANI']

print(set(map(lambda i: i.capitalize(), ["drona", "bheema", "anganda", "vani"])))
# Result: {'Vani', 'Drona', 'Bheema', 'Anganda'} (unordered set)
