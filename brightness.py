#!/usr/bin/env python

import os
import sys

monitor = "eDP-1"


brightness = (float(sys.argv[1]))/10
command = "xrandr --output "+ monitor +" --brightness {}".format(brightness)
RED = "\033[91m"
GREEN = "\033[96m"

if len(sys.argv) != 2:
    print(RED + "python script.py <brightness>")
    sys.exit(1)

if brightness < 0.1 or brightness > 1:
    print(RED + "ERROR: los niveles de brillo son entre 1 y 10 ")
    sys.exit(1)


os.system(command)
os.system("clear")
print(GREEN + "Brightness --> ", brightness)