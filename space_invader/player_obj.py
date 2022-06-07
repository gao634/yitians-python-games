import pygame
import keyboard
class Player:
    dec = 0.003
    acc = 0.005
    v_max = 1.5
    def __init__(self, icon, x, y, x_vel, y_vel, x_acc, y_acc):
        self.icon = pygame.image.load(icon)
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

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

