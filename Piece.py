

"""Piece creation"""

class Piece:
    #color attribute
    def init(self, color, x, y):
        self.color = color
        self.location_x = x
        self.location_y = y
        self.is_alive = True

    def str(self):
        return self.color[0]

    def update_location(self, x,y):
        self.location_x = x
        self.location_y = y

    def kill(self):
        self.is_alive = False

# past attempts??
# not needed???

# class Piece:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#         if self.color == WHITE:
#             self.direction = 1
        
#class Piece:
#    #color attribute
#    def __init__(self, color):
#        self.color = color
#    def __str__(self):
#        return self.color[0]