import os
import sys
from typing import Any

import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
sound_dir = os.path.join(main_dir, "sounds")


def load_image(name, color_key=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = int(size[0] * scale), int(size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, pg.RLEACCEL)

    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(sound_dir, name)
    sound = pg.mixer.Sound(fullname)
    return sound


class Fist(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("fist.png", 1)
        self.fist_offset = (-235, 80)
        self.punching = False

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect = self.rect.move(self.fist_offset)


pg.init()
screen_size = width, height = 800, 600
screen = pg.display.set_mode(screen_size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
