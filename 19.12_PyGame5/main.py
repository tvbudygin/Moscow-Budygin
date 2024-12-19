import os
import sys
import pygame


def main():
    # pygame setup
    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def load_image(name):
    fullname = os.path.join('image', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изобрадением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image