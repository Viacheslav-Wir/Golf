import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 640))
done = False
is_blue = True
x = 30
y = 35

clock = pygame.time.Clock()
background = pygame.image.load("../resources/img/background.png")
ball = pygame.image.load("../resources/img/ball.png")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        # screen.fill((0, 0, 0))

        # Set display background
        screen.blit(background, (0, 0))
        screen.blit(ball, (20, 20))

        if is_blue: 
            color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 180, 180))

        
        pygame.display.flip()
        clock.tick(60)