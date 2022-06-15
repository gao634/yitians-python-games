import pygame
class player(object):
    pieces = []
    column = 3
    def __init__(self, color):
        self.color = color

def turn(player):
    pygame.draw.circle(window, player.color, (player.column * size + size / 2, size / 2), size * 2 / 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                if player.column > 0:
                    player.column -= 1
                    print(player.column)
            elif keys[pygame.K_RIGHT]:
                if player.column < 6:
                    player.column += 1
                    print(player.column)



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

def redraw_window(current):
    window.fill((0, 0, 255))
    draw_circles()
    turn(current)
    pygame.display.update()
def main():
    global board, window, size, p1, p2
    size = 100
    window = pygame.display.set_mode((7 * size, 7 * size))
    board = create_board()
    print(board)
    flag = True
    clock = pygame.time.Clock()
    p1 = player((255, 0, 0))
    p2 = player((255, 255, 0))
    current = p1
    while flag:
        clock.tick(10)
        redraw_window(current)

main()