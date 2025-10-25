board=[' ']*9
player='X'

def show(): print('\n'.join([f"| {board[i]} | {board[i+1]} | {board[i+2]} |" for i in range(0,9,3)]), end='\n---------\n')

wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(p): return any(all(board[i]==p for i in t) for t in wins)
def tie(): return ' ' not in board

while True:
    show()
    try:
        m=int(input(f'player {player} enter 0-8: '))
        if 0<=m<=8 and board[m]==' ':
            board[m]=player
            if winner(player): show(); print(f'player {player} wins! 🎉'); break
            if tie(): show(); print('its a tie! 🤝'); break
            player='O' if player=='X' else 'X'
        else: print('Invalid move!')
    except: print('Enter 0-8!')
