import random

# make board piece using list
# global
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
# start every game with player x
currentPlayer = "X"
# create winner variable
winner = None
# gameloop
gameRunning = True

# Print board
def printBoard(board):
    # print each row
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("__________")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("__________")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# take input
def playerInput(board):
    x_or_o = int(input("Enter a number 1-9: "))
    if x_or_o >= 1 and x_or_o <= 9 and board[x_or_o-1] == "_":
        board[x_or_o -1] = currentPlayer
    else:
        print("Oops! Player is already in that spot.")

# check win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "_":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "_":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "_":
        winner = board[5]
        return True

def checkDiags(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("It's a tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiags(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        gameRunning = False



# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# computer play
def computerPlayer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()


# check win or tie 2
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    switchPlayer()
    computerPlayer(board)
    checkTie(board)
    checkWin()


