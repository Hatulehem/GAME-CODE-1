import pygame

#screen 
WINDOW_W = 900
WINDOW_H = 500

#init screen
pygame.init()
size = (WINDOW_W,WINDOW_H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("five nights at freddy's")

#infinite loop
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
