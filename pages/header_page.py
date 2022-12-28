import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base

class Header_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators:
    l_cart_button = "//a[@href='/basket/']"                         #Локатор кнопки Корзина
    l_header_word = "//h1[@id='pagetitle']"                          #Локатор заголовка
    # //h1[@id ='pagetitle']
    # Locators Catalog dropdown-menu:
    l_catalog_button = "//div[@class='btn btn-default btn-large']"                            #Локатор элемента Каталог
    l_accumulators_button = "//*[@id='header']/div[2]/div[2]/div/div/div/div[3]/div/div[2]/nav/div/table/tbody/tr/td/div/ul/li[1]/a/span[1]"  #Локатор кнопки Аккамуляторы в выпадющем списке

    # Getters:
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_cart_button)))

    def get_header_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_header_word)))


    #Getters Catalog dropdown-menu:

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_catalog_button)))

    def get_accumulators_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_accumulators_button)))


    # Actions:
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click кнопка : Корзина")

    def text_header_word(self):
        text_header_word = self.get_header_word().text
        return text_header_word


    def assert_header_word(self, title):
        assert title == self.text_header_word()
        print("Название заголовка верное : " + title)

    #Actions Catalog dropdown-menu:

    def perform_catalog_button(self):
       ActionChains(self.driver).move_to_element(self.get_catalog_button()).perform()
       print("Навели курсор на элемент : Каталог")

    def click_accumulators_button(self):
        self.get_accumulators_button().click()
        print("Click кнопка : Аккумуляторы")




    #Metods Catalog dropdown-menu:

    def cross_to_accumulators(self):  #Переходим в раздел Каталог/Аккумуляторы
        with allure.step("cross_to_accumulators: Переходим в раздел Каталог/Аккумуляторы"):
            self.perform_catalog_button()
            time.sleep(2)
            self.click_accumulators_button()
            self.assert_header_word("Аккумуляторы")



    def cross_to_cart(self):  #Переходим в раздел Каталог/Аккумуляторы
        with allure.step("cross_to_cart: Переходим в Корзину"):
            self.click_cart_button()
            self.assert_header_word("Моя корзина")
            time.sleep(2)


