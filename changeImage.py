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
img_dir_list = os.listdir(img_dir)

for img in img_dir_list:
    if "tiff" in img:
        # Get filename only.
        img_name = os.path.splitext(img)[0]
        # Set new filetype path.
        new_filetype = os.path.join(img_dir, img_name + convert_type)

        # Process and save image.
        try:
            print(img_dir + "/" + img)
            Image.open(img_dir + "/" + img).convert("RGB").resize(size).save(new_filetype, "JPEG")
        except IOError:
            print("Cannot convert image.", img)
