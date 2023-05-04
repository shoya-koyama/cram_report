import pygame

import main
from game_parts.caluclation_parts import pythagoras_theorem as pyth


class Fighter:
    def __init__(self, position, size, gravity, move_speed, contact, rigit_time):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.width = size[0]
        self.height = size[1]
        self.gravity = gravity
        self.move_speed = move_speed
        self.contact = contact
        self.rigit_time = rigit_time

    def figure(self):
        """
        キャラクターの大きさを決め、表示する

        """
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(main.SURFACE, (255, 0, 0), rect)

    def move(self, jump_speed, player_move):
        """
        キャラクターの移動を制限する
        Parameters
        ----------
        jump_speed : (int) ジャンプして一定時間後の速度を表す
        player_move : プレイヤー操作(上方向、下方向、右方向、左方向)を表す

        Returns
        -------
        変化後のキャラクターの位置情報、一定時間後のジャンプ速度、プレイヤー操作(上方向、下方向、右方向、左方向)を表す

        """

        # ジャンプボタンを押した時キャラクターをジャンプさせる。ジャンプし終えた後は重力によって落下する
        if player_move[0]:
            self.pos_y -= jump_speed
            player_move[0] = False if not jump_speed else player_move[0]
            jump_speed = 20 if not jump_speed else jump_speed - 2

        elif not self.contact[0]:
            self.pos_y += self.gravity

        # 操作キャラを左右に動かす
        if player_move[2] and not self.contact[2]:
            self.pos_x += self.move_speed

        elif player_move[3] and not self.contact[3]:
            self.pos_x -= self.move_speed

        return [self.pos_x, self.pos_y], jump_speed, player_move

    def contact_judgment(self, enemy_pos, enemy_size):
        """
        操作キャラとステージ(または敵キャラ)との接触判定、各接触方向に対して接触した場合のみCONTACTの各接触方向の要素にTrueを返す
        enemy_pos : 敵キャラの位置
        enemy_size : 敵キャラのサイズ

        Returns
        -------
        (list) 変更したcontactを返す

        """

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
        """
        操作キャラとステージとの位置補正
        Parameters
        ----------
        stage_pos : 対象ステージの位置

        Returns
        -------
        補正後の操作キャラの位置(y軸方向)

        """

        if self.contact[0] and (self.pos_y + self.height - stage_pos[1]) != 0:
            self.pos_y = stage_pos[1] - self.height

        return [self.pos_x, self.pos_y]

    def character_action(self, player_move, action, hit_judg, enemy_pos, enemy_size, enemy_damage):
        """
        敵プレイヤーを攻撃した際の判定
        Parameters
        ----------
        player_move : (list) 操作キャラの移動判定
        action : (list) 操作キャラの動作判定
        hit_judg : (list) 自分の攻撃と攻撃対象との当たり判定
        enemy_pos: (list) 攻撃対象キャラの位置
        enemy_size : (list) 攻撃対象キャラの幅と高さ
        enemy_damage : (int) 敵に与えるダメージ

        Returns
        -------

        """
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
        """
        相手の攻撃を受けた際に操作キャラの吹っ飛ぶ方向と距離を制御
        Parameters
        ----------
        hit_judg : (list) 上下左右のどちらの方向に飛ぶかの判定
        rigit_time : (int) 操作キャラの硬直時間
        blow_speed : (int) 攻撃が当たったときに吹っ飛ぶスピード

        Returns
        -------

        """
        if rigit_time == 0:
            hit_judg = [False, False, False, False]
            return [self.pos_x, self.pos_y], rigit_time, hit_judg

        if hit_judg[3] is True and self.contact[3] is False:
            self.pos_x -= blow_speed

        rigit_time -= 1

        return [self.pos_x, self.pos_y], rigit_time, hit_judg

    def life(self, damage, view):
        """
        キャラクターの体力ゲージ
        Parameters
        ----------
        damage : ダメージの蓄積量
        view : 体力ゲージの表示場所(left or right)

        """
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