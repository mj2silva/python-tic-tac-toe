from Board import Board
from Player import Player
import os


class Game:
    winner_positions = [
        [0, 3, 6],
        [0, 1, 2],
        [0, 4, 8],
        [1, 4, 7],
        [2, 5, 8],
        [2, 4, 6],
        [3, 4, 5],
        [6, 7, 8]
    ]

    def __init__(self):
        self.title = 'Mj2silva Tic-Tac-Toe'
        self.board = Board()
        self.players = [Player('x', self.board), Player('o', self.board)]
        self.turn = 0
        self.exit = False
        self.invalid_move = False
        self.game_ended = False
        self.winner = -1

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
        self.check_board_status()
        if (not self.game_ended):
            self.next_turn()

    def print_board(self):
        # os.system('clear')
        print(self.title)
        self.board.print_board()
        if (self.invalid_move):
            print(self.error)
        self.print_turn()

    def set_winner(self, player_num):
        self.winner = player_num
        self.game_ended = True

    def check_board_status(self):
        for player in self.players:
            for winner_position in Game.winner_positions:
                is_winner = False
                for position in winner_position:
                    if not position in player.owned_blocks:
                        is_winner = False
                        break
                    is_winner = True
                if is_winner:
                    self.set_winner(self.turn)

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

    def print_game_ended(self):
        if (self.game_ended):
            if (self.winner >= 0):
                print('Congrats player {winner}! You Win!'.format(winner=self.winner))
            else:
                print('There are no movements left. The game finish in a tie!')

    def start(self):
        while (not self.exit and not self.game_ended):
            self.start_next_turn()

        self.print_game_ended()
