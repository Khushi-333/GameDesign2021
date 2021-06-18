#Khushi Chhaya
#6/10/21
#we are going to learn about lists and tuples
#learn their funcitons and looping with list

# HOW to use a module or library
import random 

MyFruit=['apples', 'berries', 'mangos', 'banana']
print(MyFruit)
for fruit in MyFruit:
    print(fruit)

for fruit in MyFruit: #for the length of your array
    print(fruit, end= ', ')
counter=len(MyFruit) #lenght of list is one more than last index
index=random.randint(0,counter-1)
print('your lucky fruit is', MyFruit[index])
for x in range(0,counter-1):
    print(MyFruit[x], end= ', ')

#random method choice()
word=random.choice(MyFruit)
print('your random fruit is', word)

print(MyFruit[counter-1]) #print last term

if 'apples' in MyFruit:
    print('yes you got apples')
    MyFruit.remove('apples')
    print(MyFruit) 

MyFruit.insert(0, 'kiwi')
MyFruit.insert(2, 'papaya')
print(MyFruit)

#tuple is a list that is unchangeable
fruity=('apple', 'pears', 'banana')
print(fruity)
temp=list(fruity) #convert to list to modify
print(temp)
temp.insert(3, 'mango')
fruity=tuple(temp)
print('tuple', fruity)
print('list', temp)
for element in fruity:
    print(element)