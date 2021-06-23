import os, sys, time, pygame, random, math  
  
pygame.init()  

#Create my display screen  
WIDTH = 800  # uppercase because it behaves as constant  
HEIGHT = 800   
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Frog Game")  

#define colors
WHITE = [255,255,255]  
BLACK = [0,0,0] 
PURPLE = [182,30,246]

#load images needed
bg=pygame.image.load('final project images/sky2.png')
# Define Font objects  
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
WordFont=pygame.font.SysFont("comicsans", 50)  
LetterFont=pygame.font.SysFont("comicsans", 40) 

#for all rectangles
wbox=30

def GameMenu():
    screen.blit(bg, (0,0))
#Print message
    message='choose an option'
    text=WordFont.render(message,1,WHITE)
    screen.blit(text,(WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
#rect1 instructions option
    rect1=pygame.Rect(150, 350, wbox*6,wbox*2)
    pygame.draw.rect(screen, WHITE, rect1, width=1)
    text = LetterFont.render("Instructions", 1, PURPLE)
    screen.blit(text, (160 , 360))
#rect2 level 1 option
    rect2=pygame.Rect(370, 350, wbox*4,wbox*2)
    pygame.draw.rect(screen, WHITE, rect2, width=1)
    text = LetterFont.render("Level 1", 1, PURPLE)
    screen.blit(text, (380 , 360))
#rect3 level 2 option
    rect3=pygame.Rect(550, 350, wbox*4,wbox*2)
    pygame.draw.rect(screen, WHITE, rect3, width=1)
    text = LetterFont.render("Level 2", 1, PURPLE)
    screen.blit(text, (560 , 360))
#rect4 level 3 option
    rect4=pygame.Rect(150, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, WHITE, rect4, width=1)
    text = LetterFont.render("Level 3", 1, PURPLE)
    screen.blit(text, (160 , 460))
#rect5 leaderboard option
    rect5=pygame.Rect(370, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, WHITE, rect5, width=1)
    text = LetterFont.render("Scores", 1, PURPLE)
    screen.blit(text, (380 , 460))
#rect6 exit game option
    rect6=pygame.Rect(550, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, WHITE, rect6, width=1)
    text = LetterFont.render("Exit", 1, PURPLE)
    screen.blit(text, (560 , 460))
#clicking menu options
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my= pygame.mouse.get_pos()
            if rect1.collidepoint(mx,my):
                #call main function
                #instructions
                screen.blit(bg, (0,0))
                text = TitleFont.render("Instructions coming soon", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.time.delay(2000)
            if rect2.collidepoint((mx,my)):
                #level 1
                screen.blit(bg, (0,0))
                text = TitleFont.render("Level 1 coming soon", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.time.delay(2000)
            if rect3.collidepoint((mx,my)):
                #level 2
                screen.blit(bg, (0,0))
                text = TitleFont.render("Level 2 coming soon", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.time.delay(2000)
            if rect4.collidepoint((mx,my)):
                #level 3
                screen.blit(bg, (0,0))
                text = TitleFont.render("Level 3 coming soon", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.time.delay(2000)
            if rect5.collidepoint((mx,my)):
                #scores
                screen.blit(bg, (0,0))
                text = TitleFont.render("Scoreboard coming soon", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.time.delay(2000)
            if rect6.collidepoint((mx,my)):
                screen.blit(bg, (0,0))
                text = TitleFont.render("Goodbye!", 1, PURPLE)
                screen.blit(text, (100,100))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()
    pygame.display.update()

pygame.display.flip()
while True:
    GameMenu()

