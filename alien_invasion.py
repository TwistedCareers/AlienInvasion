"""AlienInvasion Class"""
import sys
import pygame

from settings import Settings


class AlienInvasion:
    """overall class to manage games assets and behaviour"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        """main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
