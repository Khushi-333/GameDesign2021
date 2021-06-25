import os, sys, time, pygame, random, math, datetime

from pygame.constants import USEREVENT  
  
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
walkRight = [pygame.image.load('final project images/dogs/dogR1.png'), pygame.image.load('final project images/dogs/dogR2.png'), pygame.image.load('final project images/dogs/dogR3.png')]
walkLeft = [pygame.image.load('final project images/dogs/dogL1.png'), pygame.image.load('final project images/dogs/dogL2.png'), pygame.image.load('final project images/dogs/dogL3.png')]
char = pygame.image.load('final project images/dogs/dog0.png')
bg=pygame.image.load('final project images/skyBGimage.jpg')
bgY = 0
bgY2 = bg.get_height()
bone = pygame.image.load('final project images/dogbone.png')

# Define Font objects  
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
WordFont=pygame.font.SysFont("comicsans", 50)  
LetterFont=pygame.font.SysFont("comicsans", 40) 

#for all rectangles
wbox=30


#variables
x1 = 50
y1 = 600
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
speed = 30
score = 0
strike = 1
clock = pygame.time.Clock()

#allow bones to move
bone1Y = 100
bone2Y = 200
bone3Y = 300
bone4Y = 400

#rectangles to allow for image collisions
#for bones
rect1 = pygame.Rect(400,100,60,40)
rect2 = pygame.Rect(300,200,60,40)
rect3 = pygame.Rect(200,300,60,40)
rect4 = pygame.Rect(100,400,60,40)
#for dog
rectdog = pygame.Rect(x1,y1,height,width)

def GameMenu(): #main menu
    screen.blit(bg, (0,0))
    #Print message
    message='choose an option'
    text=WordFont.render(message,1,BLACK)
    screen.blit(text,(WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
    #rect1 instructions option
    rect1=pygame.Rect(150, 350, wbox*6,wbox*2)
    pygame.draw.rect(screen, BLACK, rect1, width=1)
    text = LetterFont.render("Instructions", 1, BLACK)
    screen.blit(text, (160 , 360))
        #rect2 level 1 option
    rect2=pygame.Rect(370, 350, wbox*4,wbox*2)
    pygame.draw.rect(screen, BLACK, rect2, width=1)
    text = LetterFont.render("Level 1", 1, BLACK)
    screen.blit(text, (380 , 360))
    #rect3 level 2 option
    rect3=pygame.Rect(550, 350, wbox*4,wbox*2)
    pygame.draw.rect(screen, BLACK, rect3, width=1)
    text = LetterFont.render("Level 2", 1, BLACK)
    screen.blit(text, (560 , 360))
    #rect4 level 3 option
    rect4=pygame.Rect(150, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, BLACK, rect4, width=1)
    text = LetterFont.render("Level 3", 1, BLACK)
    screen.blit(text, (160 , 460))
    #rect5 leaderboard option
    rect5=pygame.Rect(370, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, BLACK, rect5, width=1)
    text = LetterFont.render("Scores", 1, BLACK)
    screen.blit(text, (380 , 460))
    #rect6 exit game option
    rect6=pygame.Rect(550, 450, wbox*4,wbox*2)
    pygame.draw.rect(screen, BLACK, rect6, width=1)
    text = LetterFont.render("Exit", 1, BLACK)
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
                Instructions()
            if rect2.collidepoint((mx,my)):
                #level 1
                Lvl1()
            if rect3.collidepoint((mx,my)):
                #level 2
                Lvl2()
            if rect4.collidepoint((mx,my)):
                #level 3
                Lvl3()
            if rect5.collidepoint((mx,my)):
                #scores
                screen.blit(bg, (0,0))
                text = TitleFont.render("Scores in terminal", 1, BLACK)
                screen.blit(text, (300,400))
                printScores()
                pygame.time.delay(2000)
            if rect6.collidepoint((mx,my)):
                #exit
                screen.blit(bg, (0,0))
                text = TitleFont.render("Goodbye!", 1, BLACK)
                screen.blit(text, (100,100))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()
    pygame.display.update()

def updateScores(score, level):     #store scores after each game
    print('your score is', score)
    date=datetime.datetime.now()
    line=str(date.month)+'/'+str(date.day)+'/'+str(date.year)
    File=open('FinalProjectScores.txt', 'a')        #append, will add to existing file text
    time.sleep(2)
    newline=('\n\n' + str(score) + 'pts' + '    ' + 'date: ' + str(line) + '    ' + 'level: ' + str(level))
    File.write(newline) 
    File.close()

def printScores():
    fileName='FinalProjectScores.txt'
    file=open(fileName, 'r')
    readfile=file.readlines()
    SortedData=sorted(readfile,reverse=True)        #scores in descending order

    print('top 3 scores')
    print("score, date, level")
    for line in range(3):
        print(str(line+1) + '\t' + str(SortedData[line]))
    pygame.display.update()

def Instructions():
    screen.blit(bg, (0,0))
    text = TitleFont.render("Instructions:", 1, BLACK)
    screen.blit(text, (100,100))
    step1 = LetterFont.render("* use left and right arrows to navigate", 1, BLACK)
    screen.blit(step1, (100,200))
    step2 = LetterFont.render("* try to run into the falling bones", 1, BLACK)
    screen.blit(step2, (100, 300))
    step3 = LetterFont.render("* while the dog touches a bone, your score increases", 1, BLACK)
    screen.blit(step3, (100, 400))
    step4 = LetterFont.render("* try to get the highest score you can", 1, BLACK)
    screen.blit(step4, (100, 500))
    step5 = LetterFont.render("-- you will return to the menu in a moment", 1, BLACK)
    screen.blit(step5, (100,650))
    pygame.time.delay(15000)
    pygame.display.update()
    GameMenu()

def Lvl1():
    level='one'
    bgY = 0
    bgY2 = bg.get_height()
    bone1Y = 100
    bone2Y = 200
    bone3Y = 300
    bone4Y = 400

    # Define Font objects  
    TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
    WordFont=pygame.font.SysFont("comicsans", 50)  
    LetterFont=pygame.font.SysFont("comicsans", 40) 

    x1 = 50
    y1 = 600
    width = 64
    height = 64
    vel = 5
    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    speed = 30
    score = 0
    strike = 1
    clock = pygame.time.Clock()

    #rectangles to allow for image collisions
    #for bones
    rect1 = pygame.Rect(400,100,60,40)
    rect2 = pygame.Rect(300,200,60,40)
    rect3 = pygame.Rect(200,300,60,40)
    rect4 = pygame.Rect(100,400,60,40)
    #for dog
    rectdog = pygame.Rect(x1,y1,height,width)

    #updating game window for dog walking
    def redrawGameWindow():
        global walkCount

        if walkCount + 1 >= 9:
            walkCount = 0

        if left:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkLeft[walkCount//3], (x1,y1))
            walkCount += 1
        elif right:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkRight[walkCount//3], (x1,y1))
            walkCount += 1
        else:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(char, (x1,y1))
        
        pygame.display.update()

    def redrawBG():
        screen.blit(bg, (0, bgY))                   # draws first bg image
        screen.blit(bg, (0, bgY2))                  # draws second bg image
        pygame.draw.rect(screen, BLACK, rect1)      #corresponding rectangle
        screen.blit(bone, (400,bone1Y))             #each image
        pygame.draw.rect(screen, BLACK, rect2)
        screen.blit(bone, (300,bone2Y))
        pygame.draw.rect(screen, BLACK, rect3)
        screen.blit(bone, (200,bone3Y))
        pygame.draw.rect(screen, BLACK, rect4)
        screen.blit(bone, (100,bone4Y))
    
        pygame.display.update()  # updates the screen

    #main loop
    run=True
    pygame.time.set_timer(USEREVENT+1, 500)
    while run:
        #move background down
        bgY +=2
        bgY2 +=2
        #move bones down
        bone1Y +=2
        bone2Y +=2
        bone3Y +=2
        bone4Y +=2
        #move rects down
        rect1.y +=2
        rect2.y +=2
        rect3.y +=2
        rect4.y +=2


        if bgY < bg.get_height() * -1:  # If our bg is at the -height then reset its position
            bgY = bg.get_height()
    
        if bgY2 < bg.get_height() * -1:
            bgY2 = bg.get_height()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                run = False    
                pygame.quit() 
                sys.exit()
            if event.type == USEREVENT+1: # Checks if timer goes off
                speed += 1 # Increases speed
        clock.tick(speed) 

        keys=pygame.key.get_pressed()
        #move left and right
        if keys[pygame.K_LEFT] and x1 > vel:
            x1 -= vel
            rectdog.x -= vel
            left=True
            right=False
        elif keys[pygame.K_RIGHT] and x1 < 800 - width - vel:
            x1 += vel
            rectdog.x += vel
            left=False
            right=True
            walkCount=0
        else: 
            left=False
            right=False
        #to jump
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y1 -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        #getting points/strikes
        if rectdog.colliderect(rect1):
            score +=1
        if rectdog.colliderect(rect2):
            score +=1
        if rectdog.colliderect(rect3):
            score +=1
        if rectdog.colliderect(rect4):
            score +=1
        print(score)
        if rect1.y == 750:
            screen.fill(WHITE)
            run=False
            pygame.time.delay(2000)

        redrawBG()
        redrawGameWindow()
        pygame.display.update
    updateScores(score, level)
    GameMenu()

def Lvl2():
    level = 'two'
    bgY = 0
    bgY2 = bg.get_height()
    bone1Y = 100
    bone2Y = 200
    bone3Y = 300
    bone4Y = 400

    # Define Font objects  
    TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
    WordFont=pygame.font.SysFont("comicsans", 50)  
    LetterFont=pygame.font.SysFont("comicsans", 40) 

    x1 = 50
    y1 = 600
    width = 64
    height = 64
    vel = 5
    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    speed = 30
    score = 0
    strike = 1
    clock = pygame.time.Clock()

    #rectangles to allow for image collisions
    #for bones
    rect1 = pygame.Rect(650,100,60,40)
    rect2 = pygame.Rect(250,200,60,40)
    rect3 = pygame.Rect(200,300,60,40)
    rect4 = pygame.Rect(500,400,60,40)
    #for dog
    rectdog = pygame.Rect(x1,y1,height,width)

    #updating game window for dog walking
    def redrawGameWindow():
        global walkCount

        if walkCount + 1 >= 9:
            walkCount = 0

        if left:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkLeft[walkCount//3], (x1,y1))
            walkCount += 1
        elif right:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkRight[walkCount//3], (x1,y1))
            walkCount += 1
        else:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(char, (x1,y1))
        
        pygame.display.update()

    def redrawBG():
        screen.blit(bg, (0, bgY))                   # draws first bg image
        screen.blit(bg, (0, bgY2))                  # draws second bg image
        pygame.draw.rect(screen, BLACK, rect1)      #corresponding rectangle
        screen.blit(bone, (650,bone1Y))             #each image
        pygame.draw.rect(screen, BLACK, rect2)
        screen.blit(bone, (250,bone2Y))
        pygame.draw.rect(screen, BLACK, rect3)
        screen.blit(bone, (200,bone3Y))
        pygame.draw.rect(screen, BLACK, rect4)
        screen.blit(bone, (500,bone4Y))
    
        pygame.display.update()  # updates the screen

    #main loop
    run=True
    pygame.time.set_timer(USEREVENT+1, 500)
    while run:
        #move background down
        bgY +=2
        bgY2 +=2
        #move bones down
        bone1Y +=2
        bone2Y +=2
        bone3Y +=2
        bone4Y +=2
        #move rects down
        rect1.y +=2
        rect2.y +=2
        rect3.y +=2
        rect4.y +=2


        if bgY < bg.get_height() * -1:  # If our bg is at the -height then reset its position
            bgY = bg.get_height()
    
        if bgY2 < bg.get_height() * -1:
            bgY2 = bg.get_height()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                run = False    
                pygame.quit() 
                sys.exit()
            if event.type == USEREVENT+1: # Checks if timer goes off
                speed += 1 # Increases speed
        clock.tick(speed) 

        keys=pygame.key.get_pressed()
        #move left and right
        if keys[pygame.K_LEFT] and x1 > vel:
            x1 -= vel
            rectdog.x -= vel
            left=True
            right=False
        elif keys[pygame.K_RIGHT] and x1 < 800 - width - vel:
            x1 += vel
            rectdog.x += vel
            left=False
            right=True
            walkCount=0
        else: 
            left=False
            right=False
        #to jump
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y1 -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        #getting points/strikes
        if rectdog.colliderect(rect1):
            score +=1
        if rectdog.colliderect(rect2):
            score +=1
        if rectdog.colliderect(rect3):
            score +=1
        if rectdog.colliderect(rect4):
            score +=1
        print(score)
        if rect1.y == 750:
            screen.fill(WHITE)
            run=False
            pygame.time.delay(2000)

        redrawBG()
        redrawGameWindow()
        pygame.display.update 
    updateScores(score, level) 
    GameMenu()     

def Lvl3():
    level = 'three'
    bgY = 0
    bgY2 = bg.get_height()
    bone1Y = 100
    bone2Y = 200
    bone3Y = 300
    bone4Y = 400

    # Define Font objects  
    TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
    WordFont=pygame.font.SysFont("comicsans", 50)  
    LetterFont=pygame.font.SysFont("comicsans", 40) 

    x1 = 50
    y1 = 600
    width = 64
    height = 64
    vel = 5
    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    speed = 30
    score = 0
    strike = 1
    clock = pygame.time.Clock()

    #rectangles to allow for image collisions
    #for bones
    rect1 = pygame.Rect(200,100,60,40)
    rect2 = pygame.Rect(600,200,60,40)
    rect3 = pygame.Rect(250,300,60,40)
    rect4 = pygame.Rect(550,400,60,40)
    #for dog
    rectdog = pygame.Rect(x1,y1,height,width)

    #updating game window for dog walking
    def redrawGameWindow():
        global walkCount

        if walkCount + 1 >= 9:
            walkCount = 0

        if left:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkLeft[walkCount//3], (x1,y1))
            walkCount += 1
        elif right:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(walkRight[walkCount//3], (x1,y1))
            walkCount += 1
        else:
            pygame.draw.rect(screen, WHITE, rectdog)
            screen.blit(char, (x1,y1))
        
        pygame.display.update()

    def redrawBG():
        screen.blit(bg, (0, bgY))                   # draws first bg image
        screen.blit(bg, (0, bgY2))                  # draws second bg image
        pygame.draw.rect(screen, BLACK, rect1)      #corresponding rectangle
        screen.blit(bone, (200,bone1Y))             #each image
        pygame.draw.rect(screen, BLACK, rect2)
        screen.blit(bone, (600,bone2Y))
        pygame.draw.rect(screen, BLACK, rect3)
        screen.blit(bone, (250,bone3Y))
        pygame.draw.rect(screen, BLACK, rect4)
        screen.blit(bone, (550,bone4Y))
    
        pygame.display.update()  # updates the screen

    #main loop
    run=True
    pygame.time.set_timer(USEREVENT+1, 500)
    while run:
        #move background down
        bgY +=2
        bgY2 +=2
        #move bones down
        bone1Y +=2
        bone2Y +=2
        bone3Y +=2
        bone4Y +=2
        #move rects down
        rect1.y +=2
        rect2.y +=2
        rect3.y +=2
        rect4.y +=2


        if bgY < bg.get_height() * -1:  # If our bg is at the -height then reset its position
            bgY = bg.get_height()
    
        if bgY2 < bg.get_height() * -1:
            bgY2 = bg.get_height()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                run = False    
                pygame.quit() 
                sys.exit()
            if event.type == USEREVENT+1: # Checks if timer goes off
                speed += 1 # Increases speed
        clock.tick(speed) 

        keys=pygame.key.get_pressed()
        #move left and right
        if keys[pygame.K_LEFT] and x1 > vel:
            x1 -= vel
            rectdog.x -= vel
            left=True
            right=False
        elif keys[pygame.K_RIGHT] and x1 < 800 - width - vel:
            x1 += vel
            rectdog.x += vel
            left=False
            right=True
            walkCount=0
        else: 
            left=False
            right=False
        #to jump
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y1 -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        #getting points/strikes
        if rectdog.colliderect(rect1):
            score +=1
        if rectdog.colliderect(rect2):
            score +=1
        if rectdog.colliderect(rect3):
            score +=1
        if rectdog.colliderect(rect4):
            score +=1
        print(score)
        if rect1.y == 750:
            screen.fill(WHITE)
            run=False
            pygame.time.delay(2000)

        redrawBG()
        redrawGameWindow()
        pygame.display.update
    updateScores(score, level)
    GameMenu()

pygame.display.flip()
while True:
    GameMenu()

