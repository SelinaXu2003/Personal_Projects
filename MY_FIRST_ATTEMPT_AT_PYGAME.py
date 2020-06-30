# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:02:18 2020

@author: selin
"""


import pygame
#initialise pygame
pygame.init()

#create screen
wn = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Meteor")



#Game loop
vel = 5
x = 500
y = 500
width = 40
height = 40

running = True

while running:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            running = False
            
    ## MOVING A CHARACTER ##
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
        
    if keys[pygame.K_RIGHT]:
        x += vel
    ## CREATING A CHARACTER ##
    wn.fill((0,0,0))

    pygame.draw.rect(wn, (255, 0, 0), (x, y, width, height))
    
    pygame.display.update()

pygame.quit() 
     