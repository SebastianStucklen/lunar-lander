import pygame
import os
import sys
from pygame.locals import QUIT
pygame.init()
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((800,1000))
pygame.display.set_caption("Lunar Lander")

doExit = False
clock = pygame.time.Clock()
def stars():
    ex = random.randint(0,800)
    why = random.randint(0,1000)
    pygame.draw.rect(screen,(255,255,255), (ex,why,2,2),0)
#Variables --------------------------------------
fuelCon = 1.0111
r = 255
g = 255
b = 0
fr = 55
fg = 250
xPos = 400
yPos = 0
xVel = 0
yVel = 10/60 #slide says -10/60
fuel = 800
isOnGround = False
crashed = False
landed = False
stupidSebCode = False
#font variables
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

while doExit == False:
    text1 = font.render('Vertical velocity:', True, (0,200,200)) #green means your ok speed
    text2 = font.render(str("%.2f" %(yVel*-1)), 1, (0,200,200))
    text3 = font.render('YOU CRASHED',True,(200,50,50))
    text4 = font.render('Vertical velocity:', False, (200,20,20))
    text5 = font.render(str("%.2f" %(yVel*-1)), 1, (200,20,20))
    text6 = font.render('Height:', True, (20,20,200))
    text7 = font.render(str(int(1000-yPos)),1,(20,20,200))
    text8 = font.render('YOU LANDED',True,(50,200,50))
    text9 = font.render('FUEL',True, (2,2,2))
    #GAME LOOPS
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            doExit = True
            print("test")

    #INPUT
    if event.type == pygame.KEYDOWN:
        if fuel > 0:
            if event.key == pygame.K_LEFT:
                xVel -=1/60
                yVel -=0.8/60
                fuel -= fuelCon
                fuelCon*=1.0111
                fuelCon*=1.0111
                if fr < 254:
                    fr += 0.5
                if fg > 1:
                    fg -= 0.3
                if g > 3:
                    g-=3

            if event.key == pygame.K_RIGHT:
                xVel +=1/60
                yVel -=0.8/60
                fuel -= fuelCon
                fuelCon*=1.0111
                fuelCon*=1.0111
                if fr < 254:
                    fr += 0.5
                if fg > 1:
                    fg -= 0.3
                if g > 3:
                    g-=3

            if event.key == pygame.K_UP:
                yVel -= 4.2/60
                isOnGround = False
                fuel -= fuelCon
                fuelCon*=1.0111
                fuelCon*=1.0111
                if fr < 254:
                    fr += 0.5
                if fg > 1:
                    fg -= 0.3
                if g > 3:
                    g-=3

    #physics
    xPos += xVel
    yPos += yVel
    if g < 254:
        g+=1
    if fuelCon > 1.0111:
        fuelCon/=1.0111
    if yPos >= 950:
        isOnGround = True
    if isOnGround == False:
        yVel += 1.7/60
    if isOnGround == True and abs(yVel)>1:
        crashed = True
        screen.blit(text3,(200,500))
        pygame.display.flip()
        pygame.time.wait(1000)
        xPos = 350
        yPos = 0
        yVel = 0
        xVel = 0
        isOnGround = False
        print("crashed")
        fuel = 800
        fr = 55
        fg = 255
    elif isOnGround == True and abs(yVel)<1:
        crashed=False
        screen.blit(text8,(200,500))
        pygame.display.flip()
        pygame.time.wait(1000)
        if stupidSebCode == False:
            xPos2 = xPos
            yPos2 = yPos
            stupidSebCode == True
        xPos = xPos2
        yPos = yPos2
        isOnGround = True
        print("landed")
        fuel = 800
        fr = 55
        fg = 255

        #RENDER
    if abs(yVel)<1:#green
        screen.blit(text1,(10,50))
        screen.blit(text2,(250,50))
    else:#red
        screen.blit(text4,(10,50))
        screen.blit(text5,(250,50))
    
    screen.blit(text6,(10,100))
    screen.blit(text7,(150,100))
    pygame.draw.line(screen,(fr,fg,50),(0,20),(fuel,20),50)
    pygame.draw.rect(screen, (r,g,b), (xPos,yPos,30,30),0)
    screen.blit(text9,(10,0))
    for i in range(6):
        stars()
    pygame.display.flip()
    screen.fill((0,0,0))
    print(fuelCon)
print("done")