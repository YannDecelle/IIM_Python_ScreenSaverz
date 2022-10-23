import pygame
import random

class Score:
    def __init__(self, x, y, color, width, height, font, screen, score):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.screen = screen
        self.score = score
        # store a limit to how fast the score can increment in order to avoid the player to gain more than 1 point at once
        self.update_score = 3000
        self.last_update = pygame.time.get_ticks()
        self.lvlup = pygame.mixer.Sound("sounds\lvlup.mp3")
        self.lvlup.set_volume(0.1)


    def LvL(self, x, y, width, height):
        # when the player reach the corners of the display, the score increase by 1, and wait a certain amount of time before incrementing again
        now = pygame.time.get_ticks()
        if x <= 10 and y <= 10 and now - self.last_update >= self.update_score:
            self.score += 1
            self.last_update = now
            self.lvlup.play()
            print('Score has increased: +', self.score, 'at: ', 'x: ',int(x), 'y: ',int(y))
        elif x >= width - 90 and y <= 10 and now - self.last_update >= self.update_score:
            self.score += 1
            self.last_update = now
            self.lvlup.play()
            print('Score has increased: +', self.score, 'at: ', 'x: ',int(x), 'y: ',int(y))
        elif x <= 10 and y >= height - 90 and now - self.last_update >= self.update_score:
            self.score += 1
            self.last_update = now
            self.lvlup.play()
            print('Score has increased: +', self.score, 'at: ', 'x: ',int(x), 'y: ',int(y))
        elif x >= width - 90 and y >= height - 90 and now - self.last_update >= self.update_score:
            self.score += 1
            self.last_update = now
            self.lvlup.play()
            print('Score has increased: +', self.score, 'at: ', 'x: ',int(x), 'y: ',int(y))
        # display the score
        text = self.font.render("Score: " + str(self.score), 1, self.color)
        self.screen.blit(text, (self.x, self.y))