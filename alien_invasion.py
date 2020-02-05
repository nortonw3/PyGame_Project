import sys 
import pygame
from settings import Settings
from ship import Ship

# ***Overall Class to manage game assets and behavior***
class AlienInvasion:
    
    # Initialize the game and create game resources
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    # Start the main loop of the game here
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

            # Make the most recently drawn screen visible
            pygame.display.flip()

    # Watch for keyboard and mouse events
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    # Move the ship to the right
                    if event.key ==pygame.K_RIGHT:
                        self.ship.moving_right = True
                    # Move the ship to the left
                    if event.key ==pygame.K_LEFT:
                        self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    # Stop ship movement
                    if event.key ==pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key ==pygame.K_LEFT:
                        self.ship.moving_left = False


    # Update images on the screen and flip to new screen
    def _update_screen(self):
         # Redraw the screen during each pass of the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
