import random
import string

user_stroka=input("Enter srting: ")
for symbol in user_stroka:
    print(" ".join(random.choices(user_stroka,k=len(user_stroka))) )
