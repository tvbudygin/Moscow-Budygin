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
    # image = load_image('owls.png', -1)
    #
    # robot = load_image('robot.png', -1)
    # image1 = pygame.transform.scale(robot, (200, 100))
    # screen.blit(image1, (700, 200))
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("bomb.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 200
    all_sprites.add(sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.draw(screen)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     screen.blit(image, event.pos)

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