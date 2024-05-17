import sys
import pygame


class SpaceInvaders:
    """Overall class to manage the game"""

    def __init__(self):
        """initialise the game, and create game resource"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Invaders")

    def run_game(self):
        """start main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()
