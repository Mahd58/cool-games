# Write a program where a player controls a sprite when two sprites collide , the game displaying a win message upon meeting a specific condition.
import pygame
import random
Screen_width=500
Screen_height=400
speed=3
pygame.init()
font=pygame.font.SysFont("Times New Roman",100)
bg_image=pygame.transform.scale(pygame.image.load("bg.jpg"),(Screen_width,Screen_height))
s=pygame.display.set_mode((Screen_width,Screen_height))
all_sprites=pygame.sprite.Group()
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("Orange"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(0,min(self.rect.x+x_change,Screen_width-self.rect.width))
        self.rect.y=max(0,min(self.rect.y+y_change,Screen_height-self.rect.height))
player=Sprite(pygame.Color("orange"),50,80)
player.rect.x=300
player.rect.y=200
all_sprites.add(player)
enemy=Sprite(pygame.Color("light blue"),90,70)
enemy.rect.x=50
enemy.rect.y=50
all_sprites.add(enemy)
done=False
win=False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or(event.type==pygame.KEYDOWN and pygame.key==pygame.K_x):
            done=True
            pygame.quit()
    if not win:
        keys=pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*speed
        y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*speed
        player.move(x_change,y_change)
        if player.rect.colliderect(enemy.rect):
            win=True
            all_sprites.remove(enemy)
    s.blit(bg_image,(0,0))
    all_sprites.draw(s)
    if win:
        t=font.render("you win",True,pygame.Color("Yellow"))
        s.blit(t,(0,0))
    pygame.display.flip()
    clock.tick(90)