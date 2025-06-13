from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def scroll_to_bottom(driver):
    wait = WebDriverWait(driver, 20)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            wait.until(lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height)
            last_height = driver.execute_script("return document.body.scrollHeight")
        except:
            break