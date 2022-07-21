import os
import sys

from pyparsing import line



def count_lines(name):
    with open(name, 'r') as file:
        
        lines = len(file.readlines())
        
    print('Total Number of lines:', lines)

def count_chars(name): 
    with open(name, 'r') as f:                             
        while True:                         
            symbols=len((f.readline()).rstrip('\n'))
            if not symbols:
                break
            print('Total chars of line:', symbols)

def  test(name):
    count_lines(name)
    count_chars(name)
    

test('example.txt')

