import sys
import pygame, random
from const import *
from game import Game
from snake import Snake
from apples import Apples

pygame.init()

game = Game()
snake = Snake(squares * 5, squares * 10)
apples = Apples()

font = pygame.font.Font('fonts/FRAHV.TTF', 22)

while True:

    game.draw_field()
    snake.move()

    if snake.direction == 'RIGHT' and snake.head_rect.x < WIDTH - squares:
        snake.head_rect.x += snake.speed

    if snake.direction == 'LEFT' and snake.head_rect.x > 0:
        snake.head_rect.x -= snake.speed

    if snake.direction == 'UP' and snake.head_rect.y > 0:
        snake.head_rect.y -= snake.speed

    if snake.direction == 'DOWN' and snake.head_rect.y < HEIGHT - squares:
        snake.head_rect.y += snake.speed

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

        if snake.head_rect.colliderect(apples.image_rect):
            print(snake.speed)
            snake.speed += 0.1
            game.score += 1
            apples.image_rect.x = random.randrange(1, FIELD_SIZE - 1) * squares
            apples.image_rect.y = random.randrange(1, FIELD_SIZE - 1) * squares
            snake.grow()

    # Game over si le joueur sort de l'ecran ou touche son corps
    if snake.head_rect.x <= 0:
        pygame.quit()
    if snake.head_rect.x >= WIDTH - squares:
        pygame.quit()
    if snake.head_rect.y >= HEIGHT - squares:
        pygame.quit()
    if snake.head_rect.y <= 0:
        pygame.quit()

    window.blit(snake.head, snake.head_rect)
    window.blit(apples.image, apples.image_rect)

    # Dessiner les segments du corps du serpent
    for segment in snake.body_segments:
        window.blit(snake.body, segment)

    if len(snake.body_segments) < 4:
        snake.grow()

    display_score = font.render(f'SCORE : {game.score}', True, BLACK)
    window.blit(display_score, (10, 20))

    clock.tick(fps)
    pygame.display.flip()
