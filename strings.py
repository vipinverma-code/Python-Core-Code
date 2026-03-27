# Strings in python
name = "Madhav" #creating a string
print(name)
print(type(name)) #checking data type

#String formatting ways 

#1. Old string formatting way

name="Vipin Verma"
age = 22
print("My name is %s and I'm %d" % (name,age)) # %s and %d are placeholders for the string and integers

#2. str.format() method

name1 = "Ankit Verma"
age1=24
print("my name is {} and I'm {} years old".format(name1,age1)) 


# escape characters

print("Hello \n World!")
print("My name is Vipin\tVerma")
print(" \"Hello Vipin Bhai \" ")
print(" \' Hello Vipin Bro \' ")


# String operators in python 

a="Hello"
b="Python"
print(a+b)
print(a*2)

# slice and range operator [] and [:]   --scroll below
# in and not in membership operator 

if "H" in a:
    print("Yes")
else:
    print("No")
    
#
if "h" in a:
    print("Yes")
else:
    print("no")

# Slice operator 
print(a[1])
print(a[2])
print(a[1:4])


