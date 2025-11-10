import pygame, random
from const import *

class Apples:
    def __init__(self):
        img = pygame.image.load(APPLE_SPRITE).convert_alpha()
        self.image = pygame.transform.scale(img, (squares, squares))
        self.image_rect = self.image.get_rect()
        self.image_rect.x = random.randrange(1, FIELD_SIZE - 1) * squares
        self.image_rect.y = random.randrange(1, FIELD_SIZE - 1) * squares