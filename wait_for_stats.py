# adapted from:
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
#   + https://github.com/s2t2/student-support-apt-scraper-py/blob/master/browsing5.py
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/selenium.md
# code by @s2t2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

request_url = "https://www.baseball-reference.com/players/c/cessalu01.shtml" # an example player (pitcher)
print(f"GETTING MLB STATS FROM {request_url}")

driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed
print(type(driver))

driver.get(request_url)
print(driver.title)

try:
    print("WAITING FOR PAGE CONTENTS TO LOAD...") # THIS MIGHT TAKE LIKE 20 SECONDS ACTUALLY...
    table_appears = EC.presence_of_element_located((By.ID, "pitching_value"))
    wait_duration = 3 # seconds
    WebDriverWait(driver, wait_duration).until(table_appears)
    print("PAGE CONTENTS LOADED!")

    print("PARSING HTML TABLE...")
    soup = BeautifulSoup(driver.page_source, "html.parser") # add features param to avoid warning message
    print(type(soup))
    stats_table = soup.find("table", id="pitching_value")

    #breakpoint()

    print("2019 STATS:")
    # example using one of the stats rows (2019)
    stats_row = stats_table.find("tr", id="pitching_value.2019")

    stats_data = stats_row.findAll("td")
    for td in stats_data:
        # <td class="right" data-stat="age">27</td>
        #print(type(td)) #> <class 'bs4.element.Tag'>
        #breakpoint()
        stat_name = td.attrs["data-stat"] #> age
        stat_val = td.text #> "27" (FYI: might need to convert certain stats to floats or integrers here)
        print(f"THE {stat_name} STAT VALUE IS: {stat_val}")

except TimeoutException:
    print("TIME OUT!")
finally:
    driver.quit() # always close the web browser to prevent memory issues
