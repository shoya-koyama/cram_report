import pygame
import sys
import random


class Requza():
   def __init__(self):
       self.length = 1
       self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
       self.direction = random.choice([up, down, left, right])
       self.color = (16, 27, 46)
       self.score = 0

   def get_head_position(self):
       return self.positions[0]

   def turn(self, point):
       if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
           return
       else:
           self.direction = point

   def move(self):
       cur = self.get_head_position()
       x, y = self.direction
       n = (((cur[0] + (x * GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT)
       if len(self.positions) > 2 and n in self.positions[2:]:
           self.reset()
       else:
           self.positions.insert(0, n)
           if len(self.positions) > self.length:
               self.positions.pop()

   def reset(self):
       self.length = 1
       self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
       self.direction = random.choice([up, down, left, right])
       self.score = 0

   def draw(self, surface):
       for p in self.positions:
           r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
           pygame.draw.rect(surface, self.color, r)
           pygame.draw.rect(surface, (93, 216, 218), r, 1)

   def handle_keys(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                   self.turn(up)
               elif event.key == pygame.K_DOWN:
                   self.turn(down)
               elif event.key == pygame.K_LEFT:
                   self.turn(left)
               elif event.key == pygame.K_RIGHT:
                   self.turn(right)


class Food():
   def __init__(self):
       self.position = (0, 0)
       self.color = (225, 161, 43)
       self.randomize_position()

   def randomize_position(self):
       self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

   def draw(self, surface):
       r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
       pygame.draw.rect(surface, self.color, r)
       pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):
   for y in range(0, int(GRID_HEIGHT)):
       for x in range(0, int(GRID_WIDTH)):
           if (x + y) % 2 == 0:
               r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
               pygame.draw.rect(surface, (93, 216, 228), r)
           else:
               rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
               pygame.draw.rect(surface, (84, 194, 205), rr)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def main():
   pygame.init()

   clock = pygame.time.Clock()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

   surface = pygame.Surface(screen.get_size())
   surface = surface.convert()
   drawGrid(surface)

   requza = Requza()
   food = Food()

   myfont = pygame.font.SysFont("monospace", 16)

   while (True):
       clock.tick(10)
       requza.handle_keys()
       drawGrid(surface)
       requza.move()
       if requza.get_head_position() == food.position:
           requza.length += 1
           requza.score += 1
           food.randomize_position()
       requza.draw(surface)
       food.draw(surface)
       screen.blit(surface, (0, 0))
       text = myfont.render("mega enagy {0}".format(requza.score), 1, (0, 0, 0))
       screen.blit(text, (5, 10))
       pygame.display.update()


main()