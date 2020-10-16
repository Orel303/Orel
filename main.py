import pygame
import random
import sys
import os
import time
from colors import COLOR

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,30"
# os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w * 100/100, info.current_h * 100/100
print(info.current_w, info.current_h)
print(WIDTH_WIN, HEIGHT_WIN)

path = os.path.dirname(os.path.abspath(__file__))

saturn = os.path.join(path, "6s.png")
pygame.display.set_icon(pygame.image.load(saturn))
pygame.display.set_caption("Stars")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))


FPS = 60
clock = pygame.time.Clock()
NUMBER_OF_STARS = 200
NEIGH_BG_COLOR = (5, 0, 50))

class Stars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    self.speed = random.randint(1,2)
    self.size = random.randint(1,2)
    self.pos = random.randrange(WIDTH_WIN), random.randrange(HEIGHT_WIN)
    self.image = pygame.Surface((self.size * 2, self.size * 2))
    pygame.draw.circle(self.image, pygame.Color(
        random.choice(COLOR[238:262])), [self.size, self.size] self.size)
        self.rect = self.image.get_rect(contor=self.pos)

sprites = pygame.sprite.LayeredUpdates()
for _ in range(NUMBER_OFSTARS):
    stars = Stars()
    sprites.add(stars, layer=o)



run = True
while run:
    for e in pygame.event.get:
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAP:
            run = False


sprites.update()
screen.fill(NIGHT_BG_COLOR)
sprites.draw(screen)
pygame.display.update()