print("Hello World")
instructor="Vipin Verma "
print("Python by", instructor ,sep="_")

list=[1,2,3,4,5,'Akash']
list[0]=5
print(list) #list are mutable
print(type(list))

tuple=(1,2,3,)
# tuple(0)="Vipin"  #tuples are immutable
print(tuple)

# assignment-1
print(''' Python is fun.\n "Quotes" and 'single quotes' can be tricky.''')  #\n is used to print the tex from the new line
# Q2
name="Akash"
age=22
city="Lakhimpur-Kheri"
print(f"Business Owner is {name} and age is {age} and location is {city}") 

# type casting 
a=1
b="2"
b=int(b)
print(a+b)
#Implicit type conversion
a=2
b=2.5
print(a+b)
# Assignment2 

# student_name= input("enter the name ")
# maths=int(input("enter the marks"))
# science=int(input("enter the marks"))
# english=int(input("enter the marks"))
# percentage=(maths+science+english)/300 * 100
# print(f"{student_name } got {percentage} marks")  

#Assignment 2 Question2 
# name=input("enter the name ")
# age=int(input("enter the age"))
# height=float(input("enter the height"))
# student_status=bool(input("enter the status"))
# collected_data=dict(name,age,height,)

user_data={}
user_data['name']= input("enter the name")
user_data['age']= int(input("enter the age"))
user_data['height']=float(input("enter the height"))
user_data['status']=input("Are you student:Yes/No")
print(user_data)
