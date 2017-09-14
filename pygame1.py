import pygame, sys                                   
from pygame.locals import *                          #imports all PyGame modules, you can skip writing the exact module name.

pygame.init()                                        #initualizes PyGame-- 

DISPLAYSURF = pygame.display.set_mode((400, 300))    #Dimension of the Pygame window (width:height)

pygame.display.set_caption(' Hello World!! ')        #to make text appear on caption.

while True:                                          #Main game loop
	for event in pygame.event.get(): 
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()