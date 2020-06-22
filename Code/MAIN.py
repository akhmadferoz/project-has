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


#----------Importing the important things to be used-------------#
import pygame
import random
from pygame import mixer
import time
import pygame.math as math
from pygame.time import Clock
import random as r

def theme():
    mixer.init()
    mixer.music.load("Thoughts on the Road (new ed).wav")
    mixer.music.play()
    mixer.music.set_volume(0.7)


# theme()
def win_screen(player):
    pygame.init()
    screen = pygame.display.set_mode((1200, 667))
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    win = True
    background= pygame.image.load("space-background.png")
    Ship1 = pygame.image.load('ship1-BIG.png')
    Ship2 = pygame.image.load('ship2-BIG.png')
    Ship3 = pygame.image.load('ship3-BIG.png')
    Ship4 = pygame.image.load('ship4-BIG.png')
    Ship5 = pygame.image.load('ship5-BIG.png')
    Ship6 = pygame.image.load('ship6-BIG.png')


    def display_text():
        x = 600
        y = 30
        win="Congratulations " + player + " You Won. Press SPACE to Play again. Press Enter to Quit the Game."
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(win, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (600, 30)
        screen.blit(text, textRect)


    def p1(): screen.blit(Ship1,(600,330))
    def p2(): screen.blit(Ship2,(600,330))
    def p3(): screen.blit(Ship3,(600,330))
    def p4(): screen.blit(Ship4,(600,330))
    def p5(): screen.blit(Ship5,(600,330))
    def p6(): screen.blit(Ship6,(600,330))

    while win:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                win = False
            elif event.type == pygame.KEYDOWN:  # -----If user presses enter start game---------#
                if event.key == pygame.K_SPACE:
                    start()
                    win = False
                elif event.key == pygame.K_RETURN:
                    quit()
                    win=False

        if player=="ship1": p1()
        if player=="ship2": p2()
        if player=="ship3": p3()
        if player=="ship4": p4()
        if player=="ship5": p5()
        if player=="ship6": p6()
    
        display_text()

        pygame.display.update()

def game(size=10):
    #--------------Initializing Pygame and the screen---------------#
    pygame.init()
    screen = pygame.display.set_mode((1200, 667))
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    background = pygame.image.load("space-background.png")
    #----------Loading the images of the players-----------#
    if size == 10:
        ship1 = pygame.image.load('ship1.png')
        ship2 = pygame.image.load('ship2.png')
        ship3 = pygame.image.load('ship3.png')
        ship4 = pygame.image.load('ship4.png')
        ship5 = pygame.image.load('ship5.png')
        ship6 = pygame.image.load('ship6.png')
    elif size == 15:
        ship1 = pygame.image.load('ship1-15.png')
        ship2 = pygame.image.load('ship2-15.png')
        ship3 = pygame.image.load('ship3-15.png')
        ship4 = pygame.image.load('ship4-15.png')
        ship5 = pygame.image.load('ship5-15.png')
        ship6 = pygame.image.load('ship6-15.png')

    Ship1 = pygame.image.load('ship1-BIG.png')
    Ship2 = pygame.image.load('ship2-BIG.png')
    Ship3 = pygame.image.load('ship3-BIG.png')
    Ship4 = pygame.image.load('ship4-BIG.png')
    Ship5 = pygame.image.load('ship5-BIG.png')
    Ship6 = pygame.image.load('ship6-BIG.png')

    def ship_music():
        mixer.init()
        mixer.music.load("spaceshipSound.wav")
        mixer.music.play()
        mixer.music.set_volume(0.3)

    def is_empty(lst): return len(lst) == 0
    def enQueue(lst, data): return lst.append(data)
    def front(lst): return lst[0]
    def deQueue(lst): return lst.pop(0)
    #----------Loading all the possible dice roll images------------#
    one = pygame.image.load('dice1.png')
    two = pygame.image.load('dice2.png')
    three = pygame.image.load('dice3.png')
    four = pygame.image.load('dice4.png')
    five = pygame.image.load('dice5.png')
    six = pygame.image.load('dice6.png')


    asty1 = pygame.image.load("asty1.png")
    asty2 = pygame.image.load("asty2.png")


    ast1_x, ast1_y, ast1_CX, ast1_CY= 1100,600,0,0
    ast2_x,ast2_y,ast2_CX, ast2_CY= 1000,600,0,0


    def a1(x,y): screen.blit(asty1, (x,y))
    def a2(x,y): screen.blit(asty2, (x,y))

    snakeMsg = [
        "Oh no!",
        "You've been sucked into a BLACK HOLE!!", "You'll have to start from further back",
        "Be carefull.", "Black holes have a very strong gravatational force, try to steer clear of them!",
        "Your ship has been shot down", "Mayday", "Beep Boop", "We have entered a portal", "You have been downported"]

    # indicates a ladder climb!
    ladderMsg = [
        "Congradulations!",
        "You have entered a wormhole!",
        "nailed it, Go Go Go",
        "Congratulation, this portal has transported you forward!",
        "The Force is with you, young one.",
        "We have ascended", "Your ship has risen", "Tractor beam on us", "Portaled up!", "Nice", "Wormhole imenent"]

    if size == 10:
        snakeImg = pygame.image.load('snekPortal10.png')
        snakeTail = pygame.image.load('snekPortal10_X.png')
        ladderImg = pygame.image.load('portal10.png')
        ladderHead = pygame.image.load('portal10_X.png')
    if size == 15:
        snakeImg = pygame.image.load('snekPortal15.png')
        snakeTail = pygame.image.load('snekPortal15_X.png')
        ladderImg = pygame.image.load('portal15.png')
        ladderHead = pygame.image.load('portal15_X.png')


# is board size == 10
    if size == 10:
        # -------------------------------------------------------------------------------------------------------------------------------
        numbers = []  # --------This list stores numbers from 1 to 100.--------------#
        #------------Storing all numbers from 1 to 101 in a list------------------#
        for i in range(1, 101):
            numbers.append(i)

        #--------Loading the snakes and ladder images-----------#
        snakeImg = pygame.image.load('snekPortal10.png')
        snakeTail = pygame.image.load('snekPortal10_X.png')
        ladderImg = pygame.image.load('portal10.png')
        ladderHead = pygame.image.load('portal10_X.png')

        #------------Go from Key to Value----------------#
        #----------Storing The loaction of snakes in a dictionary---------------------#
        #----------snake heads are keys and snake tails are values--------------------#
        snakes = {
            99: 41,
            95: 75,
            93: 80,
            87: 24,
            17: 7,
            62: 19,
            54: 34,
            64: 60
        }
        #----------Storing The loaction of Ladders in a dictionary---------------------#
        #----------Ladder tails are keys and Ladder heads are values--------------------#
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

        #------This dictionary stores all the locations of the board-------#
        #------Key: Number-----Value: (x,y) co-ordinate--------------#
        location = {0: (0, 600)}
        xx, yy, mm, nn = 0, 10, 19, 9
        a, b = 100, 600
        for i in range(10):
            if i % 2 == 0:
                for j in range(xx, yy):
                    location[numbers[j]] = (a, b)
                    a += 60
                xx, yy = xx+20, yy+20
            else:
                for j in range(mm, nn, -1):
                    location[numbers[j]] = (a, b)
                    a += 60
                mm, nn = mm+20, nn+20
            a, b = 100, b-60

        def xy_location(number):
            return location[number]

        nums = {}
        for number in location:
            nums[location[number]] = number

        def num_location(x, y):
            return nums[(x, y)]
    # -------------------------------------------------------------------------------------------------------------------------------
    if size == 15:
        # -------------------------------------------------------------------------------------------------------------------------------
        numbers = []  # --------This list stores numbers from 1 to 100.--------------#
        #------------Storing all numbers from 1 to 101 in a list------------------#
        for i in range(1, 226): numbers.append(i)

        # --------Loading the snakes and ladder images-----------

        #------------Go from Key to Value----------------#
        #----------Storing The loaction of snakes in a dictionary---------------------#
        #----------snake heads are keys and snake tails are values--------------------#
        snakes = {
            99: 41,
            95: 75,
            93: 80,
            87: 24,
            17: 7,
            62: 19,
            54: 34,
            64: 60,
            224: 147,
            146: 82,
            177: 154,
            101: 47,
            155: 22,
            211: 188
        }
        #----------Storing The loaction of Ladders in a dictionary---------------------#
        #----------Ladder tails are keys and Ladder heads are values--------------------#
        ladders = {
            63: 81,
            40: 59,
            20: 38,
            4: 14,
            9: 31,
            28: 84,
            71: 91,
            51: 67,
            102: 106,
            135: 180,
            120: 123,
            1: 2,
            202: 210,
            5: 17
        }

        #------This dictionary stores all the locations of the board-------#
        #------Key: Number-----Value: (x,y) co-ordinate--------------#
        location = {0: (0, 600)}
        xx, yy, mm, nn = 0, 15, 29, 14
        a, b = 100, 600
        for i in range(15):
            if i % 2 == 0:
                for j in range(xx, yy):
                    location[numbers[j]] = (a, b)
                    a += 40
                xx, yy = xx+30, yy+30
            else:
                for j in range(mm, nn, -1):
                    location[numbers[j]] = (a, b)
                    a += 40
                mm, nn = mm+30, nn+30
            a, b = 100, b-40

        def xy_location(number): return location[number]

        nums = {}
        for number in location: nums[location[number]] = number

        def num_location(x, y): return nums[(x, y)]

# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
    #-----------Keeping a track of those locations where player has to move in reverse-------------------#

    #----------Check if the player won or not----------#
    def win_check(location):
        if num_location(location[0], location[1]) == 100 or num_location(location[0], location[1]) == 225:
            return True
        else:
            return False

    #--------The players are initially not moving--------------#
    moving = None
    #------------The previous and future values re initially zero as the dice has not been rolled------------------#

    #--------------The dice value is zero initially----------#

    #---------------The co-ordinates for the roll button to be displayed------------#
    roll_x = 750
    roll_y = 550

    #-------------The co-ordinates for the dice to be displayed==============#
    dice_x = 750
    dice_y = 80

    #-----------This funcation draws the roll button-------------------#
    charterPath = pygame.image.load('rollButton.png')

    def roll_button():
        screen.blit(charterPath, (roll_x, roll_y))

    #------------This function decides which picture is to be loaded when a dice is rolled---------------#
    def which_dice(num):
        if num == 1: return one
        if num == 2: return two
        if num == 3: return three
        if num == 4: return four
        if num == 5: return five
        if num == 6: return six

    #----------This function displays the dice----------------#
    #---------According to the dice rolled--------------------#

    def display_dice():
        dice1 = random.randint(1, 6)
        img1 = which_dice(dice1)
        return img1, 97

    def display_location(xx,yy,x,y,player):
        num = num_location(xx,yy)
        msg = player + ": " + str(num)
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(msg, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    #----------This function displays the player--------------#
    def p1(x, y): 
        screen.blit(ship1, (x, y))
        display_location(x,y,60,30,"s1")
    def p2(x, y):
        screen.blit(ship2, (x, y))
        display_location(x,y,160,30,"s2")
    def p3(x, y):
        screen.blit(ship3, (x, y))
        display_location(x,y,260,30,"s3")
    def p4(x, y):
        screen.blit(ship4, (x, y))
        display_location(x,y,360,30,"s4")
    def p5(x, y):
        screen.blit(ship5, (x, y))
        display_location(x,y,460,30,"s5")
    def p6(x, y):
        screen.blit(ship6, (x, y))
        display_location(x,y,560,30,"s6")

    # Function to display helper table
    key10 = pygame.image.load('key10.png')
    key15 = pygame.image.load('key15.png')

    def dispTable():
        x, y = 975, 100
        if size == 10:
            screen.blit(key10, (x, y))
        else:
            screen.blit(key15, (x, y))
    #----------------This function tells if the player is in a snake location---------#

    def snaked(location):
        if location in snakes:
            return snakes[location]
        else:
            return False

    #---------------This function tells if the players is in a ladder location------#
    def laddered(location):
        if location in ladders:
            return ladders[location]
        else:
            return False

    def show_snake_txt():
        x = 900
        y = 30
        msg=deQueue(snakeMsg)
        enQueue(snakeMsg,msg)
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        text = font.render(msg, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def show_ladder_txt():
        x = 900
        y = 30
        msg=deQueue(ladderMsg)
        enQueue(ladderMsg,msg)
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(msg, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    #----------This function displays all the snake locations-----------------#
    def show_snakes():
        for snake in snakes:
            snake_x = xy_location(snake)[0]
            snake_y = xy_location(snake)[1]
            screen.blit(snakeImg, (snake_x, snake_y))

    def show_snakeTails():
        for snake in snakes:
            snake_x = xy_location(snakes[snake])[0]
            snake_y = xy_location(snakes[snake])[1]
            screen.blit(snakeTail, (snake_x, snake_y))

    #-------------This function displays all the ladder locations-------------#
    def show_ladders():
        for ladder in ladders:
            ladder_x = xy_location(ladder)[0]
            ladder_y = xy_location(ladder)[1]
            screen.blit(ladderImg, (ladder_x, ladder_y))

    def show_laddersHeads():
        for ladder in ladders:
            ladder_x = xy_location(ladders[ladder])[0]
            ladder_y = xy_location(ladders[ladder])[1]
            screen.blit(ladderHead, (ladder_x, ladder_y))

    #------------This function grids a particular number in a particular x,y co-ordinate-------------#
    def board(x, y, number):
        if size == 10:
            pygame.draw.rect(screen, (225, 225, 225), (x, y, 60, 60), 2)
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(number), False, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (x+30, y+30)
            screen.blit(text, textRect)
        if size == 15:
            pygame.draw.rect(screen, (225, 225, 225), (x, y, 40, 40), 2)
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(str(number), False, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (x+20, y+20)
            screen.blit(text, textRect)

    #--------------This function sends all the numbers in the above function------------#
    #--------------In such a way that we get classic snakes and ladder board------------#
    #--------------------Where every second line is reversed----------------------------#

    def square():
        red = 0
        blue = 0
        green = 0
        left = 100
        top = 60
        width = 600
        height = 600
        filled = 0
        pygame.draw.rect(screen, [red, blue, green], [
                         left, top, width, height], filled)

    def getBoard():
        if size == 10:
            xx, yy, mm, nn = 0, 10, 19, 9
            a, b = 100, 600
            for i in range(10):
                if i % 2 == 0:
                    for j in range(xx, yy):
                        board(a, b, numbers[j])
                        a += 60
                    xx, yy = xx+20, yy+20
                else:
                    for j in range(mm, nn, -1):
                        board(a, b, numbers[j])
                        a += 60
                    mm, nn = mm+20, nn+20
                a, b = 100, b-60
        elif size == 15:
            xx, yy, mm, nn = 0, 15, 29, 14
            a, b = 100, 600
            for i in range(15):
                if i % 2 == 0:
                    for j in range(xx, yy):
                        board(a, b, numbers[j])
                        a += 40
                    xx, yy = xx+30, yy+30
                else:
                    for j in range(mm, nn, -1):
                        board(a, b, numbers[j])
                        a += 40
                    mm, nn = mm+30, nn+30
                a, b = 100, b-40

    def whose_turn(x):
        if x:
            if x == "ship1": screen.blit(Ship2, (750, 300))
            if x == "ship2": screen.blit(Ship3, (750, 300))
            if x == "ship3": screen.blit(Ship4, (750, 300))
            if x == "ship4": screen.blit(Ship5, (750, 300))
            if x == "ship5": screen.blit(Ship6, (750, 300))
            if x == "ship6": screen.blit(Ship1, (750, 300))

    #-----Initially the dice is zero---------#
    dice = 0

    #-------The initial positions of the player--------#
    players = {"ship1": (0, 600), "ship2": (0, 600), "ship3": (
        0, 600), "ship4": (0, 600), "ship5": (0, 600), "ship6": (0, 600)}

    players = {"ship1":(0,600)}

    heroes = ["ship1", "ship2", "ship3", "ship4", "ship5", "ship6"]
    heroes = ["ship1"]

    ladder=False
    snake=False

    img1 = False
    ship = "ship6"
    #-----The game will be running unless the player presses the quit button----------#
    running = True
    while running:  # ------ Keep on running the game unless player presses quit--------#
        screen.fill((255, 255, 255))  # ---------FIll the screen------------#
        screen.blit(background, (0, 0))
        for event in pygame.event.get():  # --------Looping over all the events in the game---------#
            if event.type == pygame.QUIT:  # --------If the user quits the game------------#
                running = False  # ---------End the loop---------#
            if event.type == pygame.MOUSEBUTTONUP:  # -----If user presses mouse button-----------#
                pos = pygame.mouse.get_pos()  # ---------Get the position of the mouse--------#
                # print(pos)
                # ---If the player presses the roll button----------#
                if 751 <= pos[0] <= 958 and 552 <= pos[1] <= 635:
                    img1, dice = display_dice()
                    moving = True


        if ladder: show_ladder_txt()
        if snake: show_snake_txt()

        if img1:
            screen.blit(img1, (dice_x, dice_y))
        #-------- If Players are moving----------#
        while moving:
            ladder=False
            snake=False
            # -------Whose turn is it?---------#
            current_player = deQueue(heroes)
            ship = current_player
            enQueue(heroes, current_player)
            # ------Cordinates of that player------#
            xy_position = players[current_player]
            XX = xy_position[0]
            YY = xy_position[1]
            old = num_location(XX, YY)  # ------Previous Location------#
            new = dice+old  # -----------Updated Location-----#
            # -----If the player lands on snake------#
            try:
                if num_location(players[current_player][0], players[current_player][1])>100 :
                    win_screen(current_player)
                    running=False
                elif new > 0 and moving and not snaked(new) == False:
                    new = snaked(new)
                    snake=True
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
                # ---------If the player lands on ladder-------#
                elif new > 0 and moving and not laddered(new) == False:
                    new = laddered(new)
                    ladder=True
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
                elif new > 0 and moving:  # ---------If neither snake nor ladder----------#
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
            except KeyError:
                win_screen(current_player)
                running=False

        # ----updated XY-cordinate of ship1--------#
        ship1_x,ship1_y = players["ship1"][0], players["ship1"][1]
        # ----updated XY-cordinate of ship2--------#
        # ship2_x, ship2_y= players["ship2"][0], players["ship2"][1]
        # # ----updated XY-cordinate of ship3--------#
        # ship3_x,ship3_y = players["ship3"][0], players["ship3"][1]
        # # ----updated XY-cordinate of ship4--------#
        # ship4_x, ship4_y = players["ship4"][0], players["ship4"][1]
        # # ----updated XY-cordinate of ship5--------#
        # ship5_x, ship5_y = players["ship5"][0], players["ship5"][1]
        # # ----updated XY-cordinate of ship6--------#
        # ship6_x, ship6_y = players["ship6"][0], players["ship6"][1]


        whose_turn(ship)
        roll_button()  # ------Display the roll button-------#
        square()
        getBoard()  # --------Display the Board---------#
        show_ladders()  # ------Show all the ladders-------#
        show_snakes()  # --------Show all the snakes--------#
        show_snakeTails()
        show_laddersHeads()
        dispTable()
        p1(ship1_x, ship1_y)  # -------Display the player------#
        # p2(ship2_x, ship2_y)  # -------Display the player-----#
        # p3(ship3_x, ship3_y)  # -------Display the player------#
        # p4(ship4_x, ship4_y)  # -------Display the player-----#
        # p5(ship5_x, ship5_y)  # -------Display the player------#
        # p6(ship6_x, ship6_y)  # -------Display the player-----#
        a1(ast1_x,ast1_y)
        a2(ast2_x,ast2_y)
        pygame.display.update()  # ------Keep updating the display--------#


def start():  # ------The Welcome Display-------#
    pygame.init()  # -------Initialize Window------#
    screen = pygame.display.set_mode((1200, 667))
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    intro = True
    background = pygame.image.load('screen-01.png')
    while intro:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            elif event.type == pygame.KEYDOWN:  # -----If user presses enter start game---------#
                if event.key == pygame.K_1:
                    game()
                    intro = False
                if event.key == pygame.K_2:
                    game(15)
                    intro = False
        pygame.display.update()


start()  # -------This starts the game--------

