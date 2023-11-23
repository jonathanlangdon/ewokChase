import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/stormtrooper.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.level = None

    def x_collisions(self):
        block_hit_list_x = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        for block in block_hit_list_x:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

    def y_collisions(self):
        block_hit_list_y = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        for block in block_hit_list_y:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

    def screen_side_collisions(self):
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        self.x_collisions()
        self.rect.y += self.change_y
        self.y_collisions()
        self.screen_side_collisions()

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        self.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.change_y = -10

    def go_left(self):
        self.change_x = -5

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0
