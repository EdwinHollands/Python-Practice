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