from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(func.__name__,"called with",args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

if __name__ == "__main__":
    add(4,7)
    square_all(5,7,9,0)



