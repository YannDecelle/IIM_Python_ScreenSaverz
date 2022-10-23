import pygame

class Music:
    def __init__(self, path):
        self.path = path
        self.music = pygame.mixer.music.load(self.path)

    def stop(self):
        pygame.mixer.music.stop()

    def play(self):
        pygame.mixer.music.play()