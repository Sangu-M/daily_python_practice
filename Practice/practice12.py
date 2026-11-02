text = "  python Developer, PYTHON learner; python Engineer  "

t1 = text.strip()
print(len(t1))

c1 = text.count("python")
print(c1)
c2 = text.count("PYTHON")
print(c2)
print(c1+c2)

t3 = text[9:18]
print(t3)
#Q4 NOT GETTING EXPLAIN IT CLEARLY AND PROPERLY

t5=t1.lower()
print(t5)

t6 = t5.replace("python","java")
print(t6)

t7 = t1.split()
t8 = t7[::-1]
t9 = " ".join(t8)
print(t7)
print(t8)
print(t9)

s1 = "artificial intelligence machine learning"
s2 = s1.title()
print(s2)
s3=s2.split()
print(s2[0],s2[11],s2[24],s2[32],end="")
# i have tried please tell me this correctly

st1 = "Never odd or even"
st2 = st1.lower()
print(st2)
st3 = st2.split()
st4 = "".join(st3)
print(st4)
st5 = st4[::-1]
print(st5)
print(st5==st4)

s = int()
word = "banana"
for w in word:
    s = word.count(w)
    print(w , s)
    

str1= "mississippi"
set1 = set(str1)
str2 = str(set1)
str3 = "".join(str2)
print(str3)
# if anthing wwrond teach me properly

# by using the index or the in method or keyword we will use and find the substring is there or not but using the count method we will cout mhow many time the subdsting or charected is repeted we will calculate