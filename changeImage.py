#!/usr/bin/env python3
import os
from PIL import Image


# Image parameters.
size = (600, 400)
convert_type = ".jpeg"

# Linux home directory.
home = os.path.expanduser("~")
# Image directory.
img_dir = home + r"/supplier-data/images"

for root, dirs, files in os.walk(img_dir):
    for file in files:
        # Create image object.
        image_path = os.path.join(img_dir, file)
        im = Image.open(image_path)

        # Convert input image, and save.
        im.convert("RGB").resize(size)
        im.save(image_path)
