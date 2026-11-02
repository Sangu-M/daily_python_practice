marks = []

physics = int(input("Enter marks for Physics: "))
while physics < 0 or physics > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    physics = int(input("Enter marks for Physics: "))

maths = int(input("Enter marks for Maths: "))
while maths < 0 or maths > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    maths = int(input("Enter marks for Maths: "))

chemistry = int(input("Enter marks for Chemistry: "))
while chemistry < 0 or chemistry > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    chemistry = int(input("Enter marks for Chemistry: "))

biology = int(input("Enter marks for Biology: "))
while biology < 0 or biology > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    biology = int(input("Enter marks for Biology: "))

english = int(input("Enter marks for English: "))
while english < 0 or english > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    english = int(input("Enter marks for English: "))

marks.append(physics)
marks.append(maths)
marks.append(chemistry)
marks.append(biology)
marks.append(english)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

