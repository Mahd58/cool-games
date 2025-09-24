# Write a Python program to create an empty Pygame window.
import pygame
pygame.init()
screen=pygame.display.set_mode((500,300))
close=False
while not close:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()