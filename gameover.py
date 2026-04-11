import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "common")))
from constants import *

def show_gameover_screen(screen, score):
    font = pygame.font.Font(None, 40)
    big_font = pygame.font.Font(None, 80)

    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets/launcher"))
    bg = pygame.image.load(os.path.join(base,"bg.png"))
    bg = pygame.transform.scale(bg,(width, height))

    options = ["Retry", "Quit"]
    selected = 0
    score_text = f"Score: {score}"
    
    option_rects = []
    for i, text in enumerate(options):
        rect = pygame.Rect(0, 200 + i*50, width, 50)
        option_rects.append(rect)

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.blit(bg,(0,0))

        game_over_render = big_font.render("GAME OVER", True, (255, 50, 50))
        go_rect = game_over_render.get_rect(center=(width//2, 80))
        screen.blit(game_over_render, go_rect)

        if score_text:
            score_render = font.render(score_text, True, (255, 255, 255))
            score_rect = score_render.get_rect(center=(width//2, 140))
            screen.blit(score_render, score_rect)

        for i, text in enumerate(options):
            color = (0,0,0) if i == selected else (255,255,255)
            render = font.render(text, True, color)
            screen.blit(render, (250, 200 + i*50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected = i

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(event.pos):
                            selected = i
                            if selected == 0:
                                return
                            elif selected == 1:
                                pygame.quit()
                                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return
                    if selected == 1:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(60)
