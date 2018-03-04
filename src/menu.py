import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)

background_menu = pygame.image.load("resources/img/background_menu.jpg")

class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.help_status = False
        self.id = 0

    def show_help(self):
        with open("resources/Help.txt", 'r') as f:
            text = f.readline()
        position = (280,120)
        for num, line in enumerate(text.split("%")):
            if num == 1:
                position = (position[0], position[1]+65)
                self.draw_text(line, position, 35)
            elif num == 2:
                position = (position[0], position[1]+65)
                self.draw_text(line, position, 35)
            elif num == 3:
                position = (position[0], position[1]+65)
                self.draw_text(line, position, 35)
            elif num == 4:
                position = (position[0], position[1]+65)
                self.draw_text(line, position, 35)
            else:
                position = (position[0], position[1])
                self.draw_text(line, position, 35)

    def draw_text(self, text, coord_text, size, color=BLACK):
        pygame.font.init()
        font_param = pygame.font.SysFont("monospace", size)
        font_surf = font_param.render(text, True, color)
        self.screen.blit(font_surf, coord_text)

    def focus_mouse_highlight(self):
        pass

    def focus_highlight(self, back_rect_coord_size, text, coord_text, local_id=-1):
        cor = back_rect_coord_size
        if self.id == local_id:
            pygame.draw.rect(self.screen, GREY, cor)
            pygame.draw.rect(self.screen, WHITE, (cor[0]+5, cor[1]+5, cor[2]-10, cor[3]-10))
            self.draw_text(text, coord_text, 50)
        else:
            pygame.draw.rect(self.screen, WHITE, cor)
            self.draw_text(text, coord_text, 50)
