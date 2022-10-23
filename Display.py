import pygame

#Handle the display of the game
class display: 
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

