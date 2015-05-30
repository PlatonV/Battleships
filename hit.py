from random import randint
import request
import pygame
from pygame.locals import *
import startNewGame


pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]
def hit(x,y):
	print("Am pornit")
	print(x,y)	
	if (s[x-1][y-1]=="1") :
		print("lovit")
	for i in range(0,4):
		m,n=xoy[i]
		if(x+m<11)&(y+n<11)&(x+m>-1)&(y+n>-1):
			if (request.request(chr(x+m-1+ord('A')),y+n+1)in["HIT","DESTROYED"]) & ((x+m,y+n) not in lovit):		
				hit(x+m,y+n)
		lovit.append((m+x,n+y))


running = True
startNewGame.startNewGame()
xoy=[(0,-1),(1,0),(0,1),(-1,0)]
while running:

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	ok=True

	file=open("matrix.txt","r")
	s=file.readlines()
	

	while len(lovit)<100:
		
		x= randint(1,10)
		y=randint(1,10)
		g=chr(x+ord('A')-1)
		if (request.request(g,y)in["HIT","DESTROYED"]) & ((x,y) not in lovit):

			
			lovit.append((x,y))
			hit(x,y)
		print(request.request(g,y)+str(g)+str(y))


		
		
















	pygame.display.update()