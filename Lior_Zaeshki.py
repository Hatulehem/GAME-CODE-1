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
pizza_img = pygame.image.load("pizza.png")
pizza_img = pygame.transform.scale(pizza_img,(110,110))

clock = pygame.time.Clock()

pizza_img_x = 10
pizza_img_y = WINDOW_H /2
nekoarc_img_x = WINDOW_W /2
nekoarc_img_y = WINDOW_H - 123

pizza_img_x_step = 10
neko_x_step = 10
pizza_list = []

#function
def print_pizza():
    for i in range (len(pizza_list)):
        p = pizza_list[i]
    screen.blit(pizza_img, (p[0],p[1]))
    pizza_list[i] = [p[0],p[1] - 60]

    if len(pizza_list) > 0 and pizza_list[0][1] < 0:
        pizza_list.remove(pizza_list[0])










#loop
play = True

while play:
    screen.blit(bk_img , (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KYDOWN:
            if event.key == pygame.K_LEFT:
                nekoarc_img_x -= neko_x_step
            if event.key == pygame.K_RIGHT:
                nekoarc_img_x += neko_x_step
            if event.key == pygame.K_SPACE:
                pizza_list.append([nekoarc_img_x, 115/2 , nekoarc_img_y])
    
    screen.blit(nekoarc_img, nekoarc_img_x,nekoarc_img_y)
    print_pizza()




    pygame.display.flip()

    clock.tick(10)

pygame.quit()
