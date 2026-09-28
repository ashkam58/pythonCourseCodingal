# M6L2A1: Draw a rectangle!
# Activity 1: Drawing Rectangles using pygame.Rect and pygame.draw.rect()

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
