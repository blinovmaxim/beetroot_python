import random
random_list=[]
n=0
while n<10:
    random_value=random.randint(1,100)
    random_list.append(random_value)
    n+=1
print( f"Your random list: ", random_list)
print(f"Maximal value from your list: ",max(random_list)) 