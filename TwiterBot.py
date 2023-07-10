from selenium import webdriver
import  pandas as pd
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver import ActionChains

driver = webdriver.Chrome()
website = 'https://twitter.com/login'
driver.get(website)
driver.implicitly_wait(5)
driver.maximize_window()


username = driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
username.send_keys("sudorson332")
time.sleep(10)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
button.click()
time.sleep(10)
driver.implicitly_wait(5)


password = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
password.send_keys("kri82sna")
time.sleep(5)
logins = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
logins.click()
time.sleep(10)
driver.implicitly_wait(5)
