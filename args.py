# Arguments in functions 

#1.  Required Arguments (single/multiple arguments)

# def greetings(name):
#     print("Hello ", name, "!")
# # greetings("Vipin Verma")
# greetings() 

# 2 . Default Arguments    

# def greet(name = "World"):
#      print("Hello" , name, "!") #World is a default value
# greet()
# greet("Swastika")    #when you pass argument it overwrites the defualt value , it will consider passed value 

# 3 . Keyword Arguments 

# def sum(a,b):
#     return a+b
# result1=sum(30,20) # positional arguments 
# result2 =sum(a=25,b=30) # Keyword Arguments
# print(result1)
# print(result2)

#4. Arbitrary positional arguments

def sum_numbers(*args):
    return sum(args)
result3=sum_numbers(1,2,3,4,5)
print(result3) 


#ex-2
# def greet(*names):
#     for name in names:
#         print(f" Hello,{name}!")
# greet("Vipin",'Sanskar','Deepak')    

def greet(*names):
    for name in names:
        print(f"Hello! {name}")
greet("Vipin", "Swastika") 

def print_data(**kwargs):
     for key, value in kwargs.items():
         print(f"{key}:{value}")
print_data(name="Vipin Verma", age=26, city="Delhi")


# Arbitrary keyword arguments second example

def shopping_cart_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
shopping_cart_details(total=250, name_billing="Vipin Verma") 
        