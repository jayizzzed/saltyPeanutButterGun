from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

import pyautogui

from secrets import randbelow

import random


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
#
def setup_inst(url):
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

    driver.add_cookie({'name': 'mid', 'value': 'XwsV_QAAAAHkTphDg4xrw6QJIBtc'})
    driver.add_cookie({'name': 'ig_cb', 'value': '1'})
    driver.add_cookie({'name': 'ig_did', 'value': '227C20AD-91E8-442A-AEDC-830CFFA9D24B'})
    driver.add_cookie({'name': 'sessionid', 'value': '27904950104%3AAIo3V3MBBTu9nl%3A29'})
    driver.add_cookie({'name': 'shbid', 'value': '11759'})
    driver.add_cookie({'name': 'shbts', 'value': '1594562052.6612809'})
    driver.add_cookie({'name': 'rur', 'value': 'ATN'})
    driver.add_cookie({'name': 'csrftoken', 'value': 'HEgLwF8snREBwSmlQaJRKbNNE1kUeO5L'})
    driver.add_cookie({'name': 'ds_user_id', 'value': '27904950104'})
    driver.add_cookie({'name': 'urlgen', 'value': '"{\\"2003:df:5728:e400:5ea:8cfc:2a8a:d20a\\": 3320}:1jucQx:2jl-1oFCeuibubzlx1tlJ89SC7s"'})

    return driver

def log_in(driver, usr, pwd):
    driver.implicitly_wait(10)

    login = driver.find_element_by_xpath("//*[contains(text(), 'Log In')]")
    login.click()

    driver.implicitly_wait(3)

    username = driver.find_element_by_css_selector('input[name*="username"]')
    password = driver.find_element_by_css_selector('input[name*="password"]')

    username.send_keys(usr)
    password.send_keys(pwd)

    time.sleep(5)

    login = driver.find_element_by_xpath("//*[contains(text(), 'Log In')]")
    login.click()

    time.sleep(3)
    return driver

def upload(driver, path, caption):
    upload_btn = driver.find_element_by_css_selector('div[data-testid*="new-post-button"]')
    upload_btn.click()

    open_img(path)
    time.sleep(1)

    next_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
    time.sleep(1)
    next_btn.click()

    add_caption(driver, caption)

    share_btn = driver.find_element_by_xpath("//*[contains(text(), 'Share')]")
    share_btn.click()
    
def open_img(path):
    time.sleep(2)
    pyautogui.write(path)
    time.sleep(1)
    pyautogui.press('enter')
    

def add_caption(driver, caption):
    time.sleep(1)
    text_area = driver.find_element_by_xpath('//textarea')
    text_area.click()
    pyautogui.write(caption)
#

def get_img_url(driver):
    post_tnt = driver.find_element_by_class_name('PostContent__image-link ')
    #post_tnt = driver.find_element(By.XPATH("(//a[@class='PostContent__image-link '])[2]"))
    img_url = post_tnt.get_attribute('href')
    time.sleep(3)
    return img_url

def get_img_cap(driver):
    post_ptl = driver.find_element_by_class_name('PostHeader__post-title-line ')
    return post_ptl
    
def request_img(img_url):
    import requests
    import random
    
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    user_agent = random.choice(user_agent_list)

    headers = {'User-Agent': user_agent}
    
    r = requests.get(img_url,headers=headers)
    return r.content

def save_img(content, name = 'test.jpg'):
    path = 'C:\\Users\\49179\\Desktop\\Stolen Memes\\' + name
    f = open(path, 'wb')
    f.write(content)
    f.close()

def random_url():

    url_list = [
        'https://www.reddit.com/r/thatHappened/',
        'https://www.reddit.com/r/4PanelCringe/',
        'https://www.reddit.com/r/ihaveihaveihavereddit/',
        'https://www.reddit.com/r/IncelTear/',
        'https://www.reddit.com/r/Jordan_Peterson_Memes/',
        'https://www.reddit.com/r/Memes_Of_The_Dank/',
        'https://www.reddit.com/r/ComedyNecrophilia/',
        'https://www.reddit.com/r/MakeMeSuffer/',
        'https://www.reddit.com/r/terriblefacebookmemes/',
        'https://www.reddit.com/r/ComedySeizure/',
        'https://www.reddit.com/r/comedyheaven/',
        'https://www.reddit.com/r/ComedyHitmen/',
        'https://www.reddit.com/r/comedyhomicide/',
        'https://www.reddit.com/r/arabfunny/',
        'https://www.reddit.com/r/shittyadviceanimals/',
        'https://www.reddit.com/r/ElongatedPics/',
        'https://www.reddit.com/r/IMTM/',
        'https://www.reddit.com/r/worldfunnies/',
        'https://www.reddit.com/r/DeepFriedMemes/',
        'https://www.reddit.com/r/pepethefrog/',
        'https://www.reddit.com/user/HahaFunnyMeme_/',
        'https://www.reddit.com/r/wtfstockphotos/',
        'https://www.reddit.com/r/Im5andthisismacaroni/',
        'https://www.reddit.com/r/christianmemes/',
        'https://www.reddit.com/r/boomershumor/',
        'https://www.reddit.com/r/Boomerhumour/',
        'https://www.reddit.com/r/poopshitters/top/?t=day',
        'https://www.reddit.com/r/cursedimages/',
        'https://www.reddit.com/r/cursedcomments/',
        'https://www.reddit.com/r/stonks/top/',
    ]
    url = random.choice(url_list) + 'top/'
    return url

def loop():
    for x in range(48):

        sleep_minutes = randbelow(60)
        time.sleep(60*sleep_minutes)


if __name__ == '__main__':

    url = random_url()
    url_inst = 'https://www.instagram.com/'

    #sets profile, cookies & opens (reddit) url
    driver = setup(url)

    #finds image link of first element with specified class name
    img_url = get_img_url(driver)

    #finds caption of first element with specified class name
    caption = get_img_cap(driver).text

    #requests found image
    content = request_img(img_url)

    name = 'pic.jpg'
    #saves image in folder "Stolen Memes"
    save_img(content, name)

    #set profile, cookies & open (instagram) url
    driver_inst = setup_inst(url_inst)

    username = 'Tamplax@freenet.de'
    password = 'H7Vfxhmed5BvqRU'

    #logs into specified instagram account
    driver_inst = log_in(driver_inst, username, password)

    filename = name
    path = 'C:\\Users\\49179\\Desktop\\Stolen Memes\\' + filename
    
    #uploads image to instagram page and adds caption
    upload(driver_inst, path, caption)

    
