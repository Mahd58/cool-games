# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.
import pygame
pygame.init()
screen=pygame.display.set_mode((300,300))
donne=False
while not donne:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            donne=True
    pygame.draw.rect(screen,"orange",pygame.Rect(150,150,20,40))
    pygame.draw.circle(screen,"Blue",(100,90),50,5)
    pygame.draw.polygon(screen,"red",[(100,200),(150,50),(100,100)],3)
    pygame.display.flip()