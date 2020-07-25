import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("button test")

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,30))
        self.image.fill((200,200,200))
        self.font = pygame.font.SysFont('arial', 30)
        self.text = self.font.render("test",1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50,50)
        self.clicked = False
    def draw(self, win):
        win.blit(self.image, self.rect.topleft)
        win.blit(self.text, self.rect.topleft)
        if not self.clicked:
            pygame.draw.rect(win, (200,0,0), (50,50,50,30),2)
        else:
            pygame.draw.rect(win, (255,255,0), (50,50,50,30),2)
    def mouse_collide(self, mouse_x, mouse_y):
        if mouse_x < self.rect.right and mouse_x > self.rect.left:
            if mouse_y < self.rect.bottom and mouse_y > self.rect.top:
                return True

button = Button()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.mouse_collide(mouse_x, mouse_y):
                print("juhuu!")
                button.clicked = True
        else:
            button.clicked = False
    win.fill((255,255,255))
    button.draw(win)
    pygame.display.update()
