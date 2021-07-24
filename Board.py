class Board:
    def __init__(self):
        self.blocks = [i for i in range(9)]
        self.update_board()

    def update_board(self):
        self.board_repr = '''\
     a     b     c
        |     |     
  1  {xa1}  |  {xb1}  |  {xc1}  
   _____|_____|_____
        |     |     
  2  {xa2}  |  {xb2}  |  {xc2}  
   _____|_____|_____
        |     |     
  3  {xa3}  |  {xb3}  |  {xc3}  
        |     |     \
  '''.format(
            xa1=self.blocks[0],
            xb1=self.blocks[1],
            xc1=self.blocks[2],
            xa2=self.blocks[3],
            xb2=self.blocks[4],
            xc2=self.blocks[5],
            xa3=self.blocks[6],
            xb3=self.blocks[7],
            xc3=self.blocks[8]
        )

    def write_in_board(self, position, symbol):
        self.blocks[position] = symbol
        self.update_board()

    def print_board(self):
        print(self.board_repr)
