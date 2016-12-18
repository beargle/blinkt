#!/usr/bin/env python

import argparse

from envirophat import light
from blinkt import set_all, show

parser = argparse.ArgumentParser(description='Reflect enviro-phat color reading on blinkt.')
parser.add_argument('-b', '--brightness', type=float, nargs='?', default=0.1,
		    help='float between 0.0 (off) and 1.0 (brightest) to set intensity of blinkt leds')
parser.add_argument('-s', '--sleep', type=float, nargs='?', default=0.1,
		    help='seconds between blinkt led color refresh events')
args = parser.parse_args()

def reflect(light, brightness):
    r, g, b = light.rgb()
    set_all(r, g, b, brightness)
    show()

if __name__ == "__main__":

    try:
        while True:
	    reflect(light, args.brightness)
	    time.sleep(args.sleep)
    except KeyboardInterrupt:
        pass
