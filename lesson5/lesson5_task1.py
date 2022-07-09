import random
r_number=random.randint(1,10)
u_number=input("Try to guess what number: ")
if  u_number.isdigit():
    if r_number==int(u_number):
        print(f"I made a wish {r_number} , right")
    else:
        print(f"I made a wish {r_number} ! No true, try again!")
else:
     print("Please Enter Integer Number ")
