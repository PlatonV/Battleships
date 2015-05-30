import pygame
from pygame.locals import *
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	file=open("matrix.txt","r")
	#pygame.screen.fill((234,234,56))
	for i in range(10):
		s=file.readline()
		for j in range (10):
			r=Rect(200+i*25,200+j*25,23,23)
			if s[j]=="0":
				pygame.draw.rect(screen,(0,0,255),r)
			elif s[j]=="1":
				pygame.draw.rect(screen,(100,100,100),r)
			elif s[j]=="2":
				pygame.draw.rect(screen,(255,0,0),r)
	pygame.display.update()
				#pygame.draw.rect(screen,(255,234,0),(i*16,j*16,15,15))


		