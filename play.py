import pygame
import random
import time

min_length = 10 # seconds
max_length = 35 # seconds

pygame.mixer.init()
pygame.mixer.music.load('song.mp3')

pygame.mixer.music.play()

while True:
    seconds_to_play = random.randint(min_length, max_length)
    print (f'playing for {seconds_to_play} seconds')
    time.sleep(seconds_to_play)
    pygame.mixer.music.pause()
    input('resume?')
    pygame.mixer.music.unpause()
