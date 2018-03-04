import pygame
import math

class Mechanics():
    def __init__(self, x, y, y_improve, screen, ball):
        self.ball = ball
        self.screen = screen
        self.x_start = x
        self.y_start = y
        self.y_improve = y_improve
        self.path = [(self.x_start, self.y_improve)]
        self.finish_coord = (0, 0)
        self.speed = 1
        self.do_once_coord = True
        self.do_once_speed = True
        self.flag_status = False
        self.angle_club_rot = 0
        self.angle_line_rot = -45
        self.angle = math.radians(abs(self.angle_line_rot))
        self.club_angles = []
        self.hole_start = 1050
        self.club_center = (110,460)
        self.dashed_line_center = (165,550)
        # self.walls = []
        self.hit_coord = []

    def trajectory_display(self, ):
        ballrect = self.ball.get_rect()
        ballrect.right, ballrect.bottom = self.path[0]
        self.path.pop(0)
        self.screen.blit(self.ball, ballrect)
        game_period = pygame.USEREVENT+1
        pygame.time.set_timer(game_period, 1)

    def start_fin_display(self, coordinate):
        ballrect = self.ball.get_rect()
        ballrect.right, ballrect.bottom = coordinate
        self.screen.blit(self.ball, ballrect)

    def club_hit_display(self, image, mcenter):
        while self.club_angles:
            club_hit = pygame.USEREVENT+2
            pygame.time.set_timer(club_hit, 11000)
            self.rotage_smthn(image, self.club_angles[0], mcenter)
            self.club_angles.pop(0)

    def hole_display(self):
        pygame.draw.line(self.screen, (0, 0, 0), [self.hole_start, self.y_improve], [self.hole_start, self.y_improve+38], 4)
        pygame.draw.line(self.screen, (0, 0, 0), [self.hole_start, self.y_improve+38], [self.hole_start+35, self.y_improve+38], 4)
        pygame.draw.line(self.screen, (0, 0, 0), [self.hole_start+35, self.y_improve+38], [self.hole_start+35, self.y_improve], 4)

    def rotage_smthn(self, image, angle_club_rot, mcenter):
        # Rotage image - club
        rot_image = pygame.transform.rotate(image, angle_club_rot)
        rot_rect = rot_image.get_rect(center=mcenter)
        self.screen.blit(rot_image, rot_rect)

    # def get_walls(self, clist):
    #     self.walls.extend([(x, self.y_improve) for x in range(0, clist[0][0])])
    #     self.walls.extend([(clist[0][0], y) for y in range(self.y_improve, clist[1][1])])
    #     self.walls.extend([(x, clist[1][1]) for x in range(clist[0][0], clist[2][0])])
    #     self.walls.extend([(clist[2][0], clist[1][1]-num) for num in range(clist[1][1] - self.y_improve)])
    #     self.walls.extend([(x, self.y_improve) for x in range(clist[2][0], 1281)])
    #     self.walls.sort()
        # print(self.walls)

    def get_speed_angles(self):
        # Club angle from -220 to 18
        if self.do_once_speed:
            if self.angle_club_rot <= 0:
                self.speed = (abs(self.angle_club_rot) + 18) // 2
            else:
                self.speed = (18 - self.angle_club_rot) // 2
            self.do_once_speed = False

    def check_win(self):
        self.hit_coord = [y for y in range(1051,1085)]
        for i in self.path:
            if int(i[0]) in self.hit_coord and int(i[1]) == self.y_improve:
                self.path = self.path[:self.path.index(i)+1]
                self.finish_coord = (1084, 608)
                self.flag_status = True
                break
            else:
                self.finish_coord = self.path[-1]

    def get_club_angles(self):
        # Club angle from -220 to 18
        if self.angle_club_rot < 0:
            self.club_angles = [-i for i in range(1, abs(self.angle_club_rot))] + [j for j in range(19)]
            self.club_angles.sort()
        else:
            self.club_angles = [i for i in range(self.angle_club_rot+1, 19)]


    def get_trajectory(self, x_start, y_start, height):
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
                self.path.append((self.x, self.y_improve))
                self.speed //= 2
                self.get_trajectory(self.x, y_start, height)
            else:
                self.path.append((self.x, height - self.y))

    def reset(self):
        self.speed = 1
        self.path = [(self.x_start, self.y_improve)]
        self.do_once_coord = True
        self.do_once_speed = True
        self.flag_status = False
        self.angle_club_rot = 0
