import random
first_random_list=[]
n=0
while n<10:
    random_value=random.randint(1,10)
    first_random_list.append(random_value)
    n+=1
n=0
second_random_list=[]
while n<10:
    random_value=random.randint(1,10)
    second_random_list.append(random_value)
    n+=1

intersection_list=list(set(first_random_list).intersection(set(second_random_list)))

print( f"Your random list: ", first_random_list)
print( f"Your random list: ", second_random_list)
print( f"Your intersection from  lists: ", intersection_list)
