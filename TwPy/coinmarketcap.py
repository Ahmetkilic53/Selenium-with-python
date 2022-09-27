from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
import time
browser = webdriver.Firefox()
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser.maximize_window()

browser.get('https://coinmarketcap.com/currencies/gami-world/')
time.sleep(3)

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/button[1]")).click()

act = ActionChains(browser)
act.send_keys("Account mail").perform()

actions = ActionChains(browser) 
actions.send_keys(Keys.TAB)
actions.perform()

act = ActionChains(browser)
act.send_keys("password").perform()

time.sleep(3)

actions = ActionChains(browser) 
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(2)


actions = ActionChains(browser) 
actions.send_keys(Keys.ESCAPE)
actions.perform()

## account one

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/span")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/section/div[2]/div[1]/div[2]/button")).click()

# Post Like
time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/section/div[2]/div[1]/a/div/img")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div/div")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[2]/div/div/div/div[4]/div[2]/div/div")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div")).click()

time.sleep(2)
browser.get('https://coinmarketcap.com/currencies/gami-world/')

########


time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div/div/img")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div[3]")).click()

time.sleep(2)

browser.get('https://coinmarketcap.com/currencies/gami-world/')

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/button[1]")).click()

act = ActionChains(browser)
act.send_keys("Account mail").perform()

actions = ActionChains(browser) 
actions.send_keys(Keys.TAB)
actions.perform()

act = ActionChains(browser)
act.send_keys("password").perform()

time.sleep(3)

actions = ActionChains(browser) 
actions.send_keys(Keys.ENTER)
actions.perform()

#  account two

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/span")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/section/div[2]/div[1]/div[2]/button")).click()

# Post Like
time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/section/div[2]/div[1]/a/div/img")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div/div")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[2]/div/div/div/div[4]/div[2]/div/div")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div/div[4]/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div")).click()

time.sleep(2)
browser.get('https://coinmarketcap.com/currencies/gami-world/')

########


time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div/div/img")).click()

time.sleep(2)
browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div[3]")).click()

#################################


