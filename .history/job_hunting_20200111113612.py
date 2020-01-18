import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.common.keys import Keys
import re

# path for my chrome(driver)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# indeed url only for 'morocco' jobs
global start_url
start_url = "https://ma.indeed.com"

# search string
job_title = str(
    input("what job type you looking for?!! :  " + "\n" + 'job : '))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

global location_input
global location_field
location_field = ''
location_input = ''


def enter_clear_location():
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')
    try:
        if location_field == '':
            location_input = str(
                'enter location or see all available jobs ' + '\n')
            answer_me = str(
                input('yes --> give location  ||| ' + 'no --> see all'))

            print(location_input + answer_me)

            # answer is yes
            if answer_me in ('y', 'yes', 'ye'):
                ur_location = str(input('Enter location'))
                location_field.send_keys(ur_location)
                location_field.send_keys(Keys.ENTER)

            # answer == no
            if answer_me in ('n', 'no', 'nope'):
                time.sleep(2)
                location_field.send_keys(Keys.ENTER)

        # if location_field was filled (by default)
        else:
            location_field.send_keys(Keys.CONTROL + "a")
            location_field.send_keys(Keys.DELETE)
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)

    except:
        Exception()


def select_location():
    span_tag = driver.find_element_by_xpath(
        '//*[@id="rb_Location"]/div[1]/span')
    # div tag
    span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
    # ul tag
    element = span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul')
    # li tag
    lists = element.find_elements_by_tag_name('li')
    print('all Urls available :  \n ')

    # Printing all lists of hrefs / all locations
    all_links = []
    all_locations = []
    try:
        for items in lists:
            # a tag / # Get locations name
            a_tag = items.find_element_by_tag_name('a')
            link = a_tag.get_attribute('href')
            string = a_tag.get_attribute('title')
            all_links.append(link)

            # Exclude digits whene returning titles = Locations
            new_string = ''.join(re.findall("[a-zA-Z]+", string))
            all_locations.append(new_string)

        print('urls found : ', all_links, '\n')  # optional delete later
        print('Location\'s Lists :', all_locations, '\n')

        # Convert first letter to Uppercase() if user typed it lower
        choice = input(str('Fetch results by location : \n'))
        convert_choice = (choice.title())
        if choice != convert_choice:
            location_pattern = re.compile(convert_choice)
            new_return = list(filter(location_pattern.match, all_locations))
            print('location after convertion is   : ', new_return)

            # return href that has input user(Location's name)
            href_pattern = re.compile('=' + convert_choice + '&jlid')
            # link match retrieved
            new_href = list(filter(href_pattern.search, all_links))
            if new_href:
                print('url match !!  : ', new_href, '\n')
                # Copy this link to (indeed) url section
                current_url = driver.current_url
                print('Current url running :  ', current_url, '\n')

                slice_current_url = re.search(
                    r'https://\w+\.\w+\.com', current_url)
                #new_url = list(filter(slice_current_url.search, current_url))
                # this will take form index(22)=emploi until the end
                print('current url after slicing is  : ', slice_current_url)
                for slice_new_href in new_href[22:]:
                    print('final url : ', slice_new_href)
                # # past this part after (.com)
                # new_url = slice_current_url, '/', slice_new_href
                # print('Complete Url :', new_url)

            else:
                print('Nothing Match Your title in hrefs list  !!')
        else:
            print('Your choice was correct : ', choice)

    except:
        Exception()


# call the two functions
enter_clear_location()
select_location()
