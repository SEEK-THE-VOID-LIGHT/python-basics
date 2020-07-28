import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
FPS = 60

class spritesheet:
    def __init__(self):
        self.image = pygame.image.load('sheet.png')
        self.width = 7
        self.height = 4

        self.rect = self.image.get_rect()
        self.walk_left = [(i*self.rect.width//self.width,0,48,48) for i in range(self.width)]  
    def draw(self,win,x,y,index):
        win.blit(self.image,(x,y),self.walk_left[index])

s = spritesheet()
run = True
uwu = 0
print(s.walk_left)
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
    s.draw(win,200,200,uwu//4)
    uwu += 1
    if uwu == 28:
        uwu = 0
    pygame.display.update()