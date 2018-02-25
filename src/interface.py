import pygame
import pymunk
import random
import math
import sys
# import figure_etc

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done = False
x_speed, y_speed = 5, 5

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")

class Particle():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0

    # def display(self):
    #     pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
    def display(self, ball):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = self.x, self.y
        screen.blit(ball, ballrect)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle

        if self.y > height - 60 - self.size:
            self.y = 2*(height - 60 - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle

x, y, size = 150, 560, 10
particle = Particle(x, y, size)
particle.speed = 10
particle.angle = random.uniform(0, math.pi*2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # screen.blit(ball, ballrect)

        # screen.blit(golf_club, (30, 0))
        particle.move()
        particle.bounce()
        particle.display(ball)
        
        pygame.display.flip()
        clock.tick(60)
