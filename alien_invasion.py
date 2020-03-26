import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats


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

        # create an isntance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    # Start the main loop of the game here
    def run_game(self):
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()


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

        self._check_bullet_alien_collisions()

    
    # Respond to bullet-alien collisions
    def _check_bullet_alien_collisions(self):
    # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()


    # Update images on the screen and flip to new screen
    def _update_screen(self):
         # Redraw the screen during each pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


    # Create the fleet of aliens
    def _create_fleet(self):
        # make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    # Update the positions of all aliens in the fleet
    def _update_aliens(self):
        # Check if the fleet is at an edge then update positions of all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    
    #respond appropriately if any aliens have reached an edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    # Drop the entire fleet and change direction
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    
    #check if any aliens have reached the bottom of the screen
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if a ship got hit
                self._ship_hit()
                break


    # Respond to the ship being hit by an alien
    def _ship_hit(self):
        if self.stats.ships_left >= 0:
            # Decrement ships left
            self.stats.ships_left -= 1

            # get rid of any remaining aliens or bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
