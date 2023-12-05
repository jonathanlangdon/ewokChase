import pygame


class Player(pygame.sprite.Sprite):
    # New indented lines below
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/stormtrooper.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    # New indented lines above
