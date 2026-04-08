import pygame
import random
import resource.loadassets as loadassets
import classes.player as player
import classes.enemy as enemy
import classes.stick as stick
import sys
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Rooster Chase 2")
def show_text(msg, x, y, color, size):
        from main import screen
        fontobj= pygame.font.Font("resource/font/freesans.TTF",size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
def race():
    up,down,left,right = False,False,False,False
    global whowon
    paused = False
    cat = player.Player()
    rooster = enemy.Rooster()
    rooster.speed = 2
    collect = stick.Stick(random.randint(0,600),random.randint(0,450))
    score = 0
    roosterscore = 0
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
                if event.key == pygame.K_p:
                    if paused == False:
                        paused = True
                        break
                    if paused:
                        paused = False
                        break
                    print(paused)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_d:
                    right = False
        if score >= 15:
            return True
        if roosterscore >= 15:
            return False
#           Class Functions
        screen.blit(loadassets.farm,(0,0))
        if paused == False:
            cat.move(up,down,left,right)
            cat.drawself()
            rooster.drawself(screen,collect.x) #True tells the rooster that it is currently in race mode
            rooster.move(collect.x,collect.y,collect.isgold)
            show_text(str(score),320,10,(0,0,0),32)
            show_text(str(roosterscore),500,10,(0,0,0),32)
            collect.drawself(screen)
            catrectstick = pygame.Rect(cat.x,cat.y,125,125)
            stickrect = pygame.Rect(collect.x,collect.y,64,64)
            roosterrect = pygame.Rect(rooster.position.x,rooster.position.y,128,128)
            if catrectstick.colliderect(stickrect):
                if collect.isgold:
                    score += 3
                else:
                    score += 1
                loadassets.getstick.play()
                collect.moveself(catrectstick,roosterrect,True) #The true in this method is to tell the stick if race is on or not
            if stickrect.colliderect(roosterrect):
                if collect.isgold:
                    roosterscore += 3
                else:
                    roosterscore += 1
                loadassets.notgetstick.play()
                collect.moveself(catrectstick,roosterrect,True)
        if paused:
            show_text("Paused",250,200,(255,255,0),50)
        pygame.display.update()