# Import random
import random


class Board():
    '''Create Board class, create a board'''

    def __init__(self):
        self.boards = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print('---------')
        print(f"{self.boards[7]} | {self.boards[8]} | {self.boards[9]}")
        print('---------')
        print(f"{self.boards[4]} | {self.boards[5]} | {self.boards[6]}")
        print('---------')
        print(f"{self.boards[1]} | {self.boards[2]} | {self.boards[3]}")
        print('---------')

    def update_board(self, position, marker):
        '''Step 3 - update the board upon player's choice'''
        self.boards[position] = marker

    def win_check(self, player):
        '''Check if Player wins'''
        return(
            (self.boards[1] == self.boards[2] == self.boards[3] == player) or
            (self.boards[4] == self.boards[5] == self.boards[6] == player) or
            (self.boards[7] == self.boards[8] == self.boards[9] == player) or
            (self.boards[1] == self.boards[4] == self.boards[7] == player) or
            (self.boards[2] == self.boards[5] == self.boards[8] == player) or
            (self.boards[3] == self.boards[6] == self.boards[9] == player) or
            (self.boards[1] == self.boards[5] == self.boards[9] == player) or
            (self.boards[3] == self.boards[5] == self.boards[7] == player))

    def available_space(self, position):
        '''Check if space is empty'''
        return self.boards[position] == ' '

    def full_board_check(self):
        '''Check if the board is full'''
        for i in range(1, 10):
            if self.available_space(i):
                return False
        return True

def player_marker():
    '''Player choose x or o'''
    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please choose X or O: ").upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def play_first():
    '''Decide who goes first'''
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def player_move():
    '''Player's next move'''
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not board.available_space:
        position = int(input('Please choose your next move: 1-9 '))

    return position

def replay():
    '''Ask to play again'''
    replay = input('Wanna play again? YES or NO').upper()

    if replay == 'YES':
        return True
    else:
        return False

#Use while loops and functions to run the game
print("Welcome to Tic-Tac-Toe")

while True:

    # set up the board
    player1_marker, player2_marker = player_marker()

    # who plays first
    turn = play_first()
    print(f'{turn} goes first.')

    # Ask if ready to play
    ready_to_play = input("Ready to play? Yes or No").upper()
    if ready_to_play == 'YES':
        game_on = True
    else:
        game_on = False

    # start to play the game
    board = Board()
    while game_on:
        if turn == 'Player 1':
            board.display()

            position = player_move()
            board.update_board(position, player1_marker)

            # Check win or tie game
            if board.win_check(player1_marker):
                board.display()
                print("Congrats! Player 1 has won.")
                game_on = False
            else:
                if board.full_board_check():
                    board.display()
                    print("Tie game.")
                    break
                else:
                    turn = 'Player 2'
        else:
            board.display()

            position = player_move()
            board.update_board(position, player2_marker)

            if board.win_check(player2_marker):
                board.display()
                print("Congrats! Player 2 has won.")
                game_on = False
            else:
                if board.full_board_check():
                    board.display()
                    print("Tie game.")
                    break
                else:
                    turn = 'Player 1'

    # want to play again
    if replay():
        game_on = True
    else:
        exit()

