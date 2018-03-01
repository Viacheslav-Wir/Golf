import pygame
import random
import math
import sys

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x_start, y_start = 170, 68
hit_the_ball = False

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")
dashed_line = pygame.image.load("resources/img/dashed_line.png")

class Particle():
    def __init__(self):
        self.speed = 0
        self.angle = 0
        self.path = [(x_start, height - y_start)]
        self.start_coord = (0, 0)
        self.finish_coord = (0, 0)
        self.do_once_coord = True
        self. do_once_speed = True
        self.angle_rot = 0
        self.angle_line_rot = -45
        self.angle = math.radians(abs(self.angle_line_rot))
        self.club_angles = []


    def get_start_fin_coord(self):
        # Get last coordinate from path befor its empty
        if self.do_once_coord and len(self.path) > 1:
            # print(self.path)
            self.start_coord = self.path[0]
            self.finish_coord = self.path[-1]
            self.do_once_coord = False
            # print(self.start_coord, self.finish_coord)

    def trajectory_display(self):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = self.path[0]
        self.path.pop(0)
        screen.blit(ball, ballrect)

    def start_fin_display(self, coordinate):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = coordinate
        screen.blit(ball, ballrect)

    def club_hit_display(self, image, mcenter):
        # print(self.club_angles, "club_angles")
        while self.club_angles:
            # print("work ")
            club_hit = pygame.USEREVENT+2
            pygame.time.set_timer(club_hit, 11000)
            self.rotage_club(image, self.club_angles[0], mcenter)
            self.club_angles.pop(0)

    def rotage_club(self, image, angle_rot, mcenter):
        # Rotage image - club
        rot_image = pygame.transform.rotate(image, angle_rot)
        rot_rect = rot_image.get_rect(center=mcenter)
        screen.blit(rot_image, rot_rect)
        # Return coordinate-club-right wich impact with ball
        # print(rot_rect.bottomright, "bottomright")
        # print(rot_rect.topleft, "topleft")
        # return rot_rect.bottomright, rot_rect.topleft

    def get_speed_angles(self):
        # Club angle from -220 to 18
        if self.do_once_speed:
            if self.angle_rot <= 0:
                self.speed = (abs(self.angle_rot) + 18) // 2
            else:
                self.speed = (18 - self.angle_rot) // 2
            self.do_once_speed = False
            print(self.speed, "Speed")

    def get_club_angles(self):
        # Club angle from -220 to 18
        if self.angle_rot < 0:
            self.club_angles = [-i for i in range(1, abs(self.angle_rot))] + [j for j in range(19)]
            self.club_angles.sort()
            # print(self.club_angles, "club_angles")
        else:
            self.club_angles = [i for i in range(self.angle_rot+1, 19)]
            # print(self.club_angles, "club_angles")


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
particle = Particle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pressed = pygame.key.get_pressed()
        # Change rotage angle
        if pressed[pygame.K_LEFT]: particle.angle_rot -= 3
            # Bag
            # if abs(particle.angle) > 100:
            #     particle.angle_rot -= 1
            # else:
            #     print("Vse")
        if pressed[pygame.K_RIGHT]:
            if particle.angle_rot < 18: 
                particle.angle_rot += 3
        if pressed[pygame.K_UP]: particle.angle_line_rot += 3
        if pressed[pygame.K_DOWN]: particle.angle_line_rot -= 3
        if pressed[pygame.K_SPACE]: 
            particle.get_speed_angles()
            particle.get_club_angles()
            hit_the_ball = True


        # print(particle.angle_rot, "angle_rot")
        # print(particle.angle_line_rot, "angle_line_rot")

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Create ball trajectory
        particle.get_coordinates(x_start, y_start)
        particle.get_start_fin_coord()

        # Collision club and ball
        if hit_the_ball:
            # print("Impact")
            particle.angle = math.radians(particle.angle_line_rot + 90)
            # print(90 + particle.angle_line_rot, "Diference")
            # print(particle.angle,"angle")
            particle.club_hit_display(golf_club, (110,460))
            if particle.path:
                # print("trajectory")
                particle.rotage_club(golf_club, 18, (110,460))
                particle.trajectory_display()
            else:
                # print("fin")
                particle.rotage_club(golf_club, 18, (110,460))
                particle.start_fin_display(particle.finish_coord)
        if not hit_the_ball:
            # Show start position of ball
            # print("Start")
            particle.rotage_club(golf_club, particle.angle_rot, (110,460))
            particle.rotage_club(dashed_line, particle.angle_line_rot, (165,550))
            particle.start_fin_display((x_start, height - y_start))

        # Move ball with time delay
        ball_apears = pygame.USEREVENT+1
        pygame.time.set_timer(ball_apears, 50)

        # Club moving
        # particle.rotage_club(golf_club, particle.angle_rot)

        pygame.display.flip()
        clock.tick(30)
