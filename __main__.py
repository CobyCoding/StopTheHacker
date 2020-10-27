import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import how_to_play
import os
import sys

# Initialize
pygame.init()

# Global Variables Defined In constants.py

WIN = pygame.display.set_mode((1200, 800)) # The pygame window
pygame.display.set_caption("Stop The Hacker") # Set the pygame window caption

BACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\backround.jpg".format(os.getcwd())), (1200, 800))
TITLE = pygame.transform.scale(pygame.image.load("{}\\images\\title.png".format(os.getcwd())), (400, 150))


def draw_main_screen():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(TITLE, (50, 300))
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                x, y = pygame.mouse.get_pos()
                
                if x <= 450 and x >= 50:
                    if y <= 450 and y >= 300:
                        how_to_play.main(WIN)

        draw_main_screen()
    
    pygame.quit()

if __name__ == "__main__":
    main()