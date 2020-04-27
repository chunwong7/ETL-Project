#from states import us_states_list as us_states
#from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

covid19_healthdate_dates_bystate = []
covid19_healthdate_resources_bystate = []

def covid19_healthdata_scrape(state):
    formatedstate = state.lower().replace(' ', '-')
    url = f"https://covid19.healthdata.org/united-states-of-america/{formatedstate}"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    dates_div = driver.find_elements_by_xpath("/html/body/div/div/main/div[3]/div[1]/div[2]")
    dates_divs_text = [x.text for x in dates_div]
    dates_text_split = dates_divs_text[0].split('\n')
    resources_div = driver.find_elements_by_xpath("/html/body/div/div/main/div[3]/div[3]/div[2]/div/div[2]/div[2]")
    resources_div_text = [x.text for x in resources_div]
    resources_div_split = resources_div_text[0].split('\n')
    driver.close()
    dates_data = {
    'state': state,
    'Mass Gathering Restriction': dates_text_split[1],
    'Initual Business Closure': dates_text_split[3],
    'Educational Facilities Closure': dates_text_split[5],
    'Non-Essential Services Closure': dates_text_split[7],
    'Stay at Home Order': dates_text_split[9],
    'Travel severely limited': dates_text_split[11]}
    resources_data = {
    'Hospital Beds Needed': int(resources_div_split[1].replace('beds','').replace(',','')),
    'Hospital Beds Available': int(resources_div_split[3].replace('beds','').replace(',','')),
    'Hospital Beds Shortage': int(resources_div_split[5].replace('beds','').replace(',','')),
    'ICU Beds Needed': int(resources_div_split[7].replace('beds','').replace(',','')),
    'ICU Beds Available': int(resources_div_split[9].replace('beds','').replace(',','')),
    'ICU Beds Shortage': int(resources_div_split[11].replace('beds','').replace(',','')),
    'Ventilators Needed': int(resources_div_split[13].replace('ventilators','').replace(',',''))
    }
    covid19_healthdate_dates_bystate.append(dates_data)
    covid19_healthdate_resources_bystate.append(resources_data)
    
