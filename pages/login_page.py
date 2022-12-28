import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pickle

import config
from base.base import Base


class Login_page(Base):
    url_authorization = 'https://moba.ru/auth/'    #Страница Авторизацияя

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators:
    l_user_mail = "//input[@name='USER_LOGIN']"                                          #Локатор поля ввода User_name
    l_user_password = "//input[@name='USER_PASSWORD']"                                   #Локатор поля ввода User_password
    l_login_button = "//*[@id='avtorization-form']/div[3]/div[2]/button/span"            #Локатор кнопки Войти
    l_main_word = "//*[@id='header']/div[1]/div/div/div[2]/div/div/a/span/span"          #Локатор имени Пользователя, для потверждения что мы авторизовались

    #Getters:

    def get_user_mail(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_user_mail)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_main_word)))



    # Actions:

    def input_user_mail(self, user_mail):
        self.get_user_mail().send_keys(user_mail)
        print("Input user_name : " + user_mail)


    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("Input user_password : " + user_password)

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")



    """Возвращает текст на главной странице после регистрации"""
    def text_main_word(self):
        a = self.get_main_word().text
        return a


    def assert_user_name(self, user_name):
        assert user_name == self.text_main_word()
        print("Имя пользвателя верное : " + user_name)


    # Metods:
    """Метод для авторизации """

    def autorization(self):
        with allure.step("autorization: Авторизовываемся на сайте"):
            self.driver.get(self.url_authorization)
            self.driver.maximize_window()
            self.driver.refresh()               #Делаем refresh чтобы скрыть выбор города.
            self.get_current_url()
            self.input_user_mail(config.user_mail)
            self.input_user_password(config.user_password)
            self.click_login_button()
            self.assert_user_name(config.user_name)
            time.sleep(1)


    def autorization_for_cookies(self):
        with allure.step("Autorization for cookies"):
            cookies = pickle.load(open("D:\Stepik\Python_selenium_dz\cookies.pkl", "rb"))
            self.driver.get(self.url_authorization)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.driver.maximize_window()
            print("Авторизовались через куки")
            time.sleep(1)
