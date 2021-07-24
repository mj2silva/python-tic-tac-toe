from Board import Board
from Player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player('x', self.board), Player('o', self.board)]
        self.turn = 0
        self.exit = False

    def next_turn(self):
        if (self.turn == 0):
            self.turn = 1
        else:
            self.turn = 0

    def print_turn(self):
        turn_message = 'Turn of the player {player_index}'.format(
            player_index=self.turn)
        print(turn_message)

    def start(self):
        title = 'mj2silva Tic-Tac-Toe'
        while (not self.exit):
            print(title)
            self.board.print_board()
            self.print_turn()
            next_move = input('Ingrese el número del espacio: ')
            self.players[self.turn].take_block(int(next_move))
            self.board.print_board()
            self.next_turn()
