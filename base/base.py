import datetime
import random

from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver):
        self.driver = driver



    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        assert word == result
        print("Good value : " + word)

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('D:\\Adminka\\selenium\\screen\\' + name_screenshot)



    """Method assert url"""
    def assert_url(self, url):
        assert self.driver.current_url == url
        print("Url верный : " + url)











