#KhushiChhaya
#6/17/2021
#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT

import pygame, time, sys

pygame.init()
pygame.time.delay(100)
WIDTH=500
HEIGHT=600
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
radius=50
hbox,wbox=20,20
rect=pygame.Rect(x,y,hbox,wbox) #square/rectangle (only shape to declare in advance)
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    speed=5 #move 2 pixels at a time
    keyBoardKey=pygame.key.get_pressed()    #checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]:      #moving left on x (-)
        rect.x -=speed
    if keyBoardKey[pygame.K_RIGHT]:
        rect.x +=speed
    if keyBoardKey[pygame.K_DOWN]:
        rect.y +=speed
    if keyBoardKey[pygame.K_UP]:
        rect.y -=speed
    if keyBoardKey[pygame.K_s]:
        radius -=speed
    if keyBoardKey[pygame.K_f]:
        radius +=speed
    if rect.x < 0: rect.x = 0
    if rect.x > WIDTH-wbox: rect.x = WIDTH-wbox
    if rect.y < 0: rect.y = 0
    if rect.y > HEIGHT-hbox: rect.y = HEIGHT-hbox
    if radius < 0: radius = 1
    if radius > HEIGHT-y: radius = HEIGHT-y
    if radius > WIDTH-x: radius = WIDTH-x

    
    screen.fill(green)
    circ=pygame.draw.circle(screen, (white), (x/2,y/2), radius, 10) #where, color, position, radius, line thickness
    pygame.draw.rect(screen,(white),rect)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()