#Khushi Chhaya
#6/11/21
#word game
#We are creating a list of words 
#randomly select a word from the list of words for the user to guess
#give the user some turns
#show the word to the user with the characters guessed
#Play the game as long as the user has guessed the word or has turns


import random
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
answer=input('Do you want to guess a word? ')
name=input('What is your name? ')
answer=answer.upper()
def updateword(word):
     for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
while 'Y' in answer:
    print('good luck!', name)
    word=random.choice(gameWords)
    counter=len(word)
    turns=10 #should we consider controlling this number? when they miss
    guesses=''
    updateword(word)
    while counter>0 and turns>0:
        newGuess=input('\n\n Give me a letter ') 
        if newGuess not in word:
            turns -=1       #turns=turns-1
            print('wrong! you have', turns, 'turns left')
        else:
            amount=word.count(newGuess)
            counter -=amount
            print('Nice guess!')
        guesses += newGuess #guesses=guesses+newGuess
        updateword(word)
    if counter==0:
        print('\n\n you guessed right!')
    else:
        print('oops! better luck next time')    



    answer=input('would you like to play again? ').upper()
    print(name, ', Thank you for playing!')