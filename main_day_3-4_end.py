import pygame
from random import randint
from Player import Player

# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORE = 0
# new global variable below
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
    pass


def resetPlayer(player):
    # New Lines INDENTED below
    player.rect.x = 400
    player.rect.y = SCREEN_HEIGHT - player.rect.height - 10
    # New indented lines above


def gameReset(player, screen):
    pass


def game_loop(player, game_level):
    # add player inside parenthesis above also new line below:
    global ACTIVE_SPRITE_LIST
    # New line above
    global SCORE
    font = pygame.font.Font(None, 36)
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    done = False
    while not done:
        # new indented line below
        ACTIVE_SPRITE_LIST.update()
        # new indented line above
        game_level.draw(screen)
        # new indented line below
        ACTIVE_SPRITE_LIST.draw(screen)
        # new indented line above
        score_text = font.render("Ewoks caught: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_text, [10, 10])
        pygame.display.flip()


def main():
    # new line below
    global ACTIVE_SPRITE_LIST
    # new line above
    pygame.init()
    pygame.display.set_caption("Catch the Ewoks")
    # New Lines below
    player = Player()
    resetPlayer(player)
    ACTIVE_SPRITE_LIST = pygame.sprite.Group()
    ACTIVE_SPRITE_LIST.add(player)
    # New Lines above
    game_level = GameLevel()
    # add player to parameters () below
    game_loop(player, game_level)
    # add player to parameters () above
    pygame.quit()


if __name__ == "__main__":
    main()
