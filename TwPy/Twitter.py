from argparse import Action
from re import search
from selenium import webdriver
import tweepy
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Firefox()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser.maximize_window()
browser.get("https://www.twitter.com")

#Twitter giriş alanı

time.sleep(3)
browser.find_element(By.XPATH, ("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")).click()

time.sleep(2)

username = browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))
username.send_keys("username")


browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")).click()

time.sleep(3)

sifre = browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
sifre.send_keys("password")


browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")).click()

time.sleep(2)

#Gami hesabına giriş

ara = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"))
ara.send_keys("gamiworld")

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div/div/div/div[2]/div[1]")).click()

time.sleep(3)

#follow ve like işlemleri

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/span/span")).click()

time.sleep(3)

act = ActionChains(browser)
act.send_keys("j+l+j+l+j+l").perform()

time.sleep(3)

#Hesaptan çıkış

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]")).click()

time.sleep(2)

actions = ActionChains(browser) 
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(2)

actions = ActionChains(browser) 
actions.send_keys(Keys.ENTER)
actions.perform()

#####################################################################################################################################################

time.sleep(3)
browser.find_element(By.XPATH, ("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")).click()

time.sleep(2)

username = browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))
username.send_keys("username")


browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")).click()

time.sleep(3)

sifre = browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
sifre.send_keys("sifre")


browser.find_element(By.XPATH, ("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")).click()

time.sleep(2)

#Gami hesabına giriş

ara = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"))
ara.send_keys("gamiworld")

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div/div/div/div[2]/div[1]")).click()

time.sleep(3)

#follow ve like işlemleri

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/span/span")).click()

time.sleep(3)

act = ActionChains(browser)
act.send_keys("j+l+j+l+j+l").perform()

time.sleep(5)

#Hesaptan çıkış

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]")).click()

time.sleep(1)

actions = ActionChains(browser) 
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(2)

actions = ActionChains(browser) 
actions.send_keys(Keys.ENTER)
actions.perform()