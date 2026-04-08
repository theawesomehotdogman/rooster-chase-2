#It probably isnt an issue that I load everything into memory at one
import pygame
pygame.init()
pygame.mixer.init()
#Background
farm = pygame.image.load("resource/background/Farm.png")
roosterwin = pygame.image.load("resource/background/roosterwin.png")
catwin = pygame.image.load("resource/background/catwin.png")
#Character
cat = [pygame.image.load("resource/character/cat.png")]
cat.append(pygame.transform.flip(cat[0],True,False))
rooster = [pygame.image.load("resource/character/rooster.png")]
rooster.append(pygame.transform.flip(rooster[0],True,False))
stick = pygame.image.load("resource/character/stick.png")
stick = pygame.transform.scale(stick,(64,64))
goldenstick = pygame.image.load("resource/character/goldenstick.png")
#Sound
getstick = pygame.mixer.Sound("resource/sound/getstick.wav")
winsfx = pygame.mixer.Sound("resource/sound/win.mp3")
notgetstick = pygame.mixer.Sound("resource/sound/yousuck.wav")
#Other
icon = pygame.image.load("resource/cat.ico")