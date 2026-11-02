text = "  Hello Python  "
t1 = text.strip()
print(t1)
print(t1.startswith("hello"))
print(text.count("Python"))
t2 = text.replace("Python","Java")
print(t2)
print(t2.index("Java"))
print("Java" in text)
t3 = text.title()
print(t3)
t8=t3[::-1]
print(t8)
t4 = "123"
print(t4.isdigit())
t5 = "12.3"
print(t5.isdigit())
t6 = ""
print(t6.isalpha())
# string is a immutableclass so it cant be changed if we want to change it it will return new string
