#INIT
import pygame
import random
from Display import display
from Player import Player
from Progression import Score
from SoundController import Music

init = pygame.init()
print(init)

#DISPLAY
display = display(800, 450, "Screensaverz - by YannDecelle")

#SCORE
score = Score(10, 10, (255,255,255), 100, 100, pygame.font.SysFont("comicsans", 30, True), display.screen, 0)


#PLAYER
player = Player(display.width/2, display.height/2, 1, 0.4, 0.05, (0,0,255), 80, 80)

#MUSIC
music = Music("sounds\music.mp3")
music.play()
pygame.mixer.music.set_volume(0.05)

#GAME LOOP
IsRunning = True
while IsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                IsRunning = False
        player.change_direction(event)
    display.screen.fill((0,0,0))
    score.LvL(player.x, player.y, display.width, display.height)
    if score.score <= 1:
        SpeedMult = 0.05
        print('Speed multiplier: ', SpeedMult)
    else:
        SpeedMult = 0.1 * score.score
        player.speed = SpeedMult
        print('Speed multiplier: ', SpeedMult)
    player.limit(display.width, display.height)
    player.move(display.width, display.height)
    player.img(display.screen)
    pygame.display.update()
    