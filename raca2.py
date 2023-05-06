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

# ゲームの初期化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("よけて！！")
clock = pygame.time.Clock()

# フォントの設定
FONT_SIZE = 24
FONT_COLOR = BLACK
FONT = pygame.font.SysFont("Arial", FONT_SIZE)

# スプライトクラス
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
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
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT + 10:
            self.kill()


# スプライトグループ
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Fighter()
all_sprites.add(player)

# 敵を生成
ENEMY_COUNT = 10
ENEMY_SPEED = 5
for i in range(ENEMY_COUNT):
    enemy = Enemy(ENEMY_SPEED)
    all_sprites.add(enemy)
    enemies.add(enemy)

# メインループ
running = True
myfont = FONT.render("Score: 0", True, FONT_COLOR)

while running:
    clock.tick(FPS)
    player.score += 1

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新処理
    all_sprites.update()

    # 当たり判定
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        
    # 描画処理
    screen.fill(WHITE)
    all_sprites.draw(screen)
    score_text = FONT.render("Score: {}".format(player.score), True, FONT_COLOR)
    score_rect = score_text.get_rect(center=(WINDOW_WIDTH / 2, FONT_SIZE))
    screen.blit(score_text, score_rect)
    pygame.display.update()

pygame.quit()