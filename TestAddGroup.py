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
        wd.get("http://localhost/addressbook/")
        wd.find_element('user').click()
        wd.find_element("user").clear()
        wd.find_element("user").send_keys("admin")
        wd.find_element("pass").clear()
        wd.find_element("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element("new").click()
        wd.find_element("group_name").click()
        wd.find_element("group_name").clear()
        wd.find_element("group_name").send_keys("qwer")
        wd.find_element("group_header").click()
        wd.find_element("group_header").clear()
        wd.find_element("group_header").send_keys("qwer")
        wd.find_element("group_footer").click()
        wd.find_element("group_footer").clear()
        wd.find_element("group_footer").send_keys("qwer")
        wd.find_element("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()
    
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
