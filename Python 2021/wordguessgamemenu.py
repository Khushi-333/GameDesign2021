import datetime
import os
import sys
import time
import random

l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - play game       *"
l5="*    2 - get scores      *"
l6="*    3 - Exit            *"
l7="**************************"

def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print('please enter your selection 1-3')
    inputNumber = input()
    x=int(inputNumber)
    return x

x=1 #global variable

def pause():
    print('do you want to try again?')
    confirm=input()
    confirm=confirm.upper()
    if 'Y' in confirm:
        return True
    else:
        return False

     

def wordGame():
    gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
    confirm=input('Are you ready to guess a word?')
    confirm=confirm.upper()
    name=input('What is your name? ')
    score=0
    while 'Y' in confirm:
        def updateword(word):
            for char in word:
                if char in guesses:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
        print('good luck!', name)
        word=random.choice(gameWords)
        counter=len(word)
        turns=10 #should we consider controlling this number? when they miss
        guesses=''
        updateword(word)
        while counter>0 and turns>0:
            newGuess=input('\n\n Give me a letter ') 
            if newGuess not in guesses:
                if newGuess not in word:
                    turns -=1       #turns=turns-1
                    print('wrong! you have', turns, 'turns left')
                else:
                    amount=word.count(newGuess)
                    counter -=amount
                    print('Nice guess!')
                guesses += newGuess #guesses=guesses+newGuess
            else:
                print('you used this one already')
            updateword(word)
        if counter==0:
            print('\n\n you guessed right!')
            score += 1
        else:
            print('oops! better luck next time')
        confirm=input('do you want to guess again?')
        confirm=confirm.upper()
    if 'N' in confirm:
        print('your score is', score)
        date=datetime.datetime.now()
        line=str(date.month)+'/'+str(date.day)+'/'+str(date.year)
        File=open('WordGameScores.txt', 'a')        #append, will add to existing file text
        time.sleep(2)
        newline=('\n\n score:' + str(score) + '    ' + 'name: '+ name + '    ' + 'date: ' + str(line))
        File.write(newline) 
        File.close()

        
        
        
        
        

def option1(): #let the user stay in the level until they want to move
    confirm=True
    while confirm==True:
        confirm=wordGame()
        confirm=pause()

        
        
        

def option2():
    confirm=True
    while confirm==True:
        fileName='WordGameScores.txt'
        PEN=open(fileName, 'r')

        print(PEN.read())
        PEN.close()
        confirm=pause()







while (x !=3): #loop is conditioned to an event\
    x=menu()         #this is a funciton call
    if (x==1):          #if statement are selection or branching(else)
        option1()

    if (x==2):
        option2()


print("Goodbye! Thank you for playing!")