 # Import Modules for the Game
import pygame
import random
import time
import asyncio
import sys
'''
        # Changes what the score says depending on the player(if alive then shows score, if got eaten then says final score)
        if player_alive:
            score_text = score_font.render("Score: " + str(score), 1, (0, 0, 0))

        else:
            score_text = score_font.render("Final Score: " + str(score), 1, (0, 0, 0))

'''


# Start the game
pygame.init()
game_width = 1920
game_height = 1080
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

background = pygame.image.load('background.png').convert_alpha

player_x = 200

player_y = 750

player_speed = 1

player_size = 160

#player_facing_left = False

player_hitbox = pygame.Rect(player_x, player_y, int(player_size*1.25), player_size)

player_alive =  True
isjump = False
JUMP_HEIGHT = 18



async def main(screen, running, background, player, player_x, player_y, player_speed, player_size, player_facing_left, player_hitbox, player_alive, isjump, jumping,  Y_GRAVITY, JUMP_HEIGHT, Y_VELOCITY):
# Everything under 'while running' will be repeated over and over again
    while running:
        keys = pygame.key.get_pressed()

        # Makes the game stop if the player clicks the X or presses esc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    jumping = True
            
        if keys[pygame.K_a]:
            player_x -= player_speed
            player_facing_left = True



        if keys[pygame.K_s]:
            pass
            #player_y += player_speed
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_d]:
                player_x += 1.5
                #player_facing_left = False
            if keys[pygame.K_a]:
                player_x -= 1.5
                #player_facing_left = True
        if keys[pygame.K_d]:
            player_x += player_speed
            player_facing_left = False

        screen.blit(background, (0, 0))
        if jumping:
            player_y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT

            
        # Spawn a new Enemy whenever enemy_timer hits 0

        '''
        player_small = pygame.transform.scale(player, (int(player_size*1.25), player_size))

            # Draw Player
        if player_facing_left:
            player = pygame.transform.flip(player, True, False)
        screen.blit(player, (player_x, player_y))
        '''
        # Draw Player
        player_small = pygame.transform.scale(player, (int(player_size*1.25), int(player_size*1.25)))
        if player_facing_left:
            player_small = pygame.transform.flip(player_small, True, False)
        screen.blit(player_small, (player_x, player_y))


        #screen.blit(score_text, (1600, 30))
        await asyncio.sleep(0)  # Very important, and keep it 0

        # Update Screen
        pygame.display.flip()
        clock.tick(1000)
        pygame.display.set_caption("FPS: " + str(clock.get_fps()))

                                                                                                                                            
asyncio.run(main(pygame.display.set_mode((game_width, game_height)), True, pygame.image.load('background.png').convert_alpha(), pygame.image.load('bird.png').convert_alpha(), 200, 750, 1, 160, False, pygame.Rect(player_x, player_y, int(player_size*1.25), player_size), True, False, False, 0.1, 7, 7))
#async def main(screen, running, background, player, player_x, player_y, player_speed, player_size, player_facing_left, player_hitbox, player_alive, isjump):
