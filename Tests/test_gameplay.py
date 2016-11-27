""" This module tests for the possible cases
    that can happen in a tetris game play """

import sys

import os

path = str(os.getcwd())+str("/pkg")
sys.path.append(path)

from random import randint

import pygame

import BoardClass

import BlockClass

import GamePlayClass


class Test_gameplay(object):


    """ This class has all the methods to check for
        score_updation, score_bonus, remove a row(when
        filled completely), proper ending of the game """

    def test_scoreupdate(self):

        """ This method updates test the score is
            updating properly when block has fallen """

        self.board_obj = BoardClass.Board(30,32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2,self.board_obj.width/2)
        self.game_obj = GamePlayClass.Gameplay(0)
        self.piece = randint(1,5)
        self.piececonfig = randint(0,3)

        while not self.block_obj.botblock(self.piece,self.piececonfig) == self.board_obj.height-1:
            self.block_obj.movetheblock(0)

        self.game_obj.updatescore()

        assert self.game_obj.gamescore() == 10

    def test_scorebonus(self):

        """ This method updates bonus when a row
            is completely filled by the blocks """

        self.board_obj = BoardClass.Board(30,32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2,self.board_obj.width/2)
        self.game_obj = GamePlayClass.Gameplay(0)
        self.piece = randint(1,1)
        self.piececonfig = randint(1,1)

        for i in range(self.board_obj.width):
            self.board_obj.board[self.board_obj.height-1][i] = "s"
        self.board_obj.board[self.board_obj.height-1][self.board_obj.width/2] = " "

        while not self.block_obj.botblock(self.piece,self.piececonfig) == self.board_obj.height-1:
            self.block_obj.movetheblock(0)

        for ordinates in self.block_obj.drawfig(self.piece,self.piececonfig):
            row, col = ordinates
            self.board_obj.board[row][col] = "s"
        self.game_obj.checkrowfull(self.board_obj)

        assert self.game_obj.gamescore() == 100

    def test_rowclear(self):

        """ This method tests whether the row is getting cleared
            when it is completely filled """
        self.board_obj = BoardClass.Board(30,32)
        self.block_obj = BlockClass.Block(self.board_obj.height/2,self.board_obj.width/2)
        self.game_obj = GamePlayClass.Gameplay(0)
        self.piece = randint(1,1)
        self.piececonfig = randint(1,1)

        for i in range(self.board_obj.width):
            self.board_obj.board[self.board_obj.height-1][i] = "s"
        self.board_obj.board[self.board_obj.height-1][self.board_obj.width/2] = " "

        while not self.block_obj.botblock(self.piece,self.piececonfig) == self.board_obj.height-1:
            self.block_obj.movetheblock(0)

        for ordinates in self.block_obj.drawfig(self.piece,self.piececonfig):
            row, col = ordinates
            self.board_obj.board[row][col] = "s"
        self.game_obj.checkrowfull(self.board_obj)

        for ordinates in self.block_obj.drawfig(self.piece,self.piececonfig):
            row, col = ordinates
            if col == self.board_obj.width/2:
                continue
            assert self.board_obj.board[row][col] == " "
