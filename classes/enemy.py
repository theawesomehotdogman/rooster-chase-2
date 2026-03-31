import pygame
import resource.loadassets as loadassets
class Rooster:
    def __init__(self):
        self.image = loadassets.rooster
        self.x = 320
        self.y = 250
        self.speed = 3
        self.position = pygame.math.Vector2(self.x,self.y)
    def drawself(self,screen,target):
        screen = screen
        imagepicked = self.image[0]
        if target + 64 > self.x:
            imagepicked = self.image[0]
        elif target + 64 < self.x:
            imagepicked = self.image[1]
        screen.blit(imagepicked,self.position)
    def move(self,targetx,targety,isgold):
        target = pygame.math.Vector2(targetx,targety)
        if isgold:
            self.speed = 4
        if isgold == False:
            self.speed = 3
        self.position = self.position.move_towards(target,self.speed)

        