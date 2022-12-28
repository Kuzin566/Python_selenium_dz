import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import config
from base.base import Base
from pages.cart_page import Cart_page


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    last_name = config.user_name.split(" ")[1]
    first_name = config.user_name.split(" ")[0]
    email = config.user_mail
    phone = "+7 (964) 181-03-13"
    total_price = ''
    order_description = ''

    #Locators:
    l_field_last_name = "//*[@id='sale_order_props']/div[2]/div[2]/div"
    l_field_first_name = "//*[@id='sale_order_props']/div[2]/div[5]/div"
    l_field_email = "//*[@id='sale_order_props']/div[2]/div[8]/div/span"
    l_field_phone = "//*[@id='sale_order_props']/div[2]/div[11]/div/span"
    l_total_price = "//*[@id='order_form_content']/div[9]/div[2]/div[1]/table/tbody/tr[2]/td[2]"
    l_order_description = "//textarea[@name='ORDER_DESCRIPTION']"
    l_checkout_button = "//a[@id = 'submit_btn']"



    #Getters:
    def get_field_last_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_field_last_name)))

    def get_field_first_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_field_first_name)))

    def get_field_email(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_field_email)))

    def get_field_phone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_field_phone)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_total_price)))

    def get_order_description(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_order_description)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_checkout_button)))

    #Actions:

    def input_last_name(self, last_name):
        self.get_field_last_name().send_keys(last_name)
        print("Ввели фамилию : " + last_name)

    def input_first_name(self, first_name):
        self.get_field_first_name().send_keys(first_name)
        print("Ввели Имя : " + first_name)

    def input_email(self, email):
        self.get_field_email().send_keys(email)
        print("Ввели Email : " + email)

    def input_phone(self, phone):
        self.get_field_phone().send_keys(phone)
        print("Ввели номер телефона : +7" + phone)

    def assert_last_name(self, last_name):
        assert last_name == self.get_field_last_name().get_attribute('innerText')
        print("Фамилия в информации о покупателе верная : " + last_name)

    def assert_first_name(self, first_name):
        assert first_name == self.get_field_first_name().get_attribute('innerText')
        print("Имя в информации о покупателе верное : " + first_name)

    def assert_email(self, email):
        assert email == self.get_field_email().get_attribute('innerText')
        print("Email d информации о покупателе верный : " + email)

    def assert_phone(self, phone):
        assert phone == self.get_field_phone().get_attribute('innerText')
        print("Номер телефона в  информации о покупателе верный : " + phone)

    def assert_total_price(self, total_prcie):
        assert total_prcie == self.get_total_price().get_attribute('innerText').split(' ')[0]
        print("Итоговая сумма верная : " + total_prcie + "RUB")

    def input_order_description(self, description ):
        self.get_order_description().send_keys(description)
        print("Ввели комментарий к заказу : " + description)

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Нажали кнопку оформить заказ")




    #Metods:
    def registration_order(self):
        with allure.step("Проверяем информацию о покупателе, проверяем заказ и нажимаем Оформить заказ"):
            self.assert_last_name(self.last_name)
            self.assert_first_name(self.first_name)
            self.assert_email(self.email)
            self.assert_phone(self.phone)
            self.assert_total_price(self.total_price)
            self.input_order_description(self.order_description)
            # self.click_checkout_button()        #Эта строка закомментирована, потому что заказ сразу оформляется, если потом отменить, то достают звонками)


