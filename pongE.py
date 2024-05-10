#Author: Talent Koronya
#Date: 11/10/2023
# Purpose : Pong game
from cs1lib import *

WIN_HEIGHT=400
WIN_WIDTH=400
HEIGHT=80
WIDTH=20
OFFSET=2
BALLSIZE=7
GAMESTART=" "
QUIT = "q"
LEFT_UP = "a"
LEFT_DOWN = "z"
RIGHT_UP = "k"
RIGHT_DOWN = "m"
leftvalup = False
leftvaldwn = False
rightvalup = False
rightvaldwn = False
changex=0
changey=0
ly=160
ry=160
bx=200
by=200
def draw_background():
    set_clear_color(0,0,0)
    clear()

def draw_lpaddle(y):
    set_fill_color(0, 1, 1)
    draw_rectangle(0,y,WIDTH,HEIGHT)

def draw_rpaddle(y):
    set_fill_color(0,1,1)
    draw_rectangle(WIN_WIDTH-WIDTH,y,WIDTH,HEIGHT)

def k_press(x):
    global ly, ry,leftvaldwn,rightvaldwn,leftvalup,rightvalup,changex,changey
    if x==LEFT_DOWN and changey!=0:
        leftvaldwn=True
    if x == LEFT_UP and changey!=0:
        leftvalup = True
    if x == RIGHT_DOWN and changey!=0:
        rightvaldwn = True
    if x == RIGHT_UP and changey!=0:
        rightvalup = True
    if x==QUIT:
        cs1_quit()
    if x== " " and changey == 0 and changex == 0:
        changex = 1
        changey = 1

def draw_ball(x,y):
    draw_circle(x,y,BALLSIZE)



def k_release(value):
    global ly, ry,leftvaldwn,rightvaldwn,leftvalup,rightvalup
    if value==LEFT_DOWN:
        leftvaldwn = False
    if value == LEFT_UP:
        leftvalup = False
    if value == RIGHT_DOWN:
       rightvaldwn= False
    if value == RIGHT_UP:
        rightvalup= False

def reset_ball():
    global bx, by, changex, changey,ly, ry
    changey=0
    changex=0
    bx=200
    by=200
    ly = 160
    ry = 160


def ball_move():
    global bx,by, changex,changey
    bx=bx+changex
    by=by+changey
    if bx==WIN_WIDTH-(WIDTH+BALLSIZE) and by-ry<=HEIGHT:
        changex=-1
    if bx==(WIDTH+BALLSIZE) and by-ly<=HEIGHT:
        changex=1
    if by==400-BALLSIZE:
        changey=-1
    if by == BALLSIZE:
        changey = 1
    if bx==0 or bx==WIN_WIDTH:
        reset_ball()

def my_draw():
    global ly,ry
    draw_background()
    draw_rpaddle(ry)
    draw_lpaddle(ly)
    draw_ball(bx,by)
    ball_move()

    if leftvalup==True and rightvalup==True:
        if ly>0:
            ly = ly - OFFSET
        if ry>0:
            ry = ry - OFFSET
    if leftvalup==True and rightvaldwn==True:
        if ly>0:
            ly = ly - OFFSET
        if ry<(400-HEIGHT):
            ry = ry + OFFSET
    if leftvaldwn==True and rightvalup==True:
        if ly<(400-HEIGHT):
            ly = ly + OFFSET
        if ry>0:
            ry = ry - OFFSET
    if leftvaldwn==True and rightvaldwn==True:
        if ly<(400-HEIGHT):
            ly = ly + OFFSET
        if ry < (400 - HEIGHT):
            ry = ry + OFFSET
    if rightvalup== True and leftvalup==False and leftvaldwn==False and ry>0:
        ry = ry - OFFSET
    if rightvaldwn == True and leftvalup==False and leftvaldwn==False and ry<(400-HEIGHT):
        ry = ry + OFFSET
    if leftvalup== True and rightvalup==False and rightvaldwn==False and ly>0:
        ly = ly - OFFSET
    if leftvaldwn == True and rightvalup==False and rightvaldwn==False and ly<(400-HEIGHT):
        ly = ly + OFFSET



start_graphics(my_draw,key_press=k_press,height=WIN_HEIGHT,width=WIN_WIDTH,key_release=k_release, framerate=100)
