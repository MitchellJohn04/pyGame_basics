import pygame, sys 
from pygame.locals import * 

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400) ,0, 32)    #setting up the window

pygame.display.set_caption('DRAWING')

BLACK = ( 0, 0, 0)                         #setting up colour codes to be directly used while declaring shapes
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)


#Draw on surface objects


DISPLAYSURF.fill(WHITE)                  #fills the entire surface object with the colour specified.              
pygame.draw.polygon(DISPLAYSURF, GREEN,  ((140, 0), (290, 106), (230, 277),(76, 277), (21, 106)))  #POLYGON: (surface, color , pointList , Width)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)                                        #LINE: (Surface, color ,start_point, end_point , width)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120)) 
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)                                            #CIRCLE: (Surface, color, center_point, radius, width)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)                                       #ELLIPSE: (Surface, color, bounding_rectangle, width)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))                                            #RECT : (surface, color, rectangle_tuple, width) 

#pygame.PixelArray Objects 

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj                          #To declare that we have finished drawing individual pixels : if not declared it will not return to draw and will return an error: urface must be locked during blit!

while True:                                  #the game loop.
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
