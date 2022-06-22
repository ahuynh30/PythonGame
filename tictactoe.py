import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        
        

    def get_random_first_player(self):
        

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        

        # checking columns
        

        # checking diagonals
        

    def is_board_filled(self):
        

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
            

            # fixing the spot

            # checking whether current player is won or not
            if 
                print()
                break

            # checking whether the game is draw or not
            if 
                print("Match Draw!")
                break

            # swapping the turn
            

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()