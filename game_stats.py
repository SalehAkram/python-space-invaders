
class GameStats:
    """Track statistics for Space Invaders"""
    def __init__(self, si_game):
        self.ships_left = None
        self.settings = si_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
