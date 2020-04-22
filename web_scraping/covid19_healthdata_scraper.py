#from states import us_states_list as us_states
#from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

covid19_healthdate_bystate = []

def covid19_healthdata_scrape(state):
    state = state.lower().replace(' ', '-')
    url = f"https://covid19.healthdata.org/united-states-of-america/{state}"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    dates_div = driver.find_elements_by_xpath("/html/body/div/div/main/div[3]/div[1]/div[2]")
    divs_text = [x.text for x in dates_div]
    divs_text_split = divs_text[0].split('\n')
    #print(divs_text_split)
    driver.close()
    scraped_data = {
    'state': state,
    'state_data': {
        'Mass Gathering Restriction': divs_text_split[1],
        'Initial Business Closure': divs_text_split[3],
        'Educational Facilities Closure': divs_text_split[5],
        'Non-Essential Services Closure': divs_text_split[7],
        'Stay at Home Order': divs_text_split[9],
        'Travel Severely Limited': divs_text_split[11]
        }
    }
    covid19_healthdate_bystate.append(scraped_data)