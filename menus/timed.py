import pygame
import random
import loadassets
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
def timedmode():
    up,down,left,right = False,False,False,False
    paused = False
    cat = player.Player()
    rooster = enemy.Rooster()
    rooster.speed = 4
    collect = stick.Stick(random.randint(0,600),random.randint(0,450))
    score = 0  #See this after you lose
    timeleft = 10 #Timeleft shows on the screen like score
    timer = 0
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
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
            #Quit also its in keyup but who cares does the same thing
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
#           Class Functions
        screen.blit(loadassets.farm,(0,0))
        if paused == False:
            cat.move(up,down,left,right)
            cat.drawself()
            rooster.drawself(screen,cat.x) 
            rooster.move(cat.x,cat.y,collect.isgold)
            show_text(str(timeleft),320,10,(0,0,0),32)
            collect.drawself(screen)
            catrectstick = pygame.Rect(cat.x,cat.y,125,125)
            catrectrooster = pygame.Rect(cat.x + 50,cat.y + 60,30,30)
            stickrect = pygame.Rect(collect.x,collect.y,64,64)
            roosterrect = pygame.Rect(rooster.position.x,rooster.position.y,128,128)
            if catrectstick.colliderect(stickrect):
                if collect.isgold:
                    timeleft += 3
                else:
                    timeleft += 1
                timer = 0
                loadassets.getstick.play()
                collect.moveself(catrectstick,roosterrect,True)
            if stickrect.colliderect(roosterrect):
                collect.moveself(catrectstick,roosterrect,True) #I know its not really in a race but we still need golden sticks
                loadassets.getstick.play()
            if catrectrooster.colliderect(roosterrect):
                timeleft -= 4
                rooster.resetposition()
        if paused:
            show_text("Paused",250,200,(255,255,0),50)
        timer += 1
        if timer >= 60:
            timer = 0
            score += 1
            timeleft -= 1
            print("timerreset")
        if timeleft <= 0:
            return score
        pygame.display.update()