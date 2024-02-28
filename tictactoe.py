import pygame
import numpy as np
#initilize font 
pygame.font.init()


FPS = 24 #FramePerSecond
WIDTH,HEIGHT = 600,600 #size of window width & height
COLOR = (9,244,211) #color
FONTCOLOR = (224,224,224) # color of the font
BG_COLOR = (11,117,94)# background color

#create a window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tiktaktoe")
win.fill((BG_COLOR))
#variable of font
gameText = pygame.font.SysFont("comicsans",50,True)

margin = 20
padding = 30 
boxSize= WIDTH//3

#GAME Value
player= 1 
BOARD = [] #Board VAR
counter = 0 

#create a blank BOARD
def createBOARD():
    global counter
    global BOARD
    #create 3X3 array
    BOARD = np.array([0]*9).reshape(3,3)
    counter = 0


#winner && game draw text
def showText(text):
        global BOARD
        CheckAndFill()
        GAMETEXT = gameText.render(text,1,FONTCOLOR)
        win.blit(GAMETEXT,(300- GAMETEXT.get_width()//2,300 - GAMETEXT.get_height()//2))
        createBOARD()
        pygame.display.update()
        pygame.time.delay(5000)
        
        
#Draw horizontal and vertial line
def line():
    for lineNum in range(1,3):
        #pygame.draw.line(windowSrc,color,startPoint(x,y),endingPoint(x,y),width)
        #horizantal line
        pygame.draw.line(win,COLOR,
                         (lineNum*WIDTH//3, margin),
                         (lineNum*WIDTH//3,HEIGHT-margin),10)
        #vartical line
        pygame.draw.line(win,COLOR,
                         (margin, lineNum*HEIGHT//3),
                         (WIDTH-margin,lineNum*HEIGHT//3),10)

#Draw Cross
def cross(posY, posX):
    pygame.draw.line(win, COLOR,
                     (posX*(WIDTH//3)+padding,posY*(HEIGHT//3)+padding),
                     ((posX+1)*(WIDTH//3)-padding,(posY+1)*(HEIGHT//3)-padding),
                     5*3)
    pygame.draw.line(win, COLOR,
                     (posX*(WIDTH//3)+padding,(posY+1)*(HEIGHT//3)-padding),
                     ((posX+1)*(WIDTH//3)-padding,(posY)*(HEIGHT//3)+padding),
                     5*3)

#Draw Circle
def circle(posX,posY):
    pygame.draw.circle(win,COLOR,(((WIDTH*(2*posX +1 )//6)),(HEIGHT*(2*posY +1 )//6)),WIDTH//6-padding,10)
    
#fill the BOARD
def CheckAndFill():
    line()
    #loop to check every value
    for i in range(3):
        for j in range(3):
            #check value for cross
            if BOARD[i][j] == 1:
                cross(i,j)
            #check value of circle
            elif BOARD[i][j] == 2:
                circle(j,i)

#put value in BOARD
def setValue(posX,posY,BOARD):
    global counter
    global player
    #check if value is not occupied
    if BOARD[posX][posY] == 0:
        #first player
        if player:
            BOARD[posX][posY] = 1
            player = 0
        #second player
        else:
            BOARD[posX][posY] = 2
            player = 1
        counter +=1

        checkWinner(player)

#funtion to return true in winner check
def checkPlayer(i,j,player):
    if BOARD[i,j] == player+1:
        return True

#winner check
def checkWinner(player):
    for i in range(3):
        if (checkPlayer(i,1,player) and checkPlayer(i,2,player) and checkPlayer(i,0,player)) or (checkPlayer(0,i,player) and checkPlayer(1,i,player) and checkPlayer(2,i,player)):
            showText("winner is player:"+str(player+1))
    if(checkPlayer(1,1,player) and checkPlayer(2,2,player) and checkPlayer(0,0,player)) or (checkPlayer(0,2,player) and checkPlayer(2,0,player) and checkPlayer(1,1,player)):
        showText("winner is player:"+str(player+1))
    
def main():
    global BOARD
    createBOARD()
    clock = pygame.time.Clock()
    run = True
    
    while run:
        win.fill((BG_COLOR))
        # clock.tick(FPS)
        for event in pygame.event.get():
            #check for game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # check is mousedown
            if event.type == pygame.MOUSEBUTTONDOWN:
               posMouse = pygame.mouse.get_pos()  #get postion of curse Tuple (X,Y)
               posX, posY= posMouse[1]//boxSize,posMouse[0]//boxSize            
               setValue(posX,posY,BOARD)
       
        CheckAndFill()
        if counter == 9:
            showText("game Draw")
            print("this not working")
            createBOARD()
            
        pygame.display.update()
        
if __name__ =="__main__":
    main()
