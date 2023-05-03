import pygame
import random

# ゲーム画面のサイズ（ピクセル）
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ブロックのサイズ（ピクセル）
BLOCK_SIZE = 20

# ブロックの色
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 128, 0)

# ブロックの種類と色
BLOCKS = [
    ([(0, 1), (1, 1), (2, 1), (3, 1)], RED),
    ([(1, 0), (1, 1), (2, 1), (3, 1)], GREEN),
    ([(0, 1), (1, 1), (2, 1), (2, 0)], BLUE),
    ([(0, 0), (1, 0), (1, 1), (2, 1)], YELLOW),
    ([(0, 1), (0, 0), (1, 1), (1, 0)], CYAN),
    ([(0, 1), (1, 1), (1, 0), (2, 0)], MAGENTA),
    ([(0, 0), (1, 0), (2, 0), (2, 1)], ORANGE)
]

# テトロミノの初期位置（ピクセル）
INITIAL_X = SCREEN_WIDTH // 2
INITIAL_Y = 0

# ゲームオーバーのフラグ
game_over = False

# テトロミノを表すクラス
class Tetromino:
    def __init__(self, blocks):
        self.blocks = blocks
        self.color = random.choice(BLOCKS)[1]
        self.x = INITIAL_X
        self.y = INITIAL_Y
        self.rotation = 0

    # テトロミノを回転する
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    # テトロミノを下に落とす
    def drop(self):
        self.y += BLOCK_SIZE

    # テトロミノを左に移動する
    def move_left(self):
        self.x -= BLOCK_SIZE

    # テトロミノを右に移動する
    def move_right(self):
        self.x += BLOCK_SIZE

    # テトロミノを描画する
    def draw(self, surface):
        for position in self.blocks[self.rotation]:
            x = self.x + position[0] * BLOCK_SIZE
            y = self.y + position[1] * BLOCK_SIZE
            pygame.draw.rect(surface, self.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

# 画面を初期化する
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# テトロミノを作成する
tetromino = Tetromino(BLOCKS)

# ゲームループ
while not game_over:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetromino.move_left()
            elif event.key == pygame.K_RIGHT:
                tetromino.move_right()
            elif event.key == pygame.K_UP:
                tetromino.rotate()
            elif event.key == pygame.K_DOWN:
                tetromino.drop()

    # テトロミノを下に落とす
    tetromino.drop()

    # テトロミノを描画する
    screen.fill((255, 255, 255))
    tetromino.draw(screen)
    pygame.display.flip()
    
# 終了処理
pygame.quit()