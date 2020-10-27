import pygame
import os
import sys

pygame.init()

LOSERBACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\loser.png".format(os.getcwd())), (1200, 800))
WINNERBACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\winner.png".format(os.getcwd())), (1200, 800))
LAUGH = pygame.mixer.Sound("sounds/laugh.wav")

def winner(WIN):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit("THANKS FOR PLAYING")
        winner_draw(WIN)

def winner_draw(WIN):
    WIN.blit(WINNERBACKGROUND, (0, 0))
    pygame.display.update()

def loser_draw(WIN):
    WIN.blit(LOSERBACKGROUND, (0, 0))
    pygame.display.update()

def loser(WIN):
    LAUGH.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit("THANKS FOR PLAYING")
        loser_draw(WIN)
