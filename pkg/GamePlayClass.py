import pygame, sys, os, time
from pygame.locals import *
import BoardClass, BlockClass
from random import randint

class Gameplay(BoardClass.Board,BlockClass.Block):

    def __init__(self,score):           # initialises game score to zero
        self.__score = score

    def runTheGame(self,board_obj,block_obj):
        while True:                                     # game play start to run
            blockspeed = 1
            nextblock = True
            piece ,piece_prev_config, piece_color = self.selectPiece()
            block_obj.__init__(0,board_obj.width/2)
            piece_fut_config = piece_prev_config
            if self.checkRowEmpty(board_obj,block_obj,piece,piece_prev_config) == 0:
                return
            self.checkRowFull(board_obj)
            print 'score is : '+str(self.__score)
            while nextblock:
                board_obj.screen.blit(board_obj.background,(0,0))
                movL = 0
                movR = 0
                for elem in block_obj.drawFig(piece,piece_prev_config):
                    row, col = elem
                    board_obj.board[row][col] = "m"                     # make all positions of moving block as 'm'
                board_obj.fillPiecePos(piece_color)
                board_obj.removePrevPieces()
                if block_obj.botBlock(piece,piece_prev_config) == board_obj.height-1:
                    for elem in block_obj.drawFig(piece,piece_prev_config):
                        row, col = elem
                        board_obj.board[row][col] = "s"                 # make all stable or stopped positions to 's'
                    nextblock = False
                    self.updateScore()
                    break
                if board_obj.checkPiecePos(block_obj,piece,piece_prev_config) == 0:
                    for elem in block_obj.drawFig(piece,piece_prev_config):
                        row, col = elem
                        board_obj.board[row][col] = "s"             # bottom blocks are made to 's'
                    nextblock = False
                    self.updateScore()
                    break
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_a:                # press 'a' to move left
                            movL = block_obj.moveLeft(board_obj,block_obj,piece,piece_prev_config)
                        if event.key == K_d:                # press 'd' to move right
                            movR = block_obj.moveRight(board_obj,block_obj,piece,piece_prev_config)
                        if event.key == K_s:                # press 's' to rotate clockwise
                            if block_obj.rotateCheck(board_obj,piece,piece_prev_config) == 1:
                                piece_fut_config = ( piece_prev_config + 1 )% 4
                        if event.key == K_SPACE:
                            blockspeed = 10
                block_obj.moveTheBlock(movL+movR)       # moves block
                piece_prev_config = piece_fut_config
                time.sleep(0.1/blockspeed)                  # sleeps for sometime

    def checkRowEmpty(self,board_obj,block_obj,piece,piece_config):
        for elem in block_obj.drawFig(piece,piece_config):
            row, col = elem
            if board_obj.board[row][col] == "s":                # checks for possibility for starting block
                print 'Game Over'                               # to place it or not
                return 0
        return 1

    def checkRowFull(self,board_obj):
        for i in range(board_obj.height):
            stable_blocks=0                     # checks for a complete row of stable blocks if yes score
            for j in range(board_obj.width):    # increases by 100 else nothing
                if board_obj.board[i][j] == "s":
    			    stable_blocks += 1
            if stable_blocks == board_obj.width:
                del board_obj.board[i]
                self.__score += 100
                space = [" " for j in range(board_obj.width)]
                board_obj.board.insert(0 , space)

    def updateScore(self):          # updates score
        self.__score += 10

    def selectPiece(self):           # randomly selects the starting piece
        return (randint(1,5),randint(0,3),(255,171,44))
