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
def format_board(board):
    string=''
    n=0
    top=' '
    for row in board:
        n+=1
        top+=str(n)
        string+=str(n)+"".join(row)+"\n"
    return top+'\n'+string[:-1]
def format_board_pretty(board):
    string=''
    n=0
    top=' '
    for row in board:
        n+=1
        top+=' '+str(n)
        string+=str(n)+' '+"|".join(row)+"\n  "
        for _ in board:
            string+='-+'
        string=string[:-1]+"\n"
    return top+'\n'+string[:-2*len(board)-2]
def play_move(board, player):
    print(f'{player} to play:')
    x=int(input())
    y=int(input())
    board[x-1][y-1]=player
    print(format_board_pretty(board))
def make_board(size):
    row = []
    for _ in range(size):
        row.append(' ')
    board = []
    for _ in range(size):
        board.append(row.copy())
    return board
def draw(board):
    return not(any(' ' in row for row in board))
def print_winner(player):
    print(f'{player} wins!')
def print_draw():
    print("It's a draw!")
def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board_pretty(board))
    players=[player1,player2]
    active_player=player1
    while True:
        play_move(board, active_player)
        if winner(board):
            return print_winner(active_player)
        elif draw(board):
            return print_draw()
        else:
            players=[player1,player2]
            players.remove(active_player)
            active_player=players[0]
play_game(3,'X','O')