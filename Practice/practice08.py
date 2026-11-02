text = "Python Programming Python"
print(len(text))
print(text.count("Python"))
print(text.index("Python"))
t1= text.replace("Python","Java")
print(t1)
t2 = text.lower()
print(t2)
t3 = text.upper()
print(t3)
print(text.startswith("Python"))
print(text.endswith("Python"))
t4 = text.split()
print(t4)
t5="_".join(text.split())
print(t5)
print(text.isalpha())
text2 = "Python123"
print(text2.isalnum())
text3 = "12345"
print(text3.isdigit())
text4 = "PYTHON"
print(text4.isupper())
text5 = "python"
print(text5.islower())