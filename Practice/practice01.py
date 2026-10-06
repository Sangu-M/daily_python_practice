# ==============================================================================
# Module: practice01.py
# Topic: Tracing Program Execution with Python Debugger & While Loop Flow
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Tracing Loop Execution & Debugger Fundamentals
# • What is it for:
#   Understanding execution flow step-by-step, observing variable state transitions,
#   and catching bugs/logical flaws using breakpoints and debugger controls.
# • What it does:
#   - Initializes `i = 0`.
#   - The `while i < 5:` loop prints `i` with a space separator and increments `i += 1`.
#   - When executed with a debugger, pausing at a breakpoint (red dot) lets you inspect
#     the current value of `i` in memory on each step.
# • Where it is used:
#   Diagnosing off-by-one errors, inspecting variable states, tracing complex logic.
# ------------------------------------------------------------------------------

# User Notes & Questions:
# - debugger: tracing the program flow
# - bug or error or flaw: finding unexpected behavior
# - debug: to understand the flow and track execution of the program using the debugger tool
# - search the python debugger and install the extension (debugpy)
# - we can see the icon of debugger (Run and Debug) in the left sidebar
# - steps of configuration of debugger for a single file:
#   1. Click 'Run and Debug' icon (or press Ctrl+Shift+D).
#   2. Click 'Run and Debug' button or choose 'Python Debugger: Debug Python File'.
#   3. Click on the gutter to the left of a line number to set a breakpoint (red dot).
#   4. Use the floating control toolbar: Continue (F5), Step Over (F10), Step Into (F11), Step Out (Shift+F11), Restart, Stop.

i = 0
while i < 5:
    print(i, end=" ")                   # Result: 0 1 2 3 4 
    i += 1
print()

# Terminal debug output trace:
r'''
PS F:\CodePlayground\Python Workspace>  f:; cd 'f:\CodePlayground\Python Workspace'; & 'C:\Users\sanga\AppData\Local\Microsoft\WindowsApps\python3.12.exe' 'c:\Users\sanga\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '61713' '--' 'F:\CodePlayground\Python Workspace\Practice\practice01.py' 
0 1 2 3 4 
PS F:\CodePlayground\Python Workspace> 
'''