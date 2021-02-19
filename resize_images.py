#!python3 resize_images.py
# -*- coding: utf-8 -*-

"""
{This file resizes any images in a given folder to 240x320 pixels. 
It is recommended that the files are already in a 3:4 ratio before running.}
"""

# Built-in/Generic Imports
from os import listdir

# Libs
from PIL import Image


__author__ = 'Mara Fennema'
__copyright__ = 'Copyright 2021, Wie-is-het'
__credits__ = ['Mara Fennema']
__version__ = '1.0.0'
__maintainer__ = 'Mara Fennema'
__email__ = 'maradfennema@gmail.com'
__status__ = 'Dev'

path = input("What is the path of the files that need to be resized?\n")
files = listdir(path)

for f in files:
    resized = Image.open(path+f).resize((240,320))
    resized.save(path+f)

print("Your files have been resized.")