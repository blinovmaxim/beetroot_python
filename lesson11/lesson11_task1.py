from math import degrees
from re import L


def create_file():

    with open("myfile.txt",'w') as file:
        file.write("Hello file world!\n")

def open_file():
    with open("myfile.txt",'r') as file:
        data=file.read()
        print(data)


create_file()
open_file()
