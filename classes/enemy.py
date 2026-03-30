import pygame
import resource.loadassets as loadassets
class Rooster:
    def __init__(self):
        self.image = loadassets.rooster
        self.x = 320
        self.y = 250
        self.speed = 3
        self.position = pygame.math.Vector2(self.x,self.y)
    def drawself(self,screen):
        screen = screen
        screen.blit(self.image,self.position)
    def move(self,targetx,targety):
        target = pygame.math.Vector2(targetx,targety)
        self.position = self.position.move_towards(target,self.speed)

        