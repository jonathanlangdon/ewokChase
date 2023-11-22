import sys
import os
import pygame
from pygame.locals import *
import pyganim

pygame.init()

windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption("Sprite Sheet Demo")

standingRects = [
    (1, 1, 46, 67),
    (49, 1, 46, 67),
    (97, 1, 46, 67),
    (145, 1, 46, 67),
]

walkRightRects = [
    (241, 69, 46, 67),
    (193, 69, 46, 67),
    (145, 69, 46, 67),
    (97, 69, 46, 67),
    (49, 69, 46, 67),
    (1, 69, 46, 67),
]

walkLeftRects = [
    (1, 137, 46, 67),
    (49, 137, 46, 67),
    (97, 137, 46, 67),
    (145, 137, 46, 67),
    (193, 137, 46, 67),
    (241, 137, 46, 67),
]

fallingRects = [
    (1, 205, 46, 67),
    (49, 205, 46, 67),
]

jumpRightImage = pygame.image.load("images/jumpRight.png")
jumpLeftImage = pygame.image.load("images/jumpLeft.png")

standingImages = pyganim.getImagesFromSpriteSheet(
    "images/stormtrooperSprite.png", rects=standingRects
)
walkRightImages = pyganim.getImagesFromSpriteSheet(
    "images/stormtrooperSprite.png", rects=walkRightRects
)
walkLeftImages = pyganim.getImagesFromSpriteSheet(
    "images/stormtrooperSprite.png", rects=walkLeftRects
)
fallImages = pyganim.getImagesFromSpriteSheet(
    "images/stormtrooperSprite.png", rects=fallingRects
)

# Create PygAnimation objects for each animation
playerWalkRight = pyganim.PygAnimation(
    list(zip(walkRightImages, [200] * len(walkRightImages)))
)
playerWalkRight.play()

playerWalkLeft = pyganim.PygAnimation(
    list(zip(walkLeftImages, [200] * len(walkLeftImages)))
)
playerWalkLeft.play()

playerFall = pyganim.PygAnimation(list(zip(fallImages, [400] * len(fallImages))))
playerFall.play()

# Set up single images for jump right and jump left
playerJumpRight = pyganim.PygAnimation([(jumpRightImage, 200)])
playerJumpLeft = pyganim.PygAnimation([(jumpLeftImage, 200)])

playerStanding = pyganim.PygAnimation(
    list(zip(standingImages, [4000] * len(standingImages)))
)
playerStanding.play()

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)

while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    playerStanding.blit(windowSurface, (0, 0))
    playerWalkRight.blit(windowSurface, (50, 0))
    playerWalkLeft.blit(windowSurface, (100, 0))
    playerFall.blit(windowSurface, (150, 0))
    playerJumpRight.blit(windowSurface, (200, 0))
    playerJumpLeft.blit(windowSurface, (250, 0))

    pygame.display.update()
    mainClock.tick(30)
