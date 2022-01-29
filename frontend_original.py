
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
    time.sleep(1)
    screen.fill((255, 255, 255))
    pg.display.update()

    # draw the tic tac toe lines
    pg.draw.line(screen, (0, 0, 0), (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, (0, 0, 0), (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3 * 2), (width, height / 3 * 2), 7)

    pg.display.update()

    # sleep for 1 seconds
    time.sleep(1)

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
    posx = x_coord * width/100 + 30
    posy = y_coord * height/100 + 30

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
    board[j]=board[i][:]
    draw_img(j,board[j][0], board[j][1])
    return [("teleport",i,j)]

def flip(state):
    if state=="o": return "x"
    elif state=="x": return "o"
    elif state=="ox": return "xo"
    elif state=="xo": return "ox"

def cnot(i,j):
    global color
    
    if (len(board[j][0])==1):
        if board[i][0]=="x":
            board[j][0]=flip(board[j][0])
        else:
            # udpate state
            if board[j][0]=="x":
                board[j][0]=flip(board[i][0])
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



# run the game
# initiate the game
game_initiating_window()

while(True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif any(pg.mouse.get_pressed()):
            print("drawing")
            # user_click()
    pg.display.update()
    running_time.tick(fps)


