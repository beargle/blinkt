#!/usr/bin/env python

import argparse
import sys
import time

from envirophat import weather
from blinkt import set_all, show, clear

parser = argparse.ArgumentParser(description='Light blinkt once pressure threshold breached.')
parser.add_argument('-b', '--brightness', type=float, nargs='?', default=0.1,
                    help='float between 0.0 (off) and 1.0 (brightest) to set intensity of blinkt leds')
parser.add_argument('-s', '--sleep', type=float, nargs='?', default=2,
                    help='seconds between led color change events')
parser.add_argument('-p', '--pressure', type=float, nargs='?', default=1030,
                    help='Pressure unit threshold (in Hectopascals (hPa)) over which blinkt leds are lit')
parser.add_argument('-c', '--color', type=str, required=True,
                    help='Color to show on blinkt leds. Accepts a comma-delimited string of space delimited RGB values.')
args = parser.parse_args()

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

def get_pressure_in_hpa(weather):
    pa = weather.pressure()
    hpa = pa / 100
    return hpa

def show_led_all(color, brightness):
    r, g, b = color
    set_all(r, g, b, brightness)
    show()

if __name__ == "__main__":
    try:
        pressure = args.pressure
        brightness = args.brightness
        sleep = args.sleep
        colors = [color.strip().split(" ") for color in args.color.split(',')]
        while True:
            hpa = get_pressure_in_hpa(weather)
            if hpa >= pressure:
                for color in colors:
                    show_led_all(color, brightness)
                    time.sleep(sleep)
            else:
                clear()
                show()
    except KeyboardInterrupt:
        pass
