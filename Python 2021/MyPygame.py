#KhushiChhaya
#6/17/2021
#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT

import pygame, time, sys

from pygame import key

pygame.init()
pygame.time.delay(100)
WIDTH=640
HEIGHT=512
#create object to open window
white=[255, 255, 255]
purple=[200, 190, 0]
green=[50, 25, 255]

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(green)
pygame.display.set_caption('My Game')
#command to run updated code
#you must ALWAYS
check=True
x=480
y=580
x2=300
y2=300
radius=50
hbox,wbox=20,20
center= x,y
hbox2,wbox2=30,30
rect=pygame.Rect(x,y,hbox,wbox) #square/rectangle (only shape to declare in advance)
rect2=pygame.Rect(x2,y2,hbox2,wbox2)
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    speed=5 #move 2 pixels at a time
    keyBoardKey=pygame.key.get_pressed()    #checking what key is pressed

    if keyBoardKey[pygame.K_LEFT]:      #moving left on x (-)
        rect.x -=speed                 
    if keyBoardKey[pygame.K_RIGHT]:     #moving right on x (+)
        rect.x +=speed
    if keyBoardKey[pygame.K_DOWN]:      #moving down on y (+)
        rect.y +=speed
    if keyBoardKey[pygame.K_UP]:         #moving up on y (-)
        rect.y -=speed

    if keyBoardKey[pygame.K_1]:      
        rect2.x -=speed
    if keyBoardKey[pygame.K_2]:
        rect2.x +=speed
    if keyBoardKey[pygame.K_3]:
        rect2.y +=speed
    if keyBoardKey[pygame.K_4]:
        rect2.y -=speed

    if keyBoardKey[pygame.K_s]:
        radius -=speed
    if keyBoardKey[pygame.K_f]:
        radius +=speed
    
    if rect.x < 0: rect.x = 0
    if rect.x > WIDTH-wbox: rect.x = WIDTH-wbox
    if rect.y < 0: rect.y = 0
    if rect.y > HEIGHT-hbox: rect.y = HEIGHT-hbox

    if rect2.x < 0: rect2.x = 0
    if rect2.x > WIDTH-wbox2: rect2.x = WIDTH-wbox2
    if rect2.y < 0: rect2.y = 0
    if rect2.y > HEIGHT-hbox2: rect2.y = HEIGHT-hbox2

    if radius < 0: radius = 1
    if radius > HEIGHT-y: radius = HEIGHT-y
    if radius > WIDTH-x: radius = WIDTH-x

    if rect.colliderect(rect2):
        rect.x -=3
        rect2.x +=3    

    screen.fill(green)
    circ=pygame.draw.circle(screen, (white), (x/2,y/2), radius, 10) #where, color, position, radius, line thickness
    pygame.draw.rect(screen,(purple),rect2)
    pygame.draw.rect(screen,(white),rect)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()