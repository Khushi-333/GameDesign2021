#Khushi Chhaya 6/14/2021
#Learn how to use files
import os
import sys
import time

#using time to pause your games

print (' hello')
time.sleep(2)       #5 second delay
print (' there')
def readFile():
    file=input('What is the name of the file?')
    if os.path.exists(file):
        #opens the file
        PEN=open(file, 'r')
        #prints the whole file
        print(PEN.read())
        PEN.close() #always close after finished
    else:
        print('the file does not exist thank you')
fileName='KhushiGame.txt'
if os.path.exists(fileName):
    print('sorry that file already exists')
else:
    FILE=open(fileName, 'w')
    FILE.write("********** THIS IS KHUSHI'S FILE **********")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.read())
    FILE.close()
File=open('KhushiGame.txt', 'a')
newline='\n \n Whatever     or else'
File.write(newline)

