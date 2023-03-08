from selenium import webdriver
from main.models import ToDoList, Item, Flavor
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

from selenium.webdriver.common.by import By


class TestMainPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_login_button_from_main(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)
        self.browser.find_element(By.ID, 'loginButton').click()
        time.sleep(1)
        foo = self.browser.current_url
        foo = foo[:-7] + "/login/"
        self.assertEquals(
        self.browser.current_url,
        foo
        )
        time.sleep(1)

        self.browser.find_element(By.ID, 'use').send_keys("kevin")
        time.sleep(1)

        self.browser.find_element(By.ID, 'pas').send_keys("guilly44")
        time.sleep(1)

        self.browser.find_element(By.ID, 'sub').click()
        self.browser.get(self.live_server_url)
        time.sleep(5)

        self.assertEquals(
            self.browser.find_element(By.ID, "pagetitle").text,
            'Home Page'
            )


