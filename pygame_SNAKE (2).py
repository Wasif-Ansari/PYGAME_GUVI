import pygame,os,sys
from pygame.locals import * #loads constants

catx = 10
caty = 10
screen = 0

def myquit():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global catx,caty,screen
    #func to handle events
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key == K_LEFT:
                    catx -=5
                    print("Move Rect left")
                elif event.key == K_RIGHT:
                    catx+=5
                    print("Move Rect right")
                else:
                    print(event.key)
    screen.fill((255,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
    pygame.display.update()


def main():
    global screen
    pygame.init()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 480
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("THE SNAKE")
    screen = pygame.display.get_surface()

    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()


# #set up window 
# DISPLAYSURF = pygame.display.set_mode((250,250))
# pygame.display.set_caption("THE SNAKE")

# #set up a drawing surface
# screen = pygame.display.get_surface()
# screen.fill(red)
# pygame.display.set_caption("Snake")
# pygame.display.flip()

# while True:# main game loop
#     for event in pygame.event.get():
#         print(event)
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()