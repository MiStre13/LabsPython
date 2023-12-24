import os

def read_from_last(lines, fle):
    fl = fle.readlines()
    size= len(fl)
    for i in range(size-lines,size):
        print(fl[i])


file1 = open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr8/sample.txt','r+')
print(read_from_last(3,file1))
