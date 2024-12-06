from operator import contains

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_login():
    driver=webdriver.Chrome()

    driver.get("https://www.flipkart.com/")
    time.sleep(5)
    text_box = driver.find_element(By.XPATH,value="//input[@placeholder='Search for products, brands and more']")
    text_box.send_keys("Mobile")
    time.sleep(5)
