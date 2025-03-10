def assert_equal(test,value):
    print(test == value)
def row_winner(board):
    for n in range(len(board)):
        if board[n][0] == ' ':
            continue
        else:
            for m in range(len(board)):
                if board[n][0]==board[n][m]:
                    continue
                else:
                    break
            else:
                return True
    else:
        return False
def column_winner(board):
    for n in range(len(board)):
        if board[0][n] == ' ':
            continue
        else:
            for m in range(len(board)):
                if board[0][n]==board[m][n]:
                    continue
                else:
                    break
            else:
                return True
    else:
        return False
def diagonal_winner(board):
    n = len(board)
    if board[0][n-1] != ' ':
            for i in range(n):
                if board[0][n-1] == board[0+i][n-1-i]:
                    continue
                else:
                    break
            else:
                return True
    if board[0][0] != ' ':
        for i in range(n):
            if board[0][0] == board[i][i]:
                continue
            else:
                break
        else:
            return True
    return False
def winner(board):
    return column_winner(board)\
    or row_winner(board)\
    or diagonal_winner(board)
def format_board_basic(board):
    string=''
    for row in board:
        string+="".join(row)+"\n"
    return string[:-1]
def format_board(board):
    string=''
    for row in board:
        string+="|".join(row)+"\n"
        for _ in board:
            string+='-+'
        string=string[:-1]+"\n"
    return string[:-2*len(board)-1]