#Khushi Chhaya
#6/10/21
#we are going to learn about lists and tuples
#learn their funcitons and looping with list
MyFruit=['apples', 'berries', 'mangos', 'banana']
print(MyFruit)
for fruit in MyFruit:
    print(fruit)

for fruit in MyFruit: #for the length of your array
    print(fruit, end= ', ')
counter=len(MyFruit) #lenght of list is one more than last index

for x in range(0,counter-1):
    print(MyFruit[x], end= ', ')

print(MyFruit[counter-1]) #print last term

if 'apples' in MyFruit:
    print('yes you got apples')
    MyFruit.remove('apples')
    print(MyFruit) 

MyFruit.insert(0, 'kiwi')
MyFruit.insert(2, 'papaya')
print(MyFruit)


