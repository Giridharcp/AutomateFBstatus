from brainyquote import pybrainyquote
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def randomquote():#Used to return a random quote from BrainyQuotes official website.
    random=(pybrainyquote.get_random_quote())
    string=''.join(str(e) for e in random)
    string=string.replace('<img alt=','').replace('"','')
    word=string.split('.')
    return(word[0])

def update_status(): #To update a random FB status by retrieving a random quote and updating it.
    
    
    quote=randomquote()

    ### login details ########################
    username = "youremail@gmail.com"
    pwd = "password@1"
    ##########################################

    ### what is on my mind ###################
    msg = quote
    ##########################################

    # initializing driver and loading web
    chrome_path = r"chromedriver.exe"
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get("http://www.facebook.com/")
    # end initializing

    # start login
    user_input = driver.find_element_by_xpath("""//*[@id="email"]""")
    pwd_input = driver.find_element_by_xpath("""//*[@id="pass"]""")
    user_input.send_keys(username)
    pwd_input.send_keys(pwd)
    pwd_input.send_keys(Keys.ENTER)
    # end login

    # writing msg
    time.sleep(3)
    first_what_is_on_my_mind_element = driver.find_element_by_class_name("_5qtp")
    first_what_is_on_my_mind_element.click()
    time.sleep(2)
    second_what_is_on_my_mind_element = driver.switch_to.active_element
    second_what_is_on_my_mind_element.send_keys(msg)
    # end writing

    # posting
    buttons = driver.find_elements_by_tag_name('button')
    for button in buttons:
        if 'Post' in button.text:
            button.click()
    # end posting
                
    
    time.sleep(4)
    os.system('taskkill /f /im chromedriver.exe')
    os.system('taskkill /f /im chrome.exe')
    return
update_status()
