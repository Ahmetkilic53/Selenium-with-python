from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
import time
browser = webdriver.Firefox()
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser.get("https://accounts.firefox.com/?context=fx_desktop_v3&entrypoint=fxa_app_menu&action=email&service=sync")

time.sleep(2)
browser.switch_to.new_window("tab")
browser.get("https://coinmarketcap.com/currencies/gami-world/")

time.sleep(2)

action = ActionChains(browser)
 
# perform the operation
action.key_down(Keys.PAGE_DOWN).send_keys('KEY_DOWN').perform()

time.sleep(2)
action.key_down(Keys.PAGE_DOWN).send_keys('KEY_DOWN').perform()

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/section/div/div/img")).click()


