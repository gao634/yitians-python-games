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
S = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
Z = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
I = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
O = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
J = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
L = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
t = [(-1, 2), (-1, 1), (-1, -1), (-1, -2)]
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0 ,128)]
class Piece(object):
    def __init__(self, shape):
