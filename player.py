import pygame
import loadassets
class Player():
    def __init__(self):
        self.x = 30
        self.y = 200
        self.speed = 5
        self.imageleft = loadassets.cat[1]
        self.imageright = loadassets.cat[0]
        self.currentimage = self.imageright
        self.catrectstick = pygame.Rect(self.x,self.y,125,125)
        self.catrectrooster = pygame.Rect(self.x + 50,self.y + 60,30,30)
    def move(self):
        keys = pygame.key.get_pressed()
        up    = keys[pygame.K_w]
        down  = keys[pygame.K_s]
        left  = keys[pygame.K_a]
        right = keys[pygame.K_d]
        if up:
            self.y -= self.speed
        if down:
            self.y += self.speed
        if left:
            self.x -= self.speed
        if right:
            self.x += self.speed
        self.catrectstick = pygame.Rect(self.x,self.y,125,125)
        self.catrectrooster = pygame.Rect(self.x + 50,self.y + 60,30,30)
    def drawself(self):
       from main import screen
       screen.blit(self.currentimage,(self.x,self.y)) 
