import pygame
import sys
import resource.loadassets as loadassets
def show_text(msg, x, y, color, size):
        from main import screen
        fontobj= pygame.font.Font("resource/font/freesans.TTF",size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
version = "v1.4.1" #Version number so I can keep track of releases
def startscreen(screen,clock):
    gameended = False #Also bad variable name
    mouserect = None
    fullscreen = False
    frame = True
    israce = False #Bad variable name but who cares
    startbuttonrect = pygame.Rect(240,220,140,60)
    racebuttonrect = pygame.Rect(240,300,140,60)
    timedbuttonrect = pygame.Rect(240,390,140,60)
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_F11:
                    if fullscreen == False:
                        screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                        fullscreen = True
                        break
                    if fullscreen:
                        screen = pygame.display.set_mode((640,480))
                        fullscreen = False
                        break
                if event.key == pygame.K_F10:
                    if frame:
                        screen = pygame.display.set_mode((640,480),pygame.NOFRAME)
                        frame = False
                        break
                    if frame == False:
                        screen = pygame.display.set_mode((640,480))
                        frame = True
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = event.pos
                mouserect = pygame.Rect(mousex,mousey,32,32)
                #I hate how this looks but it works
                if mouserect.colliderect(startbuttonrect):
                    return 0
                elif mouserect.colliderect(racebuttonrect):
                    return 1
                elif mouserect.colliderect(timedbuttonrect):
                    return 2
        screen.blit(loadassets.farm,(0,0))
        show_text("Rooster Chase 2",140,2,(0,0,0),48)
        pygame.draw.rect(screen,(0,255,0),(240,220,140,60))
        show_text("Play",275,230,(255,255,255),30)
        pygame.draw.rect(screen,(255,0,0),(240,300,140,60))
        show_text("Race",275,310,(255,255,255),30)
        pygame.draw.rect(screen,(155,0,155),(240,380,140,60))
        show_text("Timed",270,390,(255,255,255),30)
        show_text(version,600,460,(0,0,0),15)
        #Splash text will not be added later
        pygame.display.update()