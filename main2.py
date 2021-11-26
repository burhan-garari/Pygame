# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:45:17 2021

@author: ACER Nitro 5
"""

import pygame 
import sys

pygame.init()

# Clock object 
clock = pygame.time.Clock()

# Display of main_screen
width, height = 800, 400
main_screen = pygame.display.set_mode((width, height))
main_screen.fill("White")
text_font = pygame.font.Font(None, 50)
# Adding the image surface 
sky          = pygame.image.load("graphics/Sky.png")
ground       = pygame.image.load("graphics/ground.png")
text_surface = text_font.render("Game", False, "Black")
# Game Loop 
while(True):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
    # Rendering the screen with the surfaces
    # Rendering the screen with sky background
    main_screen.blit(sky, (0,0))
    # Rendering the screen with ground 
    main_screen.blit(ground,(0,300))
    main_screen.blit(text_surface,(350, 50))
    # Updating the screen after the an event has occured 
    pygame.display.update()
    # Frame Rate 
    clock.tick(60)
    

