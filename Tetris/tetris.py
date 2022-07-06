import pygame
import numpy as np

#screen parameters
screen_width = 800
screen_height = 700
play_width = 300
play_height = play_width * 2
block_size = play_width / 10

board = np.zeros((10, 20))

#directions for shap generation
S = [(-1, 0), (0, 1), (1, 1)]
Z = [(-1, 1), (0, 1), (1, 0)]
I = [(0, 1), (0, -1), (0, -2)]
O = [(-1, 0), (-1, 1), (0, 1)]
J = [(-1, -1), (0, -1), (0, 1)]
L = [(0, 1), (0, -1), (-1, -1)]
T = [(-1, 0), (1, 0), (0, 1)]
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    global board
    def __init__(self, shape):
        self.color = shape_colors[shape]
        self.shape = shapes[shape]
        self.orientation = (0, 1)
        self.x = 4
        self.y = 18

    def generation(self):
        board[self.x, self.y] = 1
        board[self.x + self.shape[0][0], self.x + self.shape[0][1]] = 1
        board[self.x + self.shape[1][0], self.x + self.shape[1][1]] = 1
        board[self.x + self.shape[2][0], self.x + self.shape[2][1]] = 1

test = Piece(1)
test.generation()
print(board)