# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")



driver.quit()
