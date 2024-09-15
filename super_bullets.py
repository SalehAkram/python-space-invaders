import pygame
from pygame.sprite import Sprite


class SuperBullet(Sprite):
    """We need to think about refactoring bullets and super bullets, use better design patterns. A lot of repeatable
    codes: Inheritance could be used here"""
    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = si_game.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.super_bullet_width, self.settings.bullet_height)
        self.rect.midtop = si_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.super_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
