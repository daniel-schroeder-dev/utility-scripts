#!/usr/bin/python

import sys
import os

filename = sys.argv[1]
name, _ = filename.split(".")

os.system(f"ffmpeg -i {filename} -filter_complex '[0:v] palettegen' palette.png")
os.system(f"ffmpeg -i {filename} -i palette.png -filter_complex '[0:v][1:v] paletteuse' {name}.gif") 
