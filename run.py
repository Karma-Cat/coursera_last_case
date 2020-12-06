#!/usr/bin/env python3

import requests
import os

path = "/supplier-data/descriptions/"
dataKeys = ['name', 'weight', 'description', 'image_name']

files = os.listdir("path")
for file in files:
    dataDict = {}
    with open(path+file, 'r') as file_r:
	    lines = file_r.readlines()
        weight = int(lines[1].split('.')[0]) 
        lines[1] = weight
        pic_name = file.split('.')[0] + "jpeg"
        lines.append(pic_name)
	    for key, value in zip(dataKeys, lines):
		    dataDict.update({key: value})
    resp = requests.post("http://[linux-instance-external-IP]/fruits", json=dataDict)
print(resp.raise_for_status())
print(resp.status_code)
