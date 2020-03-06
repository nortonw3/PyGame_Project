# Track stats for alien invasions
class GameStats:

    # Initialize statistice
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in an active state
        self.game_active = True

    
    # Initialize stats that can change during the game
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit