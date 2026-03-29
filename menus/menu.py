import pygame
import sys
import resource.loadassets as loadassets
def show_text(msg, x, y, color, size):
        from main import screen
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def startscreen(screen,clock):
    gameended = False #Also bad variable name
    mouserect = None
    israce = False #Bad variable name but who cares
    startbuttonrect = pygame.Rect(240,220,140,60)
    racebuttonrect = pygame.Rect(240,300,140,60)
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = event.pos
                mouserect = pygame.Rect(mousex,mousey,32,32)
                if mouserect.colliderect(startbuttonrect):
                    gameended = True
                    israce = False
                elif mouserect.colliderect(racebuttonrect):
                    gameended = True
                    israce = True
        screen.blit(loadassets.farm,(0,0))
        show_text('Rooster Chase 2',140,30,(255,255,0),48)
        pygame.draw.rect(screen,(0,255,0),(240,220,140,60))
        show_text("Play",275,230,(255,255,255),30)
        pygame.draw.rect(screen,(255,0,0),(240,300,140,60))
        show_text("Race",275,310,(255,255,255),30)
        #Splash text will not be added later
        pygame.display.update()
        if gameended:
            return(israce)