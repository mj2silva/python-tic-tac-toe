class Player:
    def __init__(self, character, board):
        self.character = character
        self.winner = False
        self.owned_blocks = []
        self.board = board

    def take_block(self, block_number):
        self.owned_blocks.append(block_number)
        self.board.write_in_board(block_number, self.character)
