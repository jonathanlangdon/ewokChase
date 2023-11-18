import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600


class Player(Actor):

  def __init__(self, x, y):
    super().__init__("stormtrooper", (x, y))
    self.change_x = 0
    self.change_y = 0

  def update(self):
    self.change_y += 0.35  # Gravity
    self.y += self.change_y

    # Check for collision with edges of the screen
    if self.y > HEIGHT - self.height:
      self.y = HEIGHT - self.height  # Stop falling
      self.change_y = 0
    # if self.x < 20:
    #   self.left = 0
    # elif self.x > WIDTH - 30:
    #   self.right = WIDTH - 30


class Platform(Actor):

  def __init__(self, x, y):
    super().__init__("platform", (x, y))


def place_star():
  star.x = randint(50, WIDTH - 50)
  star.y = randint(50, HEIGHT - 200)


player = Player(50, HEIGHT)
platforms = [Platform(400, 500), Platform(600, 400), Platform(200, 300), Platform(400, 250)]
star = Actor("star", (100, 400))

score = 0
background = "background.jpg"


def draw():
  screen.blit(background, (0, 0))
  player.draw()
  for platform in platforms:
    platform.draw()
  star.draw()
  screen.draw.text("Score: " + str(score), (20, 20), color="white")


def update():
  global score

  player.update()

  player.x += player.change_x

  if player.left < 0:
    player.left = 0
  elif player.right > WIDTH:
    player.right = WIDTH

  for platform in platforms:
    if player.colliderect(platform):
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
      block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
      for block in block_hit_list:

          # Reset our position based on the top/bottom of the object.
          if self.change_y > 0:
              self.rect.bottom = block.rect.top
          elif self.change_y < 0:
              self.rect.top = block.rect.bottom

          # Stop our vertical movement
          self.change_y = 0

  # Check for collision with star
  if player.colliderect(star):
    score += 1
    place_star()


def on_key_down(key):
  if key == keys.LEFT:
    player.change_x = -5
  elif key == keys.RIGHT:
    player.change_x = 5
  elif key == keys.UP and player.change_y == 0:
    player.change_y = -10


def on_key_up(key):
  if key == keys.LEFT and player.change_x < 0:
    player.change_x = 0
  elif key == keys.RIGHT and player.change_x > 0:
    player.change_x = 0


pgzrun.go()
