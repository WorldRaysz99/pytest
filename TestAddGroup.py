# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_firm(wd)
        self.submit_group_creation(wd)
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def submit_group_creation(self, wd):
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def fill_group_firm(self, wd):
        # fill group firm
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("qwer")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("qwer")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("qwer")

    def init_group_creation(self, wd):
        # init group creation
        wd.find_element(By.NAME, "new").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd):
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
