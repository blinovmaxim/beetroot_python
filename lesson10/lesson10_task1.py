from inspect import trace


def oops():
    raise IndexError
    
def func1():
    try:
        oops()
    except IndexError:
        print('Caught Index Error')

func1() 