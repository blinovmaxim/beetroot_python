name=input("What is your name?: ")
age=input("What ius your age?: ")
if not age.isdigit():
    print("Age should be an Integer!")
else:
    print(f"Hello, {name}, on yuor next birthday you'll be {(int(age)+1)} years")