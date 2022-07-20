import os
import sys



def count_lines(name):
    with open(name, 'r') as file:
        
        lines = len(file.readlines())
        
    print('Total Number of lines:', lines)

def count_chars(name): 
    with open(name, 'r') as f:
        
        symbols=len(f.read())
        
    print('Total chars of lines:', symbols)

def  test(name):
    count_lines(name)
    count_chars(name)
if __name__ == '__main__':
    import sys
    test(sys.argv[1])



