#!/usr/bin/python
import GamePlayClass, BoardClass, BlockClass

if __name__ == "__main__":
    # game starts to run
    gameboard = BoardClass.Board(30,32)
    startTheGame = GamePlayClass.Gameplay(0)
    blockPiece = BlockClass.Block(0,gameboard.width/2)
    startTheGame.runTheGame(gameboard,blockPiece)
