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
    xCounter = 0
    oCounter = 0 
    for i in range(3):
        for j in range(3):
            if (board[i][j] != EMPTY):
                if (board[i][j] == X):
                    xCounter = xCounter + 1
                elif (board[i][j] == O):
                    oCounter = oCounter + 1

    if (xCounter == oCounter):
        return X
    elif (xCounter > oCounter):
        return O


def actions(board):
    actionList = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                actionList.append((i,j))

    return actionList


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    whoPlay = player(board)
    boardCopy = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]

    for i in range(3):
        for j in range(3):
            boardCopy[i][j] = board[i][j]

    
    rowNum = action[0]
    columnNum = action[1]

    boardCopy[rowNum][columnNum] = whoPlay

    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        xCounter = 0
        oCounter = 0
        for j in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if (xCounter == 3):
                return X
            elif (oCounter == 3):
                return O
    
    
    for j in range(3):
        xCounter = 0
        oCounter = 0
        for i in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if (xCounter == 3):
                return X
            elif (oCounter == 3):
                return O

    if ((board[0][2] == X) & (board[1][1] == X) & (board[2][0] == X)):
        return X

    if ((board[0][0] == X) & (board[1][1] == X) & (board[2][2] == X)):
        return X

    if ((board[0][2] == O) & (board[1][1] == O) & (board[2][0] == O)):
        return O

    if ((board[0][0] == O) & (board[1][1] == O) & (board[2][2] == O)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3): # 3 X's or 3 O's in the same row ?
        xCounter = 0
        oCounter = 0
        for j in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if ((xCounter == 3) | (oCounter == 3)):
                return True
    
    for j in range(3): # 3 X's or 3 O's in the same column ?
        xCounter = 0
        oCounter = 0
        for i in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if ((xCounter == 3) | (oCounter == 3)):
                return True

    if ((board[0][2] == X) & (board[1][1] == X) & (board[2][0] == X)):
        return True

    if ((board[0][0] == X) & (board[1][1] == X) & (board[2][2] == X)):
        return True

    if ((board[0][2] == O) & (board[1][1] == O) & (board[2][0] == O)):
        return True

    if ((board[0][0] == O) & (board[1][1] == O) & (board[2][2] == O)):
        return True

    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                return False

    return True
            

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        xCounter = 0
        oCounter = 0
        for j in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if (xCounter == 3):
                return 1
            elif (oCounter == 3):
                return -1
    
    
    for j in range(3):
        xCounter = 0
        oCounter = 0
        for i in range(3):
            if (board[i][j] == X):
                xCounter = xCounter + 1
            elif (board[i][j] == O):
                oCounter = oCounter + 1
            
            if (xCounter == 3):
                return 1
            elif (oCounter == 3):
                return -1

    if ((board[0][2] == X) & (board[1][1] == X) & (board[2][0] == X)):
        return 1

    if ((board[0][0] == X) & (board[1][1] == X) & (board[2][2] == X)):
        return 1

    if ((board[0][2] == O) & (board[1][1] == O) & (board[2][0] == O)):
        return -1

    if ((board[0][0] == O) & (board[1][1] == O) & (board[2][2] == O)):
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return utility(board)
    
    whoPlayer = player(board)
    
    if (whoPlayer == X):
        opAction = maxValue(board)
        return opAction[1]
    elif (whoPlayer == O):
        opAction = minValue(board)
        return opAction[1]


def maxValue(board):
    value = -10
    action = ('test','test')

    if (terminal(board)):
        return utility(board), action

    boardActions = actions(board)

    for i in range(len(boardActions)):
        newV = minValue(result(board, boardActions[i]))
        if (value < newV[0]):
            value = newV[0]
            action = boardActions[i]

    
    return value, action


def minValue(board):
    value = 10
    action = ()
    boardActions = actions(board)

    if (terminal(board)):
        return utility(board), action

    for i in range(len(boardActions)):
        newV = maxValue(result(board, boardActions[i]))
        if (newV[0] < value):
            value = newV[0]
            action = boardActions[i]

    return value, action