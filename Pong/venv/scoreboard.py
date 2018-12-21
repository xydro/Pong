import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (10, 10, 10)
        self.bgt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score1()
        self.prep_score2()
        self.prep_level()

    def prep_score1(self):
        """Turn the score into a rendered image."""
        score_to_render = self.stats.score1
        score_str = str(score_to_render)
        self.score1_image = self.font.render(score_str, True, self.text_color,
            self.bgt_color)
            
        # Display the score at the middle top right of the screen.
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.centerx = (self.screen_rect.centerx + 24)
        self.score1_rect.top = 30

    def prep_score2(self):
        score_to_render = self.stats.score2
        score_str = str(score_to_render)
        self.score2_image = self.font.render(score_str, True, self.text_color,
            self.bgt_color)

        # Display the score at the middle top right of the screen.
        self.score2_rect = self.score2_image.get_rect()
        self.score2_rect.centerx = (self.screen_rect.centerx - 24)
        self.score2_rect.top = 30

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.goal), True,
                self.text_color, self.bgt_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = 70

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.score2_image, self.score2_rect)
        self.screen.blit(self.level_image, self.level_rect)