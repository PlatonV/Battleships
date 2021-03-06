from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame

pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]

startNewGame.startNewGame(1)
xoy=[(0,-1),(1,0),(0,1),(-1,0)]


def hit(x, y):
    pygame.draw.rect(screen, (255, 0, 0), Rect(x*26, y*26, 25, 25)) 
    pygame.display.update()

def hit2(x, y):
    pygame.draw.rect(screen, (50, 0, 0), Rect(x*26, y*26, 25, 25)) 
    pygame.display.update()

def search(x,y):
    for i in range(0, 4):
        cx, cy = xoy[i]
        newx = x + cx
        newy = y + cy
        if (newx > 0) and (newx < 11) and (newy > 0) and (newy < 11) and (newx, newy) not in lovit:
            lovit.append((newx, newy))
            hit2(newx, newy)
            if request.request(chr(newx + ord('A')-1), y) in ["HIT", "DESTROYED"]:
                hit(newx, newy)
                search(newx, newy)


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    while len(lovit)<100:
        x = randint(1, 10)
        y = randint(1, 10)

        if request.request(chr(x + ord('A')-1), y) in ["HIT", "DESTROYED"] and (x, y) not in lovit:
            hit(x, y)
            lovit.append((x, y))
            search(x, y)

    print("Gata!")

