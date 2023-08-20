#3x6 board to climb
#each column has random mine
#player choose 1 spot 
#if it's mine lose else win
import random
board = []
winner = None
playing = True

def printBoard(board):
    for i in range(6):
        group = []
        for columns in range(3):
            group.append("-")
        board.append(group)

#just for a number outside
    j = 0
    for i in range(16):
        if i in [5,9,13]:
            print(j, end = "")
            j += 1
        elif i in [0, 1, 2]:
            print(" ", end = "")
        else:
            print("-", end = "")
    print()

    i = 5
    for row in board:
        print(i," | "+ " | ".join(row)+ " | ")
        i -= 1

 #making Mine Field   
def plantMine(board):
    for i in range(len(board)):
        mine = random.randint(0,2)
        for j in range(len(board[i])):
            if j == mine:
               board[i][j] = '*'


def playerInput(board, winner):
    #col = int(input("Enter a column (0 - 2) : "))
    #row = int(input("Enter a row (0-6) : "))

    count = 0
    while winner == None:
        for i in range(len(board)):
            show = []
            for j in range(len(board[i])):
                show.append((i,j))
            try:
                player = int(input(f"Select one 1.{show[0]}|2.{show[1]}|3.{show[2]} : "))
                if player not in (1,2,3):
                    raise ValueError
            except ValueError:
                print("invalid move")
        winner = False


while playing:
    printBoard(board)
    plantMine(board)
    playerInput(board, winner)
    