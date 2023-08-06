
import random
import math

print("TIC-TAC-TOE")


#to print the play board
#Player Class > to know who is playing
class Player:
    def __init__(self, player):
        self.player =player

    def getMove(self):
        pass

class computerPlayer(Player):
    def __init__(self, player):
        super().__init__(player)

    def getMove(self):
        computerMove = random.choice(Board.printBoard())
        return computerMove

class humanPlayer(Player):
    def __init__(self, player):
        super().__init__(player)

#to get an input of square from player
    def getMove(self):
        legitMove = False
        val = None 
        while not legitMove:
            userMove = input(self.player + " 's turn. Input move(0-8) : ")
            try:
                val = int(userMove)
                if val not in Board.legitMove():
                    raise ValueError
                legitMove = True
            except ValueError:
                print("Invalid Move")

        return val

#Board Class > to print board
class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

#to print Board > to play
    def printBoard(self):

        # for row in[self.board[i*3: (i+1)*3] for i in range(3)]
        for i in range(3):
            for row in [self.board[i*3 : (i+1)*3]]:
                print('| ' + ' | '.join(row) + ' |')

#to print Board > to show example of move
    def printBoardWithNumber(self):
        numberBoard = [i for i in range(j*3, (j+1)*3) for j in range(3)]
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')
    
#to know which square is available
    def legitMove(self):
        move = []

        # for i, x in enumerate(self.board) if x == ' ' 
        for i, x in enumerate(self.board):
            if x == ' ':
                move.append(i)
        return move

#to know if there is anymore move
    def emptyMove(self):
        return ' ' in self.board

#to show player move
    def makeMove(self, move, player):
        if self.board[move] == ' ':
            self.board[move] = player
            return True
        return False

def Play(Board, xPlayer, oPlayer, printGame = True):

#to start print > Board with Number > when play
    if printGame:
        Board.printBoardWithNumber()

    player = 'X'

    while Board.emptyMove:

        if player == 'X':
            move = xPlayer.getMove(Board)
        else:
            move = oPlayer.getMove(Board)

#to make player move
        if Board.makeMove(move, player):
            if printGame:
                Board.printBoard()
                print()

#to change player
        player = 'O' if player == 'X' else 'X'
