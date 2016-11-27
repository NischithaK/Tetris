""" This module tests the functionalities of the game board """

import sys

import os

path = str(os.getcwd())+str("/pkg")
sys.path.append(path)

from random import randint

import BlockClass

import BoardClass

class Test_board(object):

    """ This contains methods to test for
        board functionalities """

    def test_removepieces(self):

        self.board_obj = BoardClass.Board(30,32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2,self.board_obj.width/2)
        self.piece = randint(1,5)
        self.config = randint(0,3)

        for ordinates in self.block_obj.drawfig(self.piece,self.config):
            row, col = ordinates
            self.board_obj.board[row][col] = "m"

        self.board_obj.removeprevpieces()

        for ordinates in self.block_obj.drawfig(self.piece,self.config):
            row, col = ordinates
            assert self.board_obj.board[row][col] == " "

    def test_checkpiece(self):

        self.board_obj = BoardClass.Board(30,32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2,self.board_obj.width/2)
        self.piece = 1
        self.config = 0

        for i in range(self.board_obj.width):
            self.board_obj.board[self.board_obj.height/2 - 1][i] = "s"
            self.board_obj.board[self.board_obj.height/2 + 1][i] = "s"

        for ordinates in self.block_obj.drawfig(self.piece,self.config):
            row, col = ordinates
            self.board_obj.board[row][col] = "m"

        assert self.board_obj.checkpiecepos(self.block_obj,self.piece,self.config) == 0
