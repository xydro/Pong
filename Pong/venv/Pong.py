import pygame
from Settings import Settings
from Paddle import Paddle
from PaddleAI import PaddleAI
from Point import Point
from ball import Ball
from star import Star
from button import Button
from spritesheet import SpriteSheet
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize Game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    play_button = Button(ai_settings, screen, "Play")

    # Make a Paddle
    bottomPaddle = Paddle(ai_settings, screen, 1)
    topPaddle = Paddle(ai_settings, screen, 2)
    mainPaddle = Paddle(ai_settings, screen, 3)
    bottomPaddle_AI = PaddleAI(ai_settings, screen, 1)
    topPaddle_AI = PaddleAI(ai_settings, screen, 2)
    mainPaddle_AI = PaddleAI(ai_settings, screen, 3)

    ballPoint = Point(1,1)
    ball = Ball(ai_settings, screen, 600, 400, ballPoint)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #star1 = Star(ai_settings, screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI)

        if stats.game_state is True:
            bottomPaddle.update()
            topPaddle.update()
            mainPaddle.update()
            bottomPaddle_AI.update(ball)
            topPaddle_AI.update(ball)
            mainPaddle_AI.update(ball)
            ball.update(mainPaddle,topPaddle, bottomPaddle,  bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, stats, sb)

        gf.update_screen(ai_settings, screen, bottomPaddle, topPaddle, mainPaddle, ball, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, stats, sb, play_button)


run_game()
