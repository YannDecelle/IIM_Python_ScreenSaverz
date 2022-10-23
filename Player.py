import pygame
import random
from Progression import Score

# activate devmode which allow to move the player with the arrow keys
devmode = False
# Handle the player
class Player:
    def __init__(self, x, y, SpeedX, SpeedY, Speed_Multiplier, color, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = Speed_Multiplier
        self.speedX = SpeedX
        self.speedY = SpeedY
        self.bump = pygame.mixer.Sound("sounds\hit.mp3")
        self.bump.set_volume(0.1)

    # display the player
    def img(self, screen):
        global img
        img = pygame.image.load("img\dvd.png")
        img = pygame.transform.scale(img, (self.width, self.height))
        img.fill(self.color, special_flags=pygame.BLEND_RGB_MULT)
        screen.blit(img, (self.x, self.y))

    # set the display's border as limits
    def limit(self, width, height):
        if self.x < 0:
            self.x = 0
        elif self.x > width - self.width:
            self.x = width - self.width
        if self.y < 0:
            self.y = 0
        elif self.y > height - self.height:
            self.y = height - self.height

    # move the player
    def move(self, width, height):
        if devmode == False:
            self.x += self.speedX * self.speed
            self.y += self.speedY * self.speed
            # if the player touch the border of the display, it bounces off the border
            if self.x <= 0:
                self.speedX = 1
                self.bump.play()
                self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            elif self.x >= width - self.width:
                self.speedX = -1
                self.bump.play()
                self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if self.y <= 0:
                self.speedY = 1
                self.bump.play()
                self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            elif self.y >= height - self.height:
                self.speedY = -1
                self.bump.play()
                self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        print(self.speed)
        
    # Controls the player
    def change_direction(self, event):
        global devmode
        # this is the two sets of controls when devmode is on or off
        if event.type == pygame.KEYDOWN:
            if devmode == False:  
                if event.key == pygame.K_UP:
                    self.speedY = -1
                elif event.key == pygame.K_DOWN:
                    self.speedY = 1
                elif event.key == pygame.K_LEFT:
                    self.speedX = -1
                elif event.key == pygame.K_RIGHT:
                    self.speedX = 1
                elif event.key == pygame.K_LSHIFT:
                    devmode = True
            elif devmode == True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.x += -10
                if keys[pygame.K_RIGHT]:
                    self.x += +10
                if keys[pygame.K_UP]:
                    self.y += -10
                if keys[pygame.K_DOWN]:
                    self.y += +10
                if keys[pygame.K_LSHIFT]:
                    devmode = False
