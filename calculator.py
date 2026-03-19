# 3 steps to build a simple calculator program
# 1. functions for operations
# 2. user input
# 3. print result


#function to add two numbers
def add(num1,num2):
    return num1 + num2

# function to subtract numbers

def sub(num1,num2):
    return num1-num2

#function to multiply

def mul(num1,num2):
    return num1 * num2

# function to division
def div(num1,num2):
    return num1/num2

# function to average

def average( num1,num2):
    return (num1+num2)/2

# now we take input from user
print("Select the opeartion which you want to perform \n" \
    "1. Addition \n"
    "2. Subtraction \n" \
    "3. Multiplication\n" \
    "4. Division\n"\
    "5. Average\n")

select=int(input("Select a operation from 1,2,3,4,5"))

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number: "))

#Step3 . Print the result

if select == 1:
    print(f"the sum of {num1} and {num2} is:", add(num1,num2))

elif(select == 2):
        print(f"the subtraction of {num1} and {num2} is:", sub(num1,num2))

elif(select == 3):
       print(f"the multiplication of {num1} and {num2} is:", mul(num1,num2))

elif(select == 4):
    print(f"the division of {num1} and {num2} is:", div(num1,num2))

elif(select == 5):
    print(f"the average of {num1} and {num2} is:", average(num1,num2))
else:
    print("entered operation is incorrect")          