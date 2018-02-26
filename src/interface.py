import pygame
import pymunk
import random
import math
import sys
# import time
# import figure_etc

temp = [(60, 548), (90.75914498161482, 518.4658550183851), (121.51828996322965, 491.3817100367704), (152.27743494484446, 466.7475650551555), (183.0365799264593, 444.5634200735408), (213.7957249080741, 424.8292750919259), (244.55486988968892, 407.5451301103111), (275.3140148713037, 392.7109851286963), (306.0731598529186, 380.3268401470815), (336.8323048345334, 370.3926951654667), (367.5914498161482, 362.90855018385184), (398.350594797763, 357.8744052022371), (429.10973977937783, 355.29026022062226), (459.86888476099267, 355.15611523900736), (490.62802974260745, 357.4719702573926), (521.3871747242223, 362.2378252757778), (552.1463197058372, 369.45368029416306), (582.905464687452, 379.1195353125482), (613.6646096690667, 391.2353903309334), (644.4237546506815, 405.8012453493185), (675.1828996322964, 422.81710036770374), (705.9420446139112, 442.28295538608893), (736.701189595526, 464.1988104044742), (767.4603345771409, 488.5646654228593), (798.2194795587557, 515.3805204412445), (828.9786245403704, 544.6463754596297), (832.34693877551, 548), (847.7265112663174, 533.8454275091926), (863.1060837571248, 522.1408550183852), (878.4856562479322, 512.8862825275778), (893.8652287387397, 506.08171003677035), (909.2448012295471, 501.72713754596293), (924.6243737203545, 499.82256505515556), (940.0039462111619, 500.3679925643481), (955.3835187019693, 503.36342007354074), (970.7630911927768, 508.80884758273334), (986.1426636835841, 516.704275091926), (1001.5222361743915, 527.0497026011185), (1016.9018086651989, 539.8451301103111), (1025.4336734693875, 548), (1033.1234597147911, 541.5352137545963), (1040.813245960195, 537.5204275091926), (1048.5030322055986, 535.955641263789), (1056.1928184510023, 536.8408550183851), (1063.882604696406, 540.1760687729815), (1071.5723909418098, 545.9612825275777), (1073.7053571428569, 548), (1077.5502502655588, 545.3801068772982), (1081.3951433882605, 545.2102137545963), (1085.2400365109625, 547.4903206318944), (1085.7732780612241, 548), (1087.695724622575, 547.302553438649), (1088.790258290816, 548), (1089.544503348214, 548), (1089.7330646125636, 548)]


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
        self.speed = 1
        self.angle = 0

    def display(self, ball):
        ballrect = ball.get_rect()
        ballrect.right, ballrect.bottom = self.x, self.y
        screen.blit(ball, ballrect)

    def move(self):
        self.x = self.x + self.speed * mtime * math.cos(self.angle)
        self.y = self.y + self.speed * mtime * math.sin(self.angle) - 1/2 * 9.8 * mtime**2

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
mtime = 0
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
        mtime += 1
        particle.move()
        particle.bounce()
        particle.display(ball)

        for i in temp:
            ball_apears = pygame.USEREVENT+1
            pygame.time.set_timer(ball_apears,1000)
            # time.sleep(0.25)
            screen.blit(ball, i)
            pass
        
        pygame.display.flip()
        clock.tick(30)

