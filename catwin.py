import pygame
import sys
import resource.loadassets as loadassets
def show_text(msg, x, y, color, size):
        from main import screen
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def catwin(screen,clock):
    gameended = False
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        screen.blit(loadassets.catwin,(0,0))
        pygame.display.update()
        if gameended:
            return()