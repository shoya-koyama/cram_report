import pygame
import sys
import random

# Define screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# Define grid size and dimensions
GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE

# Define directions
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)

def drawCube(surface, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(surface, color, r)
    pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 255, 0)  # Food is green
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Poison():
   def __init__(self):
       self.position = (0, 0)
       self.color = (255, 0, 0)  # Poison is red
       self.randomize_position()

   def randomize_position(self):
       self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

   def draw(self, surface):
       r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
       pygame.draw.rect(surface, self.color, r)
       pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Requza():
   
   def __init__(self):
       self.length = 1
       self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
       self.direction = random.choice([up, down, left, right])
       self.color = (0, 255, 0)  # Green
       self.score = 0
       self.health = 100  # Add health attribute
    

   # Rest of the code...
   def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_UP]:
                    self.direction = up
                elif keys[pygame.K_DOWN]:
                    self.direction = down
                elif keys[pygame.K_LEFT]:
                    self.direction = left
                elif keys[pygame.K_RIGHT]:
                    self.direction = right
   
    # Existing code...
   def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

   def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([up, down, left, right])
     
   def get_head_position(self):
        return self.positions[0] 
   

   def draw(self, surface):
        for p in self.positions:
            drawCube(surface, self.color, p)

def main():
   pygame.init()

   clock = pygame.time.Clock()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

   surface = pygame.Surface(screen.get_size())
   surface = surface.convert()
   drawGrid(surface)

   requza = Requza()
   food = Food()
   poison = Poison()  # Create a poison object

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
       if requza.get_head_position() == poison.position:  # Decrease health if snake eats poison
           requza.health -= 10
           poison.randomize_position()
       if requza.health <= 0:  # End game if health is zero
           print("Game Over! Score was: ", requza.score)
           break
       requza.draw(surface)
       food.draw(surface)
       poison.draw(surface)  # Draw the poison
       screen.blit(surface, (0, 0))
       text = myfont.render("Score: {0}, Health: {1}".format(requza.score, requza.health), 1, (0, 0, 0))  # Update score display to include health
       screen.blit(text, (5, 10))
       pygame.display.update()

   pygame.quit()

main()
