
from multiprocessing.sharedctypes import Value


def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def validate(value,*args,**kwargs):
            if type_ == str:
                print("type is str?: ",True)
            else:
                print("Should be string")

            if len(value) > max_length:
                    raise ValueError("Please consider Max length!")
            print("Length is <=15: ",True)
            
            
        return validate
    return wrapper
    




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
create_slogan("Maxim111105@1")