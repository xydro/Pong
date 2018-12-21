import pygame


class PaddleAI:

    def __init__(self, ai_settings, screen, typepaddle):
        """Initialize the paddle and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.typeOfPaddle = typepaddle
        # Load the paddle image and get its rect.
        
        if self.typeOfPaddle is 1:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/bottompaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx / 2
            self.rect.bottom = self.screen_rect.bottom
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 2:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/bottompaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx / 2
            self.rect.top = self.screen_rect.top
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 3:
            # Load the paddle image and get its rect.
            self.image = pygame.image.load('images/mainpaddle.png')
            self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.left + 16
            self.rect.centery = (self.screen_rect.bottom / 2)
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centery)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Boundary Flags
        self.checkLeft = False
        self.checkRight = False
        self.checkTop = False
        self.checkBottom = False

    def update(self, ball):
        """Update the Paddle's position based on the movement flag"""
        # Update the ship's center value, not the rect.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.checkLeft = self.rect.left > self.screen_rect.left + 32
        self.checkRight = self.rect.right < 600
        self.checkTop = self.rect.top > 0
        self.checkBottom = self.rect.bottom < self.screen_rect.bottom

        if self.typeOfPaddle is 1 and self.rect.centerx != ball.rect.centerx:
            if self.rect.centerx < ball.rect.centerx:
                if self.checkRight:
                    self.center += self.ai_settings.paddle_speed_factor
                    self.moving_right = True
            else:
                if self.checkLeft:
                    self.center -= self.ai_settings.paddle_speed_factor
                    self.moving_left = True
        if self.typeOfPaddle is 2 and self.rect.centerx != ball.rect.centerx:
            if self.rect.centerx < ball.rect.centerx:
                if self.checkRight:
                    self.center += self.ai_settings.paddle_speed_factor
                    self.moving_right = True
            else:
                if self.checkLeft:
                    self.center -= self.ai_settings.paddle_speed_factor
                    self.moving_left = True
        if self.typeOfPaddle is 3 and self.rect.centery != ball.rect.centery:
            if self.rect.centery < ball.rect.centery:
                if self.checkBottom:
                    self.center += self.ai_settings.paddle_speed_factor
                    self.moving_up = True
            else:
                if self.checkTop:
                    self.center -= self.ai_settings.paddle_speed_factor
                    self.moving_down = False

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
            self.rect.centerx = self.screen_rect.centerx / 2
            self.rect.bottom = self.screen_rect.bottom
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 2:
            self.rect.centerx = self.screen_rect.centerx / 2
            self.rect.top = self.screen_rect.top
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centerx)
        if self.typeOfPaddle is 3:
            self.rect.centerx = self.screen_rect.left + 16
            self.rect.centery = (self.screen_rect.bottom / 2)
            # Store a decimal value for the paddle's center
            self.center = float(self.rect.centery)
