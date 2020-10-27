import pygame
import os
import random
import final
import time

def detectIfInLocation(location, m, x, y):
    pos = m.positions[location]

    # print("Clicked X:", x, "| Clicked Y:", y)

    # print(location + ")", f"if x >= {pos[0][0]} and x <= {pos[1][0]} and y >= {pos[0][1]} and y <= {pos[1][1]}")
    if x >= pos[0][0] and x <= pos[1][0] and y >= pos[0][1] and y <= pos[1][1]:
        if m.alertLocation(location):
            return location
        else:
            return None

def main(game, WIN, m):
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                x, y = pygame.mouse.get_pos()
                # print(pygame.mouse.get_pos())

                for location in m.locations:
                    if detectIfInLocation(location, m, x, y):
                        if location == m.hackerLocation:
                            final.winner(WIN)
                        else:
                            m.incorrectLocation(WIN, location)
                            m.draw(WIN)
                            time.sleep(2)
                            run = False
                    else:
                        pass

        m.draw(WIN)