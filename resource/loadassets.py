import pygame
pygame.mixer.init()
#Background
farm = pygame.image.load("resource/background/Farm.png")
#Character
cat = [pygame.image.load("resource/character/catright.png")]
cat.append(pygame.transform.flip(cat[0],True,False))
catwin = pygame.image.load("resource/background/catwin.png")
for i in range(0,2):
    cat[i] = pygame.transform.scale(cat[i],(124,124))
rooster = pygame.image.load("resource/character/rooster.png")
stick = pygame.image.load("resource/character/stick.png")
stick = pygame.transform.scale(stick,(64,64))
roosterwin = pygame.image.load("resource/background/roosterwin.png")
#Sound
getstick = pygame.mixer.Sound("resource/sound/getstick.wav")
winsfx = pygame.mixer.Sound("resource/sound/win.wav")