from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

PATH = "functional_tests/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:8000/")