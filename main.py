import pygame
import urllib2
from pygame.locals import *

pygame.inite()

screen = pygame.display.set_mode((800, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    
