import pygame
import random
import math


class cube(object):
    global width, rows
    #rows = 20
    #w = 500
    def __init__(self, start, color = (255, 0, 0)):
        #pos is coordinate tuple
        self.pos = start
        self.dirnx = 0
        self.dirny = 0
        self.color = color
        self.w = width
        self.rows = rows

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis + 1, j*dis, dis-2, dis-2))

class snake(object):
    # list of cube objects
    body = []
    # 2d list of ordered pairs (dirnx, dirny) where every element represents a coordinate
    turns = {}
    moves = []
    limit = 5
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos, (226, 135, 67))
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 0
    def moveQueue(self, move):
        if len(self.moves) < self.limit:
            self.moves.append(move)
    def checkMove(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            """"""
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.moveQueue(pygame.K_LEFT)
                elif keys[pygame.K_RIGHT]:
                    self.moveQueue(pygame.K_RIGHT)
                elif keys[pygame.K_UP]:
                    self.moveQueue(pygame.K_UP)
                elif keys[pygame.K_DOWN]:
                    self.moveQueue(pygame.K_DOWN)
            """"""
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if self.dirnx != 1:
                        self.dirnx = -1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    if self.dirnx != -1:
                        self.dirnx = 1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    if self.dirny != 1:
                        self.dirnx = 0
                        self.dirny = -1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    if self.dirny != -1:
                        self.dirnx = 0
                        self.dirny = 1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        """"""
        if len(self.moves) > 0:
            if self.moves[0] == pygame.K_LEFT:
                if self.dirnx != 1:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif self.moves[0] == pygame.K_RIGHT:
                if self.dirnx != -1:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif self.moves[0] == pygame.K_UP:
                if self.dirny != 1:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif self.moves[0] == pygame.K_DOWN:
                if self.dirny != -1:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            self.moves.pop(0)
        """"""
    def move(self):

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                # cases where it hits the edge it tps to other side
                if c.dirnx == -1 and c.pos[0] <= 0:
                    return False
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    return False
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    return False
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    return False
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)
        return True


    def addCube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny
        self.body.append(cube((tail.pos[0] - dx, tail.pos[1] - dy)))
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global width, rows, s
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack (item):
    global rows
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)
def main():
    global width, rows, s, snack
    width = 600
    rows = 15
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (rows//2, rows//2))
    flag = True
    snack = cube(randomSnack(s), (0, 255, 0))
    clock = pygame.time.Clock()
    t0 = clock.get_time()
    while flag:
        #pygame.time.delay(50)
        clock.tick(16)
        redrawWindow(win)

        flag = s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(s), (0, 255, 0))
        for i, c in enumerate(s.body):
            if i != 0 and s.body[0].pos == c.pos:
                flag = False
                break

main()