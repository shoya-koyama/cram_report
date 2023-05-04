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
        
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(main.SURFACE, (255, 0, 0), rect)

    def move(self, jump_speed, player_move):
        

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