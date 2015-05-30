import pygame
from pygame.locals import *

class Spritesheet(object):
    def __init__(self, filename, countx, county):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sprites = []
        for i in range(0, county):
            for j in range(0, countx):
                self.sheet.set_clip(pygame.Rect(j * 62.5, i * 62.5, 62.5, 62.5))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.sprites.append(self.image)

class Explosion(pygame.sprite.Sprite):
    explosions = pygame.sprite.Group()

    def __init__(self, x, y):
        super(Explosion, self).__init__()
        Explosion.explosions.add(self)
        self.sheet = Spritesheet("exp.png", 4, 4)
        self.images = self.sheet.sprites
        self.widthheight = 62.5
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(x, y, self.widthheight, self.widthheight)

    def update(self):
        if self.index >= len(self.images):
            self.image = None
        else:
            self.image = self.images[self.index]
            self.index = self.index + 1

if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))

    running = True

    clock = pygame.time.Clock()

    e = []

    while running:
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                e.append(Explosion(x - 30, y - 30))

        screen.fill((0, 0, 0))

        for index, ex in enumerate(e):
            ex.update()
            if ex.image == None:
                e.pop(index)
                Explosion.explosions.remove(ex)
                
        Explosion.explosions.draw(screen)

        pygame.display.update()

