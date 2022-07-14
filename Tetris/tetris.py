import pygame
import numpy as np
import random

pygame.init()
# screen parameters
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
backup_board = np.zeros((10, 20))

# directions for shape generation
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

    def __init__(self, shape_number):
        global flag
        self.color = shape_colors[shape_number]
        self.shape = shapes[shape_number]
        self.shape_number = shape_number
        self.orientation = [0, 1]
        self.x = self.shape[3][0]
        self.y = self.shape[3][1]
        self.placed = False
        if not self.generation():
            flag = False

    def block_valid(self, x, y, flag):
        if x < 0 or x > 9:
            return False
        if y < 0 or y > 19:
            return False
        if flag:
            if board[x, y] != 0:
                return False
        return True

    def generation(self):

        num = self.shape_number + 1
        blocks = [0, 0, 0, 0]
        blocks[0] = (self.x, self.y)
        if self.orientation[0] == 0:
            blocks[1] = (
                self.x + self.shape[0][0] * self.orientation[1], self.y + self.shape[0][1] * self.orientation[1])
            blocks[2] = (
                self.x + self.shape[1][0] * self.orientation[1], self.y + self.shape[1][1] * self.orientation[1])
            blocks[3] = (
                self.x + self.shape[2][0] * self.orientation[1], self.y + self.shape[2][1] * self.orientation[1])
        else:
            blocks[1] = (
                self.x + self.shape[0][1] * self.orientation[0], self.y + self.shape[0][0] * self.orientation[0])
            blocks[2] = (
                self.x + self.shape[1][1] * self.orientation[0], self.y + self.shape[1][0] * self.orientation[0])
            blocks[3] = (
                self.x + self.shape[2][1] * self.orientation[0], self.y + self.shape[2][0] * self.orientation[0])
        check = True
        for block in blocks:
            if self.block_valid(block[0], block[1], True):
                board[block] = num
            else:
                check = False
        return check

    def delete(self):
        blocks = [0, 0, 0, 0]
        blocks[0] = (self.x, self.y)
        if self.orientation[0] == 0:
            blocks[1] = (
                self.x + self.shape[0][0] * self.orientation[1], self.y + self.shape[0][1] * self.orientation[1])
            blocks[2] = (
                self.x + self.shape[1][0] * self.orientation[1], self.y + self.shape[1][1] * self.orientation[1])
            blocks[3] = (
                self.x + self.shape[2][0] * self.orientation[1], self.y + self.shape[2][1] * self.orientation[1])
        else:
            blocks[1] = (
                self.x + self.shape[0][1] * self.orientation[0], self.y + self.shape[0][0] * self.orientation[0])
            blocks[2] = (
                self.x + self.shape[1][1] * self.orientation[0], self.y + self.shape[1][0] * self.orientation[0])
            blocks[3] = (
                self.x + self.shape[2][1] * self.orientation[0], self.y + self.shape[2][0] * self.orientation[0])
        check = True
        for block in blocks:
            if self.block_valid(block[0], block[1], False):
                board[block] = backup_board[block]
            else:
                check = False
        return check

    def left_turn(self):
        self.delete()
        placer = self.orientation[0]
        self.orientation[0] = -self.orientation[1]
        self.orientation[1] = placer
        if not self.generation():
            self.right_turn()

    def right_turn(self):
        self.delete()
        placer = self.orientation[0]
        self.orientation[0] = self.orientation[1]
        self.orientation[1] = -placer
        if not self.generation():
            self.left_turn()

    def soft_drop(self):
        self.delete()
        self.y -= 1
        if not self.generation():
            self.delete()
            self.y += 1
        self.generation()

    def place(self):
        self.delete()
        while self.generation():
            self.delete()
            self.y -= 1
        self.delete()
        self.y += 1
        self.generation()
        self.placed = True

    def move_left(self):
        self.delete()
        self.x -= 1
        if not self.generation():
            self.delete()
            self.x += 1
        self.generation()

    def move_right(self):
        self.delete()
        self.x += 1
        if not self.generation():
            self.delete()
            self.x -= 1
        self.generation()


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
    global flag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                piece.left_turn()
            if event.key == pygame.K_d:
                piece.right_turn()
            if event.key == pygame.K_w:
                piece.left_turn()
                piece.left_turn()
            if event.key == pygame.K_s:
                piece.right_turn()
                piece.right_turn()
            if event.key == pygame.K_LEFT:
                piece.move_left()
            if event.key == pygame.K_RIGHT:
                piece.move_right()
            if event.key == pygame.K_DOWN:
                piece.soft_drop()
            if event.key == pygame.K_SPACE:
                piece.place()


def draw_pieces():
    for x in range(10):
        for y in range(20):
            if (int(board[x][y]) - 1) != -1:
                draw_square(shape_colors[int(board[x][y]) - 1], x, 19 - y)


def draw_square(color, x, y):
    pygame.draw.rect(surface, color,
                     (x * block_size + x_edge1 + 1, y * block_size + y_edge1 + 1, block_size - 1, block_size - 1))


def piece_order():
    pieces = []
    repeat = True
    while len(pieces) < 7:
        num = random.randint(0, 6)
        for piece in pieces:
            if num == piece:
                repeat = False
                break
        if repeat:
            pieces.append(num)
        repeat = True
    return pieces


def main():
    global current, flag, surface
    piece_count = 0
    num = 0
    flag = True
    pieces = piece_order()
    current = Piece(pieces[num])
    surface = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    # print(board)
    fall_speed = 100
    tick = 0
    y_check = 0
    while flag:
        clock.tick(100)
        tick += fall_speed
        if tick == 10000:
            y_check = current.y
            current.soft_drop()
            if current.y == y_check:
                current.place()
            tick = 0
        redrawWindow(surface)
        input(current)
        if current.placed:
            for x in range(10):
                for y in range(20):
                    backup_board[x][y] = board[x][y]
            piece_count += 1
            num = piece_count % 7
            current = Piece(pieces[num])
            if num == 6:
                pieces = piece_order()


main()
