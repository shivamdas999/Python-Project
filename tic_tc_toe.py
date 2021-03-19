def gameon_choice():
    
    choice = 'wrong'
    
    
    while choice not in ['Y','N']:
        
        choice=input('Would you like to play more (Y or N) ')
        
        if choice not in ['Y','N']:
            
            print('Sorry! its an invalid choice, please choose from (Y or N).')
            
            
    if choice=='Y':
        return True
    else:
        return False
    
    
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
    
    
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
    
    
def place_marker(board,marker,position):
    board[position]=marker
    
    
    
def win_check(board,mark):
    
    return ((board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[1]==mark and board[4]==mark and board[7]==mark)or
    (board[2]==mark and board[5]==mark and board[8]==mark)or
    (board[3]==mark and board[6]==mark and board[9]==mark)or
    (board[1]==mark and board[5]==mark and board[9]==mark)or
    (board[3]==mark and board[5]==mark and board[7]==mark))



import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
    
    
def space_check(board,position):
    return board[position]==' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position where you want to place the marker (1-9): '))
    return position



def replay():
    choice=input('Do you want to play again? Yes or No.: ')
    return choice=='Yes'



#while loop to keep running the game
print('Welcome to the game TIC TAC TOE')
while True:
    
    
    #setting up game(board, whose first, choosing marker X,O)
    Game_board=[' ']*10
    
    Player1_marker,Player2_marker=player_input()
    
    turn=choose_first()
    print(turn+' will go first')
    
    play_game=input('Ready to play the game? y or n?')
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    
    
    while game_on:
        if turn=='Player1':
            
            display_board(Game_board)
            
            position=player_choice(Game_board)
            
            place_marker(Game_board,Player1_marker,position)
            
            if win_check(Game_board,Player1_marker):
                display_board(Game_board)
                print('Congratulations!! Player1 has won the game')
                game_on=False
            
            else:
                if full_board_check(Game_board):
                    display_board(Game_board)
                    print('TIE Game!!')
                    break
                else:
                    turn='Player2'
        
        else:
            display_board(Game_board)
            position=player_choice(Game_board)
            place_marker(Game_board,Player2_marker,position)
            
            if win_check(Game_board,Player2_marker):
                display_board(Game_board)
                print('Congratulations!! Player2 has won the game')
                game_on=False
            else:
                if full_board_check(Game_board):
                    display_board(Game_board)
                    print('TIE Game!!')
                    break
                else:
                    turn='Player1'

    if not replay():
            break