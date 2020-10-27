import pygame
import game
import os
import sys

BACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\computer.png".format(os.getcwd())), (1200, 800))

def draw_how_to_play_screen(WIN):
    WIN.blit(BACKGROUND, (0, 0))
    # WIN.blit(TITLE, (50, 300))
    pygame.display.update()

def main(WIN):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                game.main(WIN)

        draw_how_to_play_screen(WIN)
    
    sys.exit()