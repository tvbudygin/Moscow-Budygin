import os
import sys
import pygame
from random import randrange


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group, width, height):
        super().__init__(group)
        self.image = load_image("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)
        self.image_boom = load_image("boom.png")

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(randrange(3) - 1, randrange(3) - 1)

        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                self.image = self.image_boom


def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    # image = load_image('owls.png', -1)
    #
    # robot = load_image('robot.png', -1)
    # image1 = pygame.transform.scale(robot, (200, 100))
    # screen.blit(image1, (700, 200))
    all_sprites = pygame.sprite.Group()
    # sprite = pygame.sprite.Sprite()
    # image = load_image("bomb.png", -1)
    # for _ in range(100):
    #     sprite = pygame.sprite.Sprite(all_sprites)
    #     sprite.image = image
    #     sprite.rect = sprite.image.get_rect()
    #     sprite.rect.x = randrange(width)
    #     sprite.rect.y = randrange(height)
    #     all_sprites.add(sprite)
    for _ in range(100):
        Bomb(all_sprites, width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.draw(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     screen.blit(image, event.pos)
        screen.fill("purple")
        all_sprites.draw(screen)
        all_sprites.update()
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
