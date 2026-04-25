#It probably isnt an issue that I load everything into memory at once
import pygame
import tkinter as tk
from tkinter import messagebox
import sys
import random
pygame.init()
pygame.mixer.init()
try:
    #Background

    roosterwin = pygame.image.load("resource/background/roosterwin.png")
    catwin = pygame.image.load("resource/background/catwin.png")
    choosablebackdrops = [pygame.image.load("resource/background/Farm.png"),pygame.image.load("resource/background/Jurassic.png"),pygame.image.load("resource/background/Desert.png"),pygame.image.load("resource/background/Neon Tunnel.png"),pygame.image.load("resource/background/Room.png"),pygame.image.load("resource/background/Space City 2.png"),pygame.image.load("resource/background/Spaceship.png"),pygame.image.load("resource/background/Theater.png")]
    for i in range(len(choosablebackdrops)):
        choosablebackdrops[i] = pygame.transform.scale(choosablebackdrops[i],(640,480))
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
except Exception as e:
    print(e)
    messagebox.showerror("Could not load assets","Asset folder may be missing")
    sys.exit()
def getimage():
    global choosablebackdrops
    imagetoreturn = random.randint(0,len(choosablebackdrops) - 1)
    return choosablebackdrops[imagetoreturn]