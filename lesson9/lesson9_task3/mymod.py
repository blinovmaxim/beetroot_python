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



# def test(name):
# .split('\n')
# .rstrip('\n')
#  liness=0
#         for liness in f:
#             symbols=len(f.read().split('\n'))

# filename="C:\python\lesson9\lesson9_task3\primer.txt"
# with open(filename, 'r') as file:
#         lines = len(file.readlines())
# print('Total Number of lines:', lines)

# from importlib.resources import path
# import os
# path=os.getcwd()
# print(path)
