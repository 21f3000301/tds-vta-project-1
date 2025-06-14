# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
import json

response = requests.get("https://google.com/")
# res=response.json()
# print(type(res))
print(response.text)