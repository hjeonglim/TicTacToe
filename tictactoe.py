import random


# Step 1 - display the board


def display_board(board):
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')


test_board = ['#', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
# print(display_board(test_board))

# Step 2 - player choose x or o


def player_marker():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 - please choose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Step 3 - who plays first

def play_first():

    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# print(play_first())


# Step 4 - win check

def win_check(board, marker):

    return(
        # check rows are same
        (board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or

        # check columns are same
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker) or

        # check two diagonals are same
        (board[1] == board[5] == board[9] == marker) or
        (board[7] == board[5] == board[3] == marker)
    )


# print(win_check(test_board, 'O'))


# Step 5 - take player input


def player_position(board, position, marker):
    board[position] = marker

# Step 6 - check space availability


def availability_check(board, position):
    return board[position] == ' '

# Step 7 - check if it's full board


def full_board_check(board):
    for i in range(1, 10):
        if availability_check(board, i):
            return False
    return True


# Step 8 - place the player's choice in the board


def player_move(board):

    position = 0

    while not availability_check(board, position) or position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = int(input('Please choose 1-9: '))

    return position


# print(player_move(test_board))
# Step 9 - ask to play again?


def replay():

    check = input('Want to play again? YES or NO').upper()

    if check == 'Yes':
        return True
    else:
        return False


# Step 10 - create a game using whole loops and functions

print('Welcome to Tic Tac toe')

while True:

    the_board = [' '] * 10
    player1_marker, player2_marker = player_marker()

    turn = play_first()
    print(f'{turn} will go first.')

    ready_play = input('Are you ready to play? YES or NO: ').upper()
    if ready_play == 'YES':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_move(the_board)
            player_position(the_board, position, player1_marker)

            if win_check(the_board, player1_marker):
                print("Congrats! Player 1 won")
                game_on = False
            else:
                if full_board_check(the_board):
                    print("Tie game.")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_move(the_board)
            player_position(the_board, position, player2_marker)

            if win_check(the_board, player2_marker):
                print("Congrats! Player 2 won")
                game_on = False
            else:
                if full_board_check(the_board):
                    print("Tie game.")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
