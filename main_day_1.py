import pygame
from random import randint
from Player import Player

# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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
    pass


def gameReset(player, screen):
    pass


def game_loop(game_level):
    global SCORE
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    done = False
    while not done:
        game_level.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()
    game_level = GameLevel()
    game_loop(game_level)
    pygame.quit()


if __name__ == "__main__":
    main()
