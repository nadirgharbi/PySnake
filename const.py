import pygame 

FIELD_SIZE = 20
squares = 40

SIZE = WIDTH, HEIGHT = squares * FIELD_SIZE, squares * FIELD_SIZE
GREEN = pygame.Color(134, 250, 167)
BLACK = pygame.Color(36, 36, 36)

BLUE_LIGHT = pygame.Color(184, 207, 241)
BLUE_DARK = pygame.Color(119, 148, 182)

clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode(SIZE)
