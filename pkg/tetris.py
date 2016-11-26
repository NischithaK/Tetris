#!/usr/bin/python

""" This actually runs the game by importing all
    the classes and methods """

import GamePlayClass

import BoardClass

import BlockClass

if __name__ == "__main__":
                              # game starts to run
    GAMEBOARD = BoardClass.Board(30, 32)
    GAMEBOARD.initialise()
    START_THE_GAME = GamePlayClass.Gameplay(0)
    BLOCK_PIECE = BlockClass.Block(0, GAMEBOARD.width/2)
    START_THE_GAME.runthegame(GAMEBOARD, BLOCK_PIECE)
