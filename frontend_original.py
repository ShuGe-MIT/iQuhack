
from tkinter import E
import pygame as pg
import sys
import time
from pygame.locals import *


width = 400
height = 400
extraheight = 100
fps = 15
running_time = pg.time.Clock()

board = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

color=1

choice_1=-1
choice_2=-1
twoq_gate=""


pg.init()

screen = pg.display.set_mode((width, height + extraheight), 0, 32)
pg.display.set_caption("Quantum Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("plus.png")
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")
ox_img = pg.image.load("ox.png")
xo_img = pg.image.load("xo.png")
plus_img = pg.image.load("plus.png")

# rescale window
initiating_window = pg.transform.scale(initiating_window, (width, height + extraheight))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
ox_img = pg.transform.scale(ox_img, (80, 80))
xo_img = pg.transform.scale(xo_img, (80, 80))

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen.fill((255, 255, 255))
    pg.display.update()

    # draw the tic tac toe lines
    pg.draw.line(screen, (0, 0, 0), (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, (0, 0, 0), (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3 * 2), (width, height / 3 * 2), 7)

    pg.draw.line(screen, (0,0,0), (width/4 , height), (width/4 , height+extraheight), 7)
    pg.draw.line(screen, (0,0,0), (width/4*2 , height), (width/4*2 , height+extraheight), 7)
    pg.draw.line(screen, (0,0,0), (width/4*3 , height), (width/4*3 , height+extraheight), 7)

    pg.display.update()

    # sleep for 1 seconds
    time.sleep(2)

    # add in the initial board
    for i in range(9):
        draw_img(i, "ox", (255, 255, 255))
    # draw_status()


def draw_img(index,img, color):
    '''
    Updates the respective cell with image and background color
    '''
    global board

    x_coord = index % 3
    y_coord = index // 3
    posx = x_coord * width/3 + 20
    posy = y_coord * height/3 + 20
    print(posx, posy)
    if img == "x":
        commit_img = x_img
    elif img == "o":
        commit_img = o_img
    elif img == "ox":
        if color == (255, 255, 255):
            commit_img = plus_img
        else:
            commit_img = ox_img
    elif img == "xo":
        commit_img = xo_img

    screen.blit(commit_img, (posx, posy))

    # TBD, update the background color of the cell

    pg.display.update()

# TBD: draw_button and clear
def draw_button(gate):
    if gate=="all":
        pass
    elif gate=="teleport":
        pass

def clear(gate):
    pass


## moves
def plus2o(i):
    if board[i][0]=="ox" and board[i][1]==0:
        board[i][0]="o"
        draw_img(i,"o", 0)
        return [("hadamard", i)]
    else:
        return False

def plus2x(i):
    if board[i][0]=="ox" and board[i][1]==0:
        board[i][0]="x"
        draw_img(i,"x", 0)
        return [("sigmaz", i),("hadamard", i)]

def teleport(i,j):
    board[i]=["ox",0]
    board[j]=board[i][:]
    draw_img(i,board[i][0],board[i][1])
    draw_img(j,board[j][0], board[j][1])
    return [("teleport",i,j)]

def flip_(state):
    if state=="o": return "x"
    elif state=="x": return "o"
    elif state=="ox": return "xo"
    elif state=="xo": return "ox"

def cnot(i,j):
    global color
    
    if (len(board[j][0])==1):
        if board[i][0]=="x":
            board[j][0]=flip_(board[j][0])
        else:
            # udpate state
            if board[j][0]=="x":
                board[j][0]=flip_(board[i][0])
            else:
                board[j][0]=board[i][0]

            # update color
            if board[i][1]==0:
                board[i][1]=color
                board[j][1]=color
                color+=1
                draw_img(i,board[i][0], board[i][1])
            else:
                board[j][1]=board[i][1]
        draw_img(j,board[j][0], board[j][1])
        return [("cnot",i,j)]
    return False

## handle user click
def user_click():
    global choice_1, twoq_gate, choice_2
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get column of mouse click (1-3)
    if y<height:
        if(x<width / 3):
            col = 1
        elif (x<width / 3 * 2):
            col = 2
        elif(x<width):
            col = 3
        else:
            col = None
        # get row of mouse click (1-3)
        if(y<height / 3):
            row = 1
        elif (y<height / 3 * 2):
            row = 2
        elif(y<height):
            row = 3
        else:
            row = None
        if col!=None and row!=None:
            i=(col-1)*3+(row-1)
            if not twoq_gate:
                choice_1=i
                if len(board[i][0])==1:
                    draw_button("all")
                else:
                    draw_button("teleport")
            elif choice_1>=0:
                if twoq_gate=="teleport":
                    teleport(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1
                elif twoq_gate=="cnot":
                    cnot(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1


    else:
        if(x<width / 4) and choice_1>=0:
            plus2o(choice_1)
            clear()
            choice_1=-1
        elif (x<width / 4 * 2):
            plus2x(choice_1)
            clear()
            choice_1=-1
        elif(x<width / 4 * 3):
            button = "cnot"
            twoq_gate="cnot"
        else:
            button =  "teleport"
            twoq_gate="teleport"




# run the game
# initiate the game
game_initiating_window()

run = True
while(run):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("drawing")
            # user_click()
    pg.display.update()
    running_time.tick(fps)


