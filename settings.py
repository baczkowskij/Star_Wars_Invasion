class Settings:
    def __init__(self):
        """Initializing the settings of the game"""
        #game window settings:
        self.bg_color=(0,0,0)
        self.screen_width=1200
        self.screen_height=800
        #ship settings:
        self.ship_speed=0.8
        #bullet settings:
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 10
        self.inv_bullet_color = (0,255,0)
        self.alien_speed=0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1