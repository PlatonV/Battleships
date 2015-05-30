from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame
import startNewMap
pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]


xoy=[(0,-1),(1,0),(0,1),(-1,0)]
startNewGame.startNewGame(1)
startNewMap.startNewMap(1)
startNewMap.startNewMap(1)



def hit(y,x):
   
    pygame.draw.rect(screen, (255, 0, 0), Rect(x*26, y*26, 25, 25)) 
    pygame.display.update()
def search(x,y):
    global t
    global aux
    global m
   
    for i in range(0, 4):
        cx, cy = xoy[i]

        newx = x + cx
        newy = y + cy

        if (newx > 0) and (newx < 11) and (newy > 0) and (newy < 11) and ((newx, newy) not in lovit):
            print(newx,newy)
            lovit.append((newx, newy))
            e=request.request(newx,newy)
            if e=="HIT":
                t+=1
                m+=1
                hit(newx, newy)
                search(newx, newy)

            elif e=="DESTROYED":
                t+=1
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



running = True
c=0
t=0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
   
    
    while c<10:
        x = randint(1, 10)
        y = randint(1, 10)
        print(x,y)
        if ((x, y) not in lovit) and ( ok(x,y) ) :
            c+=1
            m=1
        
            hit(x, y)
            
            search(x, y)
            print(m)
            print("am iesit")
            if m == 3:
                print(aux)
                print (sorted(aux))
                l,m=aux[1]
                request.request(l,m)
           

    if c==10:
        print(t)
        c=11
    