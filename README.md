# Linkedin Job Board

Python program to get last jobs on Linkedin.

## Packages
- Selenium
- Chrome web Driver

## Install Chrome web driver

You need to download the chrome driver for your current version of chrome installed 
>More at: https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/
> 

## Imports 

    from selenium import webdriver
    from selenium.webdriver.support import ui
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

## Code
Initializing the web driver and the url:

    url='https://www.instagram.com/'
    chrome_driver_path = "path to web driver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)

## Key commands:

1. WebDriverWait
2. expected_conditions.presence_of_element_located
3. find_element_by_xpath
4. time.sleep("time")
5. send_keys
# Note 
>These program is for educational purpose.

For more information visit the official website at:
>https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/