import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import games.snake.main as snake_game
import games.flappy.main as flappy_game
import games.shooter.main as shooter_game

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 40)

base = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets/launcher"))
bg = pygame.image.load(os.path.join(base,"bg.png"))
bg = pygame.transform.scale(bg,(600,400))

options = ["Snake", "Flappy", "Shooter"]
selected = 0

while True:
    screen.blit(bg,(0,0))

    for i, text in enumerate(options):
        color = (0,0,0) if i == selected else (255,255,255)
        render = font.render(text, True, color)
        screen.blit(render, (250, 150 + i*50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected = (selected - 1) % 3
            if event.key == pygame.K_DOWN:
                selected = (selected + 1) % 3
            if event.key == pygame.K_RETURN:
                if selected == 0:
                    snake_game.play(screen)
                if selected == 1:
                    flappy_game.play(screen)
                if selected == 2:
                    shooter_game.play(screen)

    pygame.display.update()
    clock.tick(60)
