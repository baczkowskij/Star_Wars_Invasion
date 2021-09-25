import sys
import pygame

pygame.init()
pygame.display.set_mode((1200,800))
pygame.display.update()

open = True

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
pygame.quit()
quit()