"""This module initialises & implements all the functionalities
    of a tetris game board"""

import pygame

from pygame.locals import Rect


class Board(object):

    """ This class has all the methods to initialise
        & implement all the functionalities of a board"""

    def __init__(self, h, w):

        """initialise all the board variables like cell size, height,
            width, screen window for the game"""

        self.board = []
        self.height = h
        self.width = w
        self.board = [[" " for j in range(self.width)]for i in range(self.height)]

    def initialise(self):

        """ This initialises the game board with graphics rendered """

        self.screen = pygame.display.set_mode((self.height * 20+40,
                                               self.width * 20-40))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 105, 125))

    def fillpiecepos(self, color):

        """This method colours the pieces of all
            filled pieces with the corresponding color"""

        self.screen.lock()
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == "s" or self.board[i][j] == "m":
                    pygame.draw.rect(self.screen, color,
                                     Rect((j * 20, i * 20),
                                          (18, 18))
                                    )
        pygame.display.update()
        self.screen.unlock()

    def removeprevpieces(self):

        """ This method clears up all the previous positions
            of the block and moves to next position
            based in given instruction """

        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == "m":
                    self.board[i][j] = " "

    def checkpiecepos(self, block_obj, fig, config):

        """ This method checks for the movement of the block
            for all sub blocks if any locks or not"""

        for elem in block_obj.drawfig(fig, config):
            row, col = elem
            if self.board[row + 1][col] == "s":
                return 0

        return 1
