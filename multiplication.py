#Khushi Chhaya
#We are going to print a multiplication table for 2
#Using print statements
#Input --> variables is a container to keep data 
#And they need to have valid and unique name they will have unique address
base = 2
var2 = 7
print (1 * base)
print (2 * base)
print (3 * base)
print (4 * base)
print (5 * base)
print (6 * base)
print (7 * base)
print (8 * base)
print (9 * base)
print (10 * base)
#Repetition I should think looping exact number FOR statement
for i in range(1,11): #Beginning of is included, end of range is not
    print (i * base)
base =3
print()
for i in range(1,11): #Beginning of is included, end of range is not
    print (i * base)
base =4 
print()
for i in range(11): #Beginning of is included, end of range is not
    print (i * base)
    #When we have seberal repatition we can use veral loop
    #Sometimes they can be nested loops
for var in range (2,11):
    for i in range(1,11):
        print(i * var, end= '   ')
    print()