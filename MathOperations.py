#Khushi Chhaya
#6/04/2021
#I am going to make tables for all four math operations
#Based on user input for base
print ('what is the base?')
base=int(input())
print ()
print ('addition table for', base)
for add in range (1,11):
    result = (add + base)
    print (add, '+', base, '=', result)
print ()
print ('subtraction table for', base)
for sub in range (1,11):
    result = (sub - base)
    print (sub, '-', base, '=', result)
print ()
print ('multiplication table for', base)
for mult in range (1,11):
    result = (mult * base)
    print (mult, 'x', base, '=', result)
print ()
print ('division table for', base)
for div in range (1,11):
    result = (div / base)
    print (div, '/', base, '=', result)
print ()