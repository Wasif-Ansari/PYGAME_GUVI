import pygame,os,sys
from pygame.locals import * #loads constants

pygame.init()

#setup window
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Drawing')

#setup colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#drawing shapes on the surface
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF,GREEN,((146,0),(291,106),(236,200),(100,250),(12,106)))
pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
pygame.draw.line(DISPLAYSURF,BLUE,(120,60),(60,120))
pygame.draw.line(DISPLAYSURF,BLUE,(60,120),(120,120),4)
pygame.draw.circle(DISPLAYSURF,BLUE,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,RED,(300,200,40,80),1)
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[380][280] = BLACK
pixObj[382][282] = BLACK
pixObj[384][284] = BLACK
pixObj[386][286] = BLACK
pixObj[388][288] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

















# catx = 10
# caty = 10
# screen = 0

# def myquit():
#     pygame.quit()
#     sys.exit(0)

# def check_inputs(events):
#     global catx,caty,screen
#     #func to handle events
#     for event in events:
#         if event.type == QUIT:
#             quit()
#         else:
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     myquit()
#                 elif event.key == K_LEFT:
#                     catx -=5
#                     print("Move Rect left")
#                 elif event.key == K_RIGHT:
#                     catx+=5
#                     print("Move Rect right")
#                 else:
#                     print(event.key)
#     screen.fill((255,0,0))
#     pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
#     pygame.display.update()


# def main():
#     global screen
#     pygame.init()
#     SCREEN_WIDTH = 600
#     SCREEN_HEIGHT = 480
#     window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#     pygame.display.set_caption("THE SNAKE")
#     screen = pygame.display.get_surface()

#     pygame.display.update()

#     while True:
#         check_inputs(pygame.event.get())

# main()


# # #set up window 
# # DISPLAYSURF = pygame.display.set_mode((250,250))
# # pygame.display.set_caption("THE SNAKE")

# # #set up a drawing surface
# # screen = pygame.display.get_surface()
# # screen.fill(red)
# # pygame.display.set_caption("Snake")
# # pygame.display.flip()

# # while True:# main game loop
# #     for event in pygame.event.get():
# #         print(event)
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #     pygame.display.update()