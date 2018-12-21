class GameStats():
    """Track statistics for Pong."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_state = False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.goal = 7
        self.score1 = 0
        self.score2 = 0
