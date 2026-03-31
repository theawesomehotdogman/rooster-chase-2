import pygame
import sys
import resource.loadassets as loadassets
def show_text(msg, x, y, color, size):
        from main import screen
        fontobj= pygame.font.Font("resource/font/freesans.TTF",size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def whowon(screen,clock,winner):
    gameended = False
    playedsound = False
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
        if winner:
            screen.blit(loadassets.catwin,(0,0))
            if playedsound == False:
                loadassets.winsfx.play()
                playedsound = True
        else:
            screen.blit(loadassets.roosterwin,(0,0))
        show_text("Space to return",0,450,(0,0,0),20)
        pygame.display.update()
        if gameended:
            return()