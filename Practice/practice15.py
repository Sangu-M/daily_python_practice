s1 = "Python is easy and python is powerful "
s2 = s1.split()
dict = {}
l1 = []
print(s2)
for i in s2:
    count = s1.count(i)
    dict[i]= count
# for key,values in dict:
#     maxi = max(dict[values])
#     l1.append(dict(maxi))

print(len(s2))
print(l1)
print(dict.items())
