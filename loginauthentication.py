predefined_username="Vipin Verma"
predefined_password= 123456
username=input("enter the username")
password=input("enter the passord")
if(username == predefined_username):
    if(password == predefined_password):
        print("Login successful")
    else:
        print("password do not match" )
else:
    print("username is incorrect")        