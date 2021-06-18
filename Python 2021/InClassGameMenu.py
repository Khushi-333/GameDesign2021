#Khushi Chhaya
#6/08/21
#Modifying Quentin's code
#if conditional
#funciton pieces of code that we can reuse
#to declare a function, must define function (keyword def), then name
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - Level1          *"
l5="*    2 - Level2          *"
l6="*    3 - Scores          *"
l7="*    4 - Exit Game       *"
l8="**************************"
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print('please enter your selection 1-4')
    inputNumber = input()
    x=int(inputNumber)
    return x
def score():
    print("Scores Chosen")
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)
x=1 #global variable
def pause():
    print('press enter to continue')
    input()

while (x !=4): #loop is conditioned to an event\
    x=menu()         #this is a funciton call
    if (x==1):          #if statement are selection or branching(else)
        print("Level 1 Chosen")
        print('Practice:')
        print('press spacebar to jump')
        space=str(input()) #input is a function
        jump=space.isspace() #isspace is a method of strings (smaller part of bigger thing) have to refer with a .
        print(jump) #update variable to new value if dont need original. can print (var.upper() if want to keep original answer
        print('enter nickname:')
        name=str(input())
        z=name.upper()
        print('NAME:', z)
        z=name.isalpha()
        print(z)
        pause()

    if (x==2):
        print("Level 2 Chosen")
        print('Practice:')
        print('press number 3 key to duck')
        three=str(input())
        duck=three.isnumeric()
        print(duck)
        print('enter nickname:')
        name=str(input())
        z=name.upper()
        print('NAME:', z)
        z=name.isalpha()
        print(z)
        pause()

    if (x==3):
        score()
        print('enter age:')
        a=str(input())
        b=a.isdigit()
        print(b)
        pause()

print("Goodbye! Thank you for playing!")
