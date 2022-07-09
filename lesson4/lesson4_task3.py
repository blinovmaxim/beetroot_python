import random

r_number1=random.randint(1,10)
r_number2=random.randint(1,10)
#answer for a mathematical expression "*"
answer=input("How much "+str(r_number1)+'*'+str(r_number2)+ '? ')
if answer==str((r_number1*r_number2) ):
    print("right")
else:
    print("no, go learn")
#answer for a mathematical expression "+"
answer=input("How much "+str(r_number1)+'+'+str(r_number2)+ '? ')
if answer==str((r_number1+r_number2) ):
    print("right")
else:
    print("no, go learn")