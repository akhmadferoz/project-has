
#----------Importing the important things to be used-------------#
import pygame
import random
from pygame import mixer
import math


#--------------Initializing Pygame and the screen---------------# 
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Snakes & Ladders")

#----------Loading the images of the players-----------#
player1 = pygame.image.load('batman.png')
player2 = pygame.image.load('superman.png')



#----------Loading all the possible dice roll images------------#
one = pygame.image.load('one.png')
two = pygame.image.load('two.png')
three = pygame.image.load('three.png')
four = pygame.image.load('four.png')
five = pygame.image.load('five.png')
six = pygame.image.load('six.png')



numbers=[] #--------This list stores numbers from 1 to 100.--------------#
wyes = [600,540,480,420,360,300,240,180,120,60]

#--------Loading the snakes and ladder images-----------#
snakeImg = pygame.image.load('snake.png')
ladderImg = pygame.image.load('ladder.png')



            #------------Go from Key to Value----------------#
#----------Storing The loaction of snakes in a dictionary---------------------#
#----------snake heads are keys and snake tails are values--------------------#
snakes = {
(120,60): (180,180),
(360,60):(360,180), 
(480,60): (480.180), 
(420,120): (240,480), 
(240,540): (420,600),
(120,240):(120,540), 
(420,300):(420,420),
(240,240):(60,300)
}
#----------Storing The loaction of Ladders in a dictionary---------------------#
#----------Ladder tails are keys and Ladder heads are values--------------------#
ladders = {
(180,240):(60,120),
(60,420):(120,300),
(180,420):(60,540),
(240,600):(420,540),
(540,600):(600,420),
(480,480):(240,120),
(600,180):(600,60),
(600,300):(420,540)
}

def wye(location): return location in wyes


#-----------Keeping a track of those locations where player has to move in reverse-------------------#
def reverse(location):
    reversy=[]
    for i in range(10):
        if i%2!=0: reversy.append(wyes[i])
    return location in reversy


#------------Storing all numbers from 1 to 101 in a list------------------#
for i in range(1,101):numbers.append(i)

#--------The initial Co-ordinates of the player----------#
p1_X, p1_Y= 0, 600


#--------The change in x and y co-ordinates is initally zero--------------#
p1_x_change = 0
p1_y_change = 0


#--------The players are initially not moving--------------#
moving = None


#------------The previous and future values re initially zero as the dice has not been rolled------------------#
previous = 0
future = 0

#--------------The dice value is zero initially----------#
stop = p1_X
dice_num = 0


#---------------The co-ordinates for the roll button to be displayed------------#
roll_x = 800
roll_y = 500

#-------------The co-ordinates for the dice to be displayed==============#
dice_x = 700
dice_y = 100


#-----------This funcation draws the roll button-------------------#
def roll_button():
    pygame.draw.rect(screen,(0,0,0),(roll_x,roll_y,100,100))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("ROLL", False,(0, 0, 128) )
    textRect = text.get_rect()
    textRect.center = (roll_x+50, roll_y+50) 
    screen.blit(text, textRect) 


#------------This function decides which picture is to be loaded when a dice is rolled---------------#
def which_dice(num): 
    if num==1: return one
    if num==2: return two
    if num==3: return three
    if num==4: return four
    if num==5: return five
    if num==6: return six


#----------This function displays the dice----------------#
def display_dice(x,y):
    dice = random.randint(1,6)
    img = which_dice(dice)
    screen.blit(img,(x,y))
    return 4

#----------This function displays the player--------------#
def p1(x,y): screen.blit(player1,(x,y))

#----------------This function tells if the player is in a snake location---------#
def snaked(location):
    for snake in snakes:
        if (location[0],location[1])==(snake[0],snake[1]): return True            

#---------------This function tells if the players is in a ladder location------#
def laddered(location):
    for ladder in ladders:
        if (location[0],location[1])==(ladder[0],ladder[1]): return True    

#----------This function displays all the snake locations-----------------#
def show_snakes():
    for snake in snakes:
        snake_x = snake[0]
        snake_y = snake[1]    
        screen.blit(snakeImg,(snake_x+20,snake_y+20))

#-------------This function displays all the ladder locations-------------#
def show_ladders():
    for ladder in ladders:
        ladder_x = ladder[0]
        ladder_y = ladder[1]    
        screen.blit(ladderImg,(ladder_x+20,ladder_y+20))

#------------This function grids a particular number in a particular x,y co-ordinate-------------#
def board(x,y,number):
    pygame.draw.rect(screen,(0,0,0),(x,y,60,60),2)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), False,(0, 0, 128) )
    textRect = text.get_rect()
    textRect.center = (x+30, y+30) 
    screen.blit(text, textRect)

#--------------This function sends all the numbers in the above function------------#
#--------------In such a way that we get classic snakes and ladder board------------#
#--------------------Where every second line is reversed----------------------------#
def getBoard():
    xx,yy,mm,nn = 0,10,19,9
    a,b = 60,600
    for i in range(10):
        if i%2==0:
            for j in range(xx,yy):
                board(a,b,numbers[j])
                a+=60
            xx,yy=xx+20,yy+20
        else:
            for j in range(mm,nn,-1):
                board(a,b,numbers[j])
                a+=60
            mm,nn = mm+20,nn+20
        a,b=60,b-60

#-------The initial positions of the player--------#
positions= [(0,0)]

#-----The game will be running unless the player presses the quit button----------#
running=True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if 800<=pos[0]<=900 and 500<=pos[1]<=600:
                positions.append((p1_X,p1_Y))
                dice=display_dice(dice_x,dice_y)
                future=p1_X + (60*dice)
                if reverse(p1_Y): future = p1_X - (60*dice)
                moving=True        

    xx= positions[-1][0]
    yy = positions[-1][1]

    if snaked((xx,yy)):
        newx = snakes[(xx,yy)][0]
        newy = snakes[(xx,yy)][1]
        p1_X = newx
        p1_Y = newy

    if laddered((xx,yy)):
        newx = ladders[(xx,yy)][0]
        newy = ladders[(xx,yy)][1]
        p1_X = newx
        p1_Y = newy

    if not snaked((xx,yy)) and not laddered((xx,yy)):
        p1_X += p1_x_change
        if future>600 and moving:
            steps =(600 - xx) + 60
            left = 600 - ((dice*60)-steps)
            if p1_X==left and p1_Y==yy-60:
                moving=False
                p1_x_change=0
            else:
                p1_x_change = 40
                if reverse(p1_Y): p1_x_change*=-1
                if p1_X>600:
                    p1_x_change = 0
                    p1_Y -= 60
                    p1_X = 600
        if future<0 and moving:
            steps = (xx-60)+60
            left = ((dice*60)-steps) + 60
            if p1_X==left and p1_Y==yy-60:
                moving=False
                p1_x_change=0
            else:
                p1_x_change=40
                if reverse(p1_Y):p1_x_change*=-1
                if p1_X<60:
                    p1_x_change=0
                    p1_Y -=60
                    p1_X = 60
        else:
            if p1_X>600:
                moving=False
                p1_x_change=0
                p1_X = 600
                p1_Y -= 60
            if p1_X<0:
                moving=False
                p1_x_change=0
                p1_X = 60
                p1_Y-=60
            if p1_X==future:
                moving=False
                p1_x_change=0
            if moving:
                p1_x_change = 40
                if reverse(p1_Y):
                    p1_x_change*=-1

        roll_button()
        getBoard()
        show_snakes()
        show_ladders()
        p1(p1_X,p1_Y)
        pygame.display.update()


