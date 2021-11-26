# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:28:32 2021

@author: ACER Nitro 5
"""
import pygame 
import sys
import random

pygame.init()


def display_score():
    current_time = (pygame.time.get_ticks())//(1000) - start_time
    score_surface = text_type.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 100))
    screen.blit(score_surface, score_rect)
    return current_time


# Score Variables
start_time    = 0
score         = -1
# Main screen creation 
width, height = 800, 400
screen        = pygame.display.set_mode((width,height))
screen.fill("White")
# Creation of clock 
clock = pygame.time.Clock()
# Creation of text 
text_type    = pygame.font.Font('font/Pixeltype.ttf', 50)
# Creation of surfaces 
sky               = pygame.image.load("graphics/Sky.png")
ground            = pygame.image.load("graphics/ground.png")
# State Management 
game_active       = False
# text 
text_surface      = text_type.render("Run Run", False, (64, 64, 64))

text_rect         = text_surface.get_rect(topleft = (350,50))
# game title 
game_title        = text_type.render("Run Run", False, (64, 64, 64))
game_title_rect   = game_title.get_rect(topleft = (350,50))

def game_message_at_end():
    game_message_end      = text_type.render("Press SPACE to Play Again", False, (64, 64, 64))
    game_message_rect_end = game_message_end.get_rect(center = (390,380))
    screen.blit(game_message_end , game_message_rect_end)
    
def game_message_at_intro():
    game_message_intro     = text_type.render("Press SPACE to Play ", False, (64, 64, 64))
    game_message_rect_intro = game_message_intro.get_rect(center = (400,380))
    screen.blit(game_message_intro, game_message_rect_intro)
    
# Snail Enemy 
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png")
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png")
snail_index, snail_frames   = 0, [snail_frame_1, snail_frame_2]
snail_surface = snail_frames[snail_index]
# Fly Enemy 
fly_surface = pygame.image.load("graphics/Fly/Fly1.png")
fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png")
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png")
fly_index, fly_frames = 0, [fly_frame_1, fly_frame_2]
fly_surface = fly_frames[fly_index]

# Obstacles - snails , flies 
obstacle_rec_list = []
def obstacle_movement(obstacle_rec_list):
    total = len(obstacle_rec_list)
    if(total>0):
        for obstacle_rect in obstacle_rec_list:
            if(obstacle_rect[0]):
                   obstacle_rect[1].x-=5
            else:
                obstacle_rect[1].x-=3
            
            obstacle_rec_list = [obstacle_rec for obstacle_rec in obstacle_rec_list if obstacle_rec[1].x>0]
            if(obstacle_rect[0]):
                    screen.blit(snail_surface, obstacle_rect[1])
            else:
                screen.blit(fly_surface, obstacle_rect[1])   
    return obstacle_rec_list

def is_collide(player, obstacle_rec_list):
    for obstacle in obstacle_rec_list:
        if(player.colliderect(obstacle[1])):
            return False
    return True
# Player 
player_surface             = pygame.image.load("graphics/Player/player_walk_1.png")
player_pos_x, player_pos_y = 30, 215
player_rect                = player_surface.get_rect(topleft = (player_pos_x,player_pos_y))
player_gravity = 0

# First Screen

player_stand_end        = pygame.image.load("graphics/Player/player_stand.png")
player_stand_intro      = pygame.image.load("graphics/Player/player_stand.png")
# Enlarging the photo 
player_stand_end        = pygame.transform.rotozoom(player_stand_end, 180, 2)
player_stand_rect_end   = player_stand_end.get_rect(center = (400,200))
player_stand_intro      = pygame.transform.rotozoom(player_stand_intro,0, 2)
player_stand_rect_intro = player_stand_intro.get_rect(center = (400, 200))

# Animation of player 
player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png")
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png")
player_walk   = [player_walk_1, player_walk_2]
player_jump   = pygame.image.load("graphics/Player/jump.png")
player_index  = 0
player_surface= player_walk[player_index]

def player_animation():
    # Player walking on the floor 
    # Player Jumping 
    global player_surface, player_index 
    if(player_rect.bottom<300):
        player_surface = player_jump
    else:
        player_index  += 0.1
        # print(player_index)
        player_surface = player_walk[int(player_index)]
        if(int(player_index)==1): player_index=0
        
# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
choose = 0

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 250)

# importing sound 
player_jump_sound = pygame.mixer.Sound("audio/jump.mp3")
background_music  = pygame.mixer.Sound("audio/background_music.wav")
# background_music.play(loops = 3)
# Game Loop 
while(True):
    # Event check 
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif(game_active):
            if(event.type==obstacle_timer):
                #print('test')
                placement = random.randint(900, 3500)
                choose = random.randint(0,2)
                if(choose):
                    obstacle_rec_list.append([choose,snail_surface.get_rect(center=(placement,280))])
                else:
                    obstacle_rec_list.append([choose,fly_surface.get_rect(center=(placement,200))])

            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_SPACE and player_rect.bottom==300):
                    player_gravity = -35
                    player_rect.left+=5
                    # player_jump_sound.play()
                if(event.key==pygame.K_RIGHT and player_rect.bottom==300):
                    player_rect.left+=2
                    
            if(event.type == pygame.KEYUP):
                print('key up')
            if(event.type==snail_animation_timer):
                snail_index   = 1 - snail_index 
                snail_surface = snail_frames[snail_index]
            if(event.type==fly_animation_timer):
                fly_index   = 1 - fly_index 
                fly_surface = fly_frames[fly_index]   
        else:
            if(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
                game_active     = True
                start_time      = pygame.time.get_ticks()//1000
                score           = 0
    if game_active:
        #Surface postioning on the main surface 
        screen.blit(sky   ,(0,  0))
        screen.blit(ground,(0,300))
        screen.blit(text_surface,(350,50))
        pygame.draw.rect(screen, 'Pink', text_rect, 5)
        #pygame.draw.line(screen, "Black", (0,0), (800, 400))
        screen.blit(text_surface, text_rect)
        #screen.blit(snail_surface,snail_rect)
        score = display_score()
        # Snail
        #if(snail_rect.right<0):
            #snail_rect.right = 750
        #snail_rect.right-=1
        # Player 
        player_gravity+=2
        player_rect.y+=player_gravity
        if(player_rect.bottom > 300):
            player_rect.bottom=300
        player_animation()
        screen.blit(player_surface, player_rect)
        # Obstacle_movement 
        obstacle_movement(obstacle_rec_list)
        # Collisions
        game_active = is_collide(player_rect, obstacle_rec_list)
    else:
        #pass
        # when the player has touched the enemy
        screen.fill((94, 129, 162))
        screen.blit(game_title   ,   game_title_rect)
        # background_music.play(loops = 3)
        if(score>=0):
            obstacle_rec_list = []
            player_rect.x = 30
            screen.blit(player_stand_end , player_stand_rect_end)
            game_message_at_end()
            score_text = text_type.render(f'Score  = {score}', False, (64, 64, 64))
            score_rect = score_text.get_rect(center=(400,320))
            screen.blit(score_text, score_rect)
        else:
             screen.blit(player_stand_intro ,player_stand_rect_intro)
             game_message_at_intro()
             #background_music.play()
             
            
    # Update the screen
    pygame.display.update()
    # Frame per Second - tick() method 
    clock.tick(60)