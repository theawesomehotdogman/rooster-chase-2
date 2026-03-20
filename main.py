import pygame
import loadassets
from menu import startscreen
import player
import enemy
import catwin
import stick
import roosterwin
import sys
import random
pygame.init()
screen = pygame.display.set_mode((640,480))
whowon = False   #False is rooster True is cat
pygame.display.set_caption("Rooster Chase 2")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
def maingame():
    up,down,left,right = False,False,False,False
    global whowon
    cat = player.Player()
    rooster = enemy.Rooster()
    collect = stick.Stick(0,0)
    score = 0
    collect.moveself()
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60 )    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Key Detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_d:
                    right = False
        if score == 15:
            whowon = True
            return()
#####################################################
#           Class Functions
        screen.blit(loadassets.farm,(0,0))
        cat.move(up,down,left,right)
        cat.drawself()
        rooster.drawself(screen)
        rooster.move(cat.x,cat.y)
        show_text(str(score),320,10,(0,0,0),32)
        collect.drawself(screen)
        catrectrooster = pygame.Rect(cat.x + 50,cat.y + 60,30,30)
        catrectstick = pygame.Rect(cat.x,cat.y,125,125)
        stickrect = pygame.Rect(collect.x,collect.y,64,64)
        roosterrect = pygame.Rect(rooster.position.x,rooster.position.y,128,128)
        if catrectstick.colliderect(stickrect):
            score += 1
            loadassets.getstick.play()
            collect.moveself()
        if catrectrooster.colliderect(roosterrect):
            whowon = False
            return()
        if roosterrect.colliderect(stickrect):
            collect.moveself()
        pygame.display.update()

startscreen(screen,clock)
maingame()
if whowon:
    catwin.catwin(screen,clock)
if whowon == False:
    roosterwin.rooswin(screen,clock)
sys.exit()
