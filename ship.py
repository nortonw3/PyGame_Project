import pygame

# A class to manage the ship
class Ship:

    # Initialize the ship and set its starting position
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    # Update the ship's position based on the movement flag
    def update(self):
        if self.moving_right:
            self.rect.x += 1
            #print("Moving Right")

        if self.moving_left:
            self.rect.x -= 1
            #print("Moving Left")

    # Draw the ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)