from random import randint
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
lovit=[]
def hit(x,y):
	print(x+1,y+1)	
	if (s[x][y]=="1") :
		print("lovit")
	for i in range(0,4):
		m,n=xoy[i]
		if(x+m<10)&(y+n<10)&(x+m>-1)&(y+n>-1):
			if (s[x+m][y+n]=="1") & ((x+m,y+n) not in lovit):
			
				lovit.append((m+x,n+y))
				hit(x+m,y+n)
		
				




print("Am pornit")

running = True
xoy=[(0,-1),(1,0),(0,1),(-1,0)]
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	ok=True

	file=open("matrix.txt","r")
	s=file.readlines()
	

	while ok:
		
		x= randint(0,9)
		y=randint(0,9)
		if (s[x][y]=="1") & ((x,y) not in lovit):
			lovit.append((x,y))
			hit(x,y)

		ok=False
















	pygame.display.update()