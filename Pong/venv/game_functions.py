import sys

import pygame


def check_events(ai_settings, screen, stats, sb, play_button, topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI):
    """ Responds to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, topPaddle, bottomPaddle, mainPaddle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, topPaddle, bottomPaddle, mainPaddle)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, topPaddle, bottomPaddle, mainPaddle, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_state:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_state = True

        # Reset the scoreboard images.
        sb.prep_score1()
        sb.prep_score2()
        sb.prep_level()

        mainPaddle.reset_position()
        bottomPaddle.reset_position()
        topPaddle.reset_position()

        mainPaddle_AI.reset_position()
        bottomPaddle_AI.reset_position()
        topPaddle_AI.reset_position()


def update_screen(ai_settings, screen, topPaddle, bottomPaddle, mainPaddle, ball, bottomPaddle_AI, topPaddle_AI, mainPaddle_AI, stats, sb, play_button):
    """ Updates images on the screen and flip to the new screen. """
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    topPaddle.blitme()
    bottomPaddle.blitme()
    mainPaddle.blitme()
    topPaddle_AI.blitme()
    bottomPaddle_AI.blitme()
    mainPaddle_AI.blitme()
    ball.blitme()

    sb.show_score()

    if not stats.game_state:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_keydown_events(event, topPaddle, bottomPaddle, mainPaddle):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        topPaddle.moving_right = True
        bottomPaddle.moving_right = True
    elif event.key == pygame.K_LEFT:
        topPaddle.moving_left = True
        bottomPaddle.moving_left = True

    if event.key == pygame.K_UP:
        mainPaddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        mainPaddle.moving_down = True


def check_keyup_events(event, topPaddle, bottomPaddle, mainPaddle):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        topPaddle.moving_right = False
        bottomPaddle.moving_right = False
    elif event.key == pygame.K_LEFT:
        topPaddle.moving_left = False
        bottomPaddle.moving_left = False

    if event.key == pygame.K_UP:
        mainPaddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        mainPaddle.moving_down = False


