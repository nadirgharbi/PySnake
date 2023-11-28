import pygame, random
from const import *

class Apples:
    def __init__(self):
        self.image = pygame.image.load('assets/snake_graphics/apple.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.x = random.randrange(1, FIELD_SIZE - 1) * squares
        self.image_rect.y = random.randrange(1, FIELD_SIZE - 1) * squares