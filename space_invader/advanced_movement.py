import pygame
import keyboard

pygame.init()
length = 1200
height = 950
screen = pygame.display.set_mode((length, height))
running = True
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-spaceship.png')
player = pygame.image.load('001-spaceship.png')
x_pos = 540
y_pos = 480
x_vel = 0
y_vel = 0
x_acc = 0
y_acc = 0

# can be manipulated for different terrain
dec = 0.003
acc = 0.005
v_max = 1.5

pygame.display.set_icon(icon)

def player_display():
    screen.blit(player, (x_pos, y_pos))

def acceleration():
    if keyboard.is_pressed("left arrow"):
        if x_acc > -v_max:
            x_acc = -acc
    if keyboard.is_pressed("right arrow"):
        if x_acc < v_max:
            x_acc = acc
    if keyboard.is_pressed("up arrow"):
        if y_acc > -v_max:
            y_acc = -acc
    if keyboard.is_pressed("down arrow"):
        if y_acc < v_max:
            y_acc = acc
def deceleration(x_vel, y_vel):
    if x_vel < 0:
        if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
            x_vel += dec
    elif x_vel > 0:
        if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
            x_vel += -dec
    if y_vel < 0:
        if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
            y_vel += dec
    elif y_vel > 0:
        if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
            y_vel += -dec

while running:
    x_acc = 0
    y_acc = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keyboard.is_pressed("left arrow"):
        if keyboard.is_pressed("right arrow"):
            x_acc = 0
        else:
            x_acc = -acc
    elif keyboard.is_pressed("right arrow"):
        if keyboard.is_pressed("left arrow"):
            x_acc = 0
        else:
            x_acc = acc
    if keyboard.is_pressed("up arrow"):
        if keyboard.is_pressed("down arrow"):
            y_acc = 0
        else:
            y_acc = -acc
    elif keyboard.is_pressed("down arrow"):
        if keyboard.is_pressed("up arrow"):
            y_acc = 0
        else:
            y_acc = acc
    if x_vel < 1 and x_vel > -1:
        x_vel += x_acc
    if y_vel < 1 and y_vel > -1:
        y_vel += y_acc
    if x_vel < 0:
        if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
            x_vel += dec
    elif x_vel > 0:
        if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
            x_vel += -dec
    if y_vel < 0:
        if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
            y_vel += dec
    elif y_vel > 0:
        if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
            y_vel += -dec
    if x_pos > length - 65 and x_vel < 0:
        x_pos += x_vel
    elif x_pos < 5 and x_vel > 0:
        x_pos += x_vel
    elif x_pos < length - 65 and x_pos > 5:
        x_pos += x_vel
    if y_pos > height - 60 and y_vel < 0:
        y_pos += y_vel
    elif y_pos < 5 and y_vel > 0:
        y_pos += y_vel
    elif y_pos < height - 60 and y_pos > 5:
        y_pos += y_vel

    screen.fill((255, 255, 255))
    player_display()
    pygame.display.update()
