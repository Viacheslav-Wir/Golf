import math
import random
# from interface import 

x_start = 60
y_start = 640 - 480
x_finish = 1000
angle_start = math.radians(45)
speed_start = 87
path = []

def get_coordinates():
    time = 0
    while True:
        time += 0.1
        x = x_start + speed_start * time * math.cos(angle_start)
        y = y_start + speed_start * time * math.sin(angle_start) - 1/2 * 9.8 * time**2
        if target_hit(x_finish, x):
            print("Congratulation you hit!")
            break
        else:
            if y_start > y:
                # print(path)
                time = 2 * speed_start * math.sin(angle_start) / 9.8
                x = x_start + speed_start * time * math.cos(angle_start)
                path.append((x, 640 - y_start))
                return path
            path.append((x, 640 - y))


def target_hit(target_x, ball_x):
    temp = [-2,-1,0,1,2]
    for i in temp:
        # print(target_x + i, int(ball_x))
        if target_x + i == int(ball_x):
            return True
    return False


print(get_coordinates())