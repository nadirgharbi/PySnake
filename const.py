import pygame 
from resource_path import resource_path

FIELD_SIZE = 20
squares = 50

SIZE = WIDTH, HEIGHT = squares * FIELD_SIZE, squares * FIELD_SIZE
GREEN = pygame.Color(134, 250, 167)
BLACK = pygame.Color(36, 36, 36)

BLUE_LIGHT = pygame.Color(184, 207, 241)
BLUE_DARK = pygame.Color(119, 148, 182)

clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode(SIZE)

BGM_MUSIC = resource_path("assets/audio/snake_music.wav")
APPLE_SPRITE = resource_path("assets/snake_graphics/apple.png")
EAT_APPLE_SE = resource_path("assets/audio/eat.wav")

FONT_SYS = resource_path('assets/fonts/FRAHV.TTF')
VOLUME_SYS = 0.8
