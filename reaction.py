import pygame
import os
import time
import datetime
import random
import Map as ma
import final

pygame.init()
BACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\reaction.png".format(os.getcwd())), (1200, 800))
FIREWALL = pygame.transform.scale(pygame.image.load("{}\\images\\firewall.png".format(os.getcwd())), (100, 100))
FONT = pygame.font.SysFont(None, 64)

def draw(WIN, Rtime, game):
    WIN.blit(BACKGROUND, (0, 0))
    game.draw_lives(WIN, 1060, 430)
    WIN.blit(FIREWALL, (950, 400))
    if Rtime:
        if Rtime <= 0.5:
            img = FONT.render("Previous time: " + str(Rtime), True, (0, 0, 0))
            WIN.blit(img, (450, 500))
        else:
            img = FONT.render("You failed your final time is " + str(Rtime), True, (0, 0, 0))
            WIN.blit(img, (250, 500))

    pygame.display.update()

def main(game, WIN, m):
    clicked = False
    finalClick = False
    timesPlayed = 0
    reaction_time = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                finalClick = True if clicked else False
                

                if not clicked:
                    clicked = True if not finalClick else False
                    time.sleep(random.randint(1, 5))

                    WIN.fill((0, 255, 0))
                    pygame.display.update()

                    then = time.time()
            
                if finalClick:
                    timesPlayed += 1

                    diff = then-time.time()
                    reaction_time = round(abs(diff), 2)
                    draw(WIN, reaction_time, game)
                    time.sleep(1)
                    if reaction_time <= 0.5:
                        ma.main(game, WIN, m)
                    else:
                        game.firewalls -= 1
                    
                    if game.firewalls == 0:
                        final.loser(WIN)
                
                if timesPlayed == 3:
                    return None

        if not clicked or finalClick:
            draw(WIN, reaction_time, game)
            clicked = False
            clicked = False