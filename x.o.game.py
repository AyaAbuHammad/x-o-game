def display_board(board):
    print('   |   |') #3 space + 3 space
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])#1 space
    print('   |   |')
    print('-----------')#11 -
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def select_marker_input():
    marker=''   
    while not(marker == 'x' or marker == 'o'):
        marker = input('Which mark do you want? Enter only X or O :').lower()
    if marker == 'x': 
        return 'x','o' 
    else: 
        return 'o','x'
    
    
import random
def choose_first(): #who will start the game
    if random.randint(0,1) == 0:
        return'Player 1'
    else:
        return 'Player 2'

def place_marker(board,marker,position):
    board[position] = marker

def space_check(board,position):
    return board[position] == " " 
        
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i): 
            return False 
    return True 
def player_choice(board):
    position = 0  
    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board, position) :
        position = int(input('Enter your next position from 1 to 9 (You can end the game by choosing position 10 ) :'))
        if not (space_check(board, position)) and position != 10 :
            print('Position selected before')
    return position      
# =============================================================================
# def win_check(board,marker):
#     return ((board[1]==marker and board[2]==marker and board[3]==marker) or 
#             (board[4]==marker and board[5]==marker and board[6]==marker) or
#             (board[7]==marker and board[8]==marker and board[9]==marker) or
#             (board[1]==marker and board[4]==marker and board[7]==marker) or
#             (board[2]==marker and board[5]==marker and board[8]==marker) or
#             (board[3]==marker and board[6]==marker and board[9]==marker) or
#             (board[1]==marker and board[5]==marker and board[9]==marker) or
#             (board[3]==marker and board[5]==marker and board[7]==marker) 
#           )
# =============================================================================
def win_check(board,marker): 
    for i in range(1,10,3): 
        if board[i:i+3]==[marker]*3: 
            return True
    for i in range(1,4):
        if board[i::3]==[marker]*3:
            return True
    if board[1::4] == [marker] *3: 
        return True
    if board[3:8:2] == [marker] *3: 
        return True
def replay():
    return input('Do you want to play again? ').lower().startswith('y')
    
##################################################################

while True:
    theBoard = [' ']*11 
    player1 , player2 = select_marker_input() 
    turn = choose_first()
    print(turn + ' will start the game')
    game = input('Are you ready to start the game? ')
    if game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == player1:
            display_board(theBoard)
            position = player_choice(theBoard)
            if position !=10:
                place_marker(theBoard, player1, position)
                if win_check(theBoard,player1):
                    display_board(theBoard)
                    print('Player1 wins the game')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('No one wins the game')
                        break
                    else:
                        turn = 'Player2'
            else:
                break
        else:# if turn == player2
            display_board(theBoard)
            position = player_choice(theBoard)
            if position !=10:
                place_marker(theBoard, player2, position)
                if win_check(theBoard,player2):
                    display_board(theBoard)
                    print('Player2 wins the game')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('No one wins the game')
                        break
                    else:
                        turn = 'Player1'
            else:
                break

    if not replay():
        break

