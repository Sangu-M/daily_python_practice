import copy
l = [10,20,30,[40,50]]
l1 = copy.copy(l)




l2 = copy.deepcopy(l)
l[3].append(100)
l.append(80)
# print(l2)
print(l)
print("shallow copy it wont creates the inner list  as the separate address",l1)
print("deep copy it create separate adress for each element",l2)
