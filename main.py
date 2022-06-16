import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ["PATH"] += r";C:/SeleniumDrivers"

driver = webdriver.Chrome()

driver.get("https://www.supremenewyork.com/shop")

driver.implicitly_wait(10)

newBrowserWindow = driver.find_element(By.CLASS_NAME, "jackets")

newBrowserWindow.click()
