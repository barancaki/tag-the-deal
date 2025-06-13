from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from driver.driver_path import get_the_driver_path

def setup_driver():
    driver_p = get_the_driver_path()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(driver_p), options=options)
    return driver