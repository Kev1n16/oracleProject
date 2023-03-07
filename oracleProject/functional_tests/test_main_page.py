from selenium import webdriver
from main.models import ToDoList, Item, Flavor
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestMainPage(StaticLiveServerTestCase):



    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_page_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)

        # The user requests the page for the first time
        # alert = self.browser.find_element_by_class_name('noproject-wrapper')