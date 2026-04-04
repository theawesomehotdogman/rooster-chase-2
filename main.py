import pygame
import random
import resource.loadassets as loadassets
from menus.menu import startscreen
import classes.player as player
import classes.enemy as enemy
import classes.stick as stick
import menus.race as race
import menus.winner as winner
import menus.timed as timed
import sys
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Rooster Chase 2")
game = True
pygame.display.set_icon(loadassets.icon)
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.Font("resource/font/freesans.TTF",size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
whowon = False   #False is rooster True is cat
gamemode = 0
gamestate = 0 #0 is normal, 1 is race, 2 is timed. Im sorry for using something like this but its the easiest solution i could find
timesurvived = 0
def maingame():
    up,down,left,right = False,False,False,False
    paused = False
    cat = player.Player()
    rooster = enemy.Rooster()
    collect = stick.Stick(random.randint(0,600),random.randint(0,450))
    score = 0
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60 )    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Key Detection
            if event.type == pygame.KEYDOWN:
                #WASD
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_d:
                    right = True
                #Pause
                if event.key == pygame.K_p:
                    if paused == False:
                        paused = True
                        break
                    if paused:
                        paused = False
                        break
                #Arrow Keys
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
            if event.type == pygame.KEYUP:
                #WASD
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_d:
                    right = False
                #Arrow Keys
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
        if score == 15:
            return True
#           Class Functions
        screen.blit(loadassets.farm,(0,0))
        if paused == False:
            cat.move(up,down,left,right)
            cat.drawself()
            rooster.drawself(screen,cat.x) #False tells the rooster if in race or not
            rooster.move(cat.x,cat.y,collect.isgold)
            show_text(str(score),320,10,(0,0,0),32)
            collect.drawself(screen)
            catrectrooster = pygame.Rect(cat.x + 50,cat.y + 60,30,30)
            catrectstick = pygame.Rect(cat.x,cat.y,125,125)
            stickrect = pygame.Rect(collect.x,collect.y,64,64)
            roosterrect = pygame.Rect(rooster.position.x,rooster.position.y,128,128)
            if catrectstick.colliderect(stickrect):
                if collect.isgold:
                    score += 3
                else:
                    score += 1
                loadassets.getstick.play()
                collect.moveself(catrectstick,roosterrect,False) #The false is to tell the stick that the game is not in race mode
            if catrectrooster.colliderect(roosterrect):
                return False
            if roosterrect.colliderect(stickrect):
                collect.moveself(catrectstick,roosterrect,False)
        if paused:
            show_text("Paused",250,200,(255,255,0),50)
        pygame.display.update()
while game:
    gamemode = startscreen(screen,clock)
    if gamemode == 1:
        whowon = race.race()
    elif gamemode == 0:
        whowon = maingame()
    elif gamemode == 2:
        timesurvived = timed.timedmode()
    winner.whowon(screen,clock,whowon,timesurvived)
    timesurvived = 0
