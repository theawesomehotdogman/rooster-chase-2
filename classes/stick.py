import pygame
import resource.loadassets as loadassets
import random
class Stick():
    def __init__(self,x,y):
        self.image = loadassets.stick
        self.x = x
        self.y = y
    def moveself(self,catpos,roosterpos):
        self.x = random.randint(0,600)
        self.y = random.randint(0,380)
        self.collider = pygame.Rect(self.x,self.y,64,64)
        while self.collider.colliderect(catpos) or self.collider.colliderect(roosterpos):
            self.x = random.randint(0,600)
            self.y = random.randint(0,380)
            self.collider = pygame.Rect(self.x,self.y,64,64)
    def drawself(self,screen):
        screen = screen
        screen.blit(self.image,(self.x,self.y))
    def collide(self,otherobject,score):
        selfbox = pygame.Rect(self.x,self.y,64,64)
        if selfbox.colliderect(otherobject):
            score = score
            score += 1
            self.moveself()
            return score