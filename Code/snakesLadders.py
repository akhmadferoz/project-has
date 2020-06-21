'''
This is the source code for the game of Snakes & Ladders.

Course: CS 102 - Data Structures & Algorithms (L2)
Instructor: Dr. Syeda Saleha Raza

Team Members:

Ahmad Feroz (06109)
Habib Shehzad (05888)
Synclair Samson (05901)

For information on the rules of the game and how the game is structured please refer to the Readme.md file.
'''

# --------------- Include Libraries ------------------------------------------

import pygame
import random
from pygame import mixer
import math
import time
# --------------- Stack Commands ---------------------------------------------

def push(lst, x):
    lst.append(x)
def pop(lst):
    return lst.pop()
def top(lst):
    return lst[-1]
def is_empty(lst):
    if len(lst) == 0:
        return True
    return False
# --------------- Queue Commands ---------------------------------------------
def Enqueue(lst, x, p):
    tup = (x, p)
    if len(lst) == 0:
        return lst.append(tup)
    else:
        for i in range(len(lst)):
            if lst[i][1] < p:
                lst.insert(i, tup)
                return lst
            elif lst[i][1] == p:
                if lst[i][0] > x:
                    lst.insert(i, tup)
                    return lst
                else:
                    lst.insert(i+1, tup)
                    return lst
    lst.append(tup)

def front(lst):
    return lst[0]

def Dequeue(lst):
    p = lst.pop(0)
    return p[0]

# --------------- Function Definitions --------------------------------------------------------------------------------------------------------------------------
# --------------- Dice Roll ----------------------------------------


def diceRoll():
    return random.randint(1, 6)
# --------------- Play Human ---------------------------------------


def playHuman(player, icon):
    dice1 = diceRoll
    dice2 = diceRoll

    result = move(player, dice1, dice2, icon)

    return result
# --------------- Play Computer ------------------------------------


def playComputer(machine, icon):
    dice1 = diceRoll
    dice2 = diceRoll

    result = move(machine, dice1, dice2, icon)

    return result
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------- Step Size ---------------------------------------


def stepSize(dice1, dice2):
    sum = dice1 + dice2
    return sum
# --------------- Move --------------------------------------------


def move(player, dice1, dice2, icon):
    boxes = 0
    player = stepSize(dice1, dice2)
    boxes = checkLadders(icon)

    if boxes == True:
        player += boxes
    boxes = 0
    boxes = checkSnakes(icon)
    if boxes == True:
        player -= boxes

    return player
# ----------------------------------------------------------------
# ----------------------------------------------------------------

# ---------------Check Snakes ------------------------------------


def checkSnakes(icon):
    pass
# ---------------Check Ladders -----------------------------------


def checkLadders(icon):
    pass
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------- Board Initializing -------------------------------


def initializeBoard():
    #--------------Initializing Pygame and the screen---------------# 
    pygame.init()
    screen=pygame.display.set_mode((1000,667))
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    background = pygame.image.load("screen-01.png")

    #----------Loading the images of the players-----------#
    player1 = pygame.image.load('batman.png')
    player2 = pygame.image.load('superman.png')

    def batMusic():
        mixer.init()
        mixer.music.load("BatMus.wav")
        mixer.music.play()
        mixer.music.set_volume(0.7)
        
    def supMusic():
        mixer.init()
        mixer.music.load("SupMus.wav")
        mixer.music.play()
        mixer.music.set_volume(0.7)

    #----------Loading all the possible dice roll images------------#
    one = pygame.image.load('dice1.png')
    two = pygame.image.load('dice2.png')
    three = pygame.image.load('dice3.png')
    four = pygame.image.load('dice4.png')
    five = pygame.image.load('dice5.png')
    six = pygame.image.load('dice6.png')

    snakeImg = pygame.image.load('portal15.png')
    ladderImg = pygame.image.load('portal15.png')


# ----------------------------------------------------------------
# --------------- Snakes & Ladders Initializing --------------------
  #----------Storing The loaction of snakes in a dictionary---------
  # ---------In this game, both sankes AND Ladders are represented by portals which are bi-directional
    snakes = {
    99: 78,
    95: 75,
    93: 73,
    87: 24,
    17: 7,
    62: 19,
    54: 34,
    64: 60
    }

    ladders = {
    63: 81,
    40: 59,
    20: 38,
    4: 14,
    9: 31,
    28: 84,
    71: 91,
    51: 67
    }
# ----------------------------------------------------------------

# --------------- Board Size: 10x10 ------------------------------------
numbers = [i for i in range(1,101)]
# --------------- Board Size: 15x15 ------------------------------------
numbers = [i for i in range(1, 226)]
# --------------- Ladders: x2 - 3 steps & x1 - 5 steps -----------------
# --------------- Snakes: x2 Curly - 7 steps ---------------------------

# --------------- Display Board ------------------------------------
def displayBoard(x, y, gB):  # gB type == list?
    pass
# --------------- Display Results ----------------------------------


def displayResults(player, machine, rounds):
    pass

snakeMsg = "Oh no! You've been sucked into a black hole :("
ladderMsg = "Nice work! You've entered a worm hole :D"
# --------------- Main Program Start ---------------------------------------------------------------------------------------------------------------------------------


def main():
    pass
# --------------- Main Program END -----------------------------------------------------------------------------------------------------------------------------------
main()