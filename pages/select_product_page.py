import random
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base


class Select_product_page(Base):


    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    label = ''
    model = ''
    product_position = "1"
    product_name = ''
    product_price = ''




    #Locators
    l_sort_by_price_button = "//*[@id='right_block_ajax']/div[2]/div[2]/div[1]/a[3]"               #Локатор кнопки сортировки по цене
    l_list_label = ".//label[@class='bx_filter_param_label   ']"
    l_list_models = ".//div[@data-prop_code='smodel']//span[@class = 'bx_filter_input_checkbox']"  #Локатор блока со списком моделей

    #Getters

    def get_check_box_label(self, label):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f".//label[@class='bx_filter_param_label   ']//span/span[@title = '{label}']")))

    def get_check_box_model(self, model):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f".//div[@data-prop_code='smodel']//span[@class = 'bx_filter_input_checkbox']//span[@title = '{model}']")))

    def get_sort_by_price_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_sort_by_price_button)))

    def get_product_cart_button(self, products_position):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@class='item main_item_wrapper'][{products_position}]/td/table/tbody/tr/td[4]/div/div/span/span")))

    def get_product_name(self, products_position):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f".//*[@class='item main_item_wrapper'][{products_position}]//td//table//tbody//tr//a[@class='dark_link']")))

    def get_product_price(self, products_position):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@class='item main_item_wrapper'][{products_position}]/td/table/tbody/tr/td[3]//div[@class='price']")))



    #Actions:
    """Получаем список Xpath всех Label в фильтре Label"""
    def get_list_xpath_label(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_list_label)))
        list_xpath = self.driver.find_elements(By.XPATH, ".//div[@data-prop_code='compatibility']//label[@class='bx_filter_param_label   ']//span/span[@title = *]")
        return list_xpath

    """Получаем слуйчаный атрибут title их списка всех Xpath Label"""
    def get_random_title_label(self):
        xpath_label = random.choice(self.get_list_xpath_label()).get_attribute('title')
        return xpath_label

    def choose_check_box_label(self, label):
        if not label:
            label = self.get_random_title_label()
        self.get_check_box_label(label).click()
        print("В фильтре по совместимости выбрали Label : " + label)
        return label

    """Получаем список Xpath всех моделей в фильтре модели"""
    def get_list_xpath_model(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_list_models)))
        list_xpath = self.driver.find_elements(By.XPATH, ".//div[@data-prop_code='smodel']//label[@class='bx_filter_param_label   ']//span/span[*]")
        return list_xpath

    """Получаем слуйчаный атрибут title их списка всех Xpath Model"""
    def get_random_title_model(self):
        try:
            xpath_model = random.choice(self.get_list_xpath_model()).get_attribute('title')
            return xpath_model
        except ValueError:
            print("По заданным Производителям нет моделей\
                  Пожалуйста запустите тест заново")
            self.driver.close()


    def choose_check_box_model(self, model):
        if not model:
            model = self.get_random_title_model()
        self.get_check_box_model(model).click()
        print("В фильтре Поддерживаемые модели выбрали модель : " + model)


    def click_sort_by_price_button(self):
        self.get_sort_by_price_button().click()
        print("Нажали кнопку: сортировать по цене")

    def click_add_to_cart_product(self, products_position):    #По уму бы в цикл это загнать, но как нибудь потом)
        self.get_product_cart_button(products_position).click()
        print("Добавили В корзину продукт №:" +products_position)


    def text_product_name(self, products_position):
        text_name_product = self.get_product_name(products_position).get_attribute('innerText')
        print("Название продукта №" + products_position + " : " + text_name_product)
        return text_name_product

    def text_product_price(self, products_position):
        text_price_product = self.get_product_price(products_position).get_attribute('data-value')
        print("Цена продукта №" + products_position + " = " + text_price_product + " RUB")
        return text_price_product





    #Metods
    def select_product(self):
        with allure.step("select_product: Выбераем фильтры по производителю и модели, отсортировываем заказ по цене, выбираем первый заказ сверху"):
            self.choose_check_box_label(self.label)
            self.choose_check_box_label(self.label)
            self.choose_check_box_label(self.label)
            self.choose_check_box_model(self.model)
            self.choose_check_box_model(self.model)
            self.click_sort_by_price_button()
            self.product_name = self.text_product_name(self.product_position)
            self.product_price = self.text_product_price(self.product_position)
            self.click_add_to_cart_product(self.product_position)



