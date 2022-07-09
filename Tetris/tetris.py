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
S = [(-1, 0), (0, 1), (1, 1), (4, 18)]
Z = [(-1, 1), (0, 1), (1, 0), (5, 18)]
I = [(0, 1), (0, -1), (0, -2), (4, 18)]
O = [(-1, 0), (-1, 1), (0, 1), (5, 18)]
J = [(1, 1), (0, -1), (0, 1), (4, 18)]
L = [(0, 1), (0, -1), (-1, 1), (5, 18)]
T = [(-1, 0), (1, 0), (0, -1), (4, 19)]
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    global board
    def __init__(self, shape):
        self.color = shape_colors[shape]
        self.shape = shapes[shape]
        self.orientation = (0, 1)
        self.x = self.shape[3][0]
        self.y = self.shape[3][1]
        self.placed = False

    def generation(self):
        board[self.x, self.y] = 1
        if self.orientation[0] == 0:
            board[self.x + self.shape[0][0] * self.orientation[1], self.y + self.shape[0][1] * self.orientation[1]] = 2
            board[self.x + self.shape[1][0] * self.orientation[1], self.y + self.shape[1][1] * self.orientation[1]] = 3
            board[self.x + self.shape[2][0] * self.orientation[1], self.y + self.shape[2][1] * self.orientation[1]] = 4
        else:
            board[self.x + self.shape[0][1] * self.orientation[1], self.y + self.shape[0][0] * self.orientation[1]] = 2
            board[self.x + self.shape[1][1] * self.orientation[1], self.y + self.shape[1][0] * self.orientation[1]] = 3
            board[self.x + self.shape[2][1] * self.orientation[1], self.y + self.shape[2][0] * self.orientation[1]] = 4

    def left_turn(self):
        placer = self.orientation[0]
        self.orientation[0] = -self.orientation[1]
        self.orientation[1] = placer

    def right_turn(self):
        placer = self.orientation[0]
        self.orientation[0] = self.orientation[1]
        self.orientation[1] = -placer

    def soft_drop(self):
        self.y -= 1
        if not self.valid():
            self.y += 1

    def place(self):
        while self.valid():
            self.y -= 1
        self.y += 1
        self.placed = true

    def valid(self):
        return True


def input(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for key in keys:
        if keys[pygame.K_LEFT]:
            piece.left_turn()
            print(board)
        elif keys[pygame.K_RIGHT]:
            piece.right_turn()
        elif keys[pygame.K_SPACE]:
            piece.place()
        elif keys[pygame.K_DOWN]:
            piece.soft_drop

flag = True
test = Piece(6)
test.generation()
print(board)
while flag:
    input(test)

