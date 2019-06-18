# adapted from: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
# code by @s2t2

import requests
from bs4 import BeautifulSoup

request_url = "__________"
print(f"GETTING MLB STATS FROM {request_url}")

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

parsed_response = BeautifulSoup(response.text)
print(type(parsed_response))

breakpoint()
