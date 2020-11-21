#!/usr/bin/env python3
import os
import requests

# Linux home directory.
home = os.path.expanduser("~")
# Image directory.
img_dir = home + r"/supplier-data/images"
# Upload address.
url = "http://localhost/upload"

for root, dirs, files in os.walk(img_dir):
    for file in files:
        image_path = os.path.join(img_dir, file)
        # Open request and upload image file.
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
        opened.close()
