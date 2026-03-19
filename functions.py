# functions without parameters

# def greetings():
#     print("hii, I am currently on the way to start something from scratch with some experience ")
# greetings()

# functions with parameters 
# def sum(a,b):
#     result=a+b
#     print(result)
# sum(2,6)

# function without return statement
def sum(a,b):
    result=a+b
    print(result)
    
total=sum(2,3)
print(type(total))

# function to convert celsius to fahrenheit
def cel_to_fahren(cel):
    fahren= ((cel* 9/5) + 32) 
    return fahren
final_temp= cel_to_fahren(45)
print(final_temp)
print(type(final_temp))   


