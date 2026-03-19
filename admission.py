maths_marks=int(input("enter the maths marks"))
physics_marks=int(input("enter the physics marks"))
chemistry_marks=int(input("enter the chemistry marks"))
total_marks= maths_marks + physics_marks + chemistry_marks
if(total_marks>=180) or (maths_marks +  physics_marks >=140):
    print("student is eligible for student")
else:
    print("student is not eligible ")
