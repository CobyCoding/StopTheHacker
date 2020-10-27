import pygame
import random
import os
import time
import Map as ma
import final

pygame.init()

BACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\match.png".format(os.getcwd())), (1200, 800))
FIREWALL = pygame.transform.scale(pygame.image.load("{}\\images\\firewall.png".format(os.getcwd())), (100, 100))

BLANK = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\blank.png".format(os.getcwd())), (103, 143))
COMPUTER = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\computer.png".format(os.getcwd())), (103, 143))
HEADPHONES = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\headphones.png".format(os.getcwd())), (103, 143))
KEYBOARD = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\keyboard.png".format(os.getcwd())), (103, 143))
MONITER = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\moniter.png".format(os.getcwd())), (103, 143))
MOUSE = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\mouse.png".format(os.getcwd())), (103, 143))
WINDOWS = pygame.transform.scale(pygame.image.load("{}\\images\\cardFronts\\windows.png".format(os.getcwd())), (103, 143))

FONT = pygame.font.SysFont(None, 64)

class Card:
    def __init__(self, startx, starty, endx, endy, front):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.front = front
        self.flipped = False
        self.hidden = False
        
    
    def draw_back(self, WIN):

        WIN.blit(BLANK, (self.startx, self.starty))
    
    def draw_front(self, WIN):
        WIN.blit(self.front, (self.startx, self.starty))
    
    def flip(self):
        self.flipped = not self.flipped

def draw(WIN, game, cards):
    WIN.fill([255,255,255])
    WIN.blit(BACKGROUND, (0, 0))
    game.draw_lives(WIN, 1060, 430, color=(255, 255, 255))
    WIN.blit(FIREWALL, (950, 400))

    for card in cards:
        if not card.flipped and not card.hidden:
            card.draw_back(WIN)
        elif card.flipped and not card.hidden:
            card.draw_front(WIN)

    pygame.display.update()

def detectCardFlipped(pos, cards):
    x, y = pos
    for card in cards:
        if x >= card.startx and x <= card.endx and y >= card.starty and y <= card.endy:
            return card

def isPair(selection):
    if selection[0].front == selection[1].front:
        return True
    else:
        return False

def alertPair(selection):
    time.sleep(1)
    for s in selection:
        s.hidden = True

def alertFail(selection, game, WIN):
    time.sleep(1)
    for s in selection:
        s.flip()

    game.firewalls -= 1

    if game.firewalls == 0:
        final.loser(WIN)

def flipAllCards(cards):
    for card in cards:
        card.flipped = False

def main(game, WIN):
    cards = []
    fronts = [COMPUTER, HEADPHONES, KEYBOARD, MONITER, MOUSE, WINDOWS, COMPUTER, HEADPHONES, KEYBOARD, MONITER, MOUSE, WINDOWS]

    selected = None

    y = 0
    for x in range(0, 12):
        front = random.choice(fronts)
        fronts.remove(front)

        if x < 6:
            cards.append(Card((130 * x) + 50, 300, (130 * x) + 50 + 103, 400 + 143, front))
        else:
            cards.append(Card((130 * y) + 50, 500, (130 * y) + 50 + 103, 500 + 143, front))
            y += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                pos = pygame.mouse.get_pos()
                card = detectCardFlipped(pos, cards)
                
                if selected == None:
                    selected = card
                    if selected != None:
                        selected.flip()
                    else:
                        pass
                else:
                    selection = (selected, card)
                    if selection[0] == selection[1] or selection[0] == None or selection[1] == None:
                        selected = None
                        selection = None
                    else:
                        selected = None
                        selection[1].flip()
                        draw(WIN, game, cards)
                    `   `    pair = isPair(selection)

                        if pair:
                            alertPair(selection)
                            flipAllCards(cards)
                            selection = None
                            selected = None
                            ma.main(game, WIN, game.map)
                        else:
                            alertFail(selection, game, WIN)
                            flipAllCards(cards)
                            selection = None
                            selected = None
        
        if len(cards) == 0:
            return None

        draw(WIN, game, cards)