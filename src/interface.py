import pygame
# import pymunk
# import figure_etc

pygame.init()
screen = pygame.display.set_mode((1280, 640))
done = False
is_blue = True
# x = 35
# y = 35
# temp = []

clock = pygame.time.Clock()
background = pygame.image.load("resources/img/background.png")
ball = pygame.image.load("resources/img/ball.png")
golf_club = pygame.image.load("resources/img/golf-club.png")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #                 is_blue = not is_blue
        
        # pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]: y -= 3
        # if pressed[pygame.K_DOWN]: y += 3
        # if pressed[pygame.K_LEFT]: x -= 3
        # if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))

        # Set display background
        screen.blit(background, (0, 0))
        screen.blit(ball, (60, 480))
        screen.blit(golf_club, (30, 0))

        # for i in temp:
        #     screen.blit(ball, (i))

        if is_blue: 
            color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        
        pygame.display.flip()
        clock.tick(60)