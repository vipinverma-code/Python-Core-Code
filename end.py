print("Just starting the things from basics", end="\n") 
print("evrything is good depending on your thinking process")
# type casting   
# a=2.0
# b=int(a)
# print(b)
# print(type(b))

# a=4
# b=4.0
# print(a+b)

# name=input("enter the name: ")
# print("Hello," + name + "!" )

# x=input("enter first number:")
# y=input("enter second number:")
# z=x+y
# print(z)

# my_dictionary={'name':'Vipin Verma','profession':'sotware engineer'}
# print(my_dictionary)

# List=[1,2,3,'Vipin',{'name':'Vipin'}]
# print(List)

# name=input("enter the student name")
# marks1=int(input("enter the marks"))
# marks2=int(input("enter the marks"))
# marks3=int(input("enter the marks "))
# total_marks= marks1 + marks2 + marks3
# percentage=(total_marks/300)*100
# print(f"{name} has got {percentage}% marks. Well done enjoy and explore ")


# Q.2.
# user_data={}
# user_data['name']=input("enter the name")
# user_data['age']=int(input("enter the age"))
# user_data['height']=float(input("enter the height"))
# user_data['student_status']=input("enter the status of student")
# print(user_data)

# list me ye ho skta hai 
# list=[]
# name=input("enter the name")
# age=int(input('enter the age'))
# height=float(input("enter the height"))
# student_status=input("enter student status")
# list.append(name)
# list.append(age)
# list.append(height)
# list.append(student_status)
# print(list)
# check the given year is leap year or not
year=int(input("enter the year which you have to check"))
if(year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
    print(f"entered {year} is a leap year")
else:
     print(f"enterd {year} is not a leap year")