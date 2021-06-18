#Khushi Chhaya
#6/08/21
#Modifying Quentin's code
#if conditional
#funciton pieces of code that we can reuse
#to declare a function, must define function (keyword def), then name
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - capitalize      *"
l5="*    2 - upper           *"
l6="*    3 - lowercase       *"
l7="*    4 - find index      *"
l8="*    5 - split           *"
l9="*    6 - translate       *"
l10="*   7 - Exit            *"
l11="**************************"

def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)
    print(l11)
    print('please enter your selection 1-7')
    inputNumber = input()
    x=int(inputNumber)
    return x

x=1 #global variable

def pause():
    print('press enter to continue')
    input()

def option1(): #let the user stay in the level until they want to move
    print('enter a lowercase phrase')
    phrase=str(input())
    capphrase=phrase.capitalize()
    print(capphrase)
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option1()
    if (answer=='NO'):
        pause()

def option2():
    print('enter a lowercase phrase')
    phrase=str(input())
    upphrase=phrase.upper()
    print(upphrase)
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option2()
    if (answer=='NO'):
        pause()

def option3():
    print('enter an uppercase phrase')
    phrase=str(input())
    lowphrase=phrase.lower()
    print(lowphrase)
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option3()
    if (answer=='NO'):
        pause()

def option4():
    print('enter a phrase containing the word "cat"')
    phrase=str(input())
    indphrase=phrase.index('cat')
    print(indphrase)
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option4()
    if (answer=='NO'):
        pause()

def option5():
    print('enter a phrase with 2 or more words')
    phrase=str(input())
    splitphrase=phrase.split()
    print(splitphrase)
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option5()
    if (answer=='NO'):
        pause()

def option6():
    print('enter a phrase')
    phrase=input()
    x='abcdefghijklmnopqrstuvwxyz'
    y='zyxwvutsrqponmlkjihgfedcba'
    mytable=phrase.maketrans(x,y)
    print(phrase.translate(mytable))
    print('would you like to try again? YES or NO')
    answer=str(input())
    if (answer=='YES'):
        option6()
    if (answer=='NO'):
        pause()



while (x !=7): #loop is conditioned to an event\
    x=menu()         #this is a funciton call
    if (x==1):          #if statement are selection or branching(else)
        option1()

    if (x==2):
        option2()

    if (x==3):
        option3()

    if (x==4):
        option4()

    if (x==5):
        option5()

    if (x==6):
        option6()

print("Goodbye! Thank you for playing!")
