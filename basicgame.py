import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
run = True

x = 50
y = 50
width = 50
height = 50
color = (255,255,0)

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height))
    
    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_DOWN]:
        y += 2
    if keys[pygame.K_UP]:
        y -= 2
        
    
    pygame.display.update()
pygame.quit()