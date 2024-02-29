# TicTacToe

## Module
  I make this game using [**pygame**](https://www.pygame.org/news) and [**numpy**](https://numpy.org/) and both and not pre-installed in python so before try to run this program has to install both mudule. to install copy this command 
 `py -3 -m pip install pygame && pip install numpy ` and open cmd and paste this  command there and press enter
  
## DEVELOPMENT
  For this **TicTacToe** Game project I use [**pygame**](https://www.pygame.org/news) library and [**numpy**](https://numpy.org/) library.This is fun project for me as work with GUI. this is two player game and without bot player so player and try to create your own new one you.

## GAME DESCRIPTION
  Tic Tac Toe is a two-player game. In this game, there is a board with 3 x 3 squares.

  The two players take turns putting marks on a 3x3 board. The goal of Tic Tac Toe game is to be one of the players to get three same symbols in a row - horizontally, vertically or diagonally on a 3 x 3 grid. The player who first gets 3 of his/her symbols (marks) in a row - vertically, horizontally, or diagonally wins the game, and the other loses the game. The game can be played by two players.

## GAME RULES
  A player start game get the symbol "X" and second get "O".
  1. The player that gets to play first will get the "X" mark (we call him/her player 1) and the player that gets to play second will get the "O" mark (we call him/her player 2).
  2. Player 1 and 2 take turns making moves with Player 1 playing mark “X” and Player 2 playing mark “O”.
  3. A player marks any of the 3x3 squares with his mark (“X” or “O”) and their aim is to create a straight line horizontally, vertically or diagonally with two intensions:
    a. One of the players gets three of his/her marks in a row (vertically, horizontally, or diagonally) i.e. that player wins the game.
    b. If no one can create a straight line with their own mark and all the positions on the board are occupied, then the game ends in a draw/tie.

## CODE
### VARIABLE 
- `FPS` frame rate of this game
- `WIDTH,HEIGHT` width and height of game window
- `FONTCOLOR` font color for winner & draw
- `BG_COLOR` background color of display window
- `**win**` game window object
- `boxSize` width and hight of every box in game

### FUNCATION DESCRIPTION:
- `createBOARD()` create a blank Board
- `showText( text)` show arg text on display
- `line()` draw horizantel and vertiacal line on window
- `cross() && circle(x,y)` draw symbol **X** and **O**
- `checkAndFill()` fill up board (X O and lines)
- `setValue(x,y,Board)` set symbol in board postion [x][y]
- `checkWinner(player)` when ever new value add to board we check is player win this game of not

  

