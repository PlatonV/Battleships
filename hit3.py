from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame
import startNewMap
pygame.init()

screen = pygame.display.set_mode((800, 600))

xoy=[(0,-1),(1,0),(0,1),(-1,0)]
startNewGame.startNewGame(1)

def hit(y,x):
    pygame.draw.rect(screen, (255, 0, 0), Rect(x*60, y*40, 55, 35)) 
    pygame.display.update()

def hit2(x, y):
    pygame.draw.rect(screen, (50, 0, 0), Rect(x*60, y*40, 55, 35)) 
    pygame.display.update()

def search(x,y):
    global t
    global aux
    global m
    aux.append((x,y))
    for i in range(0, 4):
        cx, cy = xoy[i]

        newx = x + cx
        newy = y + cy
        if (newx > 0) and (newx < 11) and (newy > 0) and (newy < 11) and ((newx, newy) not in lovit):
           
            lovit.append((newx, newy))
            e=request.request(newx,newy)
            t += 1
            if e=="HIT":
                m+=1
                hit(newx, newy)
                search(newx, newy)

            elif e=="DESTROYED":
                print('DESTROYED')
                hit(newx, newy)
                return
def ok(x,y):
    global t
    t+=1
    lovit.append((x, y))
    if request.request(x,y) in ["HIT", "DESTROYED"]:
        return True
    else:
        return False
def dele(t):
    for y in t :
        for i in range(4):
            m,n=y
            a,b=xoy[i]
            if (m+a > 0) and (m+a < 11) and (m+a > 0) and (n+b < 11) and ((m+a, n+b) not in lovit):
                lovit.append((m+a,b+n))

aux=[[0 for x in range(11)] for y in range(11)]
c=0
t=0

def solve():
    global c
    global t
    global aux
    global m
    global lovit
    c = 0
    t = 0
    lovit = []
    aux=[[0 for x in range(11)] for y in range(11)]
    while c<10:
        x = randint(1, 10)
        y = randint(1, 10)

        if ((x, y) not in lovit) and ( ok(x,y) ) :
            c+=1
            m=1
            aux=[]
           
            hit(x, y)
            
            search(x, y)
            dele(aux)
            print(m)
            if m == 3:
                l,m=aux[1]
                t+=1
                request.request(l,m)
            elif m > 3:
                for x, y in aux:
                    t+=1
                    if request.request(x,y) == "DESTROYED":
                        break
    if c==10:
        print(t)
        c=11

''' APP ENTRY POINT '''
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    solve()
    startNewMap.startNewMap(1)
    screen.fill((0,0,0))
    solve()
    running = False

