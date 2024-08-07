class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (230, 230, 230)
        self.ship_speed = 3.0

        # bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10.0
        # direction 1 = right and -1 = left
        self.fleet_direction = 1
