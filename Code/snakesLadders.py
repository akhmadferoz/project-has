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
# --------------- Stack Commands ---------------------------------------------
import random


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

# --------------- Python Libraries -------------------------------------------


# --------------- Function Prototypes ----------------------------------------
'''
void initializeBoard(int,int,char *);       //Sets board values based on size chosen by player
void initializeSnakesLadders(int,char *);   //Allocates snakes & ladders on board
char locateLadder(char *);                  //To be used by intSnakesLadders function
char locateCurlySnake();                    //To be used by intSnakesLadders function
char locateStraightSnake();                 //To be used by intSnakesLadders function
int move();                                 //moves player according to die values player:# computer:@
int stepSize();                             //calculates total of die values (5+6=14)
int checkSnakes(int);                       //Checks for snake head on the player's location
int checkLadders(int);                      //Checks for ladder bottom rung on the player's location
void displayBoard(int,int,char [*][*]);     //Displays the playing board on the screen canvas
void displayResults(int,int,int);           //Displays final results at the end of the game

int diceRoll();
int playComputer();
int playHuman();
'''
# --------------- Main Program Start ---------------------------------------------------------------------------------------------------------------------------------


def main():
    pass
# --------------- Main Program END -----------------------------------------------------------------------------------------------------------------------------------

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
    pass
# ----------------------------------------------------------------
# --------------- Snakes & Ladders Initializing --------------------
# ----------------------------------------------------------------
# --------------- Board Size: 10x10 ------------------------------------
# --------------- Ladders: x2 - 3 steps & x1 - 5 steps -----------------
# --------------- Snakes: x2 Curly - 7 steps ---------------------------

# --------------- Display Board ------------------------------------


def displayBoard(x, y, gB):  # gB type == list?
    pass
# --------------- Display Results ----------------------------------


def displayResults(player, machine, rounds):
    pass
