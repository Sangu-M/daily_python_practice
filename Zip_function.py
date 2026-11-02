# ==============================================================================
# Module: Zip_function.py
# Topic: Built-in 'zip()' Function, Multi-Iterable Pairing & Dictionary Integration
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Built-in 'zip()' Object Initialization & Iterator Traversal ('next()')
# Syntax: zip(*iterables)
# • What is it for:
#   Aggregating elements from two or more iterables into paired tuples on-demand,
#   without loading everything into memory at once.
# • What it does:
#   - Takes `names = ["amy", "ben", "chad", "duke"]` (4 items) and `score = [90, 80, 100, 30, 70]` (5 items).
#   - Returns a lazy `<zip object>` iterator.
#   - Each call to `next(zip_obj)` yields the next paired 2-tuple: `('amy', 90)`, `('ben', 80)`, etc.
#   - Automatically stops when the shortest collection is exhausted (stops at 4 pairs; 70 is omitted).
# • Where it is used:
#   Parallel iteration, combining separate header and value columns, and pairing IDs with records.
# • Key Takeaway:
#   `zip()` returns a lazy iterator; it only evaluates elements when requested and stops at the shortest input.
# ------------------------------------------------------------------------------
names = ["amy", "ben", "chad", "duke"]
score = [90, 80, 100, 30, 70]
rolls = [1, 2, 3, 4]

zip_obj = zip(names, score)
print(zip_obj)             # Result: <zip object at 0x...>

# It stops for the shortest iterable or shortest collection
print("------------------------------------")
print(next(zip_obj))       # Result: ('amy', 90)
print(next(zip_obj))       # Result: ('ben', 80)
print(next(zip_obj))       # Result: ('chad', 100)
print(next(zip_obj))       # Result: ('duke', 30)

print("------------------------------------")

# ------------------------------------------------------------------------------
# 2. Multi-Collection Zipping & Concrete List Materialization
# Syntax: list(zip(iterable1, iterable2, iterable3, ...))
# • What is it for:
#   Combining three or more parallel collections into a single materialized list
#   of grouped tuples.
# • What it does:
#   - Groups corresponding elements from `names`, `score`, and `rolls` into 3-tuples.
#   - Converts the iterator directly into a Python list using `list()`.
# • Where it is used:
#   Constructing tabular datasets, preparing database insert batches, and multi-sensor readings.
# • Key Takeaway:
#   Casting with `list()` immediately exhausts the zip iterator and stores all tuples in memory.
# ------------------------------------------------------------------------------
print(list(zip(names, score, rolls)))
# Result: [('amy', 90, 1), ('ben', 80, 2), ('chad', 100, 3), ('duke', 30, 4)]

print("------------------------------------")

# ------------------------------------------------------------------------------
# 3. Traversing Paired Tuples with a 'for' Loop
# Syntax: for item in zip(iterable1, iterable2, ...):
# • What is it for:
#   Iterating over multiple sequences simultaneously in lockstep without maintaining
#   manual integer index counters (`range(len(...))`).
# • What it does:
#   - In each iteration, unpacks or accesses the current matched tuple `(name, score, roll)`.
#   - Prints each tuple cleanly on a new line.
# • Where it is used:
#   Simultaneous logging, multi-list comparisons, updating matched pairs in place.
# • Key Takeaway:
#   Looping directly over `zip()` is idiomatic Python and much cleaner than `list[index]`.
# ------------------------------------------------------------------------------
for i in zip(names, score, rolls):
    print(i)
# Result:
# ('amy', 90, 1)
# ('ben', 80, 2)
# ('chad', 100, 3)
# ('duke', 30, 4)

print("------------------------------------")

# ------------------------------------------------------------------------------
# 4. Combining 'zip()' with Dictionary Comprehension & Ternary Logic
# Syntax: {k: (val_true if cond else val_false) for k, val in zip(keys, values)}
# • What is it for:
#   Building a dictionary directly from two separate lists while applying inline
#   conditional transformation logic on the fly.
# • What it does:
#   - Unpacks `name` and `score` from `zip(names, score)`.
#   - Evaluates ternary condition: if `score > 35` assigns `"Pass"`, else `"Fail"`.
#   - Maps `names` to passing status: amy, ben, chad Pass; duke (30) Fails.
# • Where it is used:
#   Merging student rosters with score sheets, parsing CSV columns into dictionaries,
#   and real-time status reporting.
# • Key Takeaway:
#   `zip()` combined with dictionary comprehension is the most pythonic way to create
#   a dictionary from two parallel sequences.
# ------------------------------------------------------------------------------
d3 = {name: ("Pass" if score > 35 else "Fail") for name, score in zip(names, score)}
print(d3)                  # Result: {'amy': 'Pass', 'ben': 'Pass', 'chad': 'Pass', 'duke': 'Fail'}
