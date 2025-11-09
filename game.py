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
    
    def play_bgm(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("assets/music/snake_music.wav")
            pygame.mixer.music.play(-1, 0, 1)