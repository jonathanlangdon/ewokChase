import pygame
from random import randint
from Player import Player

SCRN_WIDTH = 800
SCRN_HEIGHT = 600
SCORE = 0
ACTIVE_SPRITE_LIST = []


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
        self.player = player
        self.background = pygame.image.load("images/background.jpg")

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.platform_list.draw(screen)


class GameLevel(Level):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.player = player
        self.background = pygame.image.load("images/background.jpg")
        level_platforms = [
            [100, 200],
            [100, 450],
            [350, 570],
            [350, 330],
            [600, 450],
            [600, 200],
        ]
        for platform in level_platforms:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            self.platform_list.add(block)

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.platform_list.draw(screen)


def handle_input(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
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
    return False


def resetPlayer(player):
    player.rect.x = 400
    player.rect.y = SCRN_HEIGHT - player.rect.height - 100


def gameReset(player, screen):
    global SCORE
    player.stop()
    font = pygame.font.Font(None, 60)
    text = font.render(f"You died. You caught {SCORE} ewoks", True, (255, 255, 255))
    screen.blit(text, (100, SCRN_HEIGHT // 2))
    pygame.display.flip()
    start_ticks = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_ticks < 5000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    resetPlayer(player)
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.display.flip()
    SCORE = 0


def game_loop(player, ewok, game_level):
    global ACTIVE_SPRITE_LIST
    global SCORE
    font = pygame.font.Font(None, 36)
    size = [SCRN_WIDTH, SCRN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    done = False
    while not done:
        done = handle_input(player)
        if pygame.sprite.collide_rect(player, ewok):
            SCORE += 1
            ewok.placement()
        ACTIVE_SPRITE_LIST.update()
        game_level.update()
        if player.rect.right > SCRN_WIDTH:
            player.rect.right = SCRN_WIDTH
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.top > SCRN_HEIGHT + 50:
            gameReset(player, screen)
        game_level.draw(screen)
        ACTIVE_SPRITE_LIST.draw(screen)
        score_text = font.render("Ewoks caught: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_text, [10, 10])
        clock.tick(60)
        pygame.display.flip()


def main():
    global ACTIVE_SPRITE_LIST
    pygame.init()
    pygame.display.set_caption("Catch the Ewoks")
    player = Player()
    ewok = Ewok()
    game_level = GameLevel(player)
    player.level = game_level
    ACTIVE_SPRITE_LIST = pygame.sprite.Group()
    ACTIVE_SPRITE_LIST.add(ewok)
    ACTIVE_SPRITE_LIST.add(player)
    ewok.placement()
    resetPlayer(player)
    game_loop(player, ewok, game_level)
    pygame.quit()


if __name__ == "__main__":
    main()
