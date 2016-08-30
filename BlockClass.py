import BoardClass

class Block(BoardClass.Board):

    def __init__(self,x,y):                 #initialises block base point
        self.x = x
        self.y = y

    def moveTheBlock(self,dis):
        self.y += dis                       # moves the base point of the block
        self.x += 1

    def botBlock(self,piece,config):

        if piece == 1:
            if config == 0:                 # this kind of block #### gives all the four bottom points
                return self.x
            if config == 1:
                return self.x+3
            if config == 2:
                return self.x
            if config == 3:
                return self.x+3

        if piece == 2:                      # this kind of block ### gives all the four bottom points
            if config == 0:                                       #
                return self.x+1
            if config == 1:
                return self.x+2
            if config == 2:
                return self.x+1
            if config == 3:
                return self.x+2

        if piece == 3:                          # this kind of block ##  gives all the four bottom points
            if config == 0 or config == 2:                            ##
                return self.x+1
            if config == 1 or config == 3:
                return self.x+2

        if piece == 4:                                                      # this kind of block ## gives all four bottom points
            if config == 0 or config == 1 or config == 2 or config == 3:                         ##
                return self.x+1
        if piece == 5:                      # this kind of block ### gives all four bottom points
            if config == 0:                                      #
                return self.x+1
            if config == 1:
                return self.x+2
            if config == 2:
                return self.x+1
            if config == 3:
                return self.x+2

    def moveLeft(self,board_obj,block_obj,piece,piece_config):
        for elem in self.drawFig(piece,piece_config):
            row, col = elem                                 #checks for possibility of moving block left return -1 if true else 0
            if col > 0 and board_obj.board[row+1][col-1] == "s":
                return 0
            if col <= 0:
                return 0
        return -1

    def moveRight(self,board_obj,block_obj,piece,piece_config):
        for elem in self.drawFig(piece,piece_config):
            row, col = elem
            if col < board_obj.width-1 and board_obj.board[row+1][col+1] == "s":
                return 0                            #checks for possibility of moving right return 1 if true else 0
            if col >= board_obj.width-1:
                return 0
        return 1

    def drawFig(self,pieceType,config):
        if pieceType == 1:
            if config == 0:                                                                       # this figure ####
                return ((self.x,self.y-1),(self.x,self.y),(self.x,self.y+1),(self.x,self.y+2))
            if config == 1:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+2,self.y),(self.x+3,self.y))
            if config == 2:
                return ((self.x,self.y-1),(self.x,self.y),(self.x,self.y+1),(self.x,self.y+2))
            if config == 3:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+2,self.y),(self.x+3,self.y))
        if pieceType == 2:                                  # this figure ###
            if config == 0:                                                #
                return ((self.x,self.y-1),(self.x,self.y),(self.x+1,self.y),(self.x,self.y+1))
            if config == 1:
                return ((self.x,self.y),(self.x+1,self.y-1),(self.x+1,self.y),(self.x+2,self.y))
            if config == 2:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+1,self.y-1),(self.x+1,self.y+1))
            if config == 3:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+2,self.y),(self.x+1,self.y+1))
        if pieceType == 3:                              # this figure ##
            if config == 0:                                            ##
                return ((self.x,self.y-1),(self.x,self.y),(self.x+1,self.y),(self.x+1,self.y+1))
            if config == 1:
                return ((self.x+1,self.y),(self.x,self.y),(self.x+1,self.y-1),(self.x+2,self.y-1))
            if config == 2:
                return ((self.x,self.y-1),(self.x,self.y),(self.x+1,self.y),(self.x+1,self.y+1))
            if config == 3:
                return ((self.x+1,self.y),(self.x,self.y),(self.x+1,self.y-1),(self.x+2,self.y-1))
        if pieceType == 4:                                               # this figure ##
            if config == 0 or config == 1 or config == 2 or config == 3:               ##                                                                         ##
                return ((self.x,self.y-1),(self.x,self.y),(self.x+1,self.y),(self.x+1,self.y-1))
        if pieceType == 5:                          # this fugure ###
            if config == 0:                                       #
                return ((self.x,self.y),(self.x+1,self.y),(self.x,self.y+1),(self.x,self.y+2))
            if config == 1:
                return ((self.x,self.y),(self.x,self.y-1),(self.x+1,self.y),(self.x+2,self.y))
            if config == 2:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+1,self.y-1),(self.x+1,self.y-2))
            if config == 3:
                return ((self.x,self.y),(self.x+1,self.y),(self.x+2,self.y),(self.x+2,self.y+1))

    def rotateCheck(self,board_obj,piece,piece_Config):
        for elem in self.drawFig(piece,(piece_Config + 1)%4):
            row, col = elem                                     # checks for possibility of rotate returns 1 if true else 0
            if row > board_obj.height-1 or col > board_obj.width-1 or board_obj.board[row][col] == "s":
                return 0
        return 1
