import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-spaceship.png')

player = pygame.image.load('001-spaceship.png')
playerX = 370
playerY = 480
x_vel = 0.3
x_change = 0

score_value = 0
font_s = pygame.font.Font('freesansbold.ttf', 32)
sX = 10
sY = 10

font_g = pygame.font.Font('freesansbold.ttf', 64)
gX = 250
gY = 250

def game_over_display(x, y):
    text = font_g.render("Game Over", True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_score(x, y):
    score = font_s.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

enemy = []
eX = []
eY = []
eX_change = []
num_enemies = 6
eX_max_vel = 0.1
for i in range(num_enemies):
    enemy.append(pygame.image.load('001-arcade-game.png'))
    enemy[i] = pygame.transform.rotate(enemy[i], 180)
    eX.append(random.randint(0, 736))
    eY.append(random.randint(50, 150))
    eX_change.append((random.randint(0, 1) * 2 - 1) * eX_max_vel)
eY_change = 0.03
eY_acc = 0.0005
eX_acc = 0.005

bullet = pygame.image.load('001-bullet.png')
bullet = pygame.transform.rotate(bullet, 90)
bX = playerX
bY = playerY
bY_change = 0.7
bullet_vis = False
alpha = 255
alpha_change = 255
def player_display():
    screen.blit(player, (playerX, playerY))

def enemy_display(i):
    screen.blit(enemy[i], (eX[i], eY[i]))

def fire_bullet():
    global bullet_vis
    bullet_vis = True
    screen.blit(bullet, (bX, bY))

def is_collision(eX, eY, bX, bY):
    distance = math.sqrt(math.pow(eX-bX, 2) + math.pow(eY-bY, 2))
    if distance <= 30:
        return True
    return False

def game_over_animation(i, alpha):
    for j in range(num_enemies):
        if j != i:
            enemy[j].set_alpha(alpha)
pygame.display.set_icon(icon)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -x_vel
            elif event.key == pygame.K_RIGHT:
                x_change = x_vel
            if event.key == pygame.K_SPACE:
                if bullet_vis == False:
                    bY = playerY
                    bX = playerX
                    bullet_vis = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 0
    playerX += x_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    screen.fill((0, 0, 0))
    player_display()
    for i in range(num_enemies):
        eX[i] += eX_change[i]
        eY[i] += eY_change
        if eX[i] <= 0:
            eX_change[i] = eX_max_vel
        if eX[i] >= 736:
            eX_change[i] = -eX_max_vel
        enemy_display(i)
        if eY[i] > playerY - 60:
            game_over_display(gX, gY)
            #for j in range(int(255/alpha_change) + 1):
            #    game_over_animation(i, alpha)
            #    alpha -= alpha_change
            #    pygame.display.update()
            for j in range(num_enemies):
                if j != i:
                    enemy[j].set_alpha(0)
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
    if bullet_vis == True:
        fire_bullet()
        bY -= bY_change
    if bY <= 0:
        bY = playerY
        bX = playerX
        bullet_vis = False
    for i in range(num_enemies):
        if is_collision(eX[i], eY[i], bX, bY):
            bullet_vis = False
            score_value += 1
            bY = playerY
            bX = playerX
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 150)
            eX_max_vel += eX_acc
            eY_change += eY_acc
            eX_change[i] = (random.randint(0, 1) * 2 - 1) * eX_max_vel
    show_score(sX, sY)
    pygame.display.update()
