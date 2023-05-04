import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_q, K_w, K_e, K_c, \
    K_u, K_i, K_o, K_p


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
