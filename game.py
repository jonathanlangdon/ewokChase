import pygame
from random import randint

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ewok(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ewok.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def placement(self):
        self.rect.x = randint(50, SCREEN_WIDTH - 50)
        self.rect.y = randint(50, SCREEN_HEIGHT - 200)


class Player(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/stormtrooper.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """Move the player."""
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """Calculate effect of gravity."""
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """Called when user hits 'jump' button."""

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """Called when the user hits the left arrow."""
        self.change_x = -5

    def go_right(self):
        """Called when the user hits the right arrow."""
        self.change_x = 5

    def stop(self):
        """Called when the user lets off the keyboard."""
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    """Platform the user can jump on"""

    def __init__(self):
        """Platform constructor. Assumes constructed with user passing in
        an array of 5 numbers like what's defined at the top of this
        code."""
        super().__init__()
        self.image = pygame.image.load("images/platform.jpg")
        self.rect = self.image.get_rect()


class Level(object):
    """This is a generic super-class used to define a level.
    Create a child class for each level with level-specific
    info."""

    def __init__(self, player):
        """Constructor. Pass in a handle to player. Needed for when moving platforms
        collide with the player."""
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # Background image
        self.background = pygame.image.load("images/background.jpg")

    # Update everythign on this level
    def update(self):
        """Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """Draw everything on this level."""

        screen.blit(self.background, (0, 0))
        # # Draw the background

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


# Create platforms for the level
class Level_01(Level):
    """Definition for level 1."""

    def __init__(self, player):
        """Create level 1."""

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        level = [
            # [210, 70, 500, 500],
            # [210, 70, 200, 400],
            # [210, 70, 600, 300],
            [200, 250],
            [400, 570],
            [400, 350],
            [650, 450],
            [650, 250],
            [100, 570],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)


def main():
    """Main Program"""
    pygame.init()
    score = 0
    font = pygame.font.Font(None, 36)

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer Jumper")

    # Create ewok
    ewok = Ewok()

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    ewok.placement()
    active_sprite_list.add(ewok)

    player.rect.x = 340
    # Loop until the user clicks the close button.
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
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

        # Check for collisions between player and ewok
        if pygame.sprite.collide_rect(player, ewok):
            # Increase the score
            score += 1
            print("Score:", score)
            # Respawn the ewok
            ewok.placement()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [10, 10])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
