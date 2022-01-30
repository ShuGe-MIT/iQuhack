# READ THIS

# the game sort of works, you have to add in the images for the gates
# Also, Hieu (and Linh) still wants to measure state and we can add in swap as well to make 6 gates
# The measured state is measured once and cannot be used after that, not even for applying gates (which makes it doable)
# Also, board[i][1] is the color, and I am planning to represent it as a tuple rather than index of color
# plus2o and plus2x work well, the logic of others have to improved
# I would work on hover afterwards, once the game is working


from matplotlib.pyplot import draw
import pygame as pg
import sys
import time
from pygame.locals import *
from backend import *


width = 400
height = 400
extraheight = 200
textboxheight = 80
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
empty_img=pg.image.load("empty.png")
plus2x_img = pg.image.load("plus2x.png")
teleport_img = pg.image.load("teleport.png")
cnot_img = pg.image.load("cnot.png")
measure_img = pg.image.load("measure.png")
swap_img = pg.image.load("swap.png")


# rescale window
initiating_window = pg.transform.scale(initiating_window, (width, height + extraheight + textboxheight))
x_img = pg.transform.scale(x_img, (90, 90))
o_img = pg.transform.scale(o_img, (90, 90))
ox_img = pg.transform.scale(ox_img, (90, 90))
xo_img = pg.transform.scale(xo_img, (90, 90))
plus_img = pg.transform.scale(plus_img, (90, 90))
empty_img =  pg.transform.scale(empty_img,(90,90))

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
    pg.draw.line(screen, (0, 0, 0), (0, height+extraheight), (width, height+extraheight), 9)

    pg.display.update()

    # sleep for 1 seconds
    time.sleep(0.1)

    # add in the initial board
    for i in range(9):
        draw_img(i, "ox", (255, 255, 255))
        for t in board:
            t[0]="ox"
            t[1]= (255, 255, 255)
    
    update_message("Welcome to Quantum Tic Tac Toe")


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
    elif img=="":
        commit_img=empty_img


    pg.draw.rect(screen, color, pg.Rect(posx-15, posy-15, 125, 125))
    screen.blit(commit_img, (posx, posy))

    # TBD, update the background color of the cell

    pg.display.update()

# TBD: draw_button and clear
def draw_button(gate, hovered=False):
    print("draw_button", gate)
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
    elif gate=="measure":
        btn_img = measure_img
        btn_coords = (width/3, height+extraheight/2)
    elif gate=="swap":
        btn_img = swap_img
        btn_coords = (width/3*2 , height+extraheight/2)
    if not hovered:
        btn_bg_color = (150, 150, 0)
    else:
        btn_bg_color = (200, 200, 0)
    pg.draw.rect(screen, btn_bg_color, pg.Rect(btn_coords[0]+4, btn_coords[1]+4, 125, 90))
    screen.blit(btn_img, (btn_coords[0], btn_coords[1]))


def clear():
    coords=[(0,height),(width/3, height),(width/3*2,height),(0, height+extraheight/2),(width/3, height+extraheight/2), (width/3*2 , height+extraheight/2)]
    for btn_coords in coords:
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(btn_coords[0]+4, btn_coords[1]+4, 125, 90))
    pg.display.update()


## moves
def plus2o(i):
    global gates, steps
    if board[i][0]=="ox" and board[i][1]==(255, 255, 255):
        board[i][0]="o"
        print("set i to 0", board[i][0])
        draw_img(i,board[i][0], board[i][1])
        steps+=1
        gates+=[("hadamard", i)]
    else:
        return False

def plus2x(i):
    global gates, steps
    if board[i][0]=="ox" and board[i][1]==(255, 255, 255):
        board[i][0]="x"
        draw_img(i,board[i][0], board[i][1])
        steps+=1
        gates+= [("sigmaz", i),("hadamard", i)]
    else:
        return False

def teleport(i,j):
    global gates, steps
    if board[i][0]!="" and board[j][0]!="":
        for idx,b in enumerate(board):
            if idx!=i and idx!=j and b[1]==board[j][1] and board[j][1]!=(255, 255, 255):
                board[idx]=["",MEASURE_COLOR]
                draw_img(idx,board[idx][0], board[idx][1])
        board[j]=board[i][:]
        board[i]=["",MEASURE_COLOR]
        draw_img(i,board[i][0],board[i][1])
        draw_img(j,board[j][0], board[j][1])
        steps+=1
        gates+= [("teleport",i,j)]

def measure(i):
    global gates
    if board[i][0]!="":
        if board[i][1]!=(255,255,255):
            for idx,b in enumerate(board):
                if idx!=i and b[1]==board[i][1]:
                    board[idx]=["",MEASURE_COLOR]
                    draw_img(idx,board[idx][0], board[idx][1])
        board[i]=["",MEASURE_COLOR]
        draw_img(i, board[i][0], board[i][1])
        gates+=[("measure",i)]

def swap(i,j):
    global gates
    if board[i][0]!="" and board[j][0]!="":
        board[i],board[j]=board[j][:], board[i][:]
        gates+=[("swap",i,j)]
        draw_img(i,board[i][0], board[i][1])
        draw_img(j,board[j][0], board[j][1])

def flip_(state):
    if state=="o": return "x"
    elif state=="x": return "o"
    elif state=="ox": return "xo"
    elif state=="xo": return "ox"

def cnot(j,i):
    global color, gates, steps
    if board[i][0]!="" and board[j][0]!="":
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
                if board[i]==["ox",(255,255,255)]:
                    # draw_img(i,board[i][0], board[i][1])
                    draw_button("plus2o")
                    draw_button("plus2x")
                    draw_button("teleport")
                    draw_button("measure")
                    draw_button("swap")
                elif board[i][0]=="o" or board[i][0]=="x":
                    draw_button("cnot")
                    draw_button("teleport")
                    draw_button("measure")
                    draw_button("swap")
                elif board[i][0]!="":
                    draw_button("teleport")
                    draw_button("measure")
                    draw_button("swap")
                    
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
def send(gates): 
    qc = instruction(gates)
    print('------------------------------')
    print('This is gates: ', gates)
    print('------------------------------')
    mes_qb = get_measured_qubit(qc)
    print('------------------------------')
    print('This is mes_qb: ', mes_qb)
    print('------------------------------')
    result = qc.simulate(1)
    print('------------------------------')
    print('This is result: ', result)
    record = get_the_final_state(result)
    print('------------------------------')
    print('This is record: ', record)
    print('------------------------------')

    return record

def draw_res(res): 
    for i,r in enumerate(res):
        if r==0:
            draw_img(i,"o",(255,255,255))
        else:
            draw_img(i,"x",(255,255,255))
    check_winner(res)
# TBD improve draw status to give message at each point of the game

def update_message(message):
    global message_text
    message_text=message
    font = pg.font.SysFont('Arial', 20)
    text = font.render(message_text, True, (255, 105, 205))
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, height+extraheight,width, textboxheight))
    text_rect = text.get_rect(center = (width/2, height+extraheight+textboxheight/2))
    screen.blit(text, text_rect)
    pg.display.update()

def draw_status(winner):
    global draw

    if winner!="draw":
        mes = winner + " wins!"
    else:
        mes = "Game Draw!"
    update_message(mes)


def check_winner(res):
    cnts=[0,0]
    print("this is res", res)
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
        print("draw")
        draw_status("draw")
    elif cnts[0]>cnts[1]:
        print("o wins")
        draw_status("o")
    else:
        print("x wins")
        draw_status("x")


# run the game
# initiate the game
game_initiating_window()

def check_done():
    cnt=0
    for b in board:
        if b[0]=="":
            cnt+=1
    return cnt==9

run = True
while(run):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
        elif check_done():
            res=send(gates)
            print("this is res", res)
            draw_res(res)
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("drawing")
            user_click()
    
    pg.display.update()
    running_time.tick(fps)