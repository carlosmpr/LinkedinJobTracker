import os
import time

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = ""
username = ""
password = ""
url = "https://www.linkedin.com"
chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)

enter_username = WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_element_located((By.ID, 'session_key')))


enter_username.send_keys(username)

enter_password = WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.ID, 'session_password')))

enter_password.send_keys(password)
enter_password.send_keys(Keys.RETURN)

time.sleep(5)
jobs = WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.ID, 'ember23')))

jobs.click()
time.sleep(5)

search = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div/div[2]/div[1]/div/div[2]/input[1]')
search.send_keys('Front end ')
time.sleep(5)

country = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div[2]/input[1]')
country.send_keys('New York')
button = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div/div[2]/button[1]').click()
time.sleep(3)

all_jobs = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[2]')

print(all_jobs.text)


