import pygame 
from const import *

class Game:
    def __init__(self):
        self.score = 0

    def draw_field(self):
        for row in range(FIELD_SIZE):
            for col in range(FIELD_SIZE):
                x = col * squares
                y = row * squares

                if (row + col) % 2 == 0:
                    pygame.draw.rect(window, BLUE_DARK, (x, y, squares, squares))
                else:
                    pygame.draw.rect(window, BLUE_LIGHT, (x, y, squares, squares))