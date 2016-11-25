#!/usr/bin/python

""" This module has defines all the properties &
    functionalities that a falling possess block. """

class Block(object):

    """ This class defines all the methods,
        shapes required for as blocks in tetris game """

    def __init__(self, x_ordinate, y_ordinate):       #initialises block base point

        self.x_ordinate = x_ordinate
        self.y_ordinate = y_ordinate

    def movetheblock(self, dis):         # moves the base point of the block

        """ This method changes the co-ordinates block as per the user requests """

        self.y_ordinate += dis
        self.x_ordinate += 1

    def botblock(self, piece, config):

        """ This method return the co-ordinates of the bottom side of the falling block """

        if piece == 1:        # this kind of block  ####  gives all the four bottom points

            if config == 0:
                return self.x_ordinate

            if config == 1:
                return self.x_ordinate + 3

            if config == 2:
                return self.x_ordinate

            if config == 3:
                return self.x_ordinate + 3

        if piece == 2:     # this kind of block  ###  gives all the four bottom points
                                                 #
            if config == 0:
                return self.x_ordinate + 1

            if config == 1:
                return self.x_ordinate + 2

            if config == 2:
                return self.x_ordinate + 1

            if config == 3:
                return self.x_ordinate + 2

        if piece == 3:     # this kind of block  ##  gives all the four bottom points
                                                  ##
            if config == 0 or config == 2:
                return self.x_ordinate + 1

            if config == 1 or config == 3:
                return self.x_ordinate + 2

        if piece == 4:           # this kind of block  ##  gives all four bottom points
            if (config == 0 or                         ##
                    config == 1 or
                    config == 2 or
                    config == 3):
                return self.x_ordinate + 1

        if piece == 5:         # this kind of block  ###  gives all four bottom points
                                                       #
            if config == 0:
                return self.x_ordinate + 1

            if config == 1:
                return self.x_ordinate + 2

            if config == 2:
                return self.x_ordinate + 1

            if config == 3:
                return self.x_ordinate + 2

    def moveleft(self, board_obj, piece, piece_config):

        """ This method moves the block left if there is no obstacle """

        for elem in self.drawfig(piece, piece_config):
            row, col = elem
            #checks for possibility of moving block left return -1 if true else 0
            if (col > 0 and
                    board_obj.board[row + 1][col - 1] == "s"):
                return 0

            if col <= 0:
                return 0
        return -1

    def moveright(self, board_obj, piece, piece_config):

        """ This method moves the block right if there is no obstacle """

        for elem in self.drawfig(piece, piece_config):
            row, col = elem

            if (col < board_obj.width - 1 and
                    board_obj.board[row + 1][col + 1] == "s"):
                    #checks for possibility of moving right return 1 if true else 0
                return 0

            if col >= board_obj.width - 1:
                return 0
        return 1

    def drawfig(self, piecetype, config):

        """ This method gives the co-ordinates of the block at a particular instance """

        if piecetype == 1:

            if config == 0:                        # this figure ####
                return ((self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate + 1),
                        (self.x_ordinate, self.y_ordinate + 2))

            if config == 1:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate),
                        (self.x_ordinate + 3, self.y_ordinate))

            if config == 2:
                return ((self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate + 1),
                        (self.x_ordinate, self.y_ordinate + 2))

            if config == 3:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate),
                        (self.x_ordinate + 3, self.y_ordinate))

        if piecetype == 2:                # this figure ###
                                                                 #
            if config == 0:
                return ((self.x_ordinate, self.y_ordinate-1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate + 1))

            if config == 1:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate))

            if config == 2:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1),
                        (self.x_ordinate + 1, self.y_ordinate + 1))

            if config == 3:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate + 1))

        if piecetype == 3:                  # this figure ##
            if config == 0:                                         ##
                return ((self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate + 1))

            if config == 1:
                return ((self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1),
                        (self.x_ordinate + 2, self.y_ordinate - 1))
            if config == 2:
                return ((self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate + 1))

            if config == 3:
                return ((self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1),
                        (self.x_ordinate + 2, self.y_ordinate - 1))

        if piecetype == 4:              # this figure ##
                                                               ##
            if (config == 0 or
                    config == 1 or
                    config == 2 or
                    config == 3):
                return ((self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1))

        if piecetype == 5:               # this fugure ###
                                                                  #
            if config == 0:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate + 1),
                        (self.x_ordinate, self.y_ordinate + 2))

            if config == 1:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate, self.y_ordinate - 1),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate))

            if config == 2:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate - 1),
                        (self.x_ordinate + 1, self.y_ordinate - 2))

            if config == 3:
                return ((self.x_ordinate, self.y_ordinate),
                        (self.x_ordinate + 1, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate),
                        (self.x_ordinate + 2, self.y_ordinate + 1))

    def rotatecheck(self, board_obj, piece, piececonfig):

        """ This method rotates the falling block if there is no obstacle """

        for elem in self.drawfig(piece, (piececonfig + 1) % 4):
            row, col = elem
            if (row > board_obj.height - 1 or
                    col > board_obj.width - 1 or
                    board_obj.board[row][col] == "s"):
                    # checks for possibility of rotate returns 1 if true else 0
                return 0
        return 1
