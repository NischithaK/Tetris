""" This module imports all the methods from BoardClass,
    BlockClass and implements the tetris gameplay """

import sys

import time

from random import randint

import pygame

import BoardClass

import BlockClass


class Gameplay(BoardClass.Board, BlockClass.Block):

    """ This module uses the methods of all the other inhertied
        classes and runs the tetris game """

    def __init__(self, score):

        """ This method initialises game score to zero """

        self.__score = score

    def runthegame(self, board_obj, block_obj):

        """ This method runs the actual game untill the
            player either looses or fills the complete
            board """

        while True:                                                 # game play start to run
            blockspeed = 1
            nextblock = True
            piece, piece_prev_config, piece_color = self.selectpiece()
            block_obj.__init__(0, board_obj.width/2)
            piece_fut_config = piece_prev_config
            if (self.checkrowempty(board_obj, block_obj,
                                   piece, piece_prev_config) == 0):
                return
            self.checkrowfull(board_obj)
            print 'score is : ' + str(self.__score)
            while nextblock:
                board_obj.screen.blit(board_obj.background, (0, 0))
                movl = 0
                movr = 0

                for elem in block_obj.drawfig(piece,
                                              piece_prev_config):
                    row, col = elem
                                # make all positions of moving block as 'm'
                    board_obj.board[row][col] = "m"
                board_obj.fillpiecepos(piece_color)
                board_obj.removeprevpieces()

                if (block_obj.botblock(
                        piece,
                        piece_prev_config) == board_obj.height-1):

                    for elem in block_obj.drawfig(piece,
                                                  piece_prev_config):
                        row, col = elem
                        board_obj.board[row][col] = "s"
                            # make all stable or stopped positions to 's'
                    nextblock = False
                    self.updatescore()
                    break

                if (board_obj.checkpiecepos(block_obj,
                                            piece,
                                            piece_prev_config) == 0):

                    for elem in block_obj.drawfig(piece,
                                                  piece_prev_config):
                        row, col = elem
                        board_obj.board[row][col] = "s"
                                        # bottom blocks are made to 's'
                    nextblock = False
                    self.updatescore()
                    break

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_a:
                                            # press 'a' to move left
                            movl = block_obj.moveleft(board_obj,
                                                      piece,
                                                      piece_prev_config)

                        if event.key == pygame.K_d:
                                            # press 'd' to move right
                            movr = block_obj.moveright(board_obj,
                                                       piece,
                                                       piece_prev_config)

                        if event.key == pygame.K_s:
                                            # press 's' to rotate clockwise
                            if (block_obj.rotatecheck(board_obj,
                                                      piece,
                                                      piece_prev_config) == 1):
                                piece_fut_config = (piece_prev_config + 1)% 4

                        if event.key == pygame.K_SPACE:
                            blockspeed = 10

                block_obj.movetheblock(movl+movr)                # moves block
                piece_prev_config = piece_fut_config
                time.sleep(0.1/blockspeed)                      # sleeps for sometime

    def checkrowempty(self, board_obj, block_obj, piece, piece_config):

        """ This method checks for the next block to fall( is
            there a sufficient rows to accomodate the next block
            initially) """

        for elem in block_obj.drawfig(piece, piece_config):
            row, col = elem
            if board_obj.board[row][col] == "s":
                                # checks for possibility for starting block
                print 'Game Over'
                                # to place it or not
                return 0
        return 1

    def checkrowfull(self, board_obj):

        """ This method checks for a row to be empty
            if true removes the row & gives the bonus
            else continues with the normal gameplay """

        for i in range(board_obj.height):
            stable_blocks = 0
                                # checks for a complete row of stable blocks if yes score
            for j in range(board_obj.width):
                                # increases by 100 else nothing
                if board_obj.board[i][j] == "s":
    			    stable_blocks += 1
            if stable_blocks == board_obj.width:
                del board_obj.board[i]
                self.__score += 100
                space = [" " for j in range(board_obj.width)]
                board_obj.board.insert(0, space)

    def updatescore(self):          # updates score

        """ This method updates the score when a block
            falls on to the floor """

        self.__score += 10

    def selectpiece(self):           # randomly selects the starting piece

        """ This method selects a next random piece
            to fall """

        return (randint(1, 5), randint(0, 3),
                (255, 171, 44))

    def gamescore(self):

        """" This method returns the score of
             the updated game """

        return self.__score
