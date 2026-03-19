# if statement
# age=int(input("enter your age"))
# if(age>18):
#     print("you are adult")

# if-else statement  
# temperature=int(input("enter the tempearure"))
# if(temperature>25):
#     print("It is a hot day")
# else:
#     print("It is not a hot day")

# if-elif-else statement
# score=int(input("enter the score in numbers"))
# if score >= 90:
#     print("Grade - A")
# elif score>=80:
#     print("Grade - B")
# elif score >= 70:
#     print("Grade - C")
# else:
#     print("Grade - D")

#Nested if-else statement
num=int(input("enter the number"))
if num > 0:
    if(num%2 == 0):
        print("number is even")
    else:
        print("number is  odd")
else:
    if(num == 0):
        print("number is zero")
    else:
        print("number is negative ")        

#Conditional Expression or Ternary Operator

age=18
status="adult" if age>18 else "not Adult"
print(status)
    