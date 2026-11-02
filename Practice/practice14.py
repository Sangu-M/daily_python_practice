n = 5
l = [0,1]
result = 0

for i in range(n-2):
    result = l[i] + l[i+1]
    l.append(result)
print(l[-1])
