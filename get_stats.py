# adapted from: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
# code by @s2t2

import requests
from bs4 import BeautifulSoup

request_url = "https://www.baseball-reference.com/players/c/cessalu01.shtml" # an example player (pitcher)
print(f"GETTING MLB STATS FROM {request_url}")

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

soup = BeautifulSoup(response.text, features="html.parser") # add features param to avoid warning message
print(type(soup))

#breakpoint()
#stats_table = soup.find("table", "pitching_value")
# NOPE!
# referencing: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#stats_table = soup.find(id="pitching_value")
# NOPE!
# google searching: "beautifulsoup find table with given id"
# referencing: https://stackoverflow.com/questions/19591720/python-beautiful-soup-parse-a-table-with-a-specific-id
stats_table = soup.find("table", id="pitching_value")
# HMM THIS SHOULD BE CORRECT.... BUT ISN'T RETURNING ANYTHING
# SOMETIMES WEBSITES WAIT TO LOAD THE PAGE CONTENTS UNTIL LATER...
# LET'S SEE WHAT GETS LOADED BY NOW...
print(soup.text)
# SEARCH FOR <table> within that text....
# DOESN'T LOOK LIKE ANY TABLES ARE THERE
# SO WE MIGHT NOT BE ABLE TO ACCESS THE DATA
# BUT WE CAN TRY AN APPROACH USING SELENIUM TO "WAIT" FOR THE PAGE CONTENTS TO LOAD BEFORE PARSING THEM...


# SEE: get_stats2.py
