#!/usr/bin/env python

import random
import time

from blinkt import set_clear_on_exit, set_pixel, show, set_brightness, set_all

palette = [(255, 35, 0),
           (127, 255, 0),
           (128, 0, 128)]

set_clear_on_exit()
set_brightness(1)

while True:
    random_color = palette[random.randint(0, len(palette) - 1)]
    r, g, b = random_color
    set_all(r, g, b)
    show()
    time.sleep(1)
