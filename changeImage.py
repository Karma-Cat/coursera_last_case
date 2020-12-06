#!/usr/bin/env python3

import os
from PIL import Image

path = "/supplier-data/images/"
files = os.listdir(path)

for file in files:
    old_path = path + file 
    new_path = path + file.split('.')[0] + "jpeg"
    try:
        Image.open(old_path).convert("RGB").resize((600,400)).save(new_path, "JPEG")
    except IOError:
        print("cannot convert", file)