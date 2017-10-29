from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import os
import selenium.webdriver


class LoginPage:
    set_mail = "boriskina1992@gmail.com"
    set_password = "V7hs7yl"
    username_locator = "id('user_email')"
    password_locator = "id('user_password')"
    submit_locator = ".login-button"

    def __init__(self, driver):
        self.driver = driver

    def mail(self):
        wait = WebDriverWait(self.driver, 10)
        mail = wait.until(expected.element_to_be_clickable((By.XPATH, self.username_locator)))
        return mail

    def password(self):
        password = self.driver.find_element_by_xpath(self.password_locator)
        return password

    def submit_login(self):
        submit_login = self.driver.find_element_by_css_selector(self.submit_locator)
        return submit_login

    def login_in_form(self):
        self.mail().send_keys(self.set_mail)
        self.password().send_keys(self.set_password)
        self.submit_login().click()