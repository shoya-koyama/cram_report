import pygame
import random

# ゲームウィンドウの設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# 色の設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# スプライトクラス
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load('pac.png')  # Ensure this image file is in the correct path
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
        self.speed = 5
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed

# 敵クラス
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load('sun.jpg')  # Ensure this image file is in the correct path
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT + 10:
            self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("よけて！！")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Fighter()
        self.all_sprites.add(self.player)
        for i in range(10):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
        self.myfont = pygame.font.SysFont("monospace", 16)

    def event_process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.score += 1
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.running = False
            print(self.player.score)

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        score_text = self.myfont.render("Score: " + str(self.player.score), 1, BLACK)
        self.screen.blit(score_text, (5, 10))
        pygame.display.update()

    def show_game_over(self):
        game_over_text = self.myfont.render("Game Over", 1, RED)
        self.screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2))
        pygame.display.update()
        pygame.time.wait(3000)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.event_process()
            self.update()
            self.draw()
        self.show_game_over()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
