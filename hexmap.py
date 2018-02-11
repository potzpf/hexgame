import math
from settings import *
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Hexmap:
    def __init__(self):
    #settings
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.size = (X_SIZE, Y_SIZE) # (x, y)

    #init map
        self.map = []
        for x in range(0, X_SIZE):
            Y = []
            for y in range(0, Y_SIZE):
                Y.append(Hex((x, y), self.screen))
            self.map.append(Y)

        pygame.display.set_caption("uniwar2")


    def draw(self):
    # background
        self.screen.fill(WHITE)

    # hexmap
        for x in range(0, X_SIZE):
            for y in range(0, Y_SIZE):
                self.map[x][y].draw()

        pygame.display.flip()

class Hex:
    def __init__(self, pos, screen):
        self.pos = pos
        self.screen = screen

    def draw(self):
        pygame.draw.aalines(self.screen, BLACK, False, self.hex(self.map_pos_to_center(self.pos)), 2)

    def hex(self, center):
        ret = []
        for i in range(0, 7):
            rad = (i * 60 + 30) * math.pi / 180
            p = [center[0] + HEX_RADIUS * math.cos(rad), center[1] + HEX_RADIUS * math.sin(rad)]
            ret.append(p)
        return ret    

    def map_pos_to_center(self, pos):
        x = BORDER_SIZE + 2 * pos[0] * RADIUS_I + RADIUS_I
        if pos[1] % 2 == 1:
            x += RADIUS_I
        y = BORDER_SIZE + pos[1] * (RADIUS_I * 2 * math.cos(math.pi/6)) + RADIUS_I 

        return [x, y]