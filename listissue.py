#!/usr/bin/env python3
import json

import requests

api = "https://api.github.com/repos"

url = input("The Repository URL: ")
repo = url.split('https://github.com')
tag_name = input("Tag name: ")
# Request a list of issues
print("REPO", repo)
expr = api + repo[1] + '/issues?labels=' + tag_name
# print(expr)
resp = requests.get(expr)
x = json.loads(resp.text)

for values in x:
    print('#', values['number'])
    print('Title', values['title'])
