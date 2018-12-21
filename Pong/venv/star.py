import pygame
import random
from spritesheet import SpriteSheet


class Star:

    def __init__(self,  ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        ss = spritesheet.spritesheet('starsheet.png')

        # Sprite is 16x16 pixels at location 0,0 in the file...
        image = ss.image_at((0, 0, 4, 4))
        images = []
        # Load two images into an array, their transparent bit is (255, 255, 255)
        images = ss.images_at((0, 0, 4, 4), (17, 0, 16, 16), colorkey=(255, 255, 255))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def __str__(self):
        return 'Star(rect=' + str(self.rect) + ', x = ' + str(self.x) + \
                ', y =' + str(self.y) + str(self.ai_settings) + ')'

    def blitme(self):
        image = self.image
        self.screen.blit(image, self.rect)
