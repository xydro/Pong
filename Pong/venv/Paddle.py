import pygame


class Paddle:

    def __init__(self, ai_settings, screen, typePaddle):
        """Initialize the paddle and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.typeOfPaddle = typePaddle
        # Load the paddle image and get its rect.
        '''self.image = pygame.image.load('images/paddlehoriz.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()'''

        
        if self.typeOfPaddle is 1:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/bottompaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = (self.screen_rect.centerx + (self.screen_rect.centerx / 2))
            self.rect.bottom = self.screen_rect.bottom
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 2:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/bottompaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = (self.screen_rect.centerx + (self.screen_rect.centerx / 2))
            self.rect.top = self.screen_rect.top
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 3:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/mainpaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.right - 16
            self.rect.centery = (self.screen_rect.bottom / 2)
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centery)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the Paddle's position based on the movement flag"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < (self.screen_rect.right - 32):
            self.center += self.ai_settings.paddle_speed_factor
        if self.moving_left and self.rect.left > 600:
            self.center -= self.ai_settings.paddle_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.paddle_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.paddle_speed_factor

        # Update rect object from self.center.
        if self.typeOfPaddle != 3:
            self.rect.centerx = self.center
        else:
            self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def reset_position(self):
        if self.typeOfPaddle is 1:
            # Load the paddle image and get its rect.
            self.rect.centerx = (self.screen_rect.centerx + (self.screen_rect.centerx / 2))
            self.rect.bottom = self.screen_rect.bottom
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 2:
            # Load the paddle image and get its rect.
            self.rect.centerx = (self.screen_rect.centerx + (self.screen_rect.centerx / 2))
            self.rect.top = self.screen_rect.top
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 3:
            self.rect.centerx = self.screen_rect.right - 16
            self.rect.centery = (self.screen_rect.bottom / 2)
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centery)
