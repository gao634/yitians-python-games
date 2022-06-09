import pygame
import keyboard
class Player:
    dec = 0.003
    acc = 0.005
    v_max = 1.5
    x_vel = 0
    y_vel = 0
    x_acc = 0
    y_acc = 0
    def __init__(self, icon_name, x, y):
        self.icon_name = icon_name
        self.icon = pygame.image.load(icon_name)
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

    def set_icon(self, icon_name):
        self.icon_name = icon_name
        self.icon = pygame.image.load(icon_name)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_
    def display(self, screen):
        screen.blit(self.icon, (self.x, self.y))

    def acceleration(self):
        if keyboard.is_pressed("left arrow"):
            if self.x_acc > -self.v_max:
                self.x_acc = -self.acc
        if keyboard.is_pressed("right arrow"):
            if self.x_acc < self.v_max:
                self.x_acc = self.acc
        if keyboard.is_pressed("up arrow"):
            if self.y_acc > -self.v_max:
                self.y_acc = -self.acc
        if keyboard.is_pressed("down arrow"):
            if self.y_acc < self.v_max:
                self.y_acc = self.acc

    def deceleration(self):
        if self.x_vel < 0:
            if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
                self.x_vel += self.dec
        elif self.x_vel > 0:
            if not keyboard.is_pressed("left arrow") and not keyboard.is_pressed("right arrow"):
                self.x_vel += -self.dec
        if self.y_vel < 0:
            if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
                self.y_vel += self.dec
        elif self.y_vel > 0:
            if not keyboard.is_pressed("up arrow") and not keyboard.is_pressed("down arrow"):
                self.y_vel += -self.dec

    def