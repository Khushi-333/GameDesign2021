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


while (x !=4): #loop is conditioned to an event\
    x=menu()         #this is a funciton call
    if (x==1):          #if statement are selection or branching(else)
        print("Level 1 Chosen")

    if (x==2):
        print("Level 2 Chosen")

    if (x==3):
        score()
print("Goodbye! Thank you for playing!")
