text = "  Python is FUN, and Python is powerful!  "
t1 = text.strip()
print(t1)
print(text)

count = text.count("Python")
print(count)

first = text.index("Python")
sec = text.index("Python",first+len("Python"))
print(sec)

print(t1 == text)

t2 = text.replace("Python","Java")
print(t2)

t3 = text.replace("FUN","fun")
print(t3)

print(text[::-1])

t4 = text.split()
print(t4)
t5 = "-".join(t4)
print(t5)


a = "Python123"
b = "Python 123"
c = ""

print(a.isalnum())
print(b.isalnum())
print(c.isdigit())

# string are immutable they are not modified in original string if want to modify them we have tod oifya nd store it into the anthor variable than only it is possible
