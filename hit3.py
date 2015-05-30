from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame
import startNewMap
pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]

startNewGame.startNewGame(1)
xoy=[(0,-1),(1,0),(0,1),(-1,0)]

startNewMap.startNewMap(2)
#class forma(*params)

def hit(y,x):
   
    pygame.draw.rect(screen, (255, 0, 0), Rect(x*26, y*26, 25, 25)) 
    '''else:
        pygame.draw.rect(screen, (100, 100, 100), Rect(x*26, y*26, 25, 25)) '''
    pygame.display.update()
    ''' e=pygame.Surface.get_at((x, y))
    if e!=(255,0,0):'''    '''verifica culoarea'''

def hit2(x, y):
    pygame.draw.rect(screen, (50, 0, 0), Rect(x*26, y*26, 25, 25)) 
    pygame.display.update()

def search(x,y):
    global t
    for i in range(0, 4):
        cx, cy = xoy[i]
        newx = x + cx
        newy = y + cy
        if (newx > 0) and (newx < 11) and (newy > 0) and (newy < 11) and ((newx, newy) not in lovit):
           
            lovit.append((newx, newy))
            e=request.request(newx,newy)
            if e=="HIT":
                t+=1
                hit(newx, newy)
                search(newx, newy)
            elif e=="DESTROYED":
                t+=1
                hit(newx, newy)
                return


def ok(x,y):
    print(x,y)
    global t
    t+=1
    lovit.append((x, y))
    if request.request(x,y) in ["HIT", "DESTROYED"]:
    
        return True
    else:
        return False
#def existenta(x,y)


running = True
c=0
t=0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    f=open("matrix.txt","r")
    s=f.readlines()
    
    while c<10:
        print("start")
        x = randint(1, 10)
        y = randint(1, 10)

        if ((x, y) not in lovit) and ( ok(x,y) ) :
            c+=1

            hit(x, y)
            
            search(x, y)

    print("Gata!"+str(t))
    

