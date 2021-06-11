l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - add element     *"
l5="*    2 - remove element  *"
l6="*    3 - find element    *"
l7="*    4 - find index      *"
l8="*    5 - reverse order   *"
l9="*    6 - Exit            *"
l10="**************************"

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
    print('please enter your selection 1-6')
    inputNumber = input()
    x=int(inputNumber)
    return x

MyShapes=['circle', 'square', 'triangle', 'rectangle', 'trapezoid']

x=1 #global variable

def pause():
    print('do you want to try again?')
    answer1=input()
    answer1=answer1.upper()
    if 'Y' in answer1:
        return True
    else:
        return False
        

def option1(): #let the user stay in the level until they want to move
    confirm=True
    while confirm==True:
        print('INSERTING A TERM')
        print(MyShapes)
        print('choose a term to add to the list')
        add=str(input())
        print('choose a position to insert it from 0-5')
        place=int(input())
        MyShapes.insert(place, add)
        print(MyShapes)
        confirm=pause()

def option2():
    confirm=True
    while confirm==True:
        print('REMOVING A TERM')
        print(MyShapes)
        print('enter a term to remove from the list')
        term=str(input())
        MyShapes.remove(term)
        print(MyShapes)
        confirm=pause()

def option3():
    confirm=True
    while confirm==True:
        print('CONFIRMING A TERM')
        print(MyShapes)
        print('choose the term you want to confirm is in the list')
        term=str(input())
        if term in MyShapes:
            print('True')
        else:
            print('False')
        confirm=pause()

def option4():
    confirm=True
    while confirm==True:
        print('FINDING THE INDEX OF A TERM')
        print(MyShapes)
        print('choose a term in the list to find the index for')
        term=str(input())
        print(MyShapes.index(term))
        confirm=pause()

def option5():
    confirm=True
    while confirm==True:
        print('REVERSING THE LIST')
        print(MyShapes)
        MyShapes.reverse()
        print(MyShapes)
        confirm=pause()




while (x !=6): #loop is conditioned to an event\
    x=menu()         #this is a funciton call
    MyShapes=['circle', 'square', 'triangle', 'rectangle', 'trapezoid']
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


print("Goodbye! Thank you for playing!")