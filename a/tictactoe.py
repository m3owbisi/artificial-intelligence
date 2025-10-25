board = [' ']*9
player = 'X'

def show_board():
    for i in range(0, 9, 3):
        print(f"|{board[i]}|{board[i+1]}|{board[i+2]}|")
        if i < 6: print("-------")

def is_winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==p for i,j,k in wins)

def is_tie():
    return ' ' not in board

while True:
    show_board()
    try:
        move = int(input(f"Player {player}, enter 0-8: "))
        if board[move] == ' ':
            board[move] = player
            if is_winner(player):
                show_board()
                print(f"Player {player} wins!")
                break
            elif is_tie():
                show_board()
                print("It's a tie!")
                break
            player = 'O' if player=='X' else 'X'
        else:
            print("Cell occupied!")
    except (ValueError, IndexError):
        print("Enter a number 0-8")
