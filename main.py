import sys
import pygame
from const import *
from game import Game
from snake import Snake
from apples import Apples

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
# pygame.mixer.set_num_channels(8)

game = Game()
game.play_bgm()

snake = Snake(squares * 6, squares * 10)
apples = Apples()

font = pygame.font.Font(FONT_SYS, 32)

while True:
    game.draw_field()

    # Update mouvement tête + propagation au corps
    snake.move()

    if snake.direction == 'RIGHT' and snake.head_rect.x < WIDTH - squares:
        snake.head_rect.x += snake.speed
    if snake.direction == 'LEFT' and snake.head_rect.x > 0:
        snake.head_rect.x -= snake.speed
    if snake.direction == 'UP' and snake.head_rect.y > 0:
        snake.head_rect.y -= snake.speed
    if snake.direction == 'DOWN' and snake.head_rect.y < HEIGHT - squares:
        snake.head_rect.y += snake.speed

    # Gestion des événements (UNIQUEMENT entrées/sorties, pas de gameplay ici)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'

    # COLLISION vérifiée chaque frame (et plus dans la boucle d’événements)
    game.check_collide(snake, apples)

    # Game over murs
    if game.is_game_over(snake):
        pygame.quit()
        sys.exit()

    window.blit(snake.head, snake.head_rect)
    window.blit(apples.image, apples.image_rect)

    for segment in snake.body_segments:
        window.blit(snake.body, segment)

    display_score = font.render(f'SCORE : {game.score}', True, BLACK)
    window.blit(display_score, (10, 20))

    clock.tick(fps)
    pygame.display.flip()
