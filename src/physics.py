import math
import random

x_start = 60
y_start = 92
# x_finish = 1000
width = 1280
height = 640
angle_start = math.radians(45)
speed_start = 87

class BallPhysics():
    def __init__(self, angle, speed):
        self.angle = angle
        self.speed = speed
        self.path = [(x_start, height - y_start)]

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

        return self.path
        # print(self.path)

    def draw(self, x, y):
        screen.blit(ball, (x, y))

ball = BallPhysics(angle_start, speed_start)
ball.get_coordinates(x_start, y_start)


# def target_hit(target_x, ball_x):
#     temp = [-2,-1,0,1,2]
#     for i in temp:
#         # print(target_x + i, int(ball_x))
#         if target_x + i == int(ball_x):
#             return True
#     return False
