""" ship class """
import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.moving_right = False
        self.moving_left = False
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/spaceship.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.screen_rect.midbottom
        self.settings = ai_game.settings
        self.x_pos = float(self.image_rect.x)

    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x_pos += self.settings.ship_speed
        if self.moving_left and self.image_rect.left > 0:
            self.x_pos -= self.settings.ship_speed
        self.image_rect.x = self.x_pos
