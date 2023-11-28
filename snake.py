import pygame
from const import *


class Snake:
    def __init__(self, x, y):
        self.size_head = squares
        self.size_body = squares
        self.speed = 2

        self.head = pygame.Surface((self.size_head, self.size_head))
        self.head.fill(GREEN)

        self.body = pygame.Surface((self.size_body, self.size_body))
        self.body.fill(BLACK)

        self.head_rect = self.head.get_rect()
        self.head_rect.x = x
        self.head_rect.y = y

        self.body_segments = []  # Liste des segments du corps du serpent

        self.direction = 'RIGHT'

    def move(self):
        # Mettre à jour la position de chaque segment du corps en le faisant suivre le segment précédent
        if len(self.body_segments) > 0:
            prev_x, prev_y = self.head_rect.x, self.head_rect.y
            for segment in self.body_segments:
                temp_x, temp_y = segment.x, segment.y
                segment.x, segment.y = prev_x, prev_y
                prev_x, prev_y = temp_x, temp_y

    def grow(self):
        # Ajouter un segment au corps du serpent
        if len(self.body_segments) == 0:
            new_segment = self.body.get_rect()
            new_segment.x = self.head_rect.x
            new_segment.y = self.head_rect.y
        else:
            last_segment = self.body_segments[-1]
            new_segment = self.body.get_rect()
            new_segment.x = last_segment.x
            new_segment.y = last_segment.y
        self.body_segments.append(new_segment)