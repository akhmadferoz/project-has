'''
This is the source code for the game of Snakes & Ladders.
Course: CS 102 - Data Structures & Algorithms (L2)
Instructor: Dr. Syeda Saleha Raza
Team Members:
Ahmad Feroz (06109)
Habib Shahzad (05888)
Synclair Samson (05901)
For information on the rules of the game and how the game is structured please refer to the Readme.md file.
'''
#----------Importing the important things to be used-------------#
import pygame
import random
from pygame import mixer

def theme():
    # initialize
    pygame.mixer.pre_init()
    pygame.mixer.init()
    # start playing the background music
    pygame.mixer.music.load('Thoughts on the Road (new ed).wav')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=-1)
theme() #---------Background music-----#

#-------Display the win screen when a player wins----------#
def win_screen(player,rounds):
    #--------------Initializing Pygame and the screen---------------#
    pygame.init()
    #-----------Setting the size of the window-----------#
    screen = pygame.display.set_mode((1200, 667))
    #-------------Setting the caption of the window------------#
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    win = True #-------While the player celebrate his victory, this will be true----------#
    #---------Loading the background image-------------#
    background= pygame.image.load("12435.jpg")
    #-----------Loading the ship images---------------#
    Ship1 = pygame.image.load('ship1-BIG.png')
    Ship2 = pygame.image.load('ship2-BIG.png')
    Ship3 = pygame.image.load('ship3-BIG.png')
    Ship4 = pygame.image.load('ship4-BIG.png')
    Ship5 = pygame.image.load('ship5-BIG.png')
    Ship6 = pygame.image.load('ship6-BIG.png')
    
    #-------Displaying the winning text-----------#
    def display_text():
        win="Congratulations " + player + " You Won in " + str(rounds) + " rounds, Press SPACE to Play again."
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(win, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (600, 30)
        screen.blit(text, textRect)

    #-----------Drawing the winning ship-------------#
    def draw_ship(x,y):
        if player=="Daedalus": screen.blit(Ship1,(x,y))
        if player=="Explorer": screen.blit(Ship2,(x,y))
        if player=="Excalibur": screen.blit(Ship3,(x,y))
        if player=="Intrepid": screen.blit(Ship4,(x,y))
        if player=="Odyssey": screen.blit(Ship5,(x,y))
        if player=="Pleiades": screen.blit(Ship6,(x,y))

    #-----------Until win is True, Keep the Window open-------------#
    while win:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                win = False
            elif event.type == pygame.KEYDOWN:  # -----If user presses enter Space, start game again---------#
                if event.key == pygame.K_SPACE:
                    start()
                    win = False
                elif event.key == pygame.K_RETURN:
                    quit()
                    win=False
        draw_ship(500,230)
        display_text()
        pygame.display.update()

def game(num_players,size=10):
    #--------------Initializing Pygame and the screen---------------#
    pygame.init()
    #-----------Setting the size of the window-----------#
    screen = pygame.display.set_mode((1200, 667))
    #-------------Setting the caption of the window------------#
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    #----------Loading the background image---------#
    background = pygame.image.load("space-background.png")
    #----------Loading the images of the ships that are going to roll-----------#
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

#-----------Big Ships to be displayed on the side to show whose turn it is---------#
    Ship1 = pygame.image.load('ship1-BIG.png')
    Ship2 = pygame.image.load('ship2-BIG.png')
    Ship3 = pygame.image.load('ship3-BIG.png')
    Ship4 = pygame.image.load('ship4-BIG.png')
    Ship5 = pygame.image.load('ship5-BIG.png')
    Ship6 = pygame.image.load('ship6-BIG.png')

    s1,s2,s3 = pygame.image.load('ship1-15.png'), pygame.image.load('ship2-15.png'), pygame.image.load('ship3-15.png')
    s4,s5,s6 = pygame.image.load('ship4-15.png'), pygame.image.load('ship5-15.png'), pygame.image.load('ship6-15.png')

#----------Music when the ship moves--------#
    def spaceshipSound():
        sound = pygame.mixer.Sound("spaceshipSound.wav")
        channel = sound.play()      
        channel.set_volume(0.04)

#-----Some Queue functions to be used-----------#
    def is_empty(lst): return len(lst) == 0
    def enQueue(lst, data): return lst.append(data)
    def front(lst): return lst[0]
    def deQueue(lst): return lst.pop(0)

    #----------Loading all the possible dice roll images------------#
    one,two,three = pygame.image.load('dice1.png'), pygame.image.load('dice2.png'), pygame.image.load('dice3.png')
    four,five,six = pygame.image.load('dice4.png'), pygame.image.load('dice5.png'), pygame.image.load('dice6.png')

    #----Loading asteroids and setting their cordinates------------#
    asty1,asty2 = pygame.image.load("asty1.png"), pygame.image.load("asty2.png")
    ast1_x, ast1_y,= 1100,600
    ast2_x,ast2_y= 1000,600
    def a1(x,y): screen.blit(asty1, (x,y))
    def a2(x,y): screen.blit(asty2, (x,y))

    # Indicates a snake bite -------- BLACKHOLE
    snakeMsg = [
        "Oh no!",
        "You've been sucked into a BLACK HOLE!!", "You'll have to start from further back",
        "Be carefull.", "Black holes have a very strong gravatational force, try to steer clear of them!",
        "Your ship has been shot down", "Mayday", "Beep Boop", "We have entered a portal", "You have been downported"]

    # indicates a ladder climb!-----------WORMHOLE
    ladderMsg = [
        "Congradulations!",
        "You have entered a wormhole!",
        "nailed it, Go Go Go",
        "Congratulation, this portal has transported you forward!",
        "The Force is with you, young one.",
        "We have ascended", "Your ship has risen", "Tractor beam on us", "Portaled up!", "Nice", "Wormhole imenent"]


    #-----------This list will tell us that how many players do the user want------------#
    all_players = []
    for i in range(6): all_players.append(False)
    for i in range(num_players): all_players[i]= True

    #-------Storing the numbers and their coresponding cordinates-------------#
    location = {0: (0, 600)}

        #--------Loading the snakes and ladder images-----------#
    if size == 10:
        snakeImg, snakeTail = pygame.image.load('snekPortal10.png'), pygame.image.load('snekPortal10_X.png')
        ladderImg, ladderHead = pygame.image.load('portal10.png'), pygame.image.load('portal10_X.png')
    if size == 15:
        snakeImg, snakeTail = pygame.image.load('snekPortal15.png'), pygame.image.load('snekPortal15_X.png')
        ladderImg, ladderHead = pygame.image.load('portal15.png'), pygame.image.load('portal15_X.png')


#---------numbers--------#
    numbers = []

# ---------- board size == 10-----------#
    if size == 10:
        # -------------------------------------------------------------------------------------------------------------------------------
      # --------This list stores numbers from 1 to 100.--------------#
        #------------Storing all numbers from 1 to 101 in a list------------------#
        for i in range(1, 101):
            numbers.append(i)
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
        xx, yy, mm, nn = 0, 10, 19, 9
        a, b = 100, 600
        for i in range(size):
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
    # -------------------------------------------------------------------------------------------------------------------------------
    if size == 15:
        # -------------------------------------------------------------------------------------------------------------------------------
      # --------This list stores numbers from 1 to 225.--------------#
        #------------Storing all numbers from 1 to 226 in a list------------------#
        for i in range(1, 226): numbers.append(i)
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
        xx, yy, mm, nn = 0, 15, 29, 14
        a, b = 100, 600
        for i in range(size):
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

# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
#-------------Convert a number location to a x-y cordinate-------------#
    def xy_location(number):
        return location[number]

    nums = {}
    for number in location:
        nums[location[number]] = number
#---------Convert a (x,y) cordinate into a number location-----------#
    def num_location(x, y):
        return nums[(x, y)]
    #--------The players are initially not moving--------------#
    moving = None
    #------------The previous and future values re initially zero as the dice has not been rolled------------------#
    #---------------The co-ordinates for the roll button to be displayed------------#
    roll_x = 750
    roll_y = 550
    #-------------The co-ordinates for the dice to be displayed==============#
    dice_x = 750
    dice_y = 80
    #-----------This funcation draws the roll button-------------------#
    charterPath = pygame.image.load('rollButton.png')
    def roll_button(): screen.blit(charterPath, (roll_x, roll_y))

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

    def display_location(xx,yy,x,y):
        num = num_location(xx,yy)
        msg =  ": " + str(num)
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(msg, True, (255, 255, 255), (0,0,128))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    #----------This function displays the player--------------#
    def p1(x, y): 
        screen.blit(ship1, (x, y))
        screen.blit(s1,(60,12))
        display_location(x,y,110,35)
    def p2(x, y):
        screen.blit(ship2, (x, y))
        screen.blit(s2,(160,12))
        display_location(x,y,210,35)
    def p3(x, y):
        screen.blit(ship3, (x, y))
        screen.blit(s3,(260,12))
        display_location(x,y,310,35)
    def p4(x, y):
        screen.blit(ship4, (x, y))
        screen.blit(s4,(360,12))
        display_location(x,y,410,35)
    def p5(x, y):
        screen.blit(ship5, (x, y))
        screen.blit(s5,(460,12))
        display_location(x,y,510,35)
    def p6(x, y):
        screen.blit(ship6, (x, y))
        screen.blit(s6,(560,12))
        display_location(x,y,610,35)

    #------- Function to display helper table--------#
    key10,key15 = pygame.image.load('key10.png'),pygame.image.load('key15.png')

    #--------This function displays a table that tells the user about key to Value----------------#
    def dispTable():
        x, y = 975, 100
        if size == 10: screen.blit(key10, (x, y))
        else: screen.blit(key15, (x, y))

    #----------------This function tells if the player is in a snake location---------#
    def snaked(location):
        if location in snakes: return snakes[location]
        else: return False

    #---------------This function tells if the players is in a ladder location------#
    def laddered(location):
        if location in ladders: return ladders[location]
        else: return False

    def show_snake_txt():
        msg=deQueue(snakeMsg)
        enQueue(snakeMsg,msg)
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        text = font.render(msg, True, (255,255,255), (0,0,128))
        textRect = text.get_rect()
        textRect.center = (900, 30)
        screen.blit(text, textRect)

    def show_ladder_txt():
        msg=deQueue(ladderMsg)
        enQueue(ladderMsg,msg)
        font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.time.wait(500)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(msg, True, (255,255,255), (0,0,128))
        textRect = text.get_rect()
        textRect.center = (900, 30)
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
        if size == 10: radius,font_size = 60,32
        if size==15: radius, font_size = 40,15
        A = radius//2
        pygame.draw.rect(screen, (225, 225, 225), (x, y, radius, radius), 2)
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(str(number), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x+A, y+A)
        screen.blit(text, textRect)

    #--------------This function sends all the numbers in the above function------------#
    #--------------In such a way that we get classic snakes and ladder board------------#
    #--------------------Where every second line is reversed----------------------------#

    #---------Draw a square to cover the board-----------#
    def square():
        pygame.draw.rect(screen, [0, 0, 0], [
                         100, 60, 600, 600], 0)

    #---------Draw the Board and tbe numbers------------#
    def getBoard():
        for number in numbers:
            num_x, num_y = xy_location(number)[0], xy_location(number)[1]
            board(num_x,num_y,number)

    #---------This function helps in converting a string into a surface-------------#
    def display_txt(msg,x,y,font_size):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(msg, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def surfaceToName(ship):
        if ship==Ship1: ship_name = "Daedalus"
        if ship==Ship2: ship_name = "Explorer"
        if ship==Ship3: ship_name = "Excalibur"
        if ship==Ship4: ship_name = "Intrepid"
        if ship==Ship5: ship_name = "Odyssey"
        if ship==Ship6: ship_name = "Pleiades"
        return ship_name

    #----------Displays the image of the ship that has to roll next----------#
    def whose_turn(x):
        XX,YY,text_x,text_y = 750,300,900,500
        if x:  #--------If x is True------------#
            if x == "Daedalus":
                if all_players[1]: next_ship = Ship2
                else: next_ship = Ship1
            if x=="Explorer":
                if all_players[2]: next_ship = Ship3
                else: next_ship = Ship1
            if x=="Excalibur":
                if all_players[3]: next_ship = Ship4
                else: next_ship = Ship1
            if x== "Intrepid":
                if all_players[4]: next_ship = Ship5
                else: next_ship = Ship1
            if x=="Odyssey":
                if all_players[5]: next_ship = Ship6
                else: next_ship = Ship1
            if x=="Pleiades":
                next_ship = Ship1
            screen.blit(next_ship, (XX, YY))
            display_txt(surfaceToName(next_ship) + ", Roll the Dice",text_x,text_y,31)

    #-----Initially the dice is zero---------#
    dice = 0

    #-------All the players----------#
    heroes = ["Daedalus", "Explorer", "Excalibur", "Intrepid", "Odyssey", "Pleiades"]
    players = {} #--------This dictionary will story the location (x,y) of each player----------------#
    for i in range(num_players): players[heroes[i]] = (0,600)  #-------The initial positions of each player--------#
    spaceships = heroes[:num_players]  #--------The players that are playing-------------#

    #------No Player is initially at the ladder or the Snake-------#
    ladder=False
    snake=False

    #------------No dice to be displayed initially---------#
    rolled = False
    #-----------currently, Ship 1 is to be displayed, as it is after ship 6 in the queue--------#
    ship = "Pleiades"

    ast1_CY = 50

    #------No rounds have passed---------#
    counter = 0

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
                # ---If the player presses the roll button----------#
                if 751 <= pos[0] <= 958 and 552 <= pos[1] <= 635:
                    img1, dice = display_dice()
                    rolled=True
                    moving = True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    img1, dice = display_dice()
                    rolled=True
                    moving = True
        #------If player lands on a ladder or a snake, display this message----------#
        if ladder: show_ladder_txt()
        if snake: show_snake_txt()

        ast1_y-=ast1_CY
        if ast1_y<50:
            ast1_y=50
            ast1_CY*=-1
        if ast1_y>600:
            ast1_y = 600
            ast1_CY = 50

        #------If player pressed roll button then display dice---------------#
        if rolled: screen.blit(img1, (dice_x, dice_y))
        #-------- If Players are moving----------#
        while moving:
            ladder=False
            snake=False
            # -------Whose turn is it?---------#
            current_player = deQueue(spaceships) #-------Getting the player in the front of the queue-------#
            ship = current_player #---------The current player----------#
            enQueue(spaceships, current_player) #-------Adding that player back to the queue--------#
            counter+=1  #-------After each turn the counter increases by 1--------------#
            # ------Cordinates of that player------#
            xy_position = players[current_player] #---The x-y location of the current-player
            XX = xy_position[0] #------The x cordinate of the current player-------#
            YY = xy_position[1] #-----The y cordinate of the current player---------#
            old = num_location(XX, YY)  # ------Previous Location------#
            new = dice+old  # -----------Updated Location-----#
            # -----If the player lands on snake------#
            try:
                if new > 0 and moving and not snaked(new) == False:
                    new = snaked(new)
                    spaceshipSound()
                    snake=True
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
                # ---------If the player lands on ladder-------#
                elif new > 0 and moving and not laddered(new) == False:
                    new = laddered(new)
                    spaceshipSound()
                    ladder=True
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
                elif new > 0 and moving:  # ---------If neither snake nor ladder----------#
                    XX = xy_location(new)[0]
                    YY = xy_location(new)[1]
                    spaceshipSound()
                    # -----Update Location-------#
                    players[current_player] = (XX, YY)
                    moving = False
            except KeyError:
                win_screen(current_player,counter//len(spaceships))
                running=False

        # ----updated XY-cordinate of ship1--------#
        if all_players[0]:ship1_x,ship1_y = players["Daedalus"][0], players["Daedalus"][1]
        #----updated XY-cordinate of ship2--------#
        if all_players[1]:ship2_x, ship2_y= players["Explorer"][0], players["Explorer"][1]
        # ----updated XY-cordinate of ship3--------#
        if all_players[2]:ship3_x,ship3_y = players["Excalibur"][0], players["Excalibur"][1]
        # ----updated XY-cordinate of ship4--------#
        if all_players[3]:ship4_x, ship4_y = players["Intrepid"][0], players["Intrepid"][1]
        # ----updated XY-cordinate of ship5--------#
        if all_players[4]:ship5_x, ship5_y = players["Odyssey"][0], players["Odyssey"][1]
        # ----updated XY-cordinate of ship6--------#
        if all_players[5]:ship6_x, ship6_y = players["Pleiades"][0], players["Pleiades"][1]

        whose_turn(ship) #-------Display a ship that is next in the queue-----------#
        roll_button()  # ------Display the roll button-------#
        square()       #------Display a black square that covers the board-----------#
        getBoard()  # --------Display the Board---------#
        show_ladders()  # ------Show all the ladders-------#
        show_snakes()  # --------Show all the snakes--------#
        show_snakeTails() #-------Show snake tails---------#
        show_laddersHeads() #------Show ladder heads----------#
        dispTable() #----Show the key of values----------#
        #--------Display the player only if the player exists-------------#
        if all_players[0]:p1(ship1_x, ship1_y)  # -------Display the player------#
        if all_players[1]:p2(ship2_x, ship2_y)  # -------Display the player-----#
        if all_players[2]:p3(ship3_x, ship3_y)  # -------Display the player------#
        if all_players[3]:p4(ship4_x, ship4_y)  # -------Display the player-----#
        if all_players[4]:p5(ship5_x, ship5_y)  # -------Display the player------#
        if all_players[5]:p6(ship6_x, ship6_y)  # -------Display the player-----#
        a1(ast1_x,ast1_y) #---Display the asteroid---#
        a2(ast2_x,ast2_y)
        pygame.display.update()  # ------Keep updating the display--------#

def start():  # ------The Welcome Display-------#
    pygame.init()  # -------Initialize Window------#
    screen = pygame.display.set_mode((1200, 667))
    num_players = 0 #-----------no players initiallly------------#
    pygame.display.set_caption("Snakes & Ladders - Space Eddition")
    intro = True
    background = pygame.image.load('screen-01.png')
    begin = False
    def display_txt(n,x,y,font_size,b=True):
        if b: msg = "Number of Players: Enter a number ranging from 1 to 6 in your keyBoard."
        else: msg = "You want "+str(n)+" players."
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(msg, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)
    while intro:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        if not begin: display_txt(num_players,600,640,32)
        else: display_txt(num_players,600,640,32,False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            elif event.type == pygame.KEYDOWN:  # -----If user presses any key---------#
                begin=True
                if   event.key == pygame.K_1: num_players = 1
                elif event.key == pygame.K_2: num_players = 2
                elif event.key == pygame.K_3: num_players = 3
                elif event.key == pygame.K_4: num_players = 4
                elif event.key == pygame.K_5: num_players = 5
                elif event.key == pygame.K_6: num_players = 6
                if event.key == pygame.K_a: #------If user presses "a"-----------#
                    if num_players>0: #----Game won't start if players are zero--------#
                        game(num_players) #-------Board 10----------#
                        intro = False
                if event.key == pygame.K_b:#---------If user user presses "b"-----------#
                    if num_players>0: #----Game won't start if players are zero--------#
                        game(num_players,15) #------Board 15---------#
                        intro = False
        pygame.display.update()
start() # -------This starts the game--------#
