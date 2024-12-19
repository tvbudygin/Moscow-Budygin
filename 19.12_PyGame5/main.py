import os
import sys
import pygame


def main():
    # pygame setup
    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    screen.fill("purple")
    clock = pygame.time.Clock()
    image = load_image('owls.jpeg', -1)

    robot = load_image('robot.jpeg', -1)
    image1 = pygame.transform.scale(robot, (200, 100))
    screen.blit(image1, (700, 200))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(image, event.pos)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


def load_image(name, colorkey=None):
    fullname = os.path.join('image', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изобрадением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    main()