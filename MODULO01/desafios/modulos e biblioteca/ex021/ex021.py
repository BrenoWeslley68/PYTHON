import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('desafios//modulos e biblioteca/ex021/boom.wav')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)