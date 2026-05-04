import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Baby Mario")
clock = pygame.time.Clock()

background= pygame.image.load("DesertBG.jpg")
background = pygame.transform.scale(background, (width, height))
mario = pygame.image.load("mnlv2.png")
mario = pygame.transform.scale(mario, (100, 100))

mario_x = 400
mario_y = 400

#scolling background
scroll = 0
speed = 3

#main loop
running = True
while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move background
    scroll -= speed
    if scroll <= -background.get_width():
        scroll = 0

    #wrapping mario arounf the screen
    if mario_x > wideth:
        mario_x = -mario.get_width()
    elif mario_x < -mario.get_width():
        mario_x = wideth

    #MARIO MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= 5
    if keys[pygame.K_RIGHT]:
        mario_x += 5
    if key [pygames.K_SPACE] and mario_y == 400:
        mario_y -= 150
    if mario_y < 400:
        mario_y += 5

    #draw background and mario
    screen.blit(background, (scroll, 0))
    screen.blit(background, (scroll + background.get_width(), 0))
    screen.blit(mario, (mario_x, mario_y))

    pygame.display.update()
    clock.tick(60)


