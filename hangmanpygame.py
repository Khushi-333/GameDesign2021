#KhushiChhaya
#create a hangman version of the game
#use umages in a list
#use fonts, render

import pygame, math, random, sys, time, os

 
#os.system('cls')
pygame.init()

 
#create our screen or window

 
WIDTH=800
HEIGHT=500
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Hangman Game!")

 
# Define Colors
WHITE=[255,255,255]
BLACK=[0,0,0]

 
# Load images
images = []
screen.fill(WHITE)
for turns in range(7):
 image= pygame.image.load("Images/hangman"+str(turns)+ ".png")
 images.append(image) 
 # screen.blit(images[i],(80,100))
 # pygame.display.update()
 # pygame.time.delay(500)
# Words list
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

 
#Set up fonts
TitleFont = pygame.font.SysFont("comicsans", 70)
WordFont = pygame.font.SysFont("comicsans", 50)
# function to update game and screen
def updateScreen(displayWord,turns):
    screen.fill(WHITE)
    screen.blit(images[turns],(80,100))
    pygame.display.update()
    pygame.time.delay(500)
    textW=WordFont.render(displayWord, 1, BLACK)
    screen.blit(textW,(350, 150))
    text=TitleFont.render("HANGMAN", 1, BLACK)
    centerTitle=WIDTH/2-text.get_width()/2  #gets  the width of my screen/2 - width ofour text /2
    screen.blit(text, (centerTitle,20))
    screen.blit(images[turns],(80,100))
    pygame.display.update()
def updateWord(word, guesses):  # function with a parameter to update word
    displayWord = ""
    for char in word:
        if char in guesses:
            print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_"
            print('_', end =' ')
            return displayWord
check = True
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
    word=random.choice(gameWords)
    guesses=''
    counter=len(word)
    turns= 0  #should we conider controlling this number when he/she misses
    displayWord= updateWord(word, guesses)
    updateScreen(displayWord,turns)
    screen.blit(image, (80,200))

    while turns<7 and counter >0:
        newGuess=input("\n\n Give me a letter ")
 #check that the new letter has not been used before
        if newGuess not in guesses:
            if newGuess not in word:
                turns +=1  #  turns = turns -1
                print("Wrong! You have  ", (7-turns), "guesses left")
            else:
                counter -=word.count(newGuess) #delete repeated letters
                print("nice guess!")
            updateScreen(displayWord, turns)
            updateWord(word,guesses)
            guesses += newGuess 
        else:
            print("you used this one already")
            updateWord(word, guesses)
            updateScreen(displayWord, turns)
            #end of whole loop with 
    if turns==0:
        print("\n\nwrong! your word was", word, '.')
    if counter==0:
        print('\n\nGreat job! You win! Your word was', word)
pygame.display.flip()
pygame.quit()
sys.exit()
