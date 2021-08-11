"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xTurns = 0
    oTurns = 0

    for row in board:
        xTurns += row.count(X)
        oTurns += row.count(O)

    if xTurns <= oTurns:
        return X
    elif xTurns > oTurns:
        return O


def actions(board):
    """    Returns set of all possible actions (i, j) available on the board.
    """
    posibleActions = set()
    for i,row in enumerate(board):
        for j,space in enumerate(row):
            if space == EMPTY:
                posibleActions.add((i,j))

    return posibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turnOf = player(board)
    board[action[0]][action[1]] = turnOf
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows
    for row in board:
        result = findthree(row)
        if result is not None:
            return result
    #check colunms
    for i in range(3):
        colunm = []
        for row in board:
            colunm.append(row[i])

        result = findthree(colunm)

        if result is not None:
            return result

    #check diagonals
    diagonal = []
    reverseDiagonal = []

    #this is the iterator for the reverse diagonal
    for i, row in enumerate(board):
        diagonal.append(row[i])
        reverseDiagonal.append(row[(len(row) - 1)-i])

    resultDiagonal = findthree(diagonal)
    resultReverse = findthree(reverseDiagonal)

    if resultDiagonal is not None:
        return resultDiagonal
    elif resultReverse is not None:
        return resultReverse

    return None

def findthree(row):
    result = None
    if row.count(X) == 3:
            result = X 
    elif row.count(O) == 3:
            result = O
    else:
        return result            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for row in board:
            if row.count(EMPTY) > 0:
                return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turnOf = player(board)
    posibleActions = actions(board)
    posibilities = []
    optimal = (0,0)

    #explore all posible actions 
    for action in posibleActions:
            current = result(board, action)
            if terminal(current):
                value = utility(current)
                posibilities.append((value, action))
            else: 
                minimax(current)

    if turnOf == X:
        factor = -3
        for move in posibilities:
            if move[0] > factor:
                factor = move[0]
                optimal = move[1]

    if turnOf == O:
        factor = 3
        for move in posibilities:
            if move[0] < factor:
                factor = move[0]
                optimal = move[1]

    return optimal

