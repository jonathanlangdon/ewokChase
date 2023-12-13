import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/stormtrooper.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        # New indented lines below
        self.change_x = 0
        # New indented lines above

    # New indented lines below
    def update(self):
        self.rect.x += self.change_x

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

    # New indented lines above
