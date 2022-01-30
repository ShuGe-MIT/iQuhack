
# # import pygame

# # class Option:

# #     hovered = False
    
# #     def __init__(self, text, pos):
# #         self.text = text
# #         self.pos = pos
# #         self.set_rect()
# #         self.draw()
            
# #     def draw(self):
# #         self.set_rend()
# #         screen.blit(self.rend, self.rect)
        
# #     def set_rend(self):
# #         self.rend = menu_font.render(self.text, True, self.get_color())
        
# #     def get_color(self):
# #         if self.hovered:
# #             return (255, 255, 255)
# #         else:
# #             return (100, 100, 100)
        
# #     def set_rect(self):
# #         self.set_rend()
# #         self.rect = self.rend.get_rect()
# #         self.rect.topleft = self.pos

# # pygame.init()
# # screen = pygame.display.set_mode((480, 320))
# # menu_font = pygame.font.Font(None, 40)
# # options = [Option("NEW GAME", (140, 105)), Option("LOAD GAME", (135, 155)),
# #            Option("OPTIONS", (145, 205))]
# # while True:
# #     pygame.event.pump()
# #     screen.fill((0, 0, 0))
# #     for option in options:
# #         if option.rect.collidepoint(pygame.mouse.get_pos()):
# #             option.hovered = True
# #         else:
# #             option.hovered = False
# #         option.draw()
# #     pygame.display.update()

# import pygame
  
# # Initializing Pygame
# pygame.init()
  
# # Initializing surface
# surface = pygame.display.set_mode((400,300))

# plus_rect = py.rect.Rect(width, 0, width, height)
# # Initialing Color
# color = (255,0,0)
  
# # Drawing Rectangle
# def draw():
#     pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
#     pygame.display.flip()


# plus_img = pygame.image.load("plus.png")
# def draw_plus():
#     surface.blit(plus_img, (20, 20))

# run = True
# now = True
# while(run):
#     if now:
#         draw_plus()
#         draw()
#         now=False
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#     pygame.display.update()

# # importing the required libraries
# import pygame as pg
# import sys
# import time
# from pygame.locals import *

# o_state=[]
# x_state=[]
# plus_state=[]
# minus_state=[]
# ooxx_state=[]
# xoox_state=[]




# # declaring the global variables

# # for storing the 'x' or 'o'
# # value as character
# XO = 'x'

# # storing the winner's value at
# # any instant of code
# winner = None

# # to check if the game is a draw
# draw = None

# # to set width of the game window
# width = 400

# # to set height of the game window
# height = 400

# # to set background color of the
# # game window
# white = (255, 255, 255)

# # color of the straightlines on that
# # white game board, dividing board
# # into 9 parts
# line_color = (0, 0, 0)

# # setting up a 3 * 3 board in canvas
# board = [[None]*3, [None]*3, [None]*3]


# # initializing the pygame window
# pg.init()

# # setting fps manually
# fps = 30

# # this is used to track time
# CLOCK = pg.time.Clock()

# # this method is used to build the
# # infrastructure of the display
# screen = pg.display.set_mode((width, height + 100), 0, 32)

# # setting up a nametag for the
# # game window
# pg.display.set_caption("My Tic Tac Toe")

# # loading the images as python object
# initiating_window = pg.image.load("modified_cover.png")
# x_img = pg.image.load("x.png")
# o_img = pg.image.load("o.png")
# plus_img=pg.image.load("plus.png")
# minus_img = pg.image.load("minus.png")
# ox_img = pg.image.load("ox.png")
# xo_img = pg.image.load("xo.png")


# # resizing images
# initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
# x_img = pg.transform.scale(x_img, (80, 80))
# o_img = pg.transform.scale(o_img, (80, 80))
# plus_img = pg.transform.scale(plus_img, (80, 80))
# minus_img = pg.transform.scale(minus_img, (80, 80))
# ox_img = pg.transform.scale(ox_img, (80, 80))
# xo_img = pg.transform.scale(xo_img, (80, 80))

# def game_initiating_window():
	
# 	# displaying over the screen
# 	screen.blit(initiating_window, (0, 0))
	
# 	# updating the display
# 	pg.display.update()
# 	time.sleep(3)					
# 	screen.fill(white)

# 	# drawing vertical lines
# 	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
# 	pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

# 	# drawing horizontal lines
# 	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
# 	pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
# 	draw_status()

# def draw_status():
	
# 	# getting the global variable draw
# 	# into action
# 	global draw
	
# 	if winner is None:
# 		message = XO.upper() + "'s Turn"
# 	else:
# 		message = winner.upper() + " won !"
# 	if draw:
# 		message = "Game Draw !"

# 	# setting a font object
# 	font = pg.font.Font(None, 30)
	
# 	# setting the font properties like
# 	# color and width of the text
# 	text = font.render(message, 1, (255, 255, 255))

# 	# copy the rendered message onto the board
# 	# creating a small block at the bottom of the main display
# 	screen.fill ((0, 0, 0), (0, 400, 500, 100))
# 	text_rect = text.get_rect(center =(width / 2, 500-50))
# 	screen.blit(text, text_rect)
# 	pg.display.update()
	
# def check_win():
# 	global board, winner, draw

# 	# checking for winning rows
# 	for row in range(0, 3):
# 		if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
# 			winner = board[row][0]
# 			pg.draw.line(screen, (250, 0, 0),
# 						(0, (row + 1)*height / 3 -height / 6),
# 						(width, (row + 1)*height / 3 - height / 6 ),
# 						4)
# 			break

# 	# checking for winning columns
# 	for col in range(0, 3):
# 		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
# 			winner = board[0][col]
# 			pg.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), \
# 						((col + 1)* width / 3 - width / 6, height), 4)
# 			break

# 	# check for diagonal winners
# 	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
		
# 		# game won diagonally left to right
# 		winner = board[0][0]
# 		pg.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)
		
# 	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
		
# 		# game won diagonally right to left
# 		winner = board[0][2]
# 		pg.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4)

# 	if(all([all(row) for row in board]) and winner is None ):
# 		draw = True
# 	draw_status()


# # def drawXO(index, image, color):
# # 	global board, XO

# # 	# changes board


# def drawXO(row, col):
# 	global board, XO
	
# 	# for the first row, the image
# 	# should be pasted at a x coordinate
# 	# of 30 from the left margin
# 	if row == 1:
# 		posx = 30
		
# 	# for the second row, the image
# 	# should be pasted at a x coordinate
# 	# of 30 from the game line	
# 	if row == 2:

# 		# margin or width / 3 + 30 from
# 		# the left margin of the window
# 		posx = width / 3 + 30
		
# 	if row == 3:
# 		posx = width / 3 * 2 + 30

# 	if col == 1:
# 		posy = 30
		
# 	if col == 2:
# 		posy = height / 3 + 30
	
# 	if col == 3:
# 		posy = height / 3 * 2 + 30
		
# 	# setting up the required board
# 	# value to display
# 	board[row-1][col-1] = XO
	
# 	if(XO == 'x'):
		
# 		# pasting x_img over the screen
# 		# at a coordinate position of
# 		# (pos_y, posx) defined in the
# 		# above code
# 		screen.blit(x_img, (posy, posx))
# 		XO = 'o'
	
# 	else:
# 		screen.blit(o_img, (posy, posx))
# 		XO = 'x'
# 	pg.display.update()

# def user_click():
#     # get coordinates of mouse click
#     x, y = pg.mouse.get_pos()
#     # get column of mouse click (1-3)
#     if(x<width / 3):
#         col = 1

#     elif (x<width / 3 * 2):
#         col = 2

#     elif(x<width):
#         col = 3

#     else:
#         col = None

#     # get row of mouse click (1-3)
#     if(y<height / 3):
#         row = 1

#     elif (y<height / 3 * 2):
#         row = 2

#     elif(y<height):
#         row = 3

#     else:
#         row = None
        
#     # after getting the row and col,
#     # we need to draw the images at
#     # the desired positions
#     if(row and col and board[row-1][col-1] is None):
#         global XO
#         drawXO(row, col)
#         check_win()
		
# def reset_game():
# 	global board, winner, XO, draw
# 	time.sleep(3)
# 	XO = 'x'
# 	draw = False
# 	game_initiating_window()
# 	winner = None
# 	board = [[None]*3, [None]*3, [None]*3]

# game_initiating_window()

# while(True):
#     mouse_buttons = pg.mouse.get_pressed()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
#         elif any(mouse_buttons):
#             user_click()
#             if(winner or draw):
#                 reset_game()
#     pg.display.update()
#     CLOCK.tick(fps)


# READ THIS

# the game sort of works, you have to add in the images for the gates
# Also, Hieu (and Linh) still wants to measure state and we can add in swap as well to make 6 gates
# The measured state is measured once and cannot be used after that, not even for applying gates (which makes it doable)
# Also, board[i][1] is the color, and I am planning to represent it as a tuple rather than index of color
# plus2o and plus2x work well, the logic of others have to improved
# I would work on hover afterwards, once the game is working


import pygame as pg
import sys
import time
from pygame.locals import *

plus2o_buttons_drawn = False
plus2x_buttons_drawn = False
cnot_button_drawn = False
swap_button_drawn = False
teleport_buttons_drawn = False
measure_button_drawn = False

width = 400
height = 400
extraheight = 200
fps = 15
running_time = pg.time.Clock()

board = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

color=1

choice_1=-1
choice_2=-1
twoq_gate=""

steps=0
gates=[]


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
plus2o_img = pg.image.load("plus2o.png")
plus2x_img = pg.image.load("minus.png")
teleport_img = pg.image.load("minus.png")
cnot_img = pg.image.load("minus.png")


# rescale window
initiating_window = pg.transform.scale(initiating_window, (width, height + extraheight))
x_img = pg.transform.scale(x_img, (90, 90))
o_img = pg.transform.scale(o_img, (90, 90))
ox_img = pg.transform.scale(ox_img, (90, 90))
xo_img = pg.transform.scale(xo_img, (90, 90))
plus_img = pg.transform.scale(plus_img, (90, 90))

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(0.1)
    screen.fill((255, 255, 255))
    pg.display.update()

    # draw the tic tac toe lines
    pg.draw.line(screen, (0, 0, 0), (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, (0, 0, 0), (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height / 3 * 2), (width, height / 3 * 2), 7)
    pg.draw.line(screen, (0, 0, 0), (0, height), (width, height), 9)
    pg.draw.line(screen, (0,0,0), (width/3 , height), (width/3 , height+extraheight), 7)
    pg.draw.line(screen, (0,0,0), (width/3*2 , height), (width/3*2 , height+extraheight), 7)
    pg.draw.line(screen, (0,0,0), (0 , height+extraheight/2), (width , height+extraheight/2), 7)

    pg.display.update()

    # sleep for 1 seconds
    time.sleep(0.1)

    # add in the initial board
    for i in range(9):
        draw_img(i, "ox", (255, 255, 255))
        for t in board:
            t[0]="ox"
            t[1]= (255, 255, 255)


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

    pg.draw.rect(screen, color, pg.Rect(posx-15, posy-15, 125, 125))
    screen.blit(commit_img, (posx, posy))

    # TBD, update the background color of the cell

    pg.display.update()

# TBD: draw_button and clear
def draw_button(gate, hovered=False):
    print(draw_button)
    if gate=="plus2o":
        btn_img = plus2o_img
        btn_coords = (0, height)
        plus2o_buttons_drawn = True
    elif gate=="plus2x":
        btn_img = plus2x_img
        btn_coords = (width/3, height)
        plus2x_buttons_drawn = True
    elif gate=="cnot":
        btn_img = cnot_img
        btn_coords = (width/3*2, height)
        cnot_button_drawn = True
    elif gate=="teleport":
        btn_img = teleport_img
        btn_coords = (0, height+extraheight/2)
        teleport_buttons_drawn = True
    if not hovered:
        btn_bg_color = (150, 150, 0)
    else:
        btn_bg_color = (200, 200, 0)
    pg.draw.rect(screen, btn_bg_color, pg.Rect(btn_coords[0]+5, btn_coords[1]+5, 90, 90))
    screen.blit(btn_img, (btn_coords[0], btn_coords[1]))


def clear(gate=None):
    if gate == None:
        btn_coords = (0, height)
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(btn_coords[0], btn_coords[1]+5, width, extraheight))
        plus2o_buttons_drawn = False
        plus2x_buttons_drawn = False
        cnot_button_drawn = False
        teleport_buttons_drawn = False
        measure_button_drawn = False
        swap_button_drawn = False
    pg.display.update()


## moves
def plus2o(i):
    global gates, steps
    if board[i][0]=="ox" and board[i][1]==(255, 255, 255):
        board[i][0]="o"
        draw_img(i,"o", (255, 255, 255))
        steps+=1
        gates+=[("hadamard", i)]
    else:
        return False

def plus2x(i):
    global gates, steps
    if board[i][0]=="ox" and board[i][1]==(255, 255, 255):
        board[i][0]="x"
        draw_img(i,"x", (255, 255, 255))
        steps+=1
        gates+= [("sigmaz", i),("hadamard", i)]

def teleport(i,j):
    global gates, steps
    board[i]=["ox",(255,255,255)]
    board[j]=board[i][:]
    draw_img(i,board[i][0],board[i][1])
    draw_img(j,board[j][0], board[j][1])
    steps+=1
    gates+= [("teleport",i,j)]

def flip_(state):
    if state=="o": return "x"
    elif state=="x": return "o"
    elif state=="ox": return "xo"
    elif state=="xo": return "ox"

def cnot(i,j):
    global color, gates, steps
    print("cnot", i, j)
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
        steps+=1
        gates+= [("cnot",i,j)]
    return False



## handle user click
def user_click():
    global choice_1, twoq_gate, choice_2
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    print("position",x,y)
    print("choice_1", choice_1, "choice_2", choice_2)
    print("twoq_gate", twoq_gate)
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
            i=(col-1)+(row-1)*3
            print(i)
            if not twoq_gate:
                choice_1=i
                if len(board[i][0])==1:
                    draw_img(i,board[i][0], board[i][1])
                    twoq_gate=True
                    draw_button("plus2o")
                    draw_button("plus2x")
                    draw_button("cnot")
                    draw_button("teleport")
                else:
                    draw_button("plus2o")
                    draw_button("plus2x")
                    draw_button("teleport")
            elif choice_1>=0:
                print("twoq",twoq_gate)
                if twoq_gate=="teleport":
                    teleport(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1
                elif twoq_gate=="cnot":
                    print("entered cnot", choice_1, choice_2)
                    cnot(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1


    else:
        if y<height+extraheight/2:
            if(x<width / 3) and choice_1>=0:
                plus2o(choice_1)
                clear()
                choice_1=-1
            elif (x<width / 3 * 2):
                plus2x(choice_1)
                clear()
                choice_1=-1
            elif(x<width / 4 * 3):
                twoq_gate="cnot"
                print("pressed cnot")
            else:
                twoq_gate="teleport"


# TODO: send sequence of moves to backend
def send(): pass

def draw_res(res): 
    for i,r in enumerate(res):
        if r==0:
            draw_img(i,"o",0)
        else:
            draw_img(i,"x",0)
# TBD improve draw status to give message at each point of the game
def draw_status(winner):
	
	# getting the global variable draw
	# into action
	global draw
	
	if winner!="draw":
		message = winner + " won !"
	else:
		message = "Game Draw !"

def hover_over():
    x, y = pg.mouse.get_pos()

    if y<height+extraheight/2:
        if(x<width / 3) and (plus2o_buttons_drawn):
            draw_button("plus2o", True)
        elif (x<width / 3 * 2):
            plus2x(choice_1)
            clear()
            choice_1=-1
        elif(x<width / 4 * 3):
            twoq_gate="cnot"
            print("pressed cnot")
        else:
            twoq_gate="teleport"

	# setting a font object
	font = pg.font.Font(None, 30)
	
	# setting the font properties like
	# color and width of the text
	text = font.render(message, 1, (255, 255, 255))

	# copy the rendered message onto the board
	# creating a small block at the bottom of the main display
	screen.fill ((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center =(width / 2, 500-50))
	screen.blit(text, text_rect)
	pg.display.update()

def check_winner(res):
    cnts=[0,0]
    def check(i,j,k):
        if res[i]==res[j]==res[k]:
            if res[0]=="o":
                cnts[0]+=1
            else:
                cnts[1]+=1
    for i in range(3):
        check(i,i+3,i+3)
        check(i*3,i*3+1,i*3+2)
    check(0,4,8)
    check(2,4,6)

    if cnts[0]==cnts[1]:
        draw_status("draw")
    elif cnts[0]>cnts[1]:
        draw_status("o")
    else:
        draw_status("x")


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
        elif steps>9:
            res=send(gates)
            draw_res(res)
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("drawing")
            user_click()
    hover_over()
    
    pg.display.update()
    running_time.tick(fps)


