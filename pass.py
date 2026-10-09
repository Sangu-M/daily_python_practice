# ==============================================================================
# Module: pass.py
# Topic: Placeholder Statement ('pass') in Control Flow Blocks
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. The 'pass' Statement as a Syntactic Placeholder in Loops
# • What is it for:
#   Providing a syntactically valid null operation or placeholder inside a block
#   where statement syntax requires at least one indented line, but no action is needed yet.
# • What it does:
#   - Iterates through the list of `names`.
#   - Executes `pass` for every element, which performs no operation (no-op).
#   - Prevents `IndentationError` or syntax errors that would occur if the loop body was left empty.
# • Where it is used:
#   Stubbing out unimplemented functions/classes, temporary empty loop bodies during development,
#   and defining minimal exception classes.
# ------------------------------------------------------------------------------
names = ["MrSmith","MrsRao","MrJohn","MrsAdithi","MrsAmy","KrGanesh"]
for name in names:
    pass                                # Result: no operation performed for each element


print("----------------------------------------------------")
# cant leave it empty ,if it is empty it wont be execute
