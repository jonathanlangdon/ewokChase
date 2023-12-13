import pygame
from random import randint
from Player import Player

# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORE = 0
ACTIVE_SPRITE_LIST = []


class Ewok(pygame.sprite.Sprite):
    pass


class Platform(pygame.sprite.Sprite):
    pass


class GameLevel:
    def __init__(self):
        self.background = pygame.image.load("images/background.jpg")

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


def handle_input(player):
    # New INDENTED lines below:
    # Be VERY careful with INDENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.go_right()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
    return False
    # New lines above - make indents perfect!!


def resetPlayer(player):
    player.rect.x = 400
    player.rect.y = SCREEN_HEIGHT - player.rect.height - 10


def gameReset(player, screen):
    pass


def game_loop(player, game_level):
    global ACTIVE_SPRITE_LIST
    global SCORE
    font = pygame.font.Font(None, 36)
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    done = False
    while not done:
        # New line below
        done = handle_input(player)
        # New line above
        ACTIVE_SPRITE_LIST.update()
        game_level.draw(screen)
        ACTIVE_SPRITE_LIST.draw(screen)
        score_text = font.render("Ewoks caught: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_text, [10, 10])
        pygame.display.flip()


def main():
    global ACTIVE_SPRITE_LIST
    pygame.init()
    pygame.display.set_caption("Catch the Ewoks")
    player = Player()
    resetPlayer(player)
    ACTIVE_SPRITE_LIST = pygame.sprite.Group()
    ACTIVE_SPRITE_LIST.add(player)
    game_level = GameLevel()
    game_loop(player, game_level)
    pygame.quit()


if __name__ == "__main__":
    main()
