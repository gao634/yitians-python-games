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
hold_board = np.zeros((5, 4))
next_board = np.zeros((5, 12))

# directions for shape generation
S = [(-1, -1), (0, -1), (1, 0), (4, 19)]
Z = [(-1, 0), (0, -1), (1, -1), (5, 19)]
I = [(-1, 0), (1, 0), (2, 0), (4, 19)]
O = [(-1, 0), (-1, -1), (0, -1), (5, 19)]
J = [(1, -1), (-1, 0), (1, 0), (4, 19)]
L = [(1, 0), (-1, 0), (-1, -1), (5, 19)]
T = [(-1, 0), (1, 0), (0, -1), (4, 19)]
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (0, 0, 255), (255, 165, 0), (128, 0, 128)]


class Piece(object):

    def __init__(self, shape_number):
        global flag, main_flag
        self.color = shape_colors[shape_number]
        self.shape = shapes[shape_number]
        self.shape_number = shape_number
        self.orientation = [0, 1]
        self.x = self.shape[3][0]
        self.y = self.shape[3][1]
        self.placed = False
        if not self.generation():
            flag = False
            main_flag = False

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
                self.x + self.shape[0][1] * self.orientation[0], self.y - self.shape[0][0] * self.orientation[0])
            blocks[2] = (
                self.x + self.shape[1][1] * self.orientation[0], self.y - self.shape[1][0] * self.orientation[0])
            blocks[3] = (
                self.x + self.shape[2][1] * self.orientation[0], self.y - self.shape[2][0] * self.orientation[0])
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
                self.x + self.shape[0][1] * self.orientation[0], self.y - self.shape[0][0] * self.orientation[0])
            blocks[2] = (
                self.x + self.shape[1][1] * self.orientation[0], self.y - self.shape[1][0] * self.orientation[0])
            blocks[3] = (
                self.x + self.shape[2][1] * self.orientation[0], self.y - self.shape[2][0] * self.orientation[0])
        check = True
        for block in blocks:
            if self.block_valid(block[0], block[1], False):
                board[block] = backup_board[block]
            else:
                check = False
        return check

    def left_turn(self):
        if self.shape_number != 3:
            self.delete()
            placer = self.orientation[0]
            self.orientation[0] = -self.orientation[1]
            self.orientation[1] = placer
            if not self.bounce_check():
                self.right_turn()

    def right_turn(self):
        if self.shape_number != 3:
            self.delete()
            placer = self.orientation[0]
            self.orientation[0] = self.orientation[1]
            self.orientation[1] = -placer
            if not self.bounce_check():
                self.left_turn()

    def flip(self):
        if self.shape_number != 3:
            self.delete()
            self.orientation[0] *= -1
            self.orientation[1] *= -1
            if not self.bounce_check():
                self.flip()

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

    def bounce_check(self):
        if not self.generation():
            self.delete()
            self.y -= 1
            if not self.generation():
                self.delete()
                self.y += 2
                if not self.generation():
                    self.delete()
                    self.y -= 1
                    self.x -= 1
                    if not self.generation():
                        self.delete()
                        self.x += 2
                        if not self.generation():
                            self.delete()
                            self.x -= 1
                            self.y -= 2
                            if not self.generation():
                                self.delete()
                                self.y += 4
                                if not self.generation():
                                    self.delete()
                                    self.y -= 2
                                    self.x -= 2
                                    if not self.generation():
                                        self.delete()
                                        self.x += 4
                                        if not self.generation():
                                            self.delete()
                                            self.x -= 2
                                            return False
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

def hold_display():
    global hold_board, hold, surface
    for x in range(5):
        for y in range(4):
            hold_board[(x, y)] = 0
    hold_board[(1, 1)] = 1
    hold_board[(1 + shapes[hold][0][0], 1 - shapes[hold][0][1])] = 1
    hold_board[(1 + shapes[hold][1][0], 1 - shapes[hold][1][1])] = 1
    hold_board[(1 + shapes[hold][2][0], 1 - shapes[hold][2][1])] = 1
    for x in range(5):
        for y in range(4):
            if hold_board[(x, y)] == 1:
                pygame.draw.rect(surface, shape_colors[hold],
                                 (x * block_size + x_edge1 + 1 - block_size * 6, y * block_size + y_edge1 + 1, block_size - 1,
                                  block_size - 1))

def hold_piece():
    global current, hold, pieces, piece_count, hold_check
    if hold_check:
        current.delete()
        if hold == -1:
            hold = current.shape_number
            piece_count += 1
            current = Piece(pieces[piece_count % 7])
        else:
            spacer = hold
            hold = current.shape_number
            current = Piece(spacer)
        hold_display()
    hold_check = False

def next_display():
    global next_board, pieces, surface, num, next_seven, list
    #print(num)
    #print(pieces)
    #print(next_seven)
    for x in range(5):
        for y in range(12):
            next_board[(x, y)] = -1
    list = [-1, -1, -1, -1]
    x = num + 1
    index = 0
    if num < 3:
        list[0] = pieces[num + 1]
        list[1] = pieces[num + 2]
        list[2] = pieces[num + 3]
        list[3] = pieces[num + 4]
    else:
        while x < 7:
            list[index] = pieces[x]
            index += 1
            x += 1
        x -= 7
        while index < 4:
            list[index] = next_seven[x]
            index += 1
            x += 1
    next_board[(1, 0)] = list[0]
    next_board[(1 + shapes[list[0]][0][0], 0 - shapes[list[0]][0][1])] = list[0]
    next_board[(1 + shapes[list[0]][1][0], 0 - shapes[list[0]][1][1])] = list[0]
    next_board[(1 + shapes[list[0]][2][0], 0 - shapes[list[0]][2][1])] = list[0]
    next_board[(1, 3)] = list[1]
    next_board[(1 + shapes[list[1]][0][0], 3 - shapes[list[1]][0][1])] = list[1]
    next_board[(1 + shapes[list[1]][1][0], 3 - shapes[list[1]][1][1])] = list[1]
    next_board[(1 + shapes[list[1]][2][0], 3 - shapes[list[1]][2][1])] = list[1]
    next_board[(1, 6)] = list[2]
    next_board[(1 + shapes[list[2]][0][0], 6 - shapes[list[2]][0][1])] = list[2]
    next_board[(1 + shapes[list[2]][1][0], 6 - shapes[list[2]][1][1])] = list[2]
    next_board[(1 + shapes[list[2]][2][0], 6 - shapes[list[2]][2][1])] = list[2]
    next_board[(1, 9)] = list[3]
    next_board[(1 + shapes[list[3]][0][0], 9 - shapes[list[3]][0][1])] = list[3]
    next_board[(1 + shapes[list[3]][1][0], 9 - shapes[list[3]][1][1])] = list[3]
    next_board[(1 + shapes[list[3]][2][0], 9 - shapes[list[3]][2][1])] = list[3]
    #print(next_board)
    for x in range(5):
        for y in range(12):
            index = int(next_board[(x, y)])
            if index != -1:
                pygame.draw.rect(surface, shape_colors[index],
                                 (x * block_size + x_edge2 + 1 + block_size * 2, y * block_size + y_edge1 + 1, block_size - 1,
                                  block_size - 1))

def redrawWindow(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    draw_pieces()
    if hold != -1:
        hold_display()
    next_display()
    pygame.display.update()

def restart():
    global flag, main_flag
    main_flag = True
    flag = False

def input(piece):
    global flag, main_flag, key_lock
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            main_flag = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hold_piece()
            if event.key == pygame.K_a:
                piece.left_turn()
            if event.key == pygame.K_d:
                piece.right_turn()
            if event.key == pygame.K_s:
                piece.flip()
            if event.key == pygame.K_LEFT:
                piece.move_left()
            if event.key == pygame.K_RIGHT:
                piece.move_right()
            if event.key == pygame.K_DOWN:
                piece.soft_drop()
            if event.key == pygame.K_SPACE:
                piece.place()
            if event.key == pygame.K_r:
                restart()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_lock[0] = 0
            if event.key == pygame.K_RIGHT:
                key_lock[1] = 0
            if event.key == pygame.K_DOWN:
                key_lock[2] = 0

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            key_lock[0] += 1
            if key_lock[0] >= 10000:
                if key_lock[0] % 2000 == 0:
                    piece.move_left()
        if keys[pygame.K_RIGHT]:
            key_lock[1] += 1
            if key_lock[1] >= 10000:
                if key_lock[1] % 2000 == 0:
                    piece.move_right()
        if keys[pygame.K_DOWN]:
            key_lock[2] += 1
            if key_lock[2] >= 10000:
                if key_lock[2] % 1000 == 0:
                    piece.soft_drop()

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

def clear_line(line):
    for y in range(20):
        if y > line:
            for x in range(10):
                board[(x, y - 1)] = board[(x, y)]
        if y == 19:
            for x in range(10):
                board[(x, y)] = 0

def check_line():
    global lines
    for y in range(20):
        check = True
        for x in range(10):
            if board[(x, y)] == 0:
                check = False
        if check:
            lines += 1
            clear_line(y)
            check_line()
            break

def main():
    global current, flag, surface, lines, hold, pieces, num, piece_count, hold_check, board, backup_board, hold_board, next_seven, key_lock
    print("start")
    board = np.zeros((10, 20))
    backup_board = np.zeros((10, 20))
    hold_board = np.zeros((5, 4))
    next_board = np.zeros((5, 12))
    piece_count = 0
    num = 0
    lines = 0
    hold_check = True
    flag = True
    pieces = piece_order()
    next_seven = piece_order()
    current = Piece(pieces[num])
    hold = -1
    surface = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    # print(board)
    fall_speed = 100
    tick = 0
    y_check = 0
    place_tick = 0
    key_lock = [0, 0, 0]
    while flag:
        num = piece_count % 7
        clock.tick(100)
        place_tick += 1
        tick += fall_speed
        if tick >= 10000:
            y_check = current.y
            current.soft_drop()
            if current.y == y_check:
                if place_tick >= 100:
                    current.place()
                    place_tick = 0
            else:
                place_tick = 0
            tick = 0
        redrawWindow(surface)
        input(current)
        if current.placed:
            check_line()
            hold_check = True
            fall_speed += 3
            for x in range(10):
                for y in range(20):
                    backup_board[x][y] = board[x][y]
            piece_count += 1
            num = piece_count % 7
            if num == 0:
                pieces = next_seven
                next_seven = piece_order()
            current = Piece(pieces[num])

main_flag = True
while main_flag:
    main()
print(lines)