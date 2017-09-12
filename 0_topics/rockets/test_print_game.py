import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Key Down')

    font = pygame.font.SysFont(None, 48)
    label = font.render("Press Something", 1, (255, 255, 100))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                screen.fill((100, 100, 100))
                label = font.render(str(event.key), 1, (255, 255, 100))

        screen.blit(label, (20, 20))
        pygame.display.flip()


run_game()
