import pygame
import random
import time

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
    def __init__(self):
        super().__init__()
        image = pygame.image.load('sun.jpg')
        self.image = pygame.Surface((image.get_width(), image.get_height()))
        self.image.blit(image, (0, 0))
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



# スプライトグループ
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Fighter()
all_sprites.add(player)

for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# メインループ
running = True
fighter = Fighter()
myfont = pygame.font.SysFont("monospace", 16)
while running:
    clock.tick(FPS)
    fighter.score += 1
    

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
        print(fighter.score)

    # 描画処理
    screen.fill(WHITE)
    all_sprites.draw(screen)
    text = myfont.render("score {0}".format(fighter.score), 1, (0, 0, 0))
    screen.blit(text, (5, 10))
    pygame.display.update()

pygame.quit()
