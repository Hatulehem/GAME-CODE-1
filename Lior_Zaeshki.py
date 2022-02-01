import pygame

#screen size
WINDOW_W = 900
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W,WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hypnosis Arc: The Neko Battle")

#images/variables
bk_img = pygame.image.load("bk_neko arc.jpg")
nekoarc_img = pygame.image.load("neko player 1.png")
nekoarc_img = pygame.transform.scale(nekoarc_img,(115,123))


clock = pygame.time.Clock()

neko_x = WINDOW_W /2
neko_y = WINDOW_H - 123

vel_neko = 8
# pizza_img_x_step = 10
# neko_x_step = 10
# pizza_list = []

#function
# def print_pizza():
#     for i in range (len(pizza_list)):
#         p = pizza_list[i]
#         screen.blit(pizza_img, (p[0],p[1]))
#         pizza_list[i] = [p[0],p[1] - 60]

#     if len(pizza_list) > 0 and pizza_list[0][1] < 0:
#         pizza_list.remove(pizza_list[0])










#loop
play = True

while play:
    screen.blit(bk_img , (0,0))
    screen.blit(nekoarc_img, (neko_x - 115/2,neko_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    #keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        neko_x += vel_neko
    if keys[pygame.K_LEFT]:
        neko_x -= vel_neko
    if keys[pygame.K_DOWN]:
        neko_y += vel_neko
    if keys[pygame.K_UP]:
        neko_y -= vel_neko


    pygame.display.update()
    pygame.display.flip()

    clock.tick(20)

pygame.quit()
