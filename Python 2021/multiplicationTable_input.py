#KhushiChhaya
#6/04/2021
#We are going to print multiplication tables
#Ask use which table
#input --> input()
print ('what is the base?')
base=int(input())
print ()
print ('multiplication table', base)
print ()
for var in range (1,11):
    result = (base * var)
    print (base, 'x', var, '=', result)
print ()


