import pygame
import random
import math
import sys

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x_start, y_start = 170, 68
y_improve = height - y_start
hit_the_ball = False

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")
dashed_line = pygame.image.load("resources/img/dashed_line.png")
flag_start = pygame.image.load("resources/img/flag_start.png")
flag_finish = pygame.image.load("resources/img/flag_finish.png")

class Particle():
    def __init__(self):
        self.speed = 1
        self.angle = 0
        self.path = [(x_start, y_improve)]
        self.finish_coord = (0, 0)
        self.do_once_coord = True
        self. do_once_speed = True
        self.flag_status = False
        self.angle_rot = 0
        self.angle_line_rot = -45
        self.angle = math.radians(abs(self.angle_line_rot))
        self.club_angles = []
        self.hole_start = 1050
        self.walls = []
        self.hit_coord = []

    def trajectory_display(self):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = self.path[0]
        self.path.pop(0)
        screen.blit(ball, ballrect)
        game_period = pygame.USEREVENT+1
        pygame.time.set_timer(game_period, 1)

    def start_fin_display(self, coordinate):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = coordinate
        screen.blit(ball, ballrect)

    def club_hit_display(self, image, mcenter):
        while self.club_angles:
            club_hit = pygame.USEREVENT+2
            pygame.time.set_timer(club_hit, 11000)
            self.rotage_smthn(image, self.club_angles[0], mcenter)
            self.club_angles.pop(0)

    def hole_display(self):
        pygame.draw.line(screen, (0, 0, 0), [self.hole_start, y_improve], [self.hole_start, y_improve+38], 3)
        pygame.draw.line(screen, (0, 0, 0), [self.hole_start, y_improve+38], [self.hole_start+35, y_improve+38], 3)
        pygame.draw.line(screen, (0, 0, 0), [self.hole_start+35, y_improve+38], [self.hole_start+35, y_improve], 3)

    def rotage_smthn(self, image, angle_rot, mcenter):
        # Rotage image - club
        rot_image = pygame.transform.rotate(image, angle_rot)
        rot_rect = rot_image.get_rect(center=mcenter)
        screen.blit(rot_image, rot_rect)

    # def get_walls(self, clist):
    #     self.walls.extend([(x, y_improve) for x in range(0, clist[0][0])])
    #     self.walls.extend([(clist[0][0], y) for y in range(y_improve, clist[1][1])])
    #     self.walls.extend([(x, clist[1][1]) for x in range(clist[0][0], clist[2][0])])
    #     self.walls.extend([(clist[2][0], clist[1][1]-num) for num in range(clist[1][1] - y_improve)])
    #     self.walls.extend([(x, y_improve) for x in range(clist[2][0], 1281)])
    #     self.walls.sort()
        # print(self.walls)

    def get_speed_angles(self):
        # Club angle from -220 to 18
        if self.do_once_speed:
            if self.angle_rot <= 0:
                self.speed = (abs(self.angle_rot) + 18) // 2
            else:
                self.speed = (18 - self.angle_rot) // 2
            self.do_once_speed = False

    def check_win(self):
        self.hit_coord = [y for y in range(1051,1085)]
        for i in self.path:
            if int(i[0]) in self.hit_coord and int(i[1]) == y_improve:
                self.path = self.path[:self.path.index(i)+1]
                self.finish_coord = (1084, 608)
                self.flag_status = True
                break
            else:
                self.finish_coord = self.path[-1]

    # def out_of_screen(self, x_coord):
    #     for i in self.path:
    #         if int(i[0]) > width or int(i[0]) < 0:
    #             print(self.path, "Before")
    #             self.path = self.path[:self.path.index(i)+1]
    #             print(particle.path, "After")
    #             break
    #         else:
    #             print("Didnt work")

    def get_club_angles(self):
        # Club angle from -220 to 18
        if self.angle_rot < 0:
            self.club_angles = [-i for i in range(1, abs(self.angle_rot))] + [j for j in range(19)]
            self.club_angles.sort()
        else:
            self.club_angles = [i for i in range(self.angle_rot+1, 19)]

    def get_trajectory(self, x_start, y_start):
        # Create ball trajectory
        time = 0
        while True:
            time += 0.5
            self.x = x_start + self.speed * time * math.cos(self.angle)
            self.y = y_start + self.speed * time * math.sin(self.angle) - 1/2 * 9.8 * time**2
            if self.speed < 1:
                break
            if y_start > self.y:
                time = 2 * self.speed * math.sin(self.angle) / 9.8
                self.x = x_start + self.speed * time * math.cos(self.angle)
                self.path.append((self.x, y_improve))
                self.speed //= 2
                self.get_trajectory(self.x, y_start)
            else:
                self.path.append((self.x, height - self.y))

mtime = 0
particle = Particle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pressed = pygame.key.get_pressed()
        # Change rotage angle
        if pressed[pygame.K_LEFT]:
            if particle.angle_rot > -220:
                particle.angle_rot -= 3
            # particle.get_walls([(1050,572),(1085,606),(1085,606),(1050,572)])
        if pressed[pygame.K_RIGHT]:
            if particle.angle_rot < 18: 
                particle.angle_rot += 3
        if pressed[pygame.K_UP]:
            print(particle.angle_line_rot)
            if particle.angle_line_rot < 0:
                particle.angle_line_rot += 3
        if pressed[pygame.K_DOWN]:
            print(particle.angle_line_rot)
            if particle.angle_line_rot > -80:
                particle.angle_line_rot -= 3
        if pressed[pygame.K_SPACE]:
            particle.get_trajectory(x_start, y_start)
            particle.check_win()
            particle.get_speed_angles()
            particle.get_club_angles()
            hit_the_ball = True

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # Display hole
        particle.hole_display()

        # Collision club and ball
        if hit_the_ball:
            particle.angle = math.radians(particle.angle_line_rot + 90)
            particle.club_hit_display(golf_club, (110,460))
            if particle.path:
                # print("Trajectory")
                screen.blit(flag_start, (1059, 460))
                particle.rotage_smthn(golf_club, 18, (110,460))
                particle.trajectory_display()
            else:
                # print("Finish")
                if particle.flag_status:
                    screen.blit(flag_finish, (1059, 460))
                else:
                    screen.blit(flag_start, (1059, 460))
                particle.rotage_smthn(golf_club, 18, (110,460))
                particle.start_fin_display(particle.finish_coord)
        if not hit_the_ball:
            # print("Start")
            # Club rotage
            screen.blit(flag_start, (1059, 460))
            particle.rotage_smthn(golf_club, particle.angle_rot, (110,460))
            # Dashed line rotage
            particle.rotage_smthn(dashed_line, particle.angle_line_rot, (165,550))
            # Show start position of ball
            particle.start_fin_display((x_start, y_improve))

        # Time delay
        game_period = pygame.USEREVENT+1
        pygame.time.set_timer(game_period, 50)

        pygame.display.flip()
        clock.tick(30)
