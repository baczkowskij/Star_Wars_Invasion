class Settings:
    def __init__(self):
        """Initializing the settings of the game"""
        #game window settings:
        self.bg_color=(0,0,0)
        self.screen_width=1200
        self.screen_height=800
        
        #bullet settings:
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 10
        self.alien_bullet_color = (0,255,0)
        self.shpis_limit = 3
        self.speedup_scale=1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed=0.8
        self.alien_bullet_speed =0.5
        self.alien_speed=0.5
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
        self.your_level = 0
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.alien_bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points*=self.speedup_scale
        self.fleet_drop_speed = self.fleet_drop_speed*(1.2*self.speedup_scale)
        if  self.fleet_drop_speed > 50:
            self.fleet_drop_speed = 50
        self.your_level +=1