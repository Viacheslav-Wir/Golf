import pygame
import random
import math
import sys

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x_start, y_start = 170, 68
# x_club, y_club = 125, 570
angle_start = math.radians(45)
speed_start = 87
angle_rot = 0

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")

class Particle():
    def __init__(self, angle, speed):
        self.speed = speed
        self.angle = angle
        self.path = [(x_start, height - y_start)]
        self.last_coord = (0, 0)

    def finish_coord(self):
        # Get last coordinate from path befor its empty
        if len(self.path) > 1:
            self.last_coord = self.path[-1]

    def display(self):
        # Display ball trajectory
        ballrect = ball.get_rect()
        if self.path:
            ballrect.right, ballrect.bottom = self.path[0]
            temp = self.path.pop(0)
            # print(temp)
            screen.blit(ball, ballrect)
        else:
            # Show last place of ball
            ballrect.right, ballrect.bottom = self.last_coord
            screen.blit(ball, ballrect)

    def rotage_c(self, image, angle):
        # Rotage image - club
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=(110,460))
        screen.blit(rot_image, rot_rect)
        # Return coordinate-club-right wich impact with ball
        return rot_rect.right

    def get_coordinates(self, x_start, y_start):
        # Create ball trajectory
        time = 0
        while True:
            time += 0.5
            self.x = x_start + self.speed * time * math.cos(self.angle)
            self.y = y_start + self.speed * time * math.sin(self.angle) - 1/2 * 9.8 * time**2
            if self.x > width or self.x < 0 or self.speed < 1:
                break
            if y_start > self.y:
                time = 2 * self.speed * math.sin(self.angle) / 9.8
                self.x = x_start + self.speed * time * math.cos(self.angle)
                self.path.append((self.x, height - y_start))
                # self.path.append((self.x, y_start))
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

        pressed = pygame.key.get_pressed()
        # Change ratage angle
        if pressed[pygame.K_LEFT]: angle_rot -= 3
        if pressed[pygame.K_RIGHT]: angle_rot += 3

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Create ball trajectory
        particle.get_coordinates(x_start, y_start)
        particle.finish_coord()

        # Collision club and ball
        if particle.rotage_c(golf_club, angle_rot) - 0 > x_start:
            particle.display()
        else:
            # Show first place of ball
            ballrect = ball.get_rect()
            ballrect.right, ballrect.bottom = x_start, height - y_start
            screen.blit(ball, ballrect)

        # Move ball with time delay
        ball_apears = pygame.USEREVENT+1
        pygame.time.set_timer(ball_apears, 100)

        # Club moving
        particle.rotage_c(golf_club, angle_rot)

        pygame.display.flip()
        clock.tick(30)
