# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 03:03:52 2021

@author: ACER Nitro 5
"""

import pygame 
import sys

pygame.init()

width, height = 800, 600

# TO change the name of the title of the window 

pygame.display.set_caption("Scared Guy")

clock  = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
screen.fill("White")

# creation of a surface on the display surface 
surface_1 = pygame.Surface((100, 200))
surface_1.fill("Red")
# Creating a Game Loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Cration of images/ objects 
    screen.blit(surface_1, (0,0))
    screen.blit(surface_1, (700,400))
    screen.blit(surface_1, (200, 100))
    # Updations of events on the images 
    pygame.display.update()
    # Clock runs at 60 Fps
    clock.tick(60)
    
    