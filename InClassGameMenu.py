#Khushi Chhaya
#6/08/21
#Modifying Quentin's code
#if conditional
#funciton pieces of code that we can reuse
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - Level1          *"
l5="*    2 - Level2          *"
l6="*    3 - Scores          *"
l7="*    4 - Exit Game       *"
l8="**************************"
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)
print('please enter your selection 1-4')
x=int(input())
while x is not '4': #loop is conditioned to an event
    if x is '1':          #if statement are selection or branching(else)
        print("Level 1 Chosen")
    if x is '2':
        print("Level 2 Chosen")
    if x is '3':
        print("Scores Chosen")
        print(l1)
        print("*        Scores          *")
        print(l3)
        print("*    1 - ???- 999        *")
        print("*    2 - ???- 876        *")
        print("*    3 - ???- 745        *")
        print(l3)
        print(l8)
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print('please enter your selection 1-4')
    x=int(input())
if x is '4':
    print("Goodbye! Thank you for playing!")
