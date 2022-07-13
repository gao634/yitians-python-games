import pygame
import numpy as np

#screen parameters
screen_width = 800
screen_height = 700
play_width = 300
play_height = play_width * 2
block_size = play_width / 10
x_edge1 = (screen_width - play_width) / 2
y_edge1 = (screen_height - play_height) / 2
x_edge2 = screen_width - x_edge1
y_edge2 = screen_height - y_edge1

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
    def __init__(self, shape_number):
        self.color = shape_colors[shape_number]
        self.shape = shapes[shape_number]
        self.shape_number = shape_number
        self.orientation = [0, 1]
        self.x = self.shape[3][0]
        self.y = self.shape[3][1]
        self.placed = False

    def generation(self):
        num = self.shape_number + 1
        board[self.x, self.y] = num
        if self.orientation[0] == 0:
            board[self.x + self.shape[0][0] * self.orientation[1], self.y + self.shape[0][1] * self.orientation[1]] = num
            board[self.x + self.shape[1][0] * self.orientation[1], self.y + self.shape[1][1] * self.orientation[1]] = num
            board[self.x + self.shape[2][0] * self.orientation[1], self.y + self.shape[2][1] * self.orientation[1]] = num
        else:
            board[self.x + self.shape[0][1] * self.orientation[1], self.y + self.shape[0][0] * self.orientation[1]] = num
            board[self.x + self.shape[1][1] * self.orientation[1], self.y + self.shape[1][0] * self.orientation[1]] = num
            board[self.x + self.shape[2][1] * self.orientation[1], self.y + self.shape[2][0] * self.orientation[1]] = num

    def left_turn(self):
        placer = self.orientation[0]
        self.orientation[0] = self.orientation[1]
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


def drawGrid(surface):

    x = x_edge1
    y = y_edge1
    pygame.draw.line(surface, (255, 255, 255), (x, y_edge1), (x, y_edge2))
    pygame.draw.line(surface, (255, 255, 255), (x_edge1, y), (x_edge2, y))

    for l in range(10):
        x = x + block_size
        y = y + block_size
        pygame.draw.line(surface, (255, 255, 255), (x, y_edge1), (x, y_edge2))
        pygame.draw.line(surface, (255, 255, 255), (x_edge1, y), (x_edge2, y))
        y = y + block_size
        pygame.draw.line(surface, (255, 255, 255), (x_edge1, y), (x_edge2, y))

def redrawWindow(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    draw_pieces()
    pygame.display.update()

def input(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            piece.left_turn()
        elif keys[pygame.K_RIGHT]:
            piece.right_turn()
        elif keys[pygame.K_SPACE]:
            piece.place()
        elif keys[pygame.K_DOWN]:
            piece.soft_drop

def draw_pieces():
    for x in range(10):
        for y in range(20):
            if (int(board[x][y]) - 1) != -1:
                draw_square(shape_colors[int(board[x][y]) - 1], x, 19 - y)

def draw_square(color, x, y):
    pygame.draw.rect(surface, color, (x * block_size + x_edge1 + 1, y * block_size + y_edge1 + 1, block_size - 1, block_size - 1))

flag = True
test = Piece(6)
test.generation()
surface = pygame.display.set_mode((screen_width, screen_height))
while flag:
    redrawWindow(surface)
    input(test)

