# Write a program to create a Space Invader Game using Pygame Library in Python.
import math
import random
import pygame
# Constants
Screen_width=800
Screen_height=500
player_start_X=400
player_start_Y=380
Enemy_start_Y_min=50
Enemy_start_Y_max=150
Enemy_speed_y=40
Fireball_speed_y=10
Enemy_speed_x=4
Collision_distance=27
pygame.init()
Screen=pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Space invader")
icon=pygame.image.load("Rocket.png")
pygame.display.set_icon(icon)
player_image=pygame.image.load("Rocket.png")
player_x=player_start_X
player_y=player_start_Y
player_x_change=0
enemy_image=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemies=5
for i in range(0,number_of_enemies):
    alien_image=pygame.image.load("alien.png")
    enemy_image.append(alien_image)
    enemy_x.append(random.randint(0,Screen_width-64))
    enemy_y.append(random.randint(Enemy_start_Y_min,Enemy_start_Y_max))
    enemy_x_change.append(Enemy_speed_x)
    enemy_y_change.append(Enemy_speed_y)
fireball_image=pygame.image.load("fireball.png")
fireball_x=0
fireball_y=player_start_Y
fireball_x_change=0
fireball_y_change=Fireball_speed_y
bullet_state="ready"
close_screeen=False
bg=pygame.image.load("bg.jpg")
while not close_screeen:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    Screen.blit(bg,(0,0))
    pygame.display.flip()
pygame.quit()