import pygame
import numpy as np

#screen parameters
screen_width = 800
screen_height = 700
play_width = 300
play_height = play_width * 2
block_size = play_width / 10

board = np.zeros((20, 10))
print(board)

#directions for shap generation
S = [(-1, 0), (0, 1), (1, 1)]
Z = [(-1, 1), (0, 1), (1, 0)]
I = [(0, 1), (0, -1), (0, -2)]
O = [(-1, 0), (-1, 1), (0, 1)]
J = [(-1, -1), (0, -1), (0, 1)]
L = [(0, 1), (0, -1), (-1, -1)]
T = [(-1, 0), (1, 0), (0, 1)]
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0 ,128)]
class Piece(object):
    def __init__(self, shape):
        self.color = shape_colors[shape]
        self.shap = shapes[shape]
        self.orientation = (1, 1)
