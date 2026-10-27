# ==============================================================================
# Module: decorator2.py
# Topic: Universal Decorator Pattern with '*args' and '**kwargs' Across Multiple Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Generic Universal Decorator Boilerplate ('*args', '**kwargs')
# • What is it for:
#   Building a universal wrapper template capable of decorating any target function,
#   regardless of its parameter count, argument types, or invocation signatures.
# • What it does:
#   - Defines `decorator(fun)` where `wrapper(*args, **kwargs)` accepts all positional and keyword inputs.
#   - Executes standardized pre-execution routine: `print("start")`.
#   - Forwards all arguments via `fun(*args, **kwargs)`.
#   - Executes standardized post-execution routine: `print("stop...................")`.
#   - Decorates `f1(10)`, `f2(20, 30)`, and `f3(40, 50, 60)` seamlessly using the same wrapper.
# • Where it is used:
#   Execution timing profilers, audit loggers, transaction management, and exception-handling decorators.
# ------------------------------------------------------------------------------
def decorator(fun):
    def wrapper(*args, **kwargs):
        print("start")                  # Universal pre-action
        fun(*args, **kwargs)            # Generic forwarding of all arguments
        print("stop...................")# Universal post-action
    return wrapper


@decorator
def f1(*args, **kwargs):
    print("function body f1", args)     # Receives single argument tuple: (10,)

@decorator
def f2(*args, **kwargs):
    print("function body f2", args)     # Receives two-element tuple: (20, 30)

@decorator
def f3(*args, **kwargs):
    print("function body f3", args)     # Receives three-element tuple: (40, 50, 60)

f1(10)                                  # Result: start -> function body f1 (10,) -> stop
f2(20, 30)                              # Result: start -> function body f2 (20, 30) -> stop
f3(40, 50, 60)                          # Result: start -> function body f3 (40, 50, 60) -> stop
