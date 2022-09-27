from re import search
from selenium import webdriver
import time
browser = webdriver.Firefox()
from selenium.webdriver.common.by import By

#Hesap oluşturma sayfasına gidiş

browser.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1663061792&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dba1c62d0-422d-3032-95aa-99e29cc5d0e5&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=888233DE243C2CFB&bk=1663061792&uiflavor=web&lic=1&mkt=TR-TR&lc=1055&uaid=67eec449f3004f5b9f95cf5a744293e6")

#Form doldurulumu

time.sleep(2)

mail = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input"))
mail.send_keys("mail")

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input")).click()

time.sleep(2)

password = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]"))
password.send_keys("password")

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[7]/div/div/div[2]/input")).click()

time.sleep(2)

name = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[1]/input"))
name.send_keys("name")

surName = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[2]/input"))
surName.send_keys("surName")

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[2]/div/div/div[2]/input")).click()

time.sleep(2)

day = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select"))
day.send_keys("day")

month = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select"))
month.send_keys("month")

year = browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[3]/input"))
year.send_keys("year")

browser.find_element(By.XPATH, ("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[6]/div/div/div[2]/input")).click()

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div/div/div[1]/button")).click()

time.sleep(2)

browser.find_element(By.XPATH, ("/html/body/div/div/div[1]/div/div[2]/div/ul/li[2]/a")).click()

time.sleep(2)






