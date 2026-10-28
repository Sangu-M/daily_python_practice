# ==============================================================================
# Module: iterator2.py
# Topic: Tuple Iterators, Exhaustion Semantics & Collection Typecasting
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Tuple Iterator Initialization & Complete Sequential Retrieval
# • What is it for:
#   Demonstrating that immutable sequence collections (tuples) implement `__iter__()`
#   and can be navigated lazily using `next()`.
# • What it does:
#   - Defines tuple `t = (11, 22, 33)`.
#   - Creates an iterator using `itr_obj = iter(t)`.
#   - Calls `next(itr_obj)` three consecutive times, pulling 11, 22, and 33.
#   - Upon retrieving 33, all elements have been consumed and the iterator is fully exhausted.
# • Where it is used:
#   Stepping through fixed configuration tuples, token streams, and database result tuples.
# ------------------------------------------------------------------------------
t = (11, 22, 33)
itr_obj = iter(t)                       # iter() creates tuple_iterator

# explicit retrieval with next()
print(next(itr_obj))                    # Result: 11
print(next(itr_obj))                    # Result: 22
print(next(itr_obj))                    # Result: 33

# ------------------------------------------------------------------------------
# 2. Iterator Exhaustion Semantics & Collection Casting
# • What is it for:
#   Highlighting that iterators are single-pass streams; once exhausted, subsequent
#   loops yield zero iterations, while the original iterable collection remains intact.
# • What it does:
#   - Attempts to iterate over `itr_obj` with a `for` loop. Since it is already exhausted, the loop body does not run.
#   - Converts original iterable `t` into list `list(t)`, demonstrating `t` was unaffected.
# • Where it is used:
#   Avoiding bugs caused by attempting to iterate over the same iterator multiple times.
# ------------------------------------------------------------------------------
# by using for loop on exhausted iterator (does not execute since iterator is consumed)
for i in itr_obj:
    print(next(itr_obj))

print(list(t))                          # Result: [11, 22, 33] (converts original tuple to list)
