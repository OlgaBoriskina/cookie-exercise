from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import os
import selenium.webdriver


class ClickLogon:

    logon_locator = "//a[contains(@href, '/sign_in')]"

    def __init__(self, driver):
        self.driver = driver

    def logon(self):
        wait = WebDriverWait(self.driver, 10)
        logon = wait.until(expected.element_to_be_clickable((By.XPATH, self.logon_locator)))
        return logon

    def logon_click(self):
        wait = WebDriverWait(self.driver, 10)
        self.logon().click()