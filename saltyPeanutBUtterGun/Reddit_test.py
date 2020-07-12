from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

def setup(url):
    path_to_firefox = 'C:\Program Files\Mozilla Firefox\firefox.exe'
    binary = FirefoxBinary(path_to_firefox)

    profile = webdriver.FirefoxProfile()
    user_agent ="Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/83.0.268992909 Mobile/15E148 Safari/605.1"
    profile.set_preference("general.useragent.override", user_agent)
    profile.set_preference("dom.webdriver.enabled", False)
    #profile.set_preference('excludeSwitches', ["enable-automation"])
    profile.set_preference('useAutomationExtension', False)

    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

    driver.get(url)

    driver.add_cookie({'name': 'loid', 'value': '0000000000791oc7u1.2.1594567719564.Z0FBQUFBQmZDeXduaEFGR0FwWkYyc0dHRGtfX1lka3VPbzVvcUZKcDNxRk5CckEzRkxrdGw3R0puWUNIY2Y4WjNTMmFpMERLOXpxbTcwZkdOSGdyTmN3TXJUWjZzS0NlM0plWjYzdEl0Rm1yZjFrVzkxYlp1OG9VQVNvYVVuVVJMaW42QjQ0ZVRFX1o'})
    driver.add_cookie({'name': 'token', 'value': 'eyJhY2Nlc3NUb2tlbiI6Ii1JT0RESmM4ZlducU1tZzdpcnhocWpYOXNrY2siLCJ0b2tlblR5cGUiOiJiZWFyZXIiLCJleHBpcmVzIjoxNTk0NTcxMzE5NTc1LCJzY29wZSI6IioiLCJ1bnNhZmVMb2dnZWRPdXQiOnRydWV9.2'})
    driver.add_cookie({'name': 'theme', 'value': 'daymode'})
    driver.add_cookie({'name': 'compact', 'value': 'true'})
    driver.add_cookie({'name': 'session_tracker', 'value': 'qnqlmljhbgpfkfraeq.0.1594567719604.Z0FBQUFBQmZDeXdubVRFcmRaZXo2YU5UdEFudlVtMnJCb1dqcE1yWkZxNVVsRGlkUnlXdnJoN1RwNkpIMm1HUldOdjlvdndkQ1BQT2wwZFd1N0I0b1FMc2RBZW5vT2dDSkFuUHFMZEhCYnE4YlVHME5kX05vaE1fZW14cVFtaXRZbzBlcFdfS25ibUE'})
    driver.add_cookie({'name': 'edgebucket', 'value': 'B3L4p1T1Q6OKXImNUm'})
    driver.add_cookie({'name': 'EUCookieNotice', 'value': '1'})
    driver.add_cookie({'name': 'session_tracker', 'value': 'qnqlmljhbgpfkfraeq.0.1594567720756.Z0FBQUFBQmZDeXdwcGhBbmtHQU1iX1dKOFk5RnF0Z3VoYXhpMWJPalFidktpbndlYkdnT3JDanFTRU9tZXZRNV9MOFB0N3E4TExlcjdYYkI1NlZLeDhJRXdhZVBYRTdDZ1FJelBnakE3V1QwY2ZLYkJiQ1lIREM4X09kUjh4ekJkeHdSM2ZxbU9Mcmo'})
    driver.add_cookie({'name': '_recent_srs', 'value': 't5_2zzho'})

    time.sleep(5)
    con_btn = driver.find_element_by_xpath("//*[contains(text(), 'Continue')]")
    con_btn.click()
    
    return driver

def loop():
    print("start")

def get_img_url(driver):

    post_tnt = driver.find_element_by_class_name('PostContent__image-link ')
    img_url = post_tnt.get_attribute('href')
    time.sleep(3)
    return img_url

def request_img(img_url):
    import requests
    import random
    '''
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    user_agent = random.choice(user_agent_list)

    headers = {'User-Agent': user_agent,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
               'Dnt': '1',
               'Host': 'httpbin.org',
               'Upgrade-Insecure-Requests': '1'}
    '''
    r = requests.get(img_url)
    return r.content

def save_img(content, name = 'test.jpg'):
    f = open(name, 'wb')
    f.write(content)
    f.close()

if __name__ == '__main__':

    url = 'https://www.reddit.com/r/ComedyCemetery/'
    
    driver = setup(url)

    img_url = get_img_url(driver)

    content = request_img(img_url)

    save_img(content)

    
