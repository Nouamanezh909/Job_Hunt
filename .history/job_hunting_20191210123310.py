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

# path for chrome webdrive (change this path accordding to your pc)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

<<<<<<< HEAD
# job search filed 
=======
# search string
>>>>>>> origin
job_title = str(input("what job type you looking for?!! " + "\n"))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

<<<<<<< HEAD
location_field = ""

=======

location_field = ''


>>>>>>> origin
def clear_location_field(location_field):
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')

    # Declare those var as Global
    global location_input
    global name
    global answer_me

    # VAlidate if location filed empty or not (by Default)
    if location_field == '':
        location_input = str(input
                             ("Do you want to give location or proccede to see all available jobs  ???" + "\n"))

        answer_me = str(input(' Yes --> give location' +
                              ' |||' + 'No --> See all' + '\n'))
        if answer_me == 'yes':
            name = str(input('Enter location'))
            location_field.send_keys(name)
            location_field.send_keys(Keys.ENTER)

        # if answer is NO
        else:
            time.sleep(1)
            location_field.send_keys(Keys.ENTER)

<<<<<<< HEAD
    # run test to see if location was filled (by-default)
    
    
    # delete input field insearted by default 
    location_field.send_keys(Keys.CONTROL + "a")
    location_field.send_keys(Keys.DELETE)
=======
    else:
        location_field.send_keys(Keys.CONTROL + "a")
        location_field.send_keys(Keys.DELETE)
        time.sleep(3)
>>>>>>> origin

        # after deleting promte me to this string again
        print(location_input + '\n' + '--' + answer_me)

        #answer is yes
        if answer_me == 'yes':
            print(name)
            location_field.send_keys(name)
            location_field.send_keys(Keys.ENTER)
        # if answer is NO
        else:
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)


clear_location_field(location_field)