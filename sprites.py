#!/usr/bin/python

import pygame
import random as r

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
run = True
sprites = pygame.sprite.Group()
pygame.display.set_caption("pygame sprite basic")
font = pygame.font.SysFont('arial', 30, italic=1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image.png').convert()
        self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500//2,500//2)
    def collide(self, walls):
        for wall in walls:
            if pygame.sprite.collide_rect(self, wall):
                return True

class obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('obstacle.png')
        self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#--------------------
#self.image = pygame.Surface()
#self.image.fill(color)
#--------------------

player = Player()
walls = []
for i in range(10):
    walls.append(obstacle(r.randint(0,450),r.randint(0,450)))
for wall in walls:
    sprites.add(wall)
sprites.add(player)

while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.rect.right <= 500:
        player.rect.x += 1
    if keys[pygame.K_LEFT] and player.rect.left >= 0:
        player.rect.x -= 1
    if keys[pygame.K_UP] and player.rect.top > 0:
        player.rect.y -= 1
    if keys[pygame.K_DOWN] and player.rect.bottom < 500:
        player.rect.y += 1
    
    if player.collide(walls):
        text = font.render("collision", 1, (0,0,0))
    else:
        text = font.render("no collision", 1, (0,0,0))
    
    
    win.fill((255,255,255))
    win.blit(text, (20, 450))
    sprites.draw(win)
    pygame.display.update()