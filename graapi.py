import pygame
from pygame.locals import QUIT

pygame.init()

# ウィンドウのサイズを設定
WIDTH = 400
HEIGHT = 300

# ウィンドウを作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Example')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 背景色を白に設定
    screen.fill((255, 255, 255))

    # 青い矩形を描画
    pygame.draw.rect(screen, (0, 0, 255), (50, 50, 200, 100))

    # 画面を更新
    pygame.display.update()

pygame.quit()
