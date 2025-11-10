import pygame 
from const import *
import random

class Game:
    def __init__(self):
        self.score = 0
        self.sfx_eat = pygame.mixer.Sound(EAT_APPLE_SE)
        self.sfx_eat.set_volume(VOLUME_SYS)
        self.sfx_channel = pygame.mixer.Channel(1) # Canal dédié pour les SFX (différent de mixer.music)

    def draw_field(self):
        for row in range(FIELD_SIZE):
            for col in range(FIELD_SIZE):
                x = col * squares
                y = row * squares

                if (row + col) % 2 == 0:
                    pygame.draw.rect(window, BLUE_DARK, (x, y, squares, squares))
                else:
                    pygame.draw.rect(window, BLUE_LIGHT, (x, y, squares, squares))
    
    def play_bgm(self, is_playing: bool = True):
        if is_playing:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(BGM_MUSIC)
                pygame.mixer.music.set_volume(VOLUME_SYS)
                pygame.mixer.music.play(-1)

    def play_sound_effect(self, sound: pygame.mixer.Sound):
        self.sfx_channel.play(sound)

    def check_collide(self, snake, apples):
        if snake.head_rect.colliderect(apples.image_rect):
            self.play_sound_effect(self.sfx_eat)
            self.score += 1
            apples.image_rect.x = random.randrange(1, FIELD_SIZE - 1) * squares
            apples.image_rect.y = random.randrange(1, FIELD_SIZE - 1) * squares
            snake.grow()

    def is_game_over(self, snake):
        return (snake.head_rect.x < 0 or
        snake.head_rect.x > WIDTH - squares or
        snake.head_rect.y < 0 or
        snake.head_rect.y > HEIGHT - squares)
