import pygame
import keyboard

current = 0
class player(object):
    pieces = []
    column = 3
    def __init__(self, color, num):
        self.color = color
        self.num = num

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
def place(player):
    #print("called")
    for i in range(6):
        if board[player.column, i] != 0:
            board[player.column, i - 1] = player.num
            player.pieces.append((player.column, i - 1))
            break
        elif i == 5:
            board[player.column, i] = player.num
            player.pieces.append((player.column, i))
def turn(player):
    global current
    #print(current)
    pygame.draw.circle(window, player.color, (player.column * size + size / 2, size / 2), size * 2 / 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()

    if keyboard.is_pressed("left arrow"):
        if player.column > 0:
            player.column -= 1
            #pygame.time.wait(250)
    if keyboard.is_pressed("right arrow"):
        if player.column < 6:
            player.column += 1
            #pygame.time.wait(250)
    if keyboard.is_pressed("space"):
        if board[player.column, 0] == 0:
            place(player)
            current = player.num - 2
            players[current].column = 3
            #pygame.time.wait(250)
            #print(board)
def redraw_window():
    window.fill((0, 0, 255))
    draw_circles()
    turn(players[current])
    pygame.display.update()
def check_win(player):
    if len(player.pieces) >= 4:

def main():
    global board, window, size, current, players
    size = 100
    window = pygame.display.set_mode((7 * size, 7 * size))
    board = create_board()
    print(board)
    flag = True
    clock = pygame.time.Clock()
    players = [0, 0]
    p1 = player((255, 0, 0), 1)
    p2 = player((255, 255, 0), 2)
    players[0] = p1
    players[1] = p2
    while flag:
        clock.tick(5)
        redraw_window()

main()