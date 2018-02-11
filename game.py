import sys

import pygame

from hexmap import Hexmap



class game:
    def __init__(self):
        pygame.init()
        self.hexmap = Hexmap()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(30) #30 fps

            self.hexmap.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
