from re import search
from selenium import webdriver
import time
browser = webdriver.Firefox()
from selenium.webdriver.common.by import By

#Create Account

browser.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=TR&continue=https%3A%2F%2Fmail.google.com&dsh=S570454782%3A1663140288158123&flowEntry=SignUp&flowName=GlifWebSignIn&hl=tr&service=mail")

#Form 

time.sleep(2)

name = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input"))
name.send_keys("name")

surName = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input"))
surName.send_keys("surname")

mail = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input"))
mail.send_keys("mail")

password = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input"))
password.send_keys("password")

passwordX = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"))
passwordX.send_keys("password")

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")).click()

#telephone
time.sleep(2)

telephone = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div[2]/div[1]/label/input"))
telephone.send_keys("telephone")

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")).click()

time.sleep(5)

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")).click()

time.sleep(2)

day = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/input"))
day.send_keys("day")

month = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div/div/div[2]/select"))
month.send_keys("month")

year = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/input"))
year.send_keys("year")

gender = browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/input"))
gender.send_keys("gender")

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")).click()

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/span")).click()

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")).click()


#--------------------------------------
#new window
#browser.switch_to.new_window("tab")
#browser.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=TR&continue=https%3A%2F%2Fmail.google.com&dsh=S570454782%3A1663140288158123&flowEntry=SignUp&flowName=GlifWebSignIn&hl=tr&service=mail")
#--------------------------------------

#Form

