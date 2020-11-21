#! /usr/bin/env python3
import os
import requests


def create_json(content, filename):
    new_json = {}

    try:
        new_json["name"] = content[0]
        weight = content[1].split(" ")[0]
        new_json["weight"] = weight
        new_json["description"] = content[2]
        new_json["image_name"] = filename.split(".")[0] + ".jpeg"
    except KeyError:
        print("File not in correct format.")

    return new_json


if __name__ == "__main__":
    # External IP.
    external_ip = "35.222.174.222"

    # Linux home directory.
    home = os.path.expanduser("~")
    # Text file directory.
    txt_dir = home + r"/supplier-data/descriptions"

    # Iterate through directory, create, and upload JSON.
    for file in os.listdir(txt_dir):
        file_path = os.path.join(txt_dir, file)
        with open(file_path, "r") as description_file:
            # Read in and strip feedback into a list and append to new list.
            txt_content = description_file.readlines()
            txt_content = [line.strip() for line in txt_content]
            # Create dict using feedback content.
            description_json = create_json(txt_content, file)

            # Send description.
            web_address = "http://" + external_ip + "/fruits/"
            response = requests.post(web_address, json=description_json)
