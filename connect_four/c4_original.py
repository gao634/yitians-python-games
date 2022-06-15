import pygame
import keyboard

class player(object):
    global current
    pieces = []
    column = 3
    def __init__(self, color, num):
        self.color = color
        self.num = num
        self.current = current
    def place(self):
        print("called")
        for i in range(6):
            if board[self.column, i] != 0:
                board[self.column, i - 1] = self.num
                self.pieces.append(self.column, i - 1)
            elif i == 6:
                board[self.column, i] = self.num
                self.pieces.append(self.column, i)
    def turn(self):
        print(current)
        pygame.draw.circle(window, self.color, (self.column * size + size / 2, size / 2), size * 2 / 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

        if keyboard.is_pressed("left arrow"):
            if self.column > 0:
                self.column -= 1
        if keyboard.is_pressed("right arrow"):
            if self.column < 6:
                self.column += 1
        if keyboard.is_pressed("space"):
            if board[self.column, 0] == 0:
                self.place()
                self.current = self.num - 2

def create_board():
    b = {}
    for i in range(7):
        for j in range(6):
            b[(i, j)] = 0
    return b
def draw_circles():
    for i in range(7):
        for j in range(6):
            if board[(i, j)] == 0:
                pygame.draw.circle(window, (255, 255, 255), (i * size + size/2, (j + 1) * size + size/2), size * 2/5)
            if board[(i, j)] == players[0].num:
                pygame.draw.circle(window, players[0].color, (i * size + size/2, (j + 1) * size + size/2), size * 2/5)
            if board[(i, j)] == players[1].num:
                pygame.draw.circle(window, players[1].color, (i * size + size/2, (j + 1) * size + size/2), size * 2/5)

def redraw_window():
    window.fill((0, 0, 255))
    draw_circles()
    players[current].turn()
    pygame.display.update()
def main():
    global board, window, size, current, players
    size = 100
    window = pygame.display.set_mode((7 * size, 7 * size))
    board = create_board()
    current = 0
    print(board)
    flag = True
    clock = pygame.time.Clock()
    players = [0, 0]
    p1 = player((255, 0, 0), 1)
    p2 = player((255, 255, 0), 2)
    players[0] = p1
    players[1] = p2
    while flag:
        clock.tick(10)
        redraw_window()

main()