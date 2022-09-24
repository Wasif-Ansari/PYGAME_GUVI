import pygame,os,sys
from pygame.locals import * #loads constants

red = [255,0,0] #represent color as list or tuple

pygame.init()

#set up window 
DISPLAYSURF = pygame.display.set_mode((1000,600))
pygame.display.set_caption("THE SNAKE")

#set up a drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:# main game loop
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()