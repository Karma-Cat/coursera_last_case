#!/usr/bin/env python3

import os
import requests

# Path to the data
path = "/supplier-data/images/"

url = "https://local/upload/"

files = os.listdir(path)

for file in files:
    if file.split('.')[1] == "jpeg":
        with open(path+file, "rb") as opened:
            r = requests.post(url, files={file: opened})
print(r.request.body)
print(r.status_code)
