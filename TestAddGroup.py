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
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.creation_group(wd, Group("qwer1", "qwer2", "qwer3"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.creation_group(wd, Group("", "", ""))
        self.return_to_group_page(wd)
        self.logout(wd)


    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd = self.wd
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_group_page(self, wd):
        # open group page
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def creation_group(self, wd, group):
        wd = self.wd
        #init group creation
        wd.find_element(By.NAME, "new").click()
        #fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        #submit group creation
        wd.find_element(By.NAME, "submit").click()

    def return_to_group_page(self, wd):
        # return to group page
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self, wd):
        # logout
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
    
    def tearDown(self):
        wd = self.wd
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
