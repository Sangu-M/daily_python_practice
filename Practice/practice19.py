
# POSITIONAL PARAMETER we are passing inside the function dictlaration in the same way we have passed the argument inside function call and then here position of the parameter matters and also number of parameter are also matters

def func(name,age,hight):
    print(name,age,hight)

# func("sangamesh",23,5.5)

# KEY_WORD ARGUMENT we will pass the argument with key


def student(name, roll_no,age ):
    print(name,roll_no,age)

# student(name="raj",age=16,roll_no=10202651)

#DEFAULT ARGUMENT

def student1(name, roll_no,age,school_name="ADARASHA VIDHAYALAYA " ):
    print(name,roll_no,age,school_name)

# student1("raj",51,age=23)

#VARIABLE LENGTH ARGUMENT

def marks(*args):#here it came and packed again as **args <.....
    print(args)# unpacked                                      |
#                                                              ^
markss = [40,50,60,70,20] # here it is packed as the markss    |
 #                                                             |
marks(*markss)# here it is unpacked like 40,50,60,70,20  ......>
marks(64,65.5,78.8,99)
