import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGTH))

pygame.display.set_caption("Chemical Shooting")
icon = pygame.image.load("img/images.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/1.png")
target_width = 200
target_higth = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGTH - target_higth)

color = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))

score = 0
bullets = 10

running = True
while running and bullets > 0 and score < 6:
    screen.fill(color)
    font = pygame.font.SysFont('couriernew', 20)
    text = font.render(("reach 6 hits:"), True, (0,0,0))
    text_score = font.render(str(score), True, (0, 0, 0))
    text2 = font.render(("electrons:"), True, (0, 0, 0))
    text_bullets = font.render(str(bullets), True, (0, 0, 0))
    screen.blit(text, (5, 5))
    screen.blit(text_score, (175, 5))
    screen.blit(text2, (5, 35))
    screen.blit(text_bullets, (155, 35))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_higth:

                score += 1
                if score == 1:
                    target_img = pygame.image.load("img/2.png")
                elif score == 2:
                    target_img = pygame.image.load("img/3.png")
                elif score == 3:
                    target_img = pygame.image.load("img/4.png")
                elif score == 4:
                    target_img = pygame.image.load("img/5.png")
                elif score == 5:
                    target_img = pygame.image.load("img/6.png")


    target_x = target_x + random.randint(-30, 30)
    if target_x <=0:
        target_x = target_x + 30
    elif target_x >= (SCREEN_WIDTH - target_width):
        target_x = target_x - 30

    target_y = target_y + random.randint(-30, 30)
    if target_y <= 0:
        target_y = target_y + 30
    elif target_y >= (SCREEN_HIGTH - target_higth):
        target_y = target_y - 30


   # target_x = random.randint(0, SCREEN_WIDTH - target_width)
    #target_y = random.randint(0, SCREEN_HIGTH - target_higth)

    pygame.time.delay(60)


    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

if bullets <= 0 and score < 6:
    final_running = True
    while final_running:
        screen.fill(color)
        font = pygame.font.SysFont('couriernew', 90)
        gameover = font.render(("game over"), True, (0, 0, 0))
        screen.blit(gameover, (150, 230))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_running = False

        pygame.display.update()

if score >= 6:
    win_running = True
    while win_running:
        screen.fill(color)
        font = pygame.font.SysFont('couriernew', 90)
        win = font.render(("you win!"), True, (0, 0, 0))
        screen.blit(win, (150, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win_running = False
        pygame.display.update()









pygame.quit()