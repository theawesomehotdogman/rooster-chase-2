import pygame
import loadassets
class Player():
    def __init__(self):
        self.x = 30
        self.y = 200
        self.imageleft = loadassets.cat[1]
        self.imageright = loadassets.cat[0]
        self.currentimage = self.imageright
    def move(self,up,down,left,right):
        if up and self.y > 0:
            self.y -= 5
        if down and self.y < 380:
           self.y += 5
        if left:
            self.x -= 5
            self.currentimage = self.imageleft
        if right:
            self.x += 5
            self.currentimage = self.imageright
    def drawself(self):
       from main import screen
       screen.blit(self.currentimage,(self.x,self.y)) 
