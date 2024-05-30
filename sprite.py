import random
import pygame


class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/meteorite.png")
        size = random.randint(35, 75)

        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (400, random.randint(0, 300 - size))
        self.speedx = random.randint(1, 3)
        self.speedy = random.randint(-1, 1)

    def update(self):
        self.rect.x-=self.speedx
        self.rect.y-=self.speedy


class Mouse_starship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/mouse_starship.png")
        size = random.randint(70, 150)

        self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 300 - size), 0)

        self.speedy = random.randint(-2, +1)
        self.speedx = random.randint(0, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/laser.png")

        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos)

        self.speed = 2

    def update(self):
        self.rect.y -= self.speed


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/starship_horizontal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 150)

        self.mode = "vertical"

    def update(self):
        keys = pygame.key.get_pressed()
        if self.mode == "horizontal":
            if keys[pygame.K_a]:
                self.rect.x -= 3
            if keys[pygame.K_d]:
                self.rect.x += 3

        if self.mode == "vertical":
            if keys[pygame.K_w]:
                self.rect.y -= 1
            if keys[pygame.K_s]:
                self.rect.y += 1

    def switch_mode(self):
        self.image = pygame.image.load("images/starship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (200, 290)

        self.mode = "horizontal"


class Captain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/captain.png")
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-15, 300)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 2
            if self.rect.y <= 150:
                self.rect.y = 150
                self.mode = "stay"


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-15, 300)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 2
            if self.rect.y <= 150:
                self.rect.y = 150
                self.mode = "stay"
