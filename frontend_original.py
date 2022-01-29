
import pygame as pg
import sys
import time
from pygame.locals import *

width = 400
height = 400
extraheight = 100
fps = 15
running_time = pg.time.Clock()

board = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), (None, None), (None, None), (None, None)]

pg.init()

screen = pg.display.set_mode((width, height + extraheight), 0, 32)
pg.display.set_caption("Quantum Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("initial_cover.png")
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")
plus_img=pg.image.load("plus.png")
minus_img = pg.image.load("minus.png")
ox_img = pg.image.load("ox.png")
xo_img = pg.image.load("xo.png")

# rescale window
initiating_window = pg.transform.scale(initiating_window, (width, height + extraheight))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
plus_img = pg.transform.scale(plus_img, (80, 80))
minus_img = pg.transform.scale(minus_img, (80, 80))
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
        draw_img(i, "plus", (255, 255, 255))
    draw_status()
    

def draw_img(index, img, color):
    '''
    Updates the respective cell with image and background color
    '''
    global board

    x_coord = index % 3
    y_coord = index // 3
    posx = x_coord * width/100 + 30
    posy = y_coord * height/100 + 30

    board[index][0] = img
    board[index][1] = color

    if img == "x":
        commit_img = x_img
    elif img == "o":
        commit_img = o_img
    elif img == "plus":
        commit_img = plus_img
    elif img == "minus":
        commit_img = minus_img
    elif img == "ox":
        commit_img = ox_img
    elif img == "xo":
        commit_img = xo_img

    screen.blit(commit_img, (posx, posy))

    # TBD, update the background color of the cell

    pg.display.update()





