from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import os
import selenium.webdriver


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        wait = WebDriverWait(self.driver, 10)
        home = wait.until(expected.element_to_be_clickable((By.CSS_SELECTOR, ".open-my-profile-dropdown")))
        return home