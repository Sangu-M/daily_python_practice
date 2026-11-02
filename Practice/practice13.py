text = "  python Developer, PYTHON learner; python Engineer  "
word = "banana"
text2 = "mississippi"
phrase = "artificial intelligence machine learning"

t1= text.strip()
t2 = t1.split()
count1 = len(t2)
print(count1)

for word in t2:
    w=word.split(",:")
    print(w)
    print(len())