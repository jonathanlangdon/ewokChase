import pygame
from random import randint
from Player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ewok(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ewok.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def placement(self):
        self.rect.x = randint(50, 750)
        self.rect.y = randint(50, 400)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/platform.jpg")
        self.rect = self.image.get_rect()


class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.background = pygame.image.load("images/background.jpg")

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        level = [
            [100, 200],
            [100, 450],
            [350, 570],
            [350, 330],
            [600, 450],
            [600, 200],
        ]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)


def main():
    pygame.init()
    score = 0
    font = pygame.font.Font(None, 36)
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Platformer Jumper")
    ewok = Ewok()
    player = Player()
    level_list = []
    level_list.append(Level_01(player))
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    ewok.placement()
    active_sprite_list.add(ewok)
    player.rect.x = 400
    player.rect.y = SCREEN_HEIGHT - player.rect.height - 100
    active_sprite_list.add(player)
    done = False
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        if pygame.sprite.collide_rect(player, ewok):
            score += 1
            print("Score:", score)
            ewok.placement()

        active_sprite_list.update()
        current_level.update()

        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        if player.rect.left < 0:
            player.rect.left = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, [10, 10])

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
