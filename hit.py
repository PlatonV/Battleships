from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame

pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]

def hit(x, y):
    pygame.draw.rect(screen, (255, 0, 0), Rect(x*26, y*26, 25, 25)) 
    pygame.display.update()

def search(x,y):
    print("Am pornit")
    print(x,y)	
    for i in range(0,4):
        m,n=xoy[i]
        if(x+m<11)&(y+n<11)&(x+m>-1)&(y+n>-1):
            lovit.append((x, y))
            if (request.request(chr(x+m-1+ord('A')),y+n+1)in["HIT","DESTROYED"]) & ((x+m,y+n) not in lovit):		
                search(x+m,y+n)
                hit(m+x,n+y)

running = True
startNewGame.startNewGame(1)
xoy=[(0,-1),(1,0),(0,1),(-1,0)]
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    while len(lovit)<100:
        x=randint(1,10)
        y=randint(1,10)
        g=chr(x+ord('A')-1)
        if (request.request(g,y)in["HIT","DESTROYED"]) & ((x,y) not in lovit):
            hit(x, y)
            search(x,y)
        else:
            lovit.append((x, y))
        print(request.request(g,y)+str(g)+str(y))
    print("Gata!")

