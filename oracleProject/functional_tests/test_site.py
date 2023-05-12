from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

from selenium.webdriver.common.by import By
import random, string

class TestMainPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_all_pages(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)

        self.browser.find_element(By.ID, 'use').send_keys("TestAdmin")
        time.sleep(1)

        self.browser.find_element(By.ID, 'pas').send_keys("TestPassword")
        time.sleep(1)

        self.browser.find_element(By.ID, 'sub').click()
        time.sleep(2)

        self.assertEquals( #checks to ensure the page is now on the main page
            self.browser.find_element(By.ID, "pagetitle").text,
            'Prediction Tool'
            )
        self.browser.find_element(By.ID, 't2').click()
        time.sleep(1)
        self.browser.find_element(By.ID, 'createButton').click()
        time.sleep(1)
        x = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        self.browser.find_element(By.NAME, 'name').send_keys(x)
        time.sleep(.5)
        self.browser.find_element(By.NAME, 'id').send_keys("123")
        time.sleep(.5)
        self.browser.find_element(By.NAME, 'amt_vCPU').send_keys("12")
        time.sleep(.5)
        self.browser.find_element(By.NAME, 'amt_Memory').send_keys("33")
        time.sleep(.5)
        self.browser.find_element(By.NAME, 'amt_Volume').send_keys("7")
        time.sleep(.5)
        self.browser.find_element(By.NAME, 'amt_Ephemeral_Volume').send_keys("6")
        time.sleep(.5)
        self.browser.find_element(By.ID, 'sub').click()
        time.sleep(1)

        self.assertEquals( #checks to ensure the page is now on the main page
            self.browser.find_element(By.ID, "pagetitle").text,
            'Prediction Tool'
        )

        self.browser.find_element(By.ID, 't1').click() #view that the flavor just created is existing and visible
        time.sleep(2)

        self.browser.find_element(By.ID, 'predictButton').click() #goes to the prediction page
        time.sleep(1)

        self.browser.find_element(By.ID, 'id_amt_CPU').send_keys("12") #inputs information into prediction tool
        time.sleep(.5)

        self.browser.find_element(By.ID, 'id_amt_Memory').send_keys("10000") #adding one more value
        time.sleep(.5)

        self.browser.find_element(By.ID, 'submit').click() #submitting request waiting 20 seconds for result
        time.sleep(20)

