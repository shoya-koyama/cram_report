import pygame
import random
import sys

pygame.init()

# ウィンドウを作成する
screen = pygame.display.set_mode((400, 300))

# フォントを設定する
font = pygame.font.Font(None, 36)

# カーソル位置を初期化する
cursor_x = 0
cursor_y = 0

# ゲームウィンドウの大きさ
WIDTH = 640
HEIGHT = 480

# プレーヤーのサイズと速度
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5

# 画面の背景色と線の色
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# プレーヤー1の情報
player1 = {
    "x": 100,
    "y": HEIGHT // 2 - PLAYER_HEIGHT // 2,
    "width": PLAYER_WIDTH,
    "height": PLAYER_HEIGHT,
    "color": (255, 0, 0),
    "direction": 0
}

# プレーヤー2の情報
player2 = {
    "x": WIDTH - 100 - PLAYER_WIDTH,
    "y": HEIGHT // 2 - PLAYER_HEIGHT // 2,
    "width": PLAYER_WIDTH,
    "height": PLAYER_HEIGHT,
    "color": (0, 0, 255),
    "direction": 0
}

# ゲームで使用するすべてのスプライトを保持するグループ
all_sprites = pygame.sprite.Group()

# プレーヤー1を作成し、all_spritesグループに追加する
player1_sprite = pygame.sprite.Sprite()
player1_sprite.image = pygame.Surface((player1["width"], player1["height"]))
player1_sprite.image.fill(player1["color"])
player1_sprite.rect = pygame.Rect(player1["x"], player1["y"], player1["width"], player1["height"])
all_sprites.add(player1_sprite)

# プレーヤー2を作成し、all_spritesグループに追加する
player2_sprite = pygame.sprite.Sprite()
player2_sprite.image = pygame.Surface((player2["width"], player2["height"]))
player2_sprite.image.fill(player2["color"])
player2_sprite.rect = pygame.Rect(player2["x"], player2["y"], player2["width"], player2["height"])
all_sprites.add(player2_sprite)

# 初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ゲームループ
while True:
    # イベントを処理する
    for event in pygame.event.get():
        # ウィンドウを閉じるボタンが押された場合は終了する
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # キーが押された場合
        elif event.type == pygame.KEYDOWN:
            # 矢印キーが押された場合はカーソル位置を変更する
            if event.key == pygame.K_LEFT:
                cursor_x -= 1
            elif event.key == pygame.K_RIGHT:
                cursor_x += 1
            elif event.key == pygame.K_UP:
                cursor_y -= 1
            elif event.key == pygame.K_DOWN:
                cursor_y += 1


    # 両プレーヤーの方向を設定する
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1["direction"] = -1
    elif keys[pygame.K_RIGHT]:
        player1["direction"] = 1
    else:
        player1["direction"] = 0

    if keys[pygame.K_a]:
        player2["direction"] = -1
    elif keys[pygame.K_d]:
        player2["direction"] = 1
    else:
        player2["direction"] = 0

    # 両プレーヤーを移動する
    player1["x"] += PLAYER_SPEED * player1["direction"]
    player2["x"] += PLAYER_SPEED * player2["direction"]

    # プレーヤーが画面外に出ることを防ぐ
    player1["x"] = max(0, player1["x"])
    player1["x"] = min(WIDTH - player1["width"], player1["x"])
    player2["x"] = max(0, player2["x"])
    player2["x"] = min(WIDTH - player2["width"], player2["x"])

    # 画面を更新する
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))
    all_sprites.draw(screen)

    # 画面をフリップする 
    pygame.display.flip()

    # フレームレートを設定する
    clock.tick(60)

