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


width = 400
height = 400
extraheight = 200
textboxheight = 100
fps = 15
running_time = pg.time.Clock()

MEASURE_COLOR=(43,43,43)
colors=[(255,255,255),(236,224,209),(145,116,103),(166,197,224),(170,195,147)]

board = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

color=1

choice_1=-1
choice_2=-1
twoq_gate=""

steps=0
gates=[]


pg.init()

screen = pg.display.set_mode((width, height + extraheight + textboxheight), 0, 32)
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
initiating_window = pg.transform.scale(initiating_window, (width, height + extraheight + textboxheight))
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
    elif gate=="plus2x":
        btn_img = plus2x_img
        btn_coords = (width/3, height)
    elif gate=="cnot":
        btn_img = cnot_img
        btn_coords = (width/3*2, height)
    elif gate=="teleport":
        btn_img = teleport_img
        btn_coords = (0, height+extraheight/2)
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
    elif gate=="plus2o":
        btn_coords = (0, height)
    elif gate=="plus2x":
        btn_coords = (width/4, height)
    elif gate=="cnot":
        btn_coords = (width/4*2, height)
    elif gate=="teleport":
        btn_coords = (width/4*3, height)
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(btn_coords[0]+5, btn_coords[1]+5, 90, 90))

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

def measure(i):
    global gates
    board[i]=["",MEASURE_COLOR]
    gates+=[("measure",i)]

def swap(i,j):
    global gates
    board[i],board[j]=board[j][:], board[j][:]
    gates+=[("swap",i,j)]

def flip_(state):
    if state=="o": return "x"
    elif state=="x": return "o"
    elif state=="ox": return "xo"
    elif state=="xo": return "ox"

def cnot(j,i):
    global color, gates, steps
    print("cnot", i, j)
    print(board[j])
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
            if board[i][1]==(255,255,255):
                board[i][1]=colors[color]
                board[j][1]=colors[color]
                color+=1
                draw_img(i,board[i][0], board[i][1])
            else:
                board[j][1]=board[i][1][:]
        print("draw_img", board[j])
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
                choice_2=i
                print("twoq",twoq_gate)
                if twoq_gate=="teleport":
                    teleport(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1
                    twoq_gate=""
                elif twoq_gate=="cnot":
                    print("entered cnot", choice_1, choice_2)
                    cnot(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1
                    twoq_gate=""
                elif twoq_gate=="swap":
                    swap(choice_1,choice_2)
                    clear()
                    choice_1=-1
                    choice_2=-1
                    twoq_gate=""


    elif choice_1>=0:
        if y<height+extraheight/2:
            if(x<width / 3):
                plus2o(choice_1)
                clear()
                choice_1=-1
            elif (x<width / 3 * 2):
                plus2x(choice_1)
                clear()
                choice_1=-1
            else:
                twoq_gate="cnot"
                print("pressed cnot")
        else:
            if(x<width / 3):
                twoq_gate="teleport"
                print("click teleport")
            elif (x<width /3*2):
                measure(choice_1)
                clear()
                choice_1=-1
            else:
                twoq_gate="swap"
                print("click swap")


# TODO: send sequence of moves to backend
def send(): pass

def draw_res(res): 
    for i,r in enumerate(res):
        if r==0:
            draw_img(i,"o",0)
        else:
            draw_img(i,"x",0)
# TBD improve draw status to give message at each point of the game

def update_message(message):
    global message_text
    message_text=message
    print("message_text", message_text)

def draw_status(winner):
	
	# getting the global variable draw
	# into action
	global draw
	
	if winner!="draw":
		message = winner + " won !"
	else:
		message = "Game Draw !"

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
    
    pg.display.update()
    running_time.tick(fps)
