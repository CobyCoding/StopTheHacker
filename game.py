import os
import random
import sys
import time
from tkinter import *
from tkinter import messagebox

import pygame

import final
import Map as ma
import reaction
import match

BACKGROUND = pygame.transform.scale(pygame.image.load("{}\\images\\quiz.png".format(os.getcwd())), (1200, 800))
TICK = pygame.transform.scale(pygame.image.load("{}\\images\\tick.png".format(os.getcwd())), (100, 100))
CROSS = pygame.transform.scale(pygame.image.load("{}\\images\\cross.png".format(os.getcwd())), (100, 100))

class Map:
    def __init__(self, game):
        self.game = game

        self.locations = ["London", "New York", "Moscow", "Berlin", "Paris", "Sydney", "San Fransisco", "Tokyo", "Madrid", "Beijing", "Rio De Janeiro", "Toronto", "Cairo", "Lima", "Delhi"]
        self.positions = {"London": ((559, 197), (579, 214)), "New York": ((331, 238), (352, 264)), "Moscow": ((685, 161), (712, 186)), "Berlin": ((601, 204), (619, 222)), 
        "Paris": ((569, 218), (602, 234)), "Sydney":((1031, 596), (1064, 635)), "San Fransisco": ((178, 257), (205, 292)), "Tokyo":((1014, 274), (1029, 304)), "Madrid":((551, 246), (572, 272)), "Beijing": ((932, 220), (962, 256)), "Rio De Janeiro":((426, 531), (450, 565)), "Toronto":((317, 204), (333, 237)), 
        "Cairo":((659, 298), (682, 327)), "Lima": ((294, 464), (334, 494)), "Delhi": ((820, 320), (849, 353))}

        self.hackerLocation = random.choice(self.locations)
        self.map = pygame.transform.scale(pygame.image.load("{}\\images\\map.png".format(os.getcwd())), (1200, 800))
        self.cross = pygame.transform.scale(pygame.image.load("{}\\images\\mapcross.png".format(os.getcwd())), (30, 30))
        self.IncorrectFont = pygame.font.SysFont(None, 68)

        self.incorrectLocations = []
    
    def draw(self, WIN):
        WIN.blit(self.map, (0, 0))
        for il in self.incorrectLocations:
            WIN.blit(self.cross, (self.positions[il][0][0], self.positions[il][0][1]))
        pygame.display.update()
    
    def alertLocation(self, location):
        Tk().wm_withdraw() #to hide the main window
        return messagebox.askyesno(title="Super awesome hacker tracing device", message = 'Do you want to start a trace in {}'.format(location))
    
    def incorrectLocation(self, WIN, location):
        img = self.IncorrectFont.render("Incorrect location", True, (255, 0, 0))
        WIN.blit(img, (300, 100))
        pygame.display.update()
        time.sleep(2)
        self.incorrectLocations.append(location)
    


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.questionsAwnsered = 0
        self.next_question = None
        self.get_next_question()

        self.QuestionFont = pygame.font.SysFont(None, 36)
        self.AwnserFont = pygame.font.SysFont(None, 34)
        self.AwnserBoxFont = pygame.font.SysFont(None, 48)
        self.CounterFont = pygame.font.SysFont(None, 68)
    
    def get_next_question(self):
        next_question = random.choice(self.questions)
        self.questions.remove(next_question)

        self.next_question = next_question

    def draw_next_question(self, WIN):
        img = self.QuestionFont.render(self.next_question[0], True, (0, 0, 0))
        WIN.blit(img, (121, 160))

        img = self.AwnserFont.render("a) " + self.next_question[1], True, (0, 0, 0))
        WIN.blit(img, (121, 200))

        img = self.AwnserFont.render("b) " + self.next_question[2], True, (0, 0, 0))
        WIN.blit(img, (121, 230))

        img = self.AwnserFont.render("c) " + self.next_question[3], True, (0, 0, 0))
        WIN.blit(img, (121, 260))

        img = self.AwnserFont.render("d) " + self.next_question[4], True, (0, 0, 0))
        WIN.blit(img, (121, 290))


        pygame.draw.rect(WIN, (0, 0, 0), (121, 400, 100, 100), width=0)
        pygame.draw.rect(WIN, (0, 0, 0), (271, 400, 100, 100), width=0)
        pygame.draw.rect(WIN, (0, 0, 0), (421, 400, 100, 100), width=0)
        pygame.draw.rect(WIN, (0, 0, 0), (571, 400, 100, 100), width=0)

        img = self.AwnserBoxFont.render("A", True, (255, 255, 255))
        WIN.blit(img, (156, 435))

        img = self.AwnserBoxFont.render("B", True, (255, 255, 255))
        WIN.blit(img, (306, 435))

        img = self.AwnserBoxFont.render("C", True, (255, 255, 255))
        WIN.blit(img, (456, 435))

        img = self.AwnserBoxFont.render("D", True, (255, 255, 255))
        WIN.blit(img, (606, 435))
    
    def draw_counter(self, WIN):
        img = self.CounterFont.render(str(self.questionsAwnsered) + "/3", True, (0, 0, 0))
        WIN.blit(img, (1000, 50))

class gameState():
    def __init__(self):
        self.firewalls = 7
        self.questions = self.load_quiz_questions()
        self.quiz = Quiz(self.questions)
        self.map = Map(self)
        self.LiveFont = pygame.font.SysFont(None, 64)
    
    def load_quiz_questions(self):
        with open("{}\\data\\quiz.txt".format(os.getcwd())) as f:
            questions = f.readlines()
            for x in range(0, len(questions)):
                questions[x] = questions[x].split(", ")
        
        return questions
    
    def draw_lives(self, WIN, x=218, y=50, draw_image=False, color=(0, 0, 0)):
        # Draw lives
        
        if not draw_image:
            img = self.LiveFont.render(str(self.firewalls), True, color )
            WIN.blit(img, (x, y))

def draw(WIN, game):
    WIN.blit(BACKGROUND, (0, 0))
    game.draw_lives(WIN)
    game.quiz.draw_next_question(WIN)
    game.quiz.draw_counter(WIN)

    pygame.display.update()

def get_awnser(pos):
    x, y = pos

    if y <= 510 and y >= 380:
        if x <= 226 and x >= 116:
            return "a"

        elif x >= 256 and x <= 356:
            return "b"

        elif x >= 406 and x <= 506:
            return "c"
        
        elif x >= 556 and x <= 656:
            return "d"
        
        else:
            return None

    else:
        return None

def quiz(WIN, game):
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                awnser = get_awnser(pygame.mouse.get_pos())

                if isinstance(awnser, str):
                    if game.quiz.next_question[-1].replace("\n", "").lower() == awnser.lower():
                        WIN.blit(TICK, (900, 400))
                        pygame.display.update()
                        time.sleep(2)
                        game.quiz.get_next_question()
                        game.quiz.questionsAwnsered += 1
                        ma.main(game, WIN, game.map)
                        if game.quiz.questionsAwnsered == 3:
                            return None

                    else:
                        draw(WIN, game)
                        WIN.blit(CROSS, (900, 400))
                        pygame.display.update()
                        if game.firewalls == 1:
                            final.loser(WIN)
                        game.firewalls -= 1
                        time.sleep(2)

        draw(WIN, game)
    
    pygame.quit()

def main(WIN):
    g = gameState()
    while True:
        games = ["quiz", "reaction", "match"]
        random.shuffle(games)
        for game in games:
            if game == "quiz":
                quiz(WIN, g)
            elif game == "reaction":
                reaction.main(g, WIN, g.map)
            elif game == "match":
                match.main(g, WIN)  