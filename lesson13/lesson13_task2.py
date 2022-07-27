def sum(a):
    def add(b):
        return a+b
    return add


a=int(input("Введи число a: "))
test=sum(a)

b=int(input("Введи второе число b: "))
print('сумма = ',test(b))
