from Piece import Piece 

class Gamer:
    def init(self, player_number, piece_color):
        self.player_num = player_number
        self.color = piece_color
        self.piece_list = []
        self.pieces = 0

    def create_piece(self, piece_number, x, y):
        self.piece_list[piece_number] = Piece(self.color, x, y)
        self.pieces = self.pieces + 1

    def kill_piece(self, piece_number):
        self.piece_list[piece_number].kill()
        self.pieces = self.pieces - 1
        
# past attempts??
# not needed
#class Gamer:
#    def __inti__(self, piece_name, piece_color, piece_turn = True):
#        self.piece_turn = piece_turn
#        self.piece_name = piece_name
#        self.piece_color = piece_color