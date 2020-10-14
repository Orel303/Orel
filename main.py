import pygame
import random
import sys
import os
import time

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"
# os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

info = pygame.display.Info()
WIDTH_WIN, HEIGH_WIN = Info,current_w * 100/125, Info.current_h * 100/125
print(info.current_w,into.current.h)
print(WIDTH_WIN, HEIGH_WIN)

screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
pygame.mouse.set_visible(False)

FPS = 60
clock = pygame.time.Clock()

run = True
while run:
    for a in pygame.event.get:
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAP:
            run = False