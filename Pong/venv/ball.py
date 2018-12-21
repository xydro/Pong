import pygame
import random

class Ball:
    def __init__(self, ai_settings, screen, x, y, point):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.rect_pos = list(self.rect.center)
        self.sx = 0
        self.sy = 0
        self.velocity = [0, 0]
        self.coord = [600, 400]
        self.setNewVelocity()
        self.speed = 3.5

    def __str__(self):
        return 'Ball(rect=' + str(self.rect) + ', x = ' + str(self.x) + \
                ', y =' + str(self.y) + str(self.ai_settings) + ')'

    def blitme(self):
        image = self.image
        self.screen.blit(image, self.rect)

    def update(self, mainPaddle, topPaddle, bottomPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, stats, sb):
        #self.position += self.velocity * self.deltat
        check = self.off_screen()
        self.collision(topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI)
        if check:
            if self.rect_pos[0] > 600:
                stats.score2 += 1
                sb.prep_score2()
            else:
                stats.score1 += 1
                sb.prep_score1()

            if stats.score1 is 7:
                stats.game_state = False
                pygame.mouse.set_visible(True)
            if stats.score2 is 7:
                stats.game_state = False
                pygame.mouse.set_visible(True)
            
            mainPaddle.reset_position()
            bottomPaddle.reset_position()
            topPaddle.reset_position()

            mainPaddle_AI.reset_position()
            bottomPaddle_AI.reset_position()
            topPaddle_AI.reset_position()

            self.setNewVelocity()
            self.rect_pos = [600, 400]
            self.setNewCoord()
        else:
            self.setNewCoord()


    def touch_horizontal(self, paddle):
        r = self.rect
        prect = paddle.rect
        return (r.left <= prect.right) or (r.right >= prect.left)

    def touch_vertical(self, paddle):
        r = self.rect
        prect = paddle.rect
        return (r.top <= prect.bottom) or (r.bottom >= prect.top)

    def off_screen(self):
        if self.rect.centerx > 0 and self.rect.centerx < 1200:
            if self.rect.centery > 0 and self.rect.centery < 800:
                return False
            else:
                return True
        else:
            return True

    def setNewVelocity(self):
        self.sx = random.randint(-1, 1)
        self.sy = random.randint(-1, 1)

        # If both x and y are 0
        if self.sx is 0 and self.sy is 0:
            self.r = random.randint(0, 1)
            if self.r is 1:
                self.sx = random.randrange(-1, 1, 2)
            else:
                self.sy = random.randrange(-1, 1, 2)

        self.velocity = [self.sx, self.sy]

    def setNewCoord(self):
        self.rect_pos[0] += (float(self.velocity[0] / self.speed))
        self.rect_pos[1] += (float(self.velocity[1] / self.speed))
        self.rect.center = self.rect_pos

    def collision(self, topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI):
        self.rect_npos = self.rect_pos.copy()
        self.rect_npos[0] += self.velocity[0] * 2
        self.rect_npos[1] += self.velocity[1] * 2

        if topPaddle.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            if topPaddle.moving_right is True:
                self.sx = 1
            elif topPaddle.moving_left is True:
                self.sx = -1
            self.sy = 1
            self.velocity[1] = self.sy
            self.velocity[0] = self.sx
        elif bottomPaddle.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            if bottomPaddle.moving_right is True:
                self.sx = 1
            elif bottomPaddle.moving_left is True:
                self.sx = -1
            self.sy = -1
            self.velocity[1] = self.sy
            self.velocity[0] = self.sx
        elif mainPaddle.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            self.sx = -1
            if mainPaddle.moving_up is True:
                self.sy = -1
            elif mainPaddle.moving_down is True:
                self.sy = 1
            self.velocity[0] = self.sx
            self.velocity[1] = self.sy
        elif topPaddle_AI.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            if topPaddle_AI.moving_right is True:
                self.sx = 1
            elif topPaddle_AI.moving_left is True:
                self.sx = -1
            self.sy = 1
            self.velocity[1] = self.sy
            self.velocity[0] = self.sx
        elif bottomPaddle_AI.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            if bottomPaddle_AI.moving_right is True:
                self.sx = 1
            elif bottomPaddle_AI.moving_left is True:
                self.sx = -1
            elif self.velocity[0] is 0:
                self.sx = random.randrange(-1, 1, 2)
            self.sy = -1
            self.velocity[1] = self.sy
            self.velocity[0] = self.sx
        elif mainPaddle_AI.rect.collidepoint(self.rect_npos[0],  self.rect_npos[1]):
            self.sx = 1
            if mainPaddle_AI.moving_up is True:
                self.sy = -1
            elif mainPaddle_AI.moving_down is True:
                self.sy = 1
            self.velocity[0] = self.sx
            self.velocity[1] = self.sy
