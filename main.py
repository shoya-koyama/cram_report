import math
import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_q, K_w, K_e, K_c, K_u, K_i, K_o, K_p

def pythagoras_theorem(a1, a2, b1, b2):
    z_2 = (a2 - a1) ** 2 + (b2 - b1) ** 2
    z = math.sqrt(z_2)
    return z

def control_character(player_move, action, contact):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_w]:
                player_move[0] = True if contact[0] else player_move[0]

            if pygame.key.get_pressed()[K_c]:
                player_move[1] = True

            if pygame.key.get_pressed()[K_q]:
                player_move[3] = True

            if pygame.key.get_pressed()[K_e]:
                player_move[2] = True

            if pygame.key.get_pressed()[K_u]:
                action[0] = True

            if pygame.key.get_pressed()[K_i]:
                action[1] = True

            if pygame.key.get_pressed()[K_o]:
                action[2] = True

            if pygame.key.get_pressed()[K_p]:
                action[3] = True

        elif event.type == KEYUP:
            if event.key == K_c:
                player_move[1] = False

            if event.key == K_q:
                player_move[3] = False

            if event.key == K_e:
                player_move[2] = False

            if event.key == K_u:
                action[0] = False

            if event.key == K_i:
                action[1] = False

            if event.key == K_o:
                action[2] = False

            if event.key == K_p:
                action[3] = False

    return player_move, action

class Fighter:
    def __init__(self, position, size, gravity, move_speed, contact, rigit_time, direction):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.width = size[0]
        self.height = size[1]
        self.gravity = gravity
        self.move_speed = move_speed
        self.contact = contact
        self.rigit_time = rigit_time
        self.direction = direction

    def figure(self):
        if self.direction == "left":
            image = pygame.image.load("pac.png")
        else:
            image = pygame.image.load("sun.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        image_rect = image.get_rect()
        image_rect.x = self.pos_x
        image_rect.y = self.pos_y
        main.SURFACE.blit(image, image_rect)

    def move(self, jump_speed, player_move):
        if player_move[0]:
            self.pos_y -= jump_speed
            player_move[0] = False if not jump_speed else player_move[0]
            jump_speed = 20 if not jump_speed else jump_speed - 2
        elif not self.contact[0]:
            self.pos_y += self.gravity
        if player_move[2] and not self.contact[2]:
            self.pos_x += self.move_speed
        elif player_move[3] and not self.contact[3]:
            self.pos_x -= self.move_speed
        return [self.pos_x, self.pos_y], jump_speed, player_move

    def contact_judgment(self, enemy_pos, enemy_size):
        if self.pos_x == 1000 - self.width or (enemy_pos[0] <= self.pos_x + self.width <= enemy_pos[0] + enemy_size[0] and self.pos_y == enemy_pos[1]):
            self.contact[0] = True if 550 <= self.pos_y + self.height else False
            self.contact[2] = True
        elif self.pos_x == 0 or (enemy_pos[0] <= self.pos_x <= enemy_pos[0] + enemy_size[0] and self.pos_y == enemy_pos[1]):
            self.contact[0] = True if 550 <= self.pos_y + self.height else False
            self.contact[3] = True
        elif 0 < self.pos_x < 1000 - self.width:
            self.contact[0] = True if 550 <= self.pos_y + self.height else False
            self.contact[2] = False
            self.contact[3] = False
        return self.contact

    def position_corr(self, stage_pos):
        if self.contact[0] and (self.pos_y + self.height - stage_pos[1]) != 0:
            self.pos_y = stage_pos[1] - self.height
        return [self.pos_x, self.pos_y]

    def character_action(self, player_move, action, hit_judg, enemy_pos, enemy_size, enemy_damage):
        enemy_rigit = blow_speed = 0
        if self.rigit_time != 0:
            self.rigit_time -= 1
            return action, self.rigit_time, hit_judg, enemy_damage, enemy_rigit, blow_speed
        if action[0]:
            circle_pos = (self.pos_x, self.pos_y + self.height // 2)
            radius = 30
            pygame.draw.circle(main.SURFACE, (0, 0, 250), circle_pos, radius)
            distance = pyth(circle_pos[0], enemy_pos[0] + enemy_size[0] / 2, circle_pos[1], enemy_pos[1] + enemy_size[1] / 2)
            if 0 <= distance <= radius + enemy_size[1] / 2:
                hit_judg = [False, False, False, True]
                enemy_damage += 13
                enemy_rigit = 10
                self.rigit_time = 15
                blow_speed = 20
        action[0] = False
        return action, self.rigit_time, hit_judg, enemy_damage, enemy_rigit, blow_speed

    def hit_action(self, hit_judg, rigit_time, blow_speed):
        if rigit_time == 0:
            hit_judg = [False, False, False, False]
            return [self.pos_x, self.pos_y], rigit_time, hit_judg
        if hit_judg[3] is True and self.contact[3] is False:
            self.pos_x -= blow_speed
        rigit_time -= 1
        return [self.pos_x, self.pos_y], rigit_time, hit_judg

    def life(self, damage, view):
        if view == "left":
            pygame.draw.rect(main.SURFACE, (120, 120, 120), (30, 20, 400, 30))
            if damage >= 390:
                return
            pygame.draw.rect(main.SURFACE, (250, 200, 0), (35 + damage, 25, 390 - damage, 20))
        elif view == "right":
            pygame.draw.rect(main.SURFACE, (120, 120, 120), (570, 20, 400, 30))
            if damage >= 390:
                return
            pygame.draw.rect(main.SURFACE, (250, 200, 0), (575, 25, 390 - damage, 20))

def base_stage(position):
    pygame.draw.rect(main.SURFACE, (0, 250, 0), (position[0], position[1], 1500, 50))


pygame.init()
SURFACE = pygame.display.set_mode((1000, 700))
FPSCLOCK = pygame.time.Clock()
STAGE_POS = [0, 550]  # <= 表示するステージの位置


def main():
    player1_pos = [600, 470]  # <= 操作キャラの位置
    player1_size = [50, 80]  # <= 操作キャラの大きさ [横幅, 縦幅]
    move1 = [False, False, False, False]  # <= [上方向に移動、下方向に移動、右方向に移動、左方向に移動]
    jump_speed1 = 20  # <= ジャンプの初速度
    contact1 = [False, False, False, False]  # <= [キャラクターと地面との接触判定、頭上のオブジェクトとの接触判定、右側とオブジェクトとの接触判定、左側とオブジェクトの接触判定
    action1 = [False, False, False, False]  # <= [弱攻撃、必殺技、ガード、掴み]
    hit_judg1 = [False, False, False, False]  # <= [上方向にhit、下方向にhit、右方向にhit、左方向にhit]
    damage1 = 0  # <= 操作キャラが受けたトータルダメージ量
    rigit_time1 = 0  # <= 操作キャラの硬直時間
    direction1 = "left"
    blow_speed1 = 0  # <= 操作キャラが吹っ飛ばされたときの速度
    player2_pos = [200, 470]
    player2_size = [50, 80]
    move2 = [False, False, False, False]
    jump_speed2 = 20
    contact2 = [False, False, False, False]
    hit_judg2 = [False, False, False, False]
    damage2 = 0
    rigit_time2 = 0
    blow_speed2 = 0
    direction2 = "right"

    while True:
        # 背景を真っ白に設定する
        SURFACE.fill((250, 250, 250))

        # プレイヤー１のキャラクター操作
        move1, action1 = control.control_character(move1, action1, contact1)

        # 戦闘ステージを作成
        stage.base_stage(STAGE_POS)

        # プレイヤー１の操作キャラの表示、行動制御
        player_1 = fighter.Fighter(player1_pos, player1_size, 16, 10, contact1, rigit_time1,direction1)
        player_1.figure()
        player1_pos, jump_speed1, move1 = player_1.move(jump_speed1, move1)
        contact1 = player_1.contact_judgment(player2_pos, player2_size)
        player1_pos = player_1.position_corr(STAGE_POS)
        action1, rigit_time1, hit_judg2, damage2, rigit_time2, blow_speed2 = player_1.character_action(move1, action1, hit_judg2, player2_pos, player2_size, damage2)
        player_1.life(damage1, "left")

        # プレイヤー2のキャラ表示
        player_2 = fighter.Fighter(player2_pos, player2_size, 16, 10, contact2, rigit_time2,direction2)
        player_2.figure()
        player2_pos, jump_speed2, move2 = player_2.move(jump_speed2, move2)
        contact2 = player_2.contact_judgment(player1_pos, player1_size)
        player2_pos = player_2.position_corr(STAGE_POS)
        player2_pos, rigit_time2, hit_judg2 = player_2.hit_action(hit_judg2, rigit_time2, blow_speed2)
        player_2.life(damage2, "right")

        

        # 画面を更新する
        pygame.display.update()

        # 画面の更新を30fps(1秒間に30枚画面が切り替わる)に設定する
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()