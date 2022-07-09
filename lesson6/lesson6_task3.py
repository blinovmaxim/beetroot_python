list1=[]
list2=[]
n=1
i=0
while n<=100:
    list1.append(n)
    n+=1
    while i<len(list1):
        if (list1[i])%7==0 and (list1[i])%5!=0 :
            list2.append(list1[i])
        i+=1
print( f"Your first list: ",list1)
print(f"New list, Integer divisible by 7 but not a multiple of 5: ",list2)
