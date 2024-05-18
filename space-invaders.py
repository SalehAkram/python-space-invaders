import sys
import pygame
from settings import Settings
from ship import Ship


class SpaceInvaders:
    """Overall class to manage the game"""

    def __init__(self):
        """initialise the game, and create game resource"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders, Author: Saleh Akram")
        self.ship = Ship(self)


    def run_game(self):
        """start main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.screen_bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()
