import pygame
def create_board():
    board = {}
    for i in range(6):
        for j in range(7):
            board[(i, j)] = 0
    return board

def main():
    size = 100
    window = pygame.display.set_mode((6 * size, 7 * size))
    flag = True
    while flag:
        for e in pygame.events

main()