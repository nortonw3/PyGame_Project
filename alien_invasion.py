import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

# ***Overall Class to manage game assets and behavior***
class AlienInvasion:
    
    # Initialize the game and create game resources
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    # Start the main loop of the game here
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_screen()
            self._update_bullets()

            # Make the most recently drawn screen visible
            # Runs faster when this is called here instead of _update_screen()
            pygame.display.flip()
            

    # Watch for keyboard and mouse events
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                   self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    # Responds to keypresses
    def _check_keydown_events(self, event):
         # Move the ship to the right
        if event.key ==pygame.K_RIGHT:
            self.ship.moving_right = True
        # Move the ship to the left
        if event.key ==pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
                    sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    # Responds to key releases
    def _check_keyup_events(self, event):
        # Stop ship movement
        if event.key ==pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key ==pygame.K_LEFT:
            self.ship.moving_left = False


    # Create a new bullet and add it to the bullets group
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    # Update position of bullets and get rid of old bullets
    def _update_bullets(self):
        # Update bullet positions
        self.bullets.update()
        
         # Get rid of bullets that have dissappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))


    # Update images on the screen and flip to new screen
    def _update_screen(self):
         # Redraw the screen during each pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
