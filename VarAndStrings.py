#Khushi Chhaya
#6/07/21
#We are learning how to work with strings
#While loop
#Different types of var

num1=19
num2=3.5
num3=0xADEFFEDBCCCAA478752639
print(type(num1)) #How to know what type of data
print(type(num2))
print(type(num3))
phrase='Hello there!'
print(type(phrase))
#String functions
print(phrase[0:]) #Each character is assigned a number
print(phrase[3:6]) #Range begininning inclusive, ending not
print(phrase[6:]) #No end range = to end
print(phrase*2) #print it twice
#concadenation --> joining strings
phrase = phrase + 'Goodbye'
while 'there' in phrase: #There always in phrase, never stop
    print('there' in phrase)
    phrase='change'
print(phrase)
word1='vanilla '
word2='chocolate '
word3='strawberry '
print(word1)
print(word2)
print(word3)
onetwo=word1+word2
print(onetwo)
twothree=word2+word3
print(twothree)
all=word1+word2+word3
print(all)
