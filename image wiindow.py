# Write a program to create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.
import pygame
pygame.init()
screen=pygame.display.set_mode((500,300))
pygame.display.set_caption("Eagle nebula")
bg_image=pygame.transform.scale(
    pygame.image.load("Eagle nebula bg.jpeg").convert(),
    (500,300)
)
def game():
    clock=pygame.time.Clock()
    close=False
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
        screen.blit(bg_image,(0,0))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=="__main__":
    game()