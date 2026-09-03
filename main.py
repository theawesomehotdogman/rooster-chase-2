import pygame
import random
import loadassets
import menu as menu
import player as player
import enemy as enemy
import stick as stick
import race as race
import winner as winner
import timed as timed
import sys
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Rooster Chase 2")
pygame.display.set_icon(loadassets.icon)
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.Font("resource/font/freesans.TTF",size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
whowon = False   #False is rooster True is cat
game = True
gamemode = 0
gamestate = 0
timesurvived = 0
def maingame():
    up,down,left,right = False,False,False,False
    backdrop = loadassets.getimage()
    paused = False
    cat = player.Player()
    rooster = enemy.Rooster()
    collect = stick.Stick(random.randint(0,600),random.randint(0,450))
    score = 0
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #Pause
                if event.key == pygame.K_p:
                    if paused == False:
                        paused = True
                        break
                    if paused:
                        paused = False
                        break
                #Quit handling
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if score >= 15:
            return True
#           Class Functions
        screen.blit(backdrop,(0,0))
        if paused == False:
            cat.move()
            cat.drawself()
            rooster.drawself(screen,cat.x) #False tells the rooster if in race or not
            rooster.move(cat.x,cat.y,collect.isgold)
            show_text(str(score),320,10,(0,0,0),32)
            collect.drawself(screen)
            catrectrooster = pygame.Rect(cat.x + 50,cat.y + 60,30,30)
            catrectstick = pygame.Rect(cat.x,cat.y,125,125)
            stickrect = pygame.Rect(collect.x,collect.y,64,64)
            roosterrect = pygame.Rect(rooster.position.x,rooster.position.y,128,128)
            if cat.catrectstick.colliderect(stickrect):
                timeleft += collect.addscore()
                loadassets.getstick.play()
                collect.moveself(catrectstick,roosterrect,False) #The false is to tell the stick that the game is not in race mode
            if cat.catrectrooster.colliderect(roosterrect):
                return False
            if roosterrect.colliderect(stickrect):
                collect.moveself(catrectstick,roosterrect,False)
        if paused:
            show_text("Paused",250,200,(255,255,0),50)
        pygame.display.update()
while game:
    gamemode = menu.startscreen(screen=screen,clock=clock)
    match gamemode:
        case 0:
            whowon = maingame()
        case 1:
            whowon = race.race()
        case 2:
            timesurvived = timed.timedmode()
    winner.whowon(screen,clock,whowon,timesurvived)
    timesurvived = 0
