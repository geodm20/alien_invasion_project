import pygame

class Emperor:
    """A class to add the Emperor of Mankind from WH40K into the screen."""

    def __init__(self, ai_game):
        """Position the Emperor."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the Emperor image and get its rect.
        self.image = pygame.image.load('images/emperor.bmp')
        self.rect = self.image.get_rect()

        # Place the Emperor at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the Emperor at the center."""
        self.screen.blit(self.image, self.rect)