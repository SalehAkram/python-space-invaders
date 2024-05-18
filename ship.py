import pygame
class Ship:
    """A class to manage the ship"""
    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
