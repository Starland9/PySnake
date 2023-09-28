import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
dt = 0.01

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("purple")

    pygame.draw.circle(screen, "white", player_pos, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    print(player_pos)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
