import pygame, sys, os, time
from pygame.locals import *

class Board:

    def __init__(self,h,w):                 #initialise all the board variables like cell size , height ,
        pygame.init()                       # width , screen window for the game
        self.board = []
        self.height = h
        self.width = w
        self.board = [[" " for j in range(self.width)]for i in range(self.height)]
        self.screen = pygame.display.set_mode((self.height*20+40,self.width*20-40),0,32)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,105,125))

    def fillPiecePos(self,color):           # colour the pieces of all filled pieces with the
        self.screen.lock()                  # corresponding colour
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == "s" or self.board[i][j] == "m":
                    pygame.draw.rect(self.screen,color,Rect((j*20,i*20),(18,18)))
        pygame.display.update()
        self.screen.unlock()

    def removePrevPieces(self):                # clear up all the previous positions
        for i in range(self.height):            # of the block and moves to next position
            for j in range(self.width):         # based in given instruction
                if self.board[i][j] == "m":
                    self.board[i][j] = " "

    def checkPiecePos(self,block_obj,fig,config):   # checks for the movement of the block
        for elem in block_obj.drawFig(fig,config):  # for all sub blocks if any locks or not
            row, col = elem
            if self.board[row+1][col] == "s":
                return 0
        return 1
