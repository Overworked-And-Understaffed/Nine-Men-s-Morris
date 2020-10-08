# class Piece:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#         if self.color == WHITE:
#             self.direction = 1
        
"""Piece creation"""
class Piece:
    #color attribute
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color[0]