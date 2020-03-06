import pygame
from pygame.sprite import Sprite

# A class to represent a single alien in the fleet
class Alien(Sprite):

    # Initialize the aline and set its starting position
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aloen's exact horizontal position
        self.x = float(self.rect.x)

    
    # return true if alien is at edge of screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    # Move Alien to the right or left
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

