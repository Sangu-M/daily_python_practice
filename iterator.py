# ==============================================================================
# Module: iterator.py
# Topic: Python Iterator Protocol ('iter()' and 'next()')
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Creating Iterator Objects & Step-by-Step Retrieval with 'next()'
# • What is it for:
#   Converting an iterable sequence into an iterator and consuming elements on-demand
#   one item at a time (lazy evaluation).
# • What it does:
#   - Defines list `l = [2, 3, 4, 5]`.
#   - Converts iterable into an iterator object using `iter(l)`.
#   - Prints iterator object representation (showing type `<list_iterator>` and memory address).
#   - Calls `next(itr_obj)` sequentially to fetch elements: 2, 3, 4, 5.
#   - Demonstrates that the iterator maintains its internal state across arbitrary pauses.
# • Where it is used:
#   Streaming data chunks, pagination queries, and processing large datasets without loading all items.
# ------------------------------------------------------------------------------
# iterator
l = [2, 3, 4, 5]
itr_obj = iter(l)
print(itr_obj)                          # Result: <list_iterator object at 0x...>

val = next(itr_obj)
print(val)                              # Result: 2

val1 = next(itr_obj)
print(val1)                             # Result: 3

print(next(itr_obj))                    # Result: 4
print("after 30 mints")                 # State is preserved in memory
print(next(itr_obj))                    # Result: 5


print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Consuming Iterators with 'for' Loops
# • What is it for:
#   Observing how a standard `for` loop interacts with the iterator protocol,
#   automatically invoking `next()` and catching `StopIteration` cleanly.
# • What it does:
#   - Creates iterator `itr_obj = iter(l)`.
#   - Traverses items with `for i in itr_obj:`, printing each value (2, 3, 4, 5).
#   - After the loop finishes, the iterator is exhausted and cannot be reused.
# • Where it is used:
#   Clean sequential processing of any custom iterable or generator stream.
# ------------------------------------------------------------------------------
l = [2, 3, 4, 5]
itr_obj = iter(l)
for i in itr_obj:
    print(i)                            # Result: prints 2, 3, 4, 5 sequentially

print("---------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Explicit Type Casting of Iterators
# • What is it for:
#   Materializing all remaining elements of an iterator into a concrete collection
#   in memory (such as a tuple or list).
# • What it does:
#   - Passes `iter(l)` to constructor `tuple(...)`.
#   - Consumes the entire iterator immediately into `(2, 3, 4, 5)`.
# • Where it is used:
#   Converting dynamic streams into indexable in-memory data structures.
# ------------------------------------------------------------------------------
# explicit type casting

print(tuple(iter(l)))                   # Result: (2, 3, 4, 5)
