#Khushi Chhaya
#6/16/2021
#learn how to open read files
#how to read files per line
#how to make list from file
#how to manipulate the element to find what we need
import abc
import os
import sys
import time
file='practice1.txt'
FILE=open(file, 'r')
content=FILE.read() #is string with full content of the file
print(content)
FILE.close()

FILE=open(file, 'r') #close and reopen for second command
content_list=FILE.readlines() #is a list of each line of the text file
print(content_list)
FILE.close()
for element in content_list:
    print('line :', element)
    elem_list=element.split()
    print(elem_list)
    time.sleep(1)

def my_sort(line):
    line_fields = line.strip().split(',')
    amount = (line_fields[-1])
    return amount

fp=open('practice1.txt')
stuff=fp.readlines()
stuff.sort(key=my_sort)
for line in stuff:
    print(line)

fp.close()





scoredat="WordGameScores.txt" 
def pause():
    print("Press enter to continue:") 
    input() 
print("Scores Chosen") 
with open(scoredat, 'r') as first_file:
    rows=first_file.readlines()
    sorted_rows=sorted(rows,key=lambda abc:(abc.split()),reverse=True)
    with open(scoredat, 'w+') as second_file:
        for row in sorted_rows:
            second_file.write(row)
first_file.close() 
second_file.close() 
writenScores=open(scoredat, 'r')
displayScores=writenScores.read() 
print(displayScores) 
writenScores.close() 
pause() 