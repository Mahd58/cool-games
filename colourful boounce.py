# This activity, "Colorful Bounce," involves a moving rectangle (sprite) that bounces off the window edges. Each bounce changes its color and the window's background color, creating a dynamic display of colors.
import pygame
import random
pygame.init()
sprite_coolour_change_event=pygame.USEREVENT+1
background_coulor_event=pygame.USEREVENT+2
red=pygame.Color("red")
green=pygame.Color("green")
black=pygame.Color("black")
white=pygame.Color("white")
blue=pygame.Color("blue")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-5,5]),random.choice([-5,5])]
    def update_method(self):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundry_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            boundry_hit=True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(sprite_coolour_change_event))
            pygame.event.post(pygame.event.Event(background_coulor_event))
    def change_sprite_color(self):
        self.image.fill(random.choice([red,green,black]))
def change_bgcoolor():
    global bg_color
    bg_color=random.choice([white,blue])
all_sprit_list=pygame.sprite.Group()
ob1=Sprite(red,20,30)
ob1.rect.x=random.randint(0,480)
ob1.rect.y=random.randint(0,380)
all_sprit_list.add(ob1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Colourful bounce")
clock=pygame.time.Clock()
close=False
bg_color=white
while not close:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            close=True
        elif event.type==sprite_coolour_change_event:
            ob1.change_sprite_color()
        elif event.type==background_coulor_event:
            change_bgcoolor()
    all_sprit_list.update()
    screen.fill(bg_color)
    all_sprit_list.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()