import pygame
import math
import sys
import mechanics as m
import menu

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x_start, y_start = 170, 68
y_improve = height - y_start
show_menu = True
hit_the_ball = False

background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")
dashed_line = pygame.image.load("resources/img/dashed_line.png")
flag_start = pygame.image.load("resources/img/flag_start.png")
flag_finish = pygame.image.load("resources/img/flag_finish.png")

action = m.Mechanics(x_start, y_start, y_improve, screen, ball)
my_menu = menu.Menu(screen)

while True:
    if show_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and my_menu.help_status == True:
                my_menu.help_status = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RETURN]:
                if my_menu.id == 1:
                    show_menu = False
                elif my_menu.id == 2:
                    my_menu.help_status = True
                elif my_menu.id == 3:
                    sys.exit()
            if pressed[pygame.K_UP]:
                if my_menu.id == 0:
                    my_menu.id = 1
                elif my_menu.id == 1:
                    my_menu.id = 3
                else:
                    my_menu.id -= 1
            if pressed[pygame.K_DOWN]:
                if my_menu.id == 3:
                    my_menu.id = 1
                else:
                    my_menu.id += 1

            screen.fill((0, 0, 0))
            screen.blit(menu.background_menu, (0, 0))
            if not my_menu.help_status:
                my_menu.focus_highlight([900,100,200,70], "Play", (935,110), 1)
                my_menu.focus_highlight([900,200,200,70], "Readme", (910,210), 2)
                my_menu.focus_highlight([900,300,200,70], "Exit", (935,310), 3)
            else:
                pygame.draw.rect(screen, menu.WHITE, [280,120,700,350])
                my_menu.show_help()

            pygame.display.flip()
            clock.tick(700)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            pressed = pygame.key.get_pressed()
            # Change rotage angle
            if pressed[pygame.K_LEFT]:
                # print(pygame.Surface.get_size(golf_club))
                if action.angle_club_rot > -220:
                    action.angle_club_rot -= 3
                # action.get_walls([(1050,572),(1085,606),(1085,606),(1050,572)])
            if pressed[pygame.K_RIGHT]:
                if action.angle_club_rot < 18: 
                    action.angle_club_rot += 3
            if pressed[pygame.K_UP]:
                if action.angle_line_rot < 0:
                    action.angle_line_rot += 3
            if pressed[pygame.K_DOWN]:
                if action.angle_line_rot > -80:
                    action.angle_line_rot -= 3
            if pressed[pygame.K_SPACE]:
                action.get_trajectory(x_start, y_start, height)
                action.check_win()
                action.get_speed_angles()
                action.get_club_angles()
                hit_the_ball = True
            if pressed[pygame.K_BACKSPACE]:
                    hit_the_ball = False
                    action.reset()

            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            # Display hole
            action.hole_display()

            # Collision club and ball
            if hit_the_ball:
                action.angle = math.radians(action.angle_line_rot + 90)
                action.club_hit_display(golf_club, action.club_center)
                if action.path:
                    # print("Trajectory")
                    screen.blit(flag_start, (1059, 460))
                    action.rotage_smthn(golf_club, 18, action.club_center)
                    action.trajectory_display()
                else:
                    # print("Finish")
                    if action.flag_status:
                        screen.blit(flag_finish, (1059, 460))
                    else:
                        screen.blit(flag_start, (1059, 460))
                    action.rotage_smthn(golf_club, 18, action.club_center)
                    action.start_fin_display(action.finish_coord)
            if not hit_the_ball:
                # print("Start")
                # Club rotage
                screen.blit(flag_start, (1059, 460))
                action.rotage_smthn(golf_club, action.angle_club_rot, action.club_center)
                # Dashed line rotage
                action.rotage_smthn(dashed_line, action.angle_line_rot, action.dashed_line_center)
                # Show start position of ball
                action.start_fin_display((x_start, y_improve))

            # Time delay
            game_period = pygame.USEREVENT+1
            pygame.time.set_timer(game_period, 50)

            pygame.display.flip()
            clock.tick(30)
