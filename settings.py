# A class to store all settings for Alien Invasion
class Settings:

    # Initialize the game's settings
    def __init__(self):
       # Screen settings
       self.screen_width = 1200
       self.screen_height = 800
       self.bg_color = (230, 230, 230) 

       # Ship settings
       self.ship_speed = 15
       self.ship_limit = 3

       # Bullet settings
       self.bullet_speed = 30.0
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (60, 60, 60)
       self.bullets_allowed = 3

       # Alien Settings
       self.alien_speed = 5
       self.fleet_drop_speed = 10
       # Fleet_direction of 1 represents right; -1 represents left.
       self.fleet_direction = 1
