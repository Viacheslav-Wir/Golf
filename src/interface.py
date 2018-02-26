import pygame
import random
import math
import sys
# import time
# import figure_etc

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x_start, y_start = 60, 92
angle_start = math.radians(45)
speed_start = 87

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")

class Particle():
    def __init__(self, angle, speed):
        self.speed = speed
        self.angle = angle
        self.path = [(x_start, height - y_start)]

    def display(self, ball):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = self.path[0]
        self.path.pop(0)
        screen.blit(ball, ballrect)

    def get_coordinates(self, x_start, y_start):
        # print("x_start, y_start ", x_start, y_start)
        time = 0
        while True:
            time += 0.5
            self.x = x_start + self.speed * time * math.cos(self.angle)
            self.y = y_start + self.speed * time * math.sin(self.angle) - 1/2 * 9.8 * time**2
            # print(self.x, self.y)
            if self.x > width or self.x < 0 or self.speed < 1:
                break
            if y_start > self.y:
                time = 2 * self.speed * math.sin(self.angle) / 9.8
                self.x = x_start + self.speed * time * math.cos(self.angle)
                # self.path.append((self.x, y_start))
                self.path.append((self.x, height - y_start))
                self.speed /= 2
                self.get_coordinates(self.x, y_start)
            else:
                self.path.append((self.x, height - self.y))
                # self.path.append((self.x, self.y))

mtime = 0
particle = Particle(angle_start, speed_start)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # screen.blit(ball, ballrect)

        # screen.blit(golf_club, (30, 0))
        mtime += 1
        particle.get_coordinates(x_start, y_start)
        # print(particle.path)
        particle.display(ball)
        # Move ball with time delay
        ball_apears = pygame.USEREVENT+1
        pygame.time.set_timer(ball_apears,80)

        
        pygame.display.flip()
        clock.tick(30)

