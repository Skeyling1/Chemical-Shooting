import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGTH))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/images.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 100
target_higth = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGTH - target_higth)

color = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))

score = 0

running = True
while running:
    screen.fill(color)
    font = pygame.font.SysFont('couriernew', 20)
    text = font.render(("your score:"), True, (0,0,0))
    text_score = font.render(str(score), True, (0, 0, 0))
    screen.blit(text, (5, 5))
    screen.blit(text_score, (155, 5))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_higth:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HIGTH - target_higth)
                score += 1

    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()


pygame.quit()