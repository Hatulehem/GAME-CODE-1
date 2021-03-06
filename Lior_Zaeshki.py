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

dog_img = pygame.image.load("dog1.png")
red = (242,6,0)
dog_img.set_colorkey(red)

toy_chika = pygame.image.load("toy chica lol.png")
toy_chika = pygame.transform.scale(toy_chika, (80,80))
green = (7,248,19)
toy_chika.set_colorkey(green)

neko_sound = pygame.mixer.Sound("neko music.08")
pygame.mixer.find_channel().play(neko_sound)
neko_sound.set_volume(4.0)

def dog_hit(l):
  return abs(l[0] - toy_x) < 60  and abs(l[1]-toy_y) < 10




font = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()

neko_x = WINDOW_W /2
neko_y = WINDOW_H - 123
vel_neko = 8

dog_list = []

toy_x = 450
toy_y = 100
toy_x_step = 20

score = 0


#function
def print_dog():
  for i in range(len(dog_list)):
    global score
    global toy_x

    l = dog_list[i]
    screen.blit(dog_img,(l[0],l[1]))
    dog_list[i] = [l[0],l[1]-27]

    
    if dog_hit(l):
        score += 1
        toy_x = 0

        hit_sound = pygame.mixer.Sound("meow.mp3")
        pygame.mixer.find_channel().play(hit_sound)


  if len(dog_list) > 0 and dog_list[0][1] < 0:
    dog_list.remove(dog_list[0])



#loop
play = True

while play:
    #images that will appeer
    screen.blit(bk_img , (0,0))
    screen.blit(nekoarc_img, (neko_x - 115/2,neko_y))
    screen.blit(toy_chika , (toy_x-50,toy_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dog_list.append([neko_x,neko_y])

                gurnya = pygame.mixer.Sound("gurnya.mp3")
                pygame.mixer.find_channel().play(gurnya)
                gurnya.set_volume(0.4)  

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


    toy_x +=toy_x_step
    if toy_x > WINDOW_W:
        toy_x_step = -10
    if toy_x <0 :
        toy_x_step = 10



    #text
    text_surface = font.render("Meowww : " + str(score), False ,  (255,255,255))
    screen.blit(text_surface, (20,20))

    #others
    pygame.display.update()
  
    print_dog()

    pygame.display.flip()

    clock.tick(20)

pygame.quit()
