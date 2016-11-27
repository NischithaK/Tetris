""" This module tests the functionalities
    of a falling block """
import sys

import os

path = str(os.getcwd())+str("/pkg")
sys.path.append(path)

from random import randint

import pygame

import BlockClass

import BoardClass

class Test_block(object):

    """This class defines all the methods
        for testing falling block """

    def test_left(self):

        """ This method test for a block can it move
            left in all possible cases """

        self.board_obj = BoardClass.Board(30, 32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2, self.board_obj.width/2)
        self.piece = randint(1, 5)
        self.piececonfig = randint(0, 3)

        previous = []
        for ordinates in self.block_obj.drawfig(self.piece, self.piececonfig):
            row, col = ordinates
            previous.append(ordinates)
            self.board_obj.board[row][col] = "m"

        movl = self.block_obj.moveleft(self.board_obj, self.piece, self.piececonfig)
        self.board_obj.removeprevpieces()
        self.block_obj.x_ordinate += movl

        present = []
        for ordinates in self.block_obj.drawfig(self.piece, self.piececonfig):
            row, col = ordinates
            present.append(ordinates)

        for i in range(len(present)):
            assert present[i][0]-previous[i][0] == -1

    def test_right(self):

        """ This method test for a block can it move right
            in all possible cases """

        self.board_obj = BoardClass.Board(30, 32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2, self.board_obj.width/2)
        self.piece = randint(1, 5)
        self.piececonfig = randint(0, 3)

        previous = []
        for ordinates in self.block_obj.drawfig(self.piece, self.piececonfig):
            row, col = ordinates
            previous.append(ordinates)
            self.board_obj.board[row][col] = "m"

        movr = self.block_obj.moveright(self.board_obj,self.piece,self.piececonfig)
        self.board_obj.removeprevpieces()
        self.block_obj.x_ordinate += movr

        present = []
        for ordinates in self.block_obj.drawfig(self.piece,self.piececonfig):
            row, col = ordinates
            present.append(ordinates)

        for i in range(len(present)):
            assert present[i][0] - previous[i][0] == 1

    def test_rotate(self):

        """ This method test for a block can it roate
            clockwise in all possible cases """

        self.board_obj = BoardClass.Board(30, 32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2, self.board_obj.width/2)
        self.piece = randint(1, 5)
        self.pieceprevconfig = randint(0, 3)

        previous = []
        for ordinates in self.block_obj.drawfig(self.piece, self.pieceprevconfig):
            row, col = ordinates
            self.board_obj.board[row][col] = "m"

        if (self.block_obj.rotatecheck(self.board_obj,
                                       self.piece,
                                       self.pieceprevconfig) == 1):
            self.piecefutconfig = (self.pieceprevconfig + 1) % 4

        self.board_obj.removeprevpieces()
        self.rotatedblock = BlockClass.Block(self.block_obj.x_ordinate,self.block_obj.y_ordinate)

        for ordinates in self.rotatedblock.drawfig(self.piece,self.piecefutconfig):
            previous.append(ordinates)

        present = []
        for ordinates in self.block_obj.drawfig(self.piece,self.piecefutconfig):
            row, col = ordinates
            present.append(ordinates)

        assert present == previous
