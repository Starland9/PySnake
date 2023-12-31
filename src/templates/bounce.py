import sys

import pygame

pygame.init()
size = width, height = 800, 600
speed = [1, 1]
screen = pygame.display.set_mode(size)

black = 0, 0, 0

ball = pygame.image.load("assets/intro_ball.gif")
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ball_rect)

    pygame.display.flip()
