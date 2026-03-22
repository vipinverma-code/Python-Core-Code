# Arguments in functions 

#1.  Required Arguments (single/multiple arguments)

# def greetings(name):
#     print("Hello ", name, "!")
# # greetings("Vipin Verma")
# greetings() 

# 2 . Default Arguments    

def greet(name = "World"):
     print("Hello" , name, "!") #World is a default value
greet()
greet("Swastika")    #when you pass argument it overwrites the defualt value , it will consider passed value 