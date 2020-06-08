All reports and handouts should be submitted to this folder.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Proposal
---------------------------------------------------
Project Title: Snakes and Ladders Game
---------------------------------------------------
Team Members:   Ahmad Feroz (06109)
                Habib Shehzad (05888)
                Synclair Samson (05901)
---------------------------------------------------
---------------------------------------------------
Project Description:
------------------------------------------------------------------------------------------------------

In this project we will be designing a game of snakes and ladders. The game will be played by 1 – 6 players with the option to add the computer as a player as well. If there is only one human player, the computer will be added as an opponent automatically. There will be a number of “snakes” and “ladders” shown on the board, each connecting two specific board squares. The objective of the game will be to implement DS&A concepts to display the board on screen (in a command prompt or terminal window), update the respective player’s locations on the board. 

On the board, each snake will be represented by a length of alphabetical characters. The head of the snake will be represented by a capital letter while the rest of its body will consist of lowercase versions of the letter – all snakes will be represented by different letters. There may be straight or curly snakes on any given board in any game. Ladders will be represented by a hyphen (-) in the respective square and will only be vertical.

The player will have the option to choose between two board sizes: a 100 square, 10x10 board or a 225 square, 15x15 board.

To start the game, each player will roll a dice and the player with the highest number will go first. In case any players roll the same number, their roll will be deemed invalid and they will have to roll again after everyone else has rolled. The player 1 will have the advantage to decide whether to continue the game at the end of each round.

Once a round is started, each player will roll two die. Their result will be displayed on screen and their sum of which will be added to their respective positions on the board. All players including the computer will be represented by a special character on the board:
    
    ['!', '@', '#', '$', '%', '^']

On every player’s turn, the screen will be cleared, and the board with the updated with their new location. 
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
Game Rules (proposed):
---------------------------------------------------
1.	In case any two players land on the same box, the later player will go to the closest previous box available. 
2.	If a player reaches the bottom of a ladder, they will climb (go forward) to the end point
3.	If a player meets the head of a snake, they will go back to the tail of the respective snake
4.	The player who reaches the topmost box first wins!

At the end of the game, a scoreboard will be displayed, along with a prompt for the player(s) to play again or not.
The project will make use of various DS&A concepts such as a queue to determine which player’s turn it is, dictionary/ list to store and display the board. We will also use a library to help generate random numbers for the dice rolls. We will also define our own functions for various tasks such as printing the board, rolling the dice etc.
---------------------------------------------------