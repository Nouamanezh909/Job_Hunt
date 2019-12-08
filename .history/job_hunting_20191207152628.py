import requests
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# defining url
global start_url

# indeed url only for 'morocco' jobs
start_url = "https://ma.indeed.com"

# path for chrome webdrive (change this path accordding to my pc)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string
job_title = str(input("what job type you looking for?!! " + "\n"))

# ask --> if you want to specify location or not yet
location = str(
    input("Do you want to give location or proccede to see all ???" + "\n"))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')

job_field.send_keys(job_title)
location_field.send_keys(location)
location_field.send_keys(Keys.ENTER)