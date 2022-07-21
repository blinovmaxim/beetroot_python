def func ():
    try:
        a=int(input("Enter first number 'a': "))
        b=int(input("Enter ssecond Number 'b': "))
        c=a**2/b
        print("Result: ",c)
    except ValueError:
        print("Not numbers, please Enter first and second numbers: ")
    except ZeroDivisionError:
        print("oops, divizion by 0")
   
    
func()
   
   