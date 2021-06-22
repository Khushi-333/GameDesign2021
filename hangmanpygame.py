#KhushiChhaya
#create a hangman version of the game
#use umages in a list
#use fonts, render

import pygame, math, random, sys, time, os

from pygame.constants import TIMER_RESOLUTION

pygame.init()

#create our window

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman Game')
#Define colors
WHITE=[255,255,255]
BLACK=[0,0,0]
screen.fill(WHITE)

#Load images
images = []
for turns in range(7):
    image = pygame.image.load('Images/hangman'+str(turns)+'.png')
    images.append(image)
screen.blit(images[turns],(70,200))
    

#words list
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
#set up fonts
TitleFont = pygame.font.SysFont('comicsans', 70)
WordFont = pygame.font.SysFont('comicsans', 50)
def updateScreen():
    screen.fill(WHITE)
    screen.blit(images[turns], (70,200))
    pygame.display.update()
    pygame.time.delay(500)
    textword=WordFont.render(word, 1, BLACK)
    text = TitleFont.render('HANGMAN', 1, BLACK)
    centerTitle = WIDTH/2-text.get_width()/2    #gets the width of my screen/2 - width of our text/2
    screen.blit(text, (centerTitle,20))
    screen.blit(textword, (400,300))
    screen.blit(images[turns], (70,200))
def updateWord(word, guesses):  # function with a parameter to update word
    displayWord=' '
    screen.fill(WHITE)
    pygame.display.update()
    for char in word:
        if char in guesses:
            print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_ "
            print('_', end =' ')
    

check = True
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
    word=random.choice(gameWords)
    displayWord=updateWord()
    updateWord(displayWord, turns)
    counter=len(word)
    turns=0 #should we consider controlling this number? when they miss
    guesses=''  
    while counter>0 and turns<7:
        newGuess=input("\n\n Give me a letter ")
            #check that the new letter has not been used before
        if newGuess not in guesses:
            if newGuess not in word:
                turns +=1    #       turns = turns -1
                print("Wrong! You have  ", turns, "guesses left")
            else:
                counter -=word.count(newGuess) #deleten repeated letters
                print("nice guess!")
            guesses += newGuess 
        else:
            print("you used this one already")
            updateWord(word, guesses)
            #end of whole loop with 
    pygame.display.flip()
pygame.quit()
sys.exit()
