import pygame as pg,sys
from pygame.locals import *
import time

#initialize global variables
XO = 'x'                        #Default value is 'x'
winner = None
draw = False
width = 350
height = 350
white = (255, 255, 255)
line_color = (10,10,10)

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]
