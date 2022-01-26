from pickle import TRUE
import pygame

#screen 
WINDOW_W = 900
WINDOW_H = 500

#init screen
pygame.init()
size = (WINDOW_W,WINDOW_H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hypnosis Arc: The Neko Battle")

#משתנים
clock = pygame.time.Clock()
x_player = 450
y_player = 430
vel = 2

#loop
RUN =   True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

#Fill Screen
    #background
    img = pygame.image.load("neko arc.jpg")
    screen.blit(img , (0,0))
    #player
    bg_player_color = (115,152,255)
    player_img = pygame.image.load("neko ar.png").convert()
    player_img.set_colorkey(bg_player_color)
    screen.blit(player_img, [x_player,y_player])

#keys 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_player -= vel
    if keys[pygame.K_RIGHT]:
        x_player += vel
    if keys[pygame.K_UP]:
        y_player -= vel
    if keys [pygame.K_DOWN]:
        y_player += vel

    if x_player <= 0:
        x_player = 70
    if x_player >= 900:
        x_player = 830

    pygame.display.flip()

pygame.quit()
