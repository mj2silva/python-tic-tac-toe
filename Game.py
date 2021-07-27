from Board import Board
from Player import Player
import os


class Game:
    def __init__(self):
        self.title = 'Mj2silva Tic-Tac-Toe'
        self.board = Board()
        self.players = [Player('x', self.board), Player('o', self.board)]
        self.turn = 0
        self.exit = False
        self.invalid_move = False

    def next_turn(self):
        if (self.turn == 0):
            self.turn = 1
        else:
            self.turn = 0

    def print_turn(self):
        turn_message = 'Turn of the player {player_index}'.format(
            player_index=self.turn)
        print(turn_message)

    def check_move(self, move):
        valid_move = True
        for player in self.players:
            if (move in player.owned_blocks):
                print(move, ' in ', player.owned_blocks)
                valid_move = False
        return valid_move

    def move_player(self, next_move):
        self.players[self.turn].take_block(next_move)
        self.next_turn()

    def print_board(self):
        os.system('clear')
        print(self.title)
        self.board.print_board()
        if (self.invalid_move):
            print(self.error)
        self.print_turn()

    def start_next_turn(self):
        try:
            self.print_board()
            next_move_input = input(
                'Enter the number of an empty position or x to exit: ')
            if (next_move_input.lower() == 'x'):
                self.exit = True
            else:
                next_move = int(next_move_input)
                self.invalid_move = not self.check_move(next_move)
                if (not self.invalid_move):
                    self.move_player(next_move)
                else:
                    self.error = 'Invalid move, the block is already taken'
        except:
            self.invalid_move = True
            self.error = 'Invalid move, you should enter a number between 0 and 8'

    def start(self):
        while (not self.exit):
            self.start_next_turn()
